import streamlit as st
import json
from pathlib import Path
from components.home import render_home
from components.reading_journal import show as show_reading_journal

BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"

def load_json(filename):
    with open(DATA_DIR / filename, "r", encoding="utf-8") as f:
        return json.load(f)
    
BUTTERSCOTCH = "#D8A54A"
SAGE = "#7C9A7A"
DUSTY_BLUE = "#5E81AC"
LAVENDER = "#A78BFA"
BURGUNDY = "#6F1D1B"
CHARCOAL = "#111418"
CARD = "#181B23"


def you(text: str = "you") -> str:
    return f"<span class='you'>{text}</span>"


st.set_page_config(
    page_title="If Anyone Builds It, Everyone Dies",
    page_icon="📖",
    layout="wide"
)

st.markdown(f"""
<style>
    .stApp {{
        background-color: {CHARCOAL};
        color: #F4F1EA;
    }}

    .hero {{
        padding: 3rem 2rem;
        border-radius: 24px;
        background: linear-gradient(135deg, #1f2937 0%, #111827 70%);
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
""", unsafe_allow_html=True)

st.sidebar.title("📚 Reading Guide")

page = st.sidebar.radio(
    "Start here",
    [
        "Home",
        "Reading Journal",
        "Concepts",
        "Side Trails",
        "Ask Me",
        "About"
    ]
)

st.sidebar.markdown("---")
st.sidebar.caption("An interactive field notebook for AI risk, alignment, governance, and the rabbit holes around them.")


if page == "Home":
    render_home(you)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="card">
            <h3>📖 Reading Journal</h3>
            <p>Chapter-by-chapter claims, agreements, disagreements, and questions.</p>
            <span class="tag">claims</span>
            <span class="tag">notes</span>
            <span class="tag">chapters</span>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <h3>🧠 Concepts</h3>
            <p>Definitions, examples, related ideas, and why each concept matters.</p>
            <span class="tag">agency</span>
            <span class="tag">alignment</span>
            <span class="tag">governance</span>
        </div>
        """, unsafe_allow_html=True)

    col3, col4 = st.columns(2)

    with col3:
        st.markdown("""
        <div class="card">
            <h3>🧪 Rabbit Holes</h3>
            <p>Research papers, white papers, essays, and reading paths.</p>
            <span class="tag">papers</span>
            <span class="tag">sources</span>
            <span class="tag">research</span>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="card">
            <h3>💭 Ask Me</h3>
            <p>A future Q&A layer based on my notes, not generic internet answers.</p>
            <span class="tag">questions</span>
            <span class="tag">debate</span>
            <span class="tag">perspective</span>
        </div>
        """, unsafe_allow_html=True)

elif page == "Reading Journal":
    show_reading_journal(you)

elif page == "Concepts":
    st.title("🧠 Concepts")

    concept = st.selectbox(
        "Choose a concept",
        ["Agency", "Grey Box", "Instrumental Convergence", "Governance", "Recursive Self-Improvement"]
    )

    if concept == "Agency":
        st.header("Agency")
        st.markdown("""
        <div class="blue-box">
            <h3>Definition</h3>
            <p>The capacity to select and execute actions that influence future states according to an objective.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="sage-box">
            <h3>My Position</h3>
            <p>Agency should be separated from intelligence, cognition, and sentience. A system can be highly capable without being strongly agentic.</p>
        </div>
        """, unsafe_allow_html=True)

    elif concept == "Grey Box":
        st.header("Grey Box")
        st.markdown("""
        <div class="blue-box">
            <h3>Definition</h3>
            <p>A system whose internal mechanisms are inspectable but not fully interpretable.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="sage-box">
            <h3>My Position</h3>
            <p>LLMs are grey boxes, not black boxes. Understanding is incomplete, not absent.</p>
        </div>
        """, unsafe_allow_html=True)

    else:
        st.info("Concept page coming next.")

elif page == "Side Trails":
    st.title("🧪 Side Trails")
    st.info("Next we’ll add research papers and white papers by concept.")

elif page == "Ask Me":
    st.title("💭 Ask Me")
    question = st.text_input("Ask a question about my notes")

    if question:
        st.markdown("""
        <div class="lavender-box">
            This feature will eventually answer from my notes and sources.
            For now, it is a placeholder.
        </div>
        """, unsafe_allow_html=True)

elif page == "About":
    st.title("About This Project")

    st.markdown(f"""
    <div class="card">
        <h3>Why I built this</h3>
        <p>
        I knew we'd end up talking about this book for hours anyway.
        This is a way to be a massive nerd and make it more engaging.
        </p>
        <p>
        My goal was never to make {you()} agree with me.
        It was to make my reasoning visible.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="burgundy-box">
        <h3>Design note</h3>
        <p>
        If the word <span class="you">you</span> appears in butterscotch, that's intentional.
        </p>
    </div>
    """, unsafe_allow_html=True)