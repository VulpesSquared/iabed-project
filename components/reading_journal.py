import streamlit as st

from chapters.chapter1 import render_chapter1
from chapters.chapter2 import render_chapter2
from chapters.chapter3 import render_chapter3
from chapters.chapter4 import render_chapter4
from chapters.chapter5 import render_chapter5
from chapters.chapter6 import render_chapter6


def show(you):
    st.title("📖 Read With Me")

    st.markdown(
        """
This is the annotated-book version.

I broke each chapter into the places where I paused: the ideas that made me agree,
disagree, ask for a better definition, or wander down a side trail.
"""
    )

    chapter = st.selectbox(
        "Choose a chapter",
        [
            "Intro + Chapter 1",
            "Chapter 2",
            "Chapter 3",
            "Chapter 4",
            "Chapter 5",
            "Chapter 6",
            "Chapter 7",
            "Chapter 8",
            "Chapter 9",
        ],
    )

    chapter_renderers = {
        "Intro + Chapter 1": render_chapter1,
        "Chapter 2": render_chapter2,
        "Chapter 3": render_chapter3,
        "Chapter 4": render_chapter4,
        "Chapter 5": render_chapter5,
        "Chapter 6": render_chapter6,
    }

    renderer = chapter_renderers.get(chapter)

    if renderer:
        renderer(you)
    else:
        st.info("This chapter is coming next.")