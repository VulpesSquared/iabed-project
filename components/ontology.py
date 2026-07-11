import html
import json
from pathlib import Path
from typing import Any

import streamlit as st


PROJECT_DIR = Path(__file__).resolve().parents[1]
ONTOLOGY_FILE = PROJECT_DIR / "data" / "shared_ontology.json"


def load_shared_ontology() -> Any:
    """Load the shared ontology JSON file."""

    if not ONTOLOGY_FILE.exists():
        raise FileNotFoundError(
            f"Could not find the shared ontology at: {ONTOLOGY_FILE}"
        )

    try:
        with ONTOLOGY_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError as error:
        raise ValueError(
            "The shared ontology contains invalid JSON. "
            f"Check line {error.lineno}, column {error.colno}."
        ) from error


def ontology_records(ontology: Any) -> list[dict]:
    """Normalize the ontology into term records for both views."""

    if isinstance(ontology, list):
        return [record for record in ontology if isinstance(record, dict)]

    if isinstance(ontology, dict):
        records = []

        for term, content in ontology.items():
            if isinstance(content, dict):
                records.append({"term": term, **content})

        return records

    return []


def render_tags(items: list[str]) -> None:
    if not items:
        return

    tags = "".join(
        f'<span class="tag">{html.escape(str(item))}</span>'
        for item in items
    )
    st.markdown(tags, unsafe_allow_html=True)


def render_definition(record: dict) -> None:
    """Render the original and refined definitions without collapsing them."""

    term = record.get("term", "Untitled Term")
    original = record.get("your_definition", "")
    refined = record.get("refined_definition", "")
    notes = record.get("notes", "")
    related = record.get("related_terms", [])

    st.header(term)

    if original:
        st.markdown(
            f"""
            <div class="sage-box">
                <h3>Original Definition</h3>
                <p>{html.escape(str(original))}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    if refined:
        st.markdown(
            f"""
            <div class="card">
                <h3>Refined Definition</h3>
                <p>{html.escape(str(refined))}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    if notes:
        st.markdown(
            f"""
            <div class="lavender-box">
                <h3>Why the Distinction Matters</h3>
                <p>{html.escape(str(notes))}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    if related:
        st.markdown("#### Related Terms")
        render_tags(related)


def dot_quote(value: str) -> str:
    """Quote arbitrary ontology text for Graphviz DOT."""

    escaped = str(value).replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def graph_records(records: list[dict], focus: str) -> list[dict]:
    """Return either the full ontology or one term's immediate neighborhood."""

    if focus == "Entire ontology":
        return records

    by_term = {
        str(record.get("term", "")): record
        for record in records
        if record.get("term")
    }
    selected = by_term.get(focus)

    if not selected:
        return records

    included = {focus, *selected.get("related_terms", [])}

    # Include reverse relationships so the focused map does not hide terms
    # that point toward the selected term.
    for record in records:
        if focus in record.get("related_terms", []):
            included.add(str(record.get("term", "")))

    return [
        record
        for record in records
        if str(record.get("term", "")) in included
    ]


def build_dot(records: list[dict], focus: str) -> str:
    """Build a directed ontology graph from related_terms relationships."""

    visible = graph_records(records, focus)
    visible_terms = {
        str(record.get("term", ""))
        for record in visible
        if record.get("term")
    }
    lines = [
        "digraph ontology {",
        'bgcolor="transparent";',
        'rankdir="TB";',
        'graph [pad="0.35", nodesep="0.45", ranksep="0.65"];',
        (
            'node [shape="box", style="rounded,filled", '
            'fontname="Helvetica", fontsize="12", margin="0.18,0.12", '
            'color="#5E81AC", fillcolor="#181B23", '
            'fontcolor="#F4F1EA", penwidth="1.5"];'
        ),
        (
            'edge [color="#7C9A7A", fontcolor="#D8D1C7", '
            'fontname="Helvetica", fontsize="9", arrowsize="0.7", '
            'penwidth="1.3"];'
        ),
    ]

    for term in sorted(visible_terms):
        attributes = []

        if term == focus:
            attributes = [
                'fillcolor="#6F1D1B"',
                'color="#D8A54A"',
                'penwidth="2.5"',
            ]

        attribute_text = ""

        if attributes:
            attribute_text = f" [{', '.join(attributes)}]"

        lines.append(f"{dot_quote(term)}{attribute_text};")

    edges = set()

    for record in visible:
        source = str(record.get("term", ""))

        for target in record.get("related_terms", []):
            target = str(target)

            if source in visible_terms and target in visible_terms:
                edges.add((source, target))

    for source, target in sorted(edges):
        lines.append(
            f"{dot_quote(source)} -> {dot_quote(target)} "
            '[label=" related to "];'
        )

    lines.append("}")
    return "\n".join(lines)


def render_definitions(records: list[dict]) -> None:
    terms = [
        str(record.get("term", "Untitled Term"))
        for record in records
    ]
    selected_term = st.selectbox(
        "Choose a term",
        options=terms,
        key="ontology_definition_term",
    )
    selected = next(
        record
        for record in records
        if str(record.get("term", "Untitled Term")) == selected_term
    )
    render_definition(selected)

    st.divider()
    st.markdown("### All Definitions")
    st.caption(
        "The complete ontology remains available here in its original form."
    )

    for record in records:
        term = record.get("term", "Untitled Term")

        with st.expander(str(term)):
            if record.get("your_definition"):
                st.markdown("**Original definition**")
                st.write(record["your_definition"])

            if record.get("refined_definition"):
                st.markdown("**Refined definition**")
                st.write(record["refined_definition"])

            if record.get("notes"):
                st.markdown("**Notes**")
                st.write(record["notes"])

            if record.get("related_terms"):
                st.markdown("**Related terms**")
                render_tags(record["related_terms"])


def render_visual_map(records: list[dict]) -> None:
    st.markdown(
        """
        The map shows how the terms point toward one another. Choose a term
        to isolate its immediate conceptual neighborhood, or open the entire
        ontology to see the full structure.
        """
    )
    terms = sorted(
        str(record.get("term", ""))
        for record in records
        if record.get("term")
    )
    focus = st.selectbox(
        "Map view",
        options=["Entire ontology", *terms],
        key="ontology_graph_focus",
    )

    if focus != "Entire ontology":
        st.caption(
            "The selected term is highlighted in burgundy and butterscotch."
        )

    st.graphviz_chart(
        build_dot(records, focus),
        use_container_width=True,
    )

    if focus != "Entire ontology":
        selected = next(
            (
                record
                for record in records
                if str(record.get("term", "")) == focus
            ),
            None,
        )

        if selected:
            st.divider()
            render_definition(selected)


def show() -> None:
    """Display the definitions and visual ontology map."""

    st.title("🕸️ Knowledge Map")
    st.caption(
        "The connective structure behind the Atlas: the original definitions, "
        "their refinements, and the relationships between them."
    )

    try:
        ontology = load_shared_ontology()
    except (FileNotFoundError, ValueError) as error:
        st.error(str(error))
        return

    records = ontology_records(ontology)

    if not records:
        st.warning("The ontology loaded, but no term records were found.")
        return

    st.markdown(
        f"""
        <div class="blue-box">
            <strong>{len(records)} foundational terms</strong><br>
            Two definitions for each idea: the original language that began
            the conversation and the refined version used across the Atlas.
        </div>
        """,
        unsafe_allow_html=True,
    )

    definitions_tab, map_tab = st.tabs(
        ["📚 Definitions", "🕸️ Visual Map"]
    )

    with definitions_tab:
        render_definitions(records)

    with map_tab:
        render_visual_map(records)