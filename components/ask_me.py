import html

import streamlit as st

from services.atlas_corpus import build_corpus
from services.atlas_retrieval import retrieve


SUGGESTED_QUESTIONS = [
    "Do you think current AI systems are agents?",
    "Where do you disagree with the book most?",
    "What would change your mind about existential risk?",
    "Why do you call neural networks gray boxes?",
    "Is alignment an engineering problem or a political one?",
    "How should we reason about catastrophic risk under uncertainty?",
]


@st.cache_data
def load_corpus() -> list[dict]:
    return build_corpus()


def set_question(question: str) -> None:
    st.session_state.ask_me_question = question


def render_result(result: dict) -> None:
    title = result.get("title", "Untitled")
    location = result.get("location", "")
    kind = result.get("kind", "").replace("_", " ").title()

    with st.expander(f"{title} · {location}"):
        st.caption(kind)

        if result.get("definition"):
            st.markdown("**Relevant idea**")
            st.write(result["definition"])

        if result.get("position"):
            st.markdown("**My position**")
            st.write(result["position"])

        if result.get("reasoning"):
            st.markdown("**Why it matters here**")
            st.write(result["reasoning"])

        if result.get("change_mind"):
            st.markdown("**What would change my mind**")
            st.write(result["change_mind"])

        related = result.get("related", [])

        if related:
            tags = "".join(
                f'<span class="tag">{html.escape(item)}</span>'
                for item in related
            )
            st.markdown(tags, unsafe_allow_html=True)


def show() -> None:
    st.title("💭 Ask Me")

    st.markdown(
        """
        Ask about an idea, disagreement, open question, or connection
        somewhere inside the Atlas.

        This searches my notes and recorded positions. It does not answer
        from the general internet, and it will not invent an opinion I
        haven't written down.
        """
    )

    corpus = load_corpus()

    if not corpus:
        st.warning("The Atlas corpus could not be loaded.")
        return

    if "ask_me_question" not in st.session_state:
        st.session_state.ask_me_question = ""

    st.markdown("#### A few places to begin")

    columns = st.columns(2)

    for index, question in enumerate(SUGGESTED_QUESTIONS):
        with columns[index % 2]:
            st.button(
                question,
                key=f"suggested_question_{index}",
                use_container_width=True,
                on_click=set_question,
                args=(question,),
            )

    question = st.text_input(
        "Ask the Atlas",
        key="ask_me_question",
        placeholder=(
            "Try: What do you think separates optimization from agency?"
        ),
    )

    if not question:
        return

    results = retrieve(
        query=question,
        corpus=corpus,
        limit=6,
    )

    st.divider()

    if not results:
        st.markdown(
            """
            <div class="lavender-box">
                <h3>I haven't written enough about that yet</h3>
                <p>
                    I couldn't find a strong match in the Atlas. That may be
                    a useful sign that this belongs in the Reading Journal,
                    Concepts, or a new Side Trail.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        return

    st.subheader("What the Atlas contains")

    for result in results:
        render_result(result)