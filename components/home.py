import streamlit as st


def render_home(you):
    st.markdown(f"""
    <div class="hero">
        <h1>📖 If Anyone Builds It, Everyone Dies</h1>
        <div class="subtitle">Interactive Reading Companion</div>
        <div class="quote">
            Built this because I wanted to be able to think through the book with {you()} in a way that was more interactive than just reading.<br><br>
            And also because I am a massive nerd.
        </div>
    </div>
    """, unsafe_allow_html=True)

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
            <h3>🧪 Side Trails</h3>
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