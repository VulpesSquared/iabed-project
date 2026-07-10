import html
import json
from collections import Counter
from pathlib import Path

import streamlit as st


PROJECT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_DIR / "data"

CONCEPT_FILES = [
    ("Tier 0", "tier0_concepts.json"),
    ("Tier 1", "tier1_concepts.json"),
    ("Tier 2", "tier2_concepts.json"),
]


def load_concepts() -> list[dict]:
    """Load and combine every concept tier."""

    concepts: list[dict] = []

    for tier_name, filename in CONCEPT_FILES:
        file_path = DATA_DIR / filename

        if not file_path.exists():
            st.error(f"Could not find `{filename}` in the data folder.")
            continue

        try:
            with file_path.open("r", encoding="utf-8") as file:
                tier_concepts = json.load(file)
        except json.JSONDecodeError as error:
            st.error(
                f"`{filename}` contains invalid JSON. "
                f"Check line {error.lineno}, column {error.colno}."
            )
            continue

        if not isinstance(tier_concepts, list):
            st.error(f"`{filename}` must contain a JSON list.")
            continue

        for concept in tier_concepts:
            if not isinstance(concept, dict):
                continue

            concept["_tier"] = tier_name
            concepts.append(concept)

    return sorted(
        concepts,
        key=lambda concept: concept.get("name", "").casefold(),
    )


def create_concept_labels(concepts: list[dict]) -> dict[str, dict]:
    """
    Create selectbox labels.

    Tier names are only shown when the same concept name appears
    in more than one file.
    """

    name_counts = Counter(
        concept.get("name", "Untitled Concept")
        for concept in concepts
    )

    labels: dict[str, dict] = {}

    for concept in concepts:
        name = concept.get("name", "Untitled Concept")
        tier = concept.get("_tier", "")

        if name_counts[name] > 1:
            label = f"{name} · {tier}"
        else:
            label = name

        labels[label] = concept

    return labels


def render_tags(items: list[str]) -> None:
    """Render a group of tags using the application's existing tag style."""

    if not items:
        return

    tags = "".join(
        f'<span class="tag">{html.escape(str(item))}</span>'
        for item in items
    )

    st.markdown(tags, unsafe_allow_html=True)


def render_sources(sources: list[dict]) -> None:
    """Render the research sources attached to a concept."""

    if not sources:
        st.caption("No research sources have been added yet.")
        return

    for source in sources:
        title = source.get("title", "Untitled source")
        authors = source.get("authors")
        year = source.get("year")
        source_type = source.get("type")
        importance = source.get("importance")
        url = source.get("url")

        heading_parts = [str(title)]

        if year:
            heading_parts.append(str(year))

        heading = " · ".join(heading_parts)

        with st.expander(heading):
            if authors:
                st.markdown(f"**Authors:** {authors}")

            if source_type:
                st.markdown(f"**Source type:** {source_type}")

            if importance:
                st.markdown(f"**Why it is here:** {importance}")

            if url:
                st.link_button(
                    "Open source",
                    url,
                    use_container_width=False,
                )


def show() -> None:
    st.title("🧠 Concepts")
    st.caption(
        "A permanent map of the ideas behind the book, the research around "
        "them, and how my thinking is developing."
    )

    concepts = load_concepts()

    if not concepts:
        st.warning("No concepts could be loaded.")
        return

    labels = create_concept_labels(concepts)

    selected_label = st.selectbox(
        "Choose a concept",
        options=list(labels.keys()),
        index=0,
    )

    concept = labels[selected_label]

    name = concept.get("name", "Untitled Concept")
    tier = concept.get("_tier", "")
    definition = concept.get("definition", "")
    my_take = concept.get("my_take", "")
    why_it_matters = concept.get("why_it_matters", "")
    related_concepts = concept.get("related_concepts", [])
    appears_in = concept.get("appears_in", [])
    sources = concept.get("sources", [])

    st.header(name)

    metadata = [tier]

    if appears_in:
        metadata.append(" · ".join(str(chapter) for chapter in appears_in))

    st.caption(" | ".join(item for item in metadata if item))

    if definition:
        st.markdown(
            f"""
            <div class="card">
                <h3>Definition</h3>
                <p>{html.escape(definition)}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    if my_take:
        st.markdown(
            f"""
            <div class="sage-box">
                <h3>My Take</h3>
                <p>{html.escape(my_take)}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    if why_it_matters:
        st.markdown(
            f"""
            <div class="burgundy-box">
                <h3>Why It Matters</h3>
                <p>{html.escape(why_it_matters)}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    if related_concepts:
        st.subheader("Related Concepts")
        render_tags(related_concepts)

    if appears_in:
        st.subheader("Appears In")
        render_tags(appears_in)

    st.subheader("Research")
    render_sources(sources)