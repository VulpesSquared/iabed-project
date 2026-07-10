import streamlit as st

from chapters.chapter1 import render_chapter1
from chapters.chapter2 import render_chapter2
from chapters.chapter3 import render_chapter3
from chapters.chapter4 import render_chapter4
from chapters.chapter5 import render_chapter5
from chapters.chapter6 import render_chapter6
from chapters.chapter7 import render_chapter7
from chapters.chapter8 import render_chapter8
from chapters.chapter9 import render_chapter9
from chapters.chapter10 import render_chapter10
from chapters.chapter11 import render_chapter11
from chapters.chapter12 import render_chapter12
from chapters.chapter13 import render_chapter13
from chapters.chapter14 import render_chapter14



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
            "Chapter 10",
            "Chapter 11",
            "Chapter 12",
            "Chapter 13",
            "Chapter 14",
        ],
    )

    chapter_renderers = {
        "Intro + Chapter 1": render_chapter1,
        "Chapter 2": render_chapter2,
        "Chapter 3": render_chapter3,
        "Chapter 4": render_chapter4,
        "Chapter 5": render_chapter5,
        "Chapter 6": render_chapter6,
        "Chapter 7": render_chapter7,
        "Chapter 8": render_chapter8,
        "Chapter 9": render_chapter9,
        "Chapter 10": render_chapter10,
        "Chapter 11": render_chapter11,
        "Chapter 12": render_chapter12,
        "Chapter 13": render_chapter13,
        "Chapter 14": render_chapter14,
    }

    renderer = chapter_renderers.get(chapter)

    if renderer:
        renderer(you)
    else:
        st.info("This chapter is coming next.")