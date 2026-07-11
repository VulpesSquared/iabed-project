import streamlit as st


def render_home(you) -> None:
    st.markdown(
        f"""
        <div class="hero">
            <h1>📖 If Anyone Builds It, Everyone Dies</h1>
            <div class="subtitle">Interactive Reading Companion</div>
            <div class="quote">
                Built this because I wanted to be able to think through the book
                with {you()} in a way that was more interactive than just reading.
                <br><br>
                And also because I am a massive nerd.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            <div class="card">
                <h3>📖 Reading Journal</h3>
                <p>
                    A chapter-by-chapter record of where I paused, what I questioned,
                    and how my interpretation changes as I keep reading.
                </p>
                <span class="tag">claims</span>
                <span class="tag">margin notes</span>
                <span class="tag">reflection</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class="card">
                <h3>🧠 Concepts & Knowledge Base</h3>
                <p>
                    Permanent concept pages connecting definitions, my interpretation,
                    book chapters, research, and related ideas across the Atlas.
                </p>
                <span class="tag">concept map</span>
                <span class="tag">connections</span>
                <span class="tag">evidence</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

    col3, col4 = st.columns(2)

    with col3:
        st.markdown(
            """
            <div class="card">
                <h3>🕸️ Knowledge Map</h3>
                <p>
                    A map of how ideas connect across the book, my notes,
                    the research, and the questions I keep returning to.
                </p>
                <span class="tag">connections</span>
                <span class="tag">idea paths</span>
                <span class="tag">related concepts</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col4:
        st.markdown(
            """
            <div class="card">
                <h3>🧭 Side Trails</h3>
                <p>
                    The papers, technical questions, historical parallels,
                    and unexpected research paths that lead beyond the book itself.
                </p>
                <span class="tag">research trails</span>
                <span class="tag">open questions</span>
                <span class="tag">deeper reading</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

    col5, col6 = st.columns(2)

    with col5:
        st.markdown(
            """
            <div class="card">
                <h3>💭 Ask Me</h3>
                <p>
                    A future way to explore my notes, sources, disagreements,
                    and evolving positions without reducing them to generic answers.
                </p>
                <span class="tag">reasoning</span>
                <span class="tag">uncertainty</span>
                <span class="tag">what would change my mind</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col6:
        st.markdown(
            """
            <div class="card">
                <h3>☕ About This Project</h3>
                <p>
                    Why I built the Atlas, how it is organized,
                    and what I hope it makes visible.
                </p>
                <span class="tag">purpose</span>
                <span class="tag">process</span>
                <span class="tag">design</span>
            </div>
            """,
            unsafe_allow_html=True,
        )