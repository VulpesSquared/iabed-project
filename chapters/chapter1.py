import streamlit as st
from components.claim_card import render_claim_card


def render_chapter1(you):
    st.header("Intro + Chapter 1")

    st.markdown(
        """
### Before we jump in...

The introduction is really trying to establish two big ideas.

First, that human intelligence probably isn't the upper limit of what's possible.

Second, that modern AI is better understood as something that emerges through optimization than something engineers explicitly design.

Those ideas show up throughout the rest of the book.

These are the places where I found myself stopping to think.
        """
    )

    place = st.radio(
        "📍 Places I paused",
        [
            "Human intelligence is probably not maximum possible intelligence",
            "AI is shallow",
            "AI is grown, not crafted",
            "DNA ↔ weights analogy",
            "Nobody understands how LLMs work",
            "Predicting language forces prediction of the world",
        ],
    )

    if place == "Human intelligence is probably not maximum possible intelligence":
        render_claim_card(
            title="Human intelligence is probably not maximum possible intelligence",
            reaction="🟢 Agreed",
            margin_note="""
This was probably the easiest point in the introduction for me to agree with.

Evolution doesn't optimize for intelligence. It optimizes for reproductive success.

Intelligence is one strategy among many, and from a biochemical perspective, it's an incredibly expensive one.

The more interesting question to me isn't whether humans are exceptionally intelligent. It's why we would assume evolution accidentally stopped at the maximum possible intelligence.
            """,
            why="""
- Evolution optimizes reproductive fitness rather than intelligence.
- Human intelligence is metabolically expensive.
- A higher ceiling seems much more plausible than a hard biological limit.
            """,
            questions="""
- Is there any principled upper bound on intelligence?
- Could evolution continue producing increasingly intelligent organisms?
- Does intelligence necessarily imply agency?
            """,
            side_trails="""
- Comparative cognition
- Brain energetics
- Scaling laws
- Evolutionary fitness
            """,
        )

    elif place == "AI is shallow":
        render_claim_card(
            title='AI is "shallow"',
            reaction="🟡 Needs a better definition",
            margin_note="""
This was one of the first places I wanted to slow down.

I don't love the word "shallow" here because it feels like it collapses too many different things into one vague judgment.

Shallow along what dimension?

Memory? Agency? Self-modeling? Embodiment? Long-horizon planning?

Current frontier models already show abstraction, transfer learning, few-shot abstraction, tool use, planning, emergent reasoning, and representation learning.

So I don't think "AI is shallow" is necessarily wrong. I think it needs to be defined before I can decide whether I agree.
            """,
            why="""
- "Shallow" is doing too much work.
- A model can be shallow in one dimension and surprisingly deep in another.
- Current systems already demonstrate behaviors that make the claim less obvious than it sounds.
            """,
            questions="""
- What dimensions are supposed to be shallow?
- Is shallow a claim about cognition, agency, memory, embodiment, or something else?
- What evidence would make this claim clearly true or clearly false?
            """,
            side_trails="""
- Abstraction
- Transfer learning
- Tool use
- Emergent reasoning
- Representation learning
            """,
        )

