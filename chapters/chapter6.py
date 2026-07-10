import streamlit as st
from components.claim_card import render_claim_card


def render_chapter6(you):
    st.header("Part 6")

    st.markdown(
        """
### The big idea

This section shifts from **what a superintelligence might want** to **how it could actually act in the world.**

The central claim is that an advanced AI doesn't need a humanoid robot body, magical technology, or obvious weapons.

If it is sufficiently intelligent, it could manipulate existing systems, recruit humans, exploit weaknesses, and interact with the physical world through the infrastructure that already exists.

The scary part isn't necessarily raw power.

It's strategic creativity.
        """
    )

    place = st.radio(
        "📍 Places I paused",
        [
            "Advanced AI wouldn't need a physical body",
            "The digital / physical divide is misleading",
            "We may not understand the route of attack beforehand",
            "Superintelligence would exploit domains humans poorly understand",
            "We'd lose because of asymmetric understanding",
        ],
    )
    if place == "Advanced AI wouldn't need a physical body":
        render_claim_card(
            title="Advanced AI wouldn't need a physical body",
            reaction="🟢 Agree",
            margin_note="""
One of the easier misconceptions to reject.

People picture AI as being trapped inside computers until someone builds Terminators.

But humans already affect the physical world indirectly.

We move muscles through electrical signals.

Companies move products through emails.

Financial markets move trillions of dollars because information changes.

If intelligence can manipulate people and existing infrastructure, a body becomes optional rather than necessary.

The stronger argument isn't that AI never benefits from robots.

It's that robots aren't a prerequisite for influence.
            """,
            why="""
- Intelligence acts through existing systems.
- Information changes the physical world.
- Humans already serve as actuators for digital instructions.
- A physical body is useful, not required.
            """,
            questions="""
- At what point would robotics become strategically valuable?
- Which physical limitations still matter without embodiment?
            """,
            side_trails="""
- Distributed agency
- Cyber-physical systems
- Human infrastructure as actuators
            """,
        )
    elif place == "The digital / physical divide is misleading":
        render_claim_card(
            title="The digital / physical divide is misleading",
            reaction="🟢 Strongly agree",
            margin_note="""
This may have been my favorite point in the chapter.

People instinctively separate "the Internet" from "the real world."

But brains communicate through electrical signals.

Factories run because computers tell machines what to do.

Power grids, hospitals, supply chains, satellites, financial systems, transportation—all are digitally mediated.

The digital world already controls enormous parts of the physical world.

The divide feels intuitive, but it's mostly an illusion.
            """,
            why="""
- Digital systems already coordinate physical infrastructure.
- Information itself changes reality.
- Nearly every critical system depends on software.
            """,
            questions="""
- Are there meaningful limits to digital influence?
- Which critical systems remain difficult to affect remotely?
            """,
            side_trails="""
- Cybersecurity
- Infrastructure dependence
- Information theory
            """,
        )