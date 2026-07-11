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

The scary part isn't necessarily raw power. It's strategic creativity. Which is something we covered extensively in my doctoral program.
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
One of the easier misconceptions to reject. People picture AI as being trapped inside computers until someone builds Terminators. But humans already affect the physical world indirectly.

We move muscles through electrical signals. Companies move products through emails. Financial markets move trillions of dollars because information changes.

If intelligence can manipulate people and existing infrastructure, a body becomes optional rather than necessary.
The stronger argument isn't that AI never benefits from robots. It's that robots aren't a prerequisite for influence.
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
This may have been my favorite point in the chapter!

People instinctively separate "the Internet" from "the real world." But brains communicate through electrical signals.

Factories run because computers tell machines what to do. Power grids, hospitals, supply chains, satellites, financial systems, transportation—all are digitally mediated.
The digital world already controls enormous parts of the physical world. The divide feels intuitive, but it's mostly an illusion.
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
    elif place == "We may not understand the route of attack beforehand":
        render_claim_card(
            title="We may not understand the route of attack beforehand",
            reaction="🟢 Plausible",
            margin_note="""
The Aztec analogy is doing A LOT of work here, but I think the underlying point is fair.

A less capable civilization may not be able to imagine the strategic options available to a more capable one. That does not mean the more capable system is magical.

It means the weaker side may be reasoning inside the wrong hypothesis space.

The routes of attack we imagine are usually extensions of technologies and strategies we already understand. A sufficiently advanced intelligence may find vulnerabilities, combinations, or forms of leverage that are not obvious to us in advance.
The strongest version of this argument is not, "We cannot name the weapon, therefore anything is possible." It is, "Our inability to specify the mechanism does not prove the mechanism does not exist."
            """,
            why="""
- Strategic options depend on what a system understands about the environment.
- A large intelligence gap may create an equally large gap in imaginable tactics.
- Humans are often poor at forecasting genuinely novel capabilities.
            """,
            questions="""
- How do we reason responsibly about threats we cannot specify?
- When does uncertainty become an excuse for unfalsifiable claims?
- What kinds of evaluations can test for unknown strategic capabilities?
            """,
            side_trails="""
- The Aztec analogy
- Unknown unknowns
- Strategic surprise
- Capability evaluations
            """,
        )

    elif place == "Superintelligence would exploit domains humans poorly understand":
        render_claim_card(
            title="Superintelligence would exploit domains humans poorly understand",
            reaction="🟢 Agree, with caveats",
            margin_note="""
The argument is strongest in domains where the underlying rules are real, humans only partially understand them, and better models could reveal usable structure.

Biology is an obvious example. So are cognition, cybersecurity, complex infrastructure, and social systems.

We already know that small improvements in understanding can create enormous practical leverage. A system that models those domains far better than we do could identify interventions that look surprising or even impossible from our current perspective.
That does not mean every speculative scenario in the chapter is equally plausible.

But I do think asymmetric understanding is a real source of strategic advantage.
            """,
            why="""
- Many important systems contain structure humans only partly understand.
- Better models can expose exploitable regularities.
- Scientific and technical leverage often comes from finding structure others cannot see.
            """,
            questions="""
- Which domains are most vulnerable to asymmetric understanding?
- Are biology and cybersecurity qualitatively different from other fields?
- Can interpretability or containment reduce the advantage?
            """,
            side_trails="""
- Biology
- Cybersecurity
- Complex systems
- Scientific discovery
- Gray-box systems
            """,
        )

    elif place == "We'd lose because of asymmetric understanding":
        render_claim_card(
            title="We'd lose because of asymmetric understanding",
            reaction="🟢 Mostly agree",
            margin_note="""
The most convincing version of the "we'd lose" argument is not that AI would be magical or omnipotent.

It is that enough of an intelligence gap becomes a strategic gap. Humans are already easy to influence through recommendation systems, propaganda, targeted advertising, social engineering, and incentive design.

A system that predicts human behavior more accurately, acts faster, coordinates across many channels, and understands our institutions better than we do may be able to steer outcomes without anything that looks like direct control.
The point is not mind control. The point is that prediction, persuasion, timing, and leverage can compound until meaningful human control becomes unrealistic.

That is where I found the chapter persuasive.
            """,
            why="""
- Humans are already vulnerable to behavioral influence.
- Better prediction improves persuasion and strategic planning.
- Influence can remain invisible to the people being influenced.
- Strategic dominance does not require physical force.
            """,
            questions="""
- At what point does influence become control?
- Is prediction the key threshold, or access to resources and institutions?
- How could humans preserve meaningful oversight under a large intelligence gap?
            """,
            side_trails="""
- Social engineering
- Persuasive systems
- Human factors
- Institutional capture
- Control theory
            """,
        )