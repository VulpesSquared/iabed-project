import html
from typing import Optional

import streamlit as st

from services.atlas_corpus import build_corpus
from services.atlas_retrieval import retrieve


ROUTES = {
    "argue": {
        "icon": "⚔️",
        "label": "Something we'll probably argue about",
        "description": "A claim with enough friction to be worth defending.",
        "query": "agency optimization intelligence alignment risk disagreement",
        "question": (
            "Where do you think the distinction breaks: in the definition, "
            "the mechanism, or the evidence?"
        ),
    },
    "weird": {
        "icon": "🛸",
        "label": "The weirdest Side Trail",
        "description": "Consciousness, artificial minds, and stranger terrain.",
        "query": "machine consciousness sentience artificial minds subjectivity",
        "question": (
            "What is the strangest conclusion here that you still think might "
            "actually be true?"
        ),
    },
    "ten_minutes": {
        "icon": "⏱️",
        "label": "A 10-minute rabbit hole",
        "description": "One compact path through a claim, concept, and question.",
        "query": "gray box interpretability understanding models",
        "question": (
            "What would count as understanding a model well enough to trust "
            "an explanation of its behavior?"
        ),
    },
    "flight": {
        "icon": "✈️",
        "label": "A paper for the flight",
        "description": "A reading with enough substance to survive airplane mode.",
        "query": "interpretability agency alignment AI safety research paper",
        "question": (
            "Which assumption in this reading would you push on first?"
        ),
    },
    "changed": {
        "icon": "🔄",
        "label": "Where I complicated my own position",
        "description": "A place where the answer became less tidy as I read.",
        "query": "uncertainty disagreement shallow agency governance risk",
        "question": (
            "Does this look like genuine updating, or just a more elaborate "
            "version of the position I started with?"
        ),
    },
    "watts": {
        "icon": "🧛",
        "label": "Something connected to Peter Watts",
        "description": "Intelligence, consciousness, agency, and deeply rude biology.",
        "query": "consciousness intelligence sentience cognition agency mind",
        "question": (
            "If consciousness is not necessary for intelligence, what—if "
            "anything—does it contribute to agency?"
        ),
    },
    "for_you": {
        "icon": "💌",
        "label": "A question I want you to answer",
        "description": "The conversation was the point of this whole thing.",
        "query": "optimization genuine agency principled distinction goals",
        "question": (
            "Is there a principled distinction between increasingly persistent "
            "optimization and genuine agency?"
        ),
    },
}


@st.cache_data
def load_corpus() -> list[dict]:
    return build_corpus()


def choose_route(route_id: str) -> None:
    current = st.session_state.get("rabbit_hole_route")
    st.session_state.rabbit_hole_route = route_id

    if current == route_id:
        st.session_state.rabbit_hole_offset = (
            st.session_state.get("rabbit_hole_offset", 0) + 1
        )
    else:
        st.session_state.rabbit_hole_offset = 0


def pick_kind(
    results: list[dict],
    kind: str,
    offset: int = 0,
) -> Optional[dict]:
    matches = [result for result in results if result.get("kind") == kind]

    if not matches:
        return None

    return matches[offset % len(matches)]


def first_reading(results: list[dict], offset: int = 0) -> Optional[dict]:
    readings = []

    for result in results:
        for source in result.get("sources", []):
            if not isinstance(source, dict) or not source.get("title"):
                continue

            normalized = dict(source)
            normalized["atlas_location"] = result.get("title", "")
            readings.append(normalized)

    if not readings:
        return None

    return readings[offset % len(readings)]


def short_text(value: str, limit: int = 700) -> str:
    compact = " ".join(str(value).split())

    if len(compact) <= limit:
        return compact

    return f"{compact[:limit].rsplit(' ', 1)[0]}…"


def render_atlas_card(
    eyebrow: str,
    record: Optional[dict],
    color_class: str,
) -> None:
    if not record:
        return

    title = record.get("title", "Untitled")
    location = record.get("location", "")
    position = record.get("position", "")
    body = position or record.get("definition", "") or record.get(
        "reasoning", ""
    )

    st.markdown(
        f"""
        <div class="{color_class}">
            <p style="text-transform:uppercase;letter-spacing:.08em;
                      font-size:.75rem;margin-bottom:.35rem;">
                {html.escape(eyebrow)}
            </p>
            <h3>{html.escape(str(title))}</h3>
            <p style="color:#D8D1C7;">{html.escape(str(location))}</p>
            <p>{html.escape(short_text(body))}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_reading(reading: Optional[dict]) -> None:
    if not reading:
        return

    title = reading.get("title", "Untitled Reading")
    creator = reading.get("authors") or reading.get("creator", "")
    year = reading.get("year", "")
    note = reading.get("importance") or reading.get("why_read_it") or reading.get(
        "note", ""
    )
    url = reading.get("url", "")

    st.markdown(
        f"""
        <div class="blue-box">
            <p style="text-transform:uppercase;letter-spacing:.08em;
                      font-size:.75rem;margin-bottom:.35rem;">
                THE READING
            </p>
            <h3>{html.escape(str(title))}</h3>
            <p>{html.escape(str(creator))}{' · ' if creator and year else ''}{html.escape(str(year))}</p>
            <p>{html.escape(short_text(note))}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if url:
        st.link_button("Open the reading", url)


def route_results(route: dict, corpus: list[dict]) -> list[dict]:
    results = retrieve(route["query"], corpus, limit=30)

    # A broad second pass keeps every route structurally complete even when
    # its most distinctive keywords favor only one document type.
    if not any(result.get("kind") == "chapter_claim" for result in results):
        results.extend(retrieve("agency intelligence alignment", corpus, 20))

    if not any(result.get("kind") == "concept" for result in results):
        results.extend(retrieve("agency consciousness alignment", corpus, 20))

    if not any(result.get("kind") == "side_trail" for result in results):
        results.extend(retrieve("AI minds risk governance", corpus, 20))

    deduplicated = []
    seen = set()

    for result in results:
        result_id = result.get("id")

        if not result_id or result_id in seen:
            continue

        seen.add(result_id)
        deduplicated.append(result)

    return deduplicated


def render_route(route_id: str, corpus: list[dict]) -> None:
    route = ROUTES[route_id]
    offset = st.session_state.get("rabbit_hole_offset", 0)
    results = route_results(route, corpus)

    claim = pick_kind(results, "chapter_claim", offset)
    concept = pick_kind(results, "concept", offset)
    trail = pick_kind(results, "side_trail", offset)
    reading = first_reading(results, offset)

    st.divider()
    st.markdown(
        f"## {route['icon']} {route['label']}"
    )
    st.caption(route["description"])

    render_atlas_card(
        "THE PLACE I PAUSED",
        claim,
        "burgundy-box",
    )

    columns = st.columns(2)

    with columns[0]:
        render_atlas_card("THE CONCEPT", concept, "sage-box")

    with columns[1]:
        render_atlas_card("THE SIDE TRAIL", trail, "lavender-box")

    render_reading(reading)

    st.markdown(
        f"""
        <div class="card">
            <p style="text-transform:uppercase;letter-spacing:.08em;
                      font-size:.75rem;margin-bottom:.35rem;">
                THE QUESTION FOR YOU
            </p>
            <h3>{html.escape(route['question'])}</h3>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.button(
        "Give me another version of this rabbit hole",
        key=f"another_{route_id}_{offset}",
        use_container_width=True,
        on_click=choose_route,
        args=(route_id,),
    )


def show() -> None:
    st.title("🐇 Choose a Rabbit Hole")
    st.markdown(
        """
        You can absolutely explore this like a serious research atlas.

        Or you can choose a door and let me hand you one claim, one concept,
        one Side Trail, one reading, and one question I want to talk about.
        """
    )

    corpus = load_corpus()

    if not corpus:
        st.warning("The Atlas corpus could not be loaded.")
        return

    route_items = list(ROUTES.items())

    for index in range(0, len(route_items), 2):
        columns = st.columns(2)

        for column, (route_id, route) in zip(
            columns,
            route_items[index:index + 2],
        ):
            with column:
                st.markdown(
                    f"""
                    <div class="card">
                        <h3>{route['icon']} {html.escape(route['label'])}</h3>
                        <p>{html.escape(route['description'])}</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
                st.button(
                    "Choose this door (and look down)",
                    key=f"rabbit_hole_{route_id}",
                    use_container_width=True,
                    on_click=choose_route,
                    args=(route_id,),
                )

    selected_route = st.session_state.get("rabbit_hole_route")

    if selected_route in ROUTES:
        render_route(selected_route, corpus)
