import streamlit as st


def show() -> None:
    st.title("About")

    st.markdown(
        """
        This is my very normal, very nerdy, but maybe you kind of get it, notebook.

        It started with one book and then immediately became a collection of
        margin notes, research papers, concept maps, questions, disagreements,
        and side trails I absolutely did not plan to follow.

        The goal is simple:

        **to show how I think, not just what I think...BUT "make it fun"**
        """
    )

    st.markdown(
        """
        <div class="card">
            <h3>A few things to know</h3>
            <p>
                I may agree with an argument, disagree with it, change my mind,
                or leave a question unresolved for a while.
            </p>
            <p>
                That is not a bug. That is the entire project.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="sage-box">
            <h3>Also</h3>
            <p>
                I like evidence, footnotes, careful definitions, and occasionally
                disappearing down a research rabbit hole for no practical reason.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.caption(
        "Built with curiosity, too many tabs, and a highly questionable sense of scope."
    )