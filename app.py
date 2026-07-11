from pathlib import Path

import streamlit as st

from components.about import show as show_about
from components.concepts import show as show_concepts
from components.home import render_home
from components.ontology import show as show_ontology
from components.reading_journal import show as show_reading_journal
from components.side_trails import show as show_side_trails
from components.ask_me import show as show_ask_me


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

BUTTERSCOTCH = "#D8A54A"
SAGE = "#7C9A7A"
DUSTY_BLUE = "#5E81AC"
LAVENDER = "#A78BFA"
BURGUNDY = "#6F1D1B"
CHARCOAL = "#111418"
CARD = "#181B23"


def you(text: str = "you") -> str:
    """Render direct references to 'you' in butterscotch."""

    return f"<span class='you'>{text}</span>"


st.set_page_config(
    page_title="If Anyone Builds It, Everyone Dies",
    page_icon="📖",
    layout="wide",
)


st.markdown(
    f"""
    <style>
        .stApp {{
            background-color: {CHARCOAL};
            color: #F4F1EA;
        }}

        .hero {{
            padding: 3rem 2rem;
            border-radius: 24px;
            background: linear-gradient(
                135deg,
                #1f2937 0%,
                #111827 70%
            );
            border: 1px solid #374151;
            margin-bottom: 2rem;
        }}

        .hero h1 {{
            font-size: 3.5rem;
            margin-bottom: 0.3rem;
            color: #F4F1EA;
        }}

        .subtitle {{
            font-size: 1.35rem;
            color: #D8D1C7;
            margin-bottom: 1.5rem;
        }}

        .quote {{
            font-size: 1.1rem;
            color: #E8E1D8;
            border-left: 4px solid {BUTTERSCOTCH};
            padding-left: 1rem;
            line-height: 1.7;
        }}

        .you {{
            color: {BUTTERSCOTCH};
            font-weight: 700;
        }}

        .card {{
            padding: 1.4rem;
            border-radius: 18px;
            background-color: {CARD};
            border: 1px solid #2f3542;
            min-height: 170px;
            margin-bottom: 1rem;
        }}

        .sage-box {{
            padding: 1rem;
            border-radius: 14px;
            background-color: rgba(124, 154, 122, 0.12);
            border: 1px solid {SAGE};
            margin-bottom: 1rem;
        }}

        .blue-box {{
            padding: 1rem;
            border-radius: 14px;
            background-color: rgba(94, 129, 172, 0.12);
            border: 1px solid {DUSTY_BLUE};
            margin-bottom: 1rem;
        }}

        .lavender-box {{
            padding: 1rem;
            border-radius: 14px;
            background-color: rgba(167, 139, 250, 0.12);
            border: 1px solid {LAVENDER};
            margin-bottom: 1rem;
        }}

        .burgundy-box {{
            padding: 1rem;
            border-radius: 14px;
            background-color: rgba(111, 29, 27, 0.22);
            border: 1px solid {BURGUNDY};
            margin-bottom: 1rem;
        }}

        .tag {{
            display: inline-block;
            padding: 0.25rem 0.65rem;
            border-radius: 999px;
            background-color: #253047;
            color: #c7d2fe;
            font-size: 0.85rem;
            margin-right: 0.4rem;
            margin-bottom: 0.4rem;
        }}
    </style>
    """,
    unsafe_allow_html=True,
)


st.sidebar.title("📚 Reading Guide")

page = st.sidebar.radio(
    "Start here",
    [
        "Home",
        "Reading Journal",
        "Concepts",
        "Knowledge Map",
        "Side Trails",
        "Ask Me",
        "About",
    ],
)

st.sidebar.markdown("---")

st.sidebar.caption(
    "An interactive field notebook for AI risk, alignment, governance, "
    "and the rabbit holes around them."
)


if page == "Home":
    render_home(you)

elif page == "Reading Journal":
    show_reading_journal(you)

elif page == "Concepts":
    show_concepts()

elif page == "Knowledge Map":
    show_ontology()

elif page == "Side Trails":
    show_side_trails()

elif page == "Ask Me":
    show_ask_me()

elif page == "About":
    show_about()