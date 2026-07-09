import streamlit as st

st.set_page_config(
    page_title="If Anyone Builds It",
    page_icon="📖",
    layout="wide"
)

st.markdown("""
<style>
    .main {
        background-color: #0f1117;
    }
    .hero {
        padding: 3rem 2rem;
        border-radius: 24px;
        background: linear-gradient(135deg, #1f2937 0%, #111827 60%);
        border: 1px solid #374151;
        margin-bottom: 2rem;
    }
    .hero h1 {
        font-size: 3.5rem;
        margin-bottom: 0.3rem;
    }
    .subtitle {
        font-size: 1.35rem;
        color: #d1d5db;
        margin-bottom: 1.5rem;
    }
    .quote {
        font-size: 1.1rem;
        color: #e5e7eb;
        border-left: 4px solid #9ca3af;
        padding-left: 1rem;
        line-height: 1.7;
    }
    .card {
        padding: 1.4rem;
        border-radius: 18px;
        background-color: #181b23;
        border: 1px solid #2f3542;
        min-height: 170px;
    }
    .card h3 {
        margin-top: 0;
    }
    .tag {
        display: inline-block;
        padding: 0.25rem 0.65rem;
        border-radius: 999px;
        background-color: #253047;
        color: #c7d2fe;
        font-size: 0.85rem;
        margin-right: 0.4rem;
        margin-bottom: 0.4rem;
    }
</style>
""", unsafe_allow_html=True)

st.sidebar.title("📚 Reading Guide")

page = st.sidebar.radio(
    "Start here",
    [
        "Home",
        "Reading Sessions",
        "Concept Explorer",
        "Research Library",
        "Glossary",
        "Ask Christina",
    ]
)

st.sidebar.markdown("---")
st.sidebar.caption("Built as an interactive field notebook for AI risk, governance, alignment, and the rabbit holes around them.")

if page == "Home":
    st.markdown("""
    <div class="hero">
        <h1>📖 If Anyone Builds It</h1>
        <div class="subtitle">Christina's Interactive Reading Companion</div>
        <div class="quote">
            I didn't build this because I wanted you to agree with me.<br><br>
            I built it because this book changed how I think, and I wanted to make the reasoning visible.
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="card">
            <h3>📚 Reading Sessions</h3>
            <p>Chapter-by-chapter claims, agreements, disagreements, and notes.</p>
            <span class="tag">claims</span>
            <span class="tag">notes</span>
            <span class="tag">chapters</span>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <h3>🧠 Concept Explorer</h3>
            <p>Definitions, examples, related ideas, and why each concept matters.</p>
            <span class="tag">alignment</span>
            <span class="tag">agency</span>
            <span class="tag">governance</span>
        </div>
        """, unsafe_allow_html=True)

    col3, col4 = st.columns(2)

    with col3:
        st.markdown("""
        <div class="card">
            <h3>📄 Research Library</h3>
            <p>White papers, essays, primary sources, and rabbit-hole reading paths.</p>
            <span class="tag">papers</span>
            <span class="tag">white papers</span>
            <span class="tag">links</span>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="card">
            <h3>💬 Ask Christina</h3>
            <p>A future question-answering layer based on my notes, claims, and research trail.</p>
            <span class="tag">questions</span>
            <span class="tag">debate</span>
            <span class="tag">perspective</span>
        </div>
        """, unsafe_allow_html=True)

elif page == "Reading Sessions":
    st.title("📚 Reading Sessions")
    st.info("Next: we’ll add Chapter 7, Chapter 8, Chapter 9, and the claim/agree/disagree notes.")

elif page == "Concept Explorer":
    st.title("🧠 Concept Explorer")
    st.info("Next: we’ll add agency, instrumental convergence, recursive self-improvement, governance, and grey-box models.")

elif page == "Research Library":
    st.title("📄 Research Library")
    st.info("Next: we’ll add papers, white papers, essays, and concept-linked sources.")

elif page == "Glossary":
    st.title("📓 Glossary")
    st.info("Next: we’ll define key terms at beginner, intermediate, and graduate levels.")

elif page == "Ask Christina":
    st.title("💬 Ask Christina")
    st.info("Next: we’ll make this pull from your notes instead of being generic.")