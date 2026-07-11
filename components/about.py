import streamlit as st


def show() -> None:
    st.title("About")

    st.markdown(
        """
        This is my very normal, very nerdy, but maybe you kind of get it, notebook.

        It started with a book suggestio from you and then immediately 
        became a collection of margin notes, research papers, concept maps, 
        questions, disagreements, and side trails I absolutely did not plan to follow.

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
                You might be thinking "OMG why did she do all this?!
                But I thought this was way more fun to give to you than a PDF of my notes.
                Is it probably too much? Yes. But that's just how I am
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
                I really appreciate all your book suggestions, 
                the way you engage with ideas and the way your mind works
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.caption(
        "Built with WAY too many tabs open, late nights over" \
        "a July weekend and handfuls of gummie bears"
    )