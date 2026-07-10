import streamlit as st


def render_claim_card(
    title,
    reaction,
    margin_note,
    why=None,
    questions=None,
    side_trails=None,
):

    with st.container(border=True):

        st.caption("📍 PLACE I PAUSED")

        st.subheader(title)

        st.markdown(f"### {reaction}")

        st.divider()

        st.markdown("### Here's what I wrote in the margin")

        st.write(margin_note)

        if why:
            with st.expander("💭 Why I think this"):
                st.markdown(why)

        if questions:
            with st.expander("❓Questions I'd love to talk about"):
                st.markdown(questions)

        if side_trails:
            with st.expander("🥾 Side Trails"):
                st.markdown(side_trails)