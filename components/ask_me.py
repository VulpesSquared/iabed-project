import html
import os
from typing import Optional

import streamlit as st

from services.atlas_corpus import build_corpus
from services.atlas_retrieval import retrieve
from services.atlas_synthesis import (
    DEFAULT_MODEL,
    evidence_status,
    fallback_answer,
    synthesize_answer,
)


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


def secret_value(name: str, default: str = "") -> str:
    """Read local/Streamlit configuration without requiring a secrets file."""

    try:
        value = st.secrets.get(name, default)
    except (FileNotFoundError, KeyError):
        value = default

    return str(value or os.getenv(name, default))


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


def source_index(results: list[dict]) -> dict[str, dict]:
    return {
        result.get("id", ""): result
        for result in results
        if result.get("id")
    }


def render_answer(answer: dict, results: list[dict]) -> None:
    partial = answer.get("answer_status") == "partial"
    heading = "What I can say from the Atlas"

    if partial:
        heading = "I haven't completely settled this"

    st.markdown(
        f"""
        <div class="sage-box">
            <h3>{heading}</h3>
            <p>{html.escape(answer.get("short_answer", ""))}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    reasoning = answer.get("reasoning", [])

    if reasoning:
        st.markdown("#### Why I think that")

        for point in reasoning:
            st.markdown(f"- {point}")

    uncertainty = answer.get("uncertainty", "")

    if uncertainty:
        st.markdown("#### Where I'm uncertain")
        st.write(uncertainty)

    change_mind = answer.get("what_would_change_my_mind", "")

    if change_mind:
        st.markdown("#### What would change my mind")
        st.write(change_mind)

    indexed = source_index(results)
    citations = [
        indexed[source_id]
        for source_id in answer.get("source_ids", [])
        if source_id in indexed
    ]

    if citations:
        st.markdown("#### Where this comes from")

        for citation in citations:
            st.markdown(
                f"- **{citation.get('title', 'Untitled')}** — "
                f"{citation.get('location', '')}"
            )

    if answer.get("fallback"):
        st.caption(
            "Shown directly from my written notes. Grounded synthesis is "
            "available when the Atlas API key is configured."
        )
    else:
        st.caption("Composed from my written notes.")


def answer_question(
    question: str,
    corpus: list[dict],
) -> tuple[list[dict], Optional[dict], str]:
    results = retrieve(query=question, corpus=corpus, limit=8)
    evidence = evidence_status(results)

    if evidence == "insufficient":
        return results, None, evidence

    api_key = secret_value("OPENAI_API_KEY")
    model = secret_value("OPENAI_MODEL", DEFAULT_MODEL)
    answer = None

    if api_key:
        answer = synthesize_answer(
            question=question,
            results=results,
            api_key=api_key,
            model=model,
        )

    if answer is None:
        answer = fallback_answer(results, evidence)

    return results, answer, evidence


def show() -> None:
    st.title("💭 Ask Me")

    st.markdown(
        """
        Ask about an idea, disagreement, open question, or connection
        somewhere inside the Atlas.

        Answers are composed only from my notes and recorded positions. If I
        haven't written enough to answer honestly, the Atlas will say so.
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
    ask_clicked = st.button(
        "Ask",
        type="primary",
        use_container_width=True,
        disabled=not question.strip(),
    )

    if ask_clicked:
        with st.spinner("Looking through the Atlas..."):
            results, answer, evidence = answer_question(question, corpus)

        st.session_state.ask_me_response = {
            "question": question,
            "results": results,
            "answer": answer,
            "evidence": evidence,
        }

    response = st.session_state.get("ask_me_response")

    if not response or response.get("question") != question:
        return

    results = response.get("results", [])
    answer = response.get("answer")
    evidence = response.get("evidence", "insufficient")

    st.divider()

    if evidence == "insufficient" or not results:
        st.markdown(
            """
            <div class="lavender-box">
                <h3>I haven't written enough about that yet</h3>
                <p>
                    I couldn't find strong enough evidence in the Atlas to
                    answer without inventing a position. That may be a useful
                    sign that this belongs in the Reading Journal, Concepts,
                    or a new Side Trail.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        return

    if answer:
        render_answer(answer, results)

    st.markdown("### Explore the source notes")

    for result in results:
        render_result(result)
