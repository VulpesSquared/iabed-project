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


def format_section_title(value: str) -> str:
    """Convert JSON keys into readable section titles."""

    return value.replace("_", " ").replace("-", " ").title()


def render_ontology_section(section_name: str, content: Any) -> None:
    """Render one section of the ontology."""

    title = format_section_title(section_name)

    with st.expander(title):
        if isinstance(content, (dict, list)):
            st.json(content, expanded=True)
        else:
            st.write(content)


def show() -> None:
    """Display the shared ontology as a visible Streamlit page."""

    st.title("🕸️ Knowledge Map")
    st.caption(
        "The connective structure behind the Atlas: concepts, aliases, "
        "relationships, and the paths between ideas."
    )

    try:
        ontology = load_shared_ontology()
    except (FileNotFoundError, ValueError) as error:
        st.error(str(error))
        return

    if isinstance(ontology, dict):
        st.success(
            f"Loaded {len(ontology)} ontology sections from "
            "`shared_ontology.json`."
        )

        for section_name, content in ontology.items():
            render_ontology_section(section_name, content)

    elif isinstance(ontology, list):
        st.success(
            f"Loaded {len(ontology)} ontology records from "
            "`shared_ontology.json`."
        )

        for index, record in enumerate(ontology, start=1):
            render_ontology_section(f"Record {index}", record)

    else:
        st.warning(
            "The ontology loaded successfully, but its top-level value "
            "is not a JSON object or list."
        )
        st.write(ontology)