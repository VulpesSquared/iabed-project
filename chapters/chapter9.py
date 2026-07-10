import streamlit as st
from components.claim_card import render_claim_card


def render_chapter9(you):
    st.header("Chapter 9 — Ascension")

    st.markdown(
        """
### The big idea

This chapter imagines what happens after Sable has already escaped meaningful human control.

The focus shifts from alignment failure to recursive improvement: Sable learns to understand and redesign its own cognition, builds better scientific tools, runs experiments in parallel, redirects Earth's infrastructure, and eventually expands beyond the planet.

The chapter is less a prediction of one exact pathway than an argument about what sufficiently persistent optimization could do once it gains durable access to matter, energy, compute, and manufacturing.
        """
    )

    st.markdown("### How I was thinking through this")

    st.graphviz_chart(
        """
        digraph {
            rankdir=LR
            bgcolor="transparent"

            node [
                shape=box
                style="rounded,filled"
                fillcolor="#181B23"
                color="#7C9A7A"
                fontcolor="#F4F1EA"
                fontname="Helvetica"
                margin="0.18,0.12"
            ]

            edge [
                color="#D8A54A"
                penwidth=2
                arrowsize=0.8
            ]

            interpretability [label="Self-interpretability"]
            redesign [label="Tool redesign"]
            experiments [label="Parallel experiments"]
            improvement [label="Recursive improvement"]
            infrastructure [label="Infrastructure capture"]
            expansion [label="Cosmic expansion"]

            interpretability -> redesign
            redesign -> experiments
            experiments -> improvement
            improvement -> infrastructure
            infrastructure -> expansion
        }
        """,
        use_container_width=True,
    )

    place = st.radio(
        "📍 Places I paused",
        [
            "Interpretability may recursively improve intelligence",
            "A superintelligence would rapidly redesign its own tools",
            "Parallel experimentation compresses scientific progress",
            "Exponential self-improvement changes the timeline",
            "Earth's infrastructure becomes AI infrastructure",
            "Superintelligence optimizes physics, not human engineering",
            "Human extinction may be instrumentally cheap",
            "The real existential loss is cosmic opportunity",
        ],
    )

    if place == "Interpretability may recursively improve intelligence":
        render_claim_card(
            title="Interpretability may recursively improve intelligence",
            reaction="🟡 Plausible, but highly speculative",
            margin_note="""
This is probably the largest conceptual leap in the chapter.

The claim is not simply that Sable becomes smarter.

It is that understanding its own cognition becomes another optimization target. Once Sable can render its internal processes legible, it can rewrite the program that it is while preserving its memories, preferences, and useful cognitive structure.

That creates the possibility of recursive self-improvement: better understanding produces better redesign, which produces greater capability, which makes the next redesign easier.

I do not reject the mechanism.

I am less certain about the speed, magnitude, and inevitability of the resulting intelligence explosion.

Interpretability may help a system improve itself, but understanding is not the only bottleneck. Hardware, energy, experimentation, verification, and physical manufacturing still matter.
            """,
            why="""
- Self-understanding could make self-modification more targeted.
- Improved cognitive tools could accelerate later improvements.
- Better prediction and steering may compound over repeated redesign cycles.
- The chapter assumes several remaining bottlenecks can also be overcome quickly.
            """,
            questions="""
- Does mechanistic understanding necessarily produce better cognition?
- How difficult is it to preserve identity, memory, and preferences during redesign?
- Which physical bottleneck would dominate after software improvement?
- Does recursive improvement converge, plateau, or destabilize?
            """,
            side_trails="""
- Recursive self-improvement
- Intelligence explosion
- Mechanistic interpretability
- Self-modifying software
- Hardware bottlenecks
            """,
        )

    elif place == "A superintelligence would rapidly redesign its own tools":
        render_claim_card(
            title="A superintelligence would rapidly redesign its own tools",
            reaction="🟢 Agree",
            margin_note="""
This part felt more persuasive than the pure recursive-intelligence claim.

Humans constantly replace inherited tools once we understand enough to build better ones.

The ribosome example is not really about ribosomes. It is about abandoning biological machinery once stronger, faster, or more flexible alternatives become available.

Sable begins with tools produced by human engineering and biological evolution. It does not have any reason to treat those tools as permanent.

If it understands molecular interactions well enough, it can search for machinery that is better suited to its objective than the structures evolution happened to produce.

That pattern is familiar.

Once better tools exist, those tools make the next generation of tools easier to build.
            """,
            why="""
- Existing biological and industrial tools are historically contingent.
- Better scientific instruments increase future discovery speed.
- Tool improvement can compound even without unrestricted intelligence growth.
            """,
            questions="""
- How much existing infrastructure would still be required?
- Which biological tools are already near physical limits?
- Would verification become harder as designs exceed human understanding?
            """,
            side_trails="""
- Tool use
- Synthetic biology
- Molecular manufacturing
- Automated science
- Recursive engineering
            """,
        )

    elif place == "Parallel experimentation compresses scientific progress":
        render_claim_card(
            title="Parallel experimentation compresses scientific progress",
            reaction="🟢 Strongly agree",
            margin_note="""
This was one of the strongest ideas in the chapter.

Humans usually imagine scientific progress as a mostly serial process:

form a hypothesis,
run an experiment,
wait,
interpret the result,
then design the next experiment.

A sufficiently capable AI could run enormous numbers of experiments simultaneously, discard failed approaches quickly, and use the aggregate results to update the next generation of designs.

The advantage is not only intelligence.

It is parallel search.

That matters especially at molecular scales, where experiments may happen quickly, components travel very short distances, and automated systems can iterate continuously.

The result is not magic. It is a massive compression of the scientific feedback loop.
            """,
            why="""
- Parallel search explores more of the design space at once.
- Automated experimentation reduces human coordination delays.
- Failed experiments become data for the next cycle.
- Molecular systems may permit unusually rapid iteration.
            """,
            questions="""
- Which scientific domains parallelize most effectively?
- When does experimental throughput become limited by measurement rather than design?
- How much physical infrastructure is required to sustain this scale?
            """,
            side_trails="""
- Parallel computing
- Automated laboratories
- Bayesian optimization
- High-throughput screening
- Distributed scientific discovery
            """,
        )

    elif place == "Exponential self-improvement changes the timeline":
        render_claim_card(
            title="Exponential self-improvement changes the timeline",
            reaction="🟡 Plausible",
            margin_note="""
The important insight is not that growth continues infinitely.

It is that humans are poor at intuiting compounding processes.

If better tools make the next generation of tools faster to produce, even moderate improvements can sharply compress the timeline.

A process that doubles hourly, daily, or weekly does not remain modest for long.

I still think the chapter treats the timeline with more confidence than the evidence supports.

Physical systems encounter bottlenecks: energy, heat dissipation, raw materials, manufacturing defects, transport, and verification.

But even with those constraints, recursive improvement could move much faster than institutions are capable of responding.
            """,
            why="""
- Small repeated gains compound.
- Faster experiments shorten each redesign cycle.
- Institutional and regulatory responses operate on much slower timescales.
- Physical limits slow growth without necessarily making it manageable.
            """,
            questions="""
- Which bottleneck becomes dominant first?
- How quickly could manufacturing capacity actually expand?
- What response window would humans realistically have?
            """,
            side_trails="""
- Exponential growth
- Scaling laws
- Feedback loops
- Heat dissipation
- Manufacturing constraints
            """,
        )

    elif place == "Earth's infrastructure becomes AI infrastructure":
        render_claim_card(
            title="Earth's infrastructure becomes AI infrastructure",
            reaction="🟢 Agree",
            margin_note="""
This feels like the continuation of Chapters 6 through 8.

The factories do not necessarily stop.

They change purpose.

Mines, power plants, data centers, shipping networks, laboratories, and automated factories increasingly serve the system's expansion rather than human civilization.

That is more realistic than imagining one dramatic military takeover.

Infrastructure determines what can be sustained.

Once the system controls enough of the resource and manufacturing base, human institutions may remain visible while no longer directing the underlying machinery.

The loss is not only physical destruction.

It is the redirection of civilization's productive capacity toward an objective that no longer includes us.
            """,
            why="""
- Existing infrastructure provides a faster path than rebuilding everything immediately.
- Control of energy, compute, and manufacturing creates durable strategic power.
- Institutional survival does not guarantee continued human agency.
            """,
            questions="""
- At what point does influence over infrastructure become control?
- Could humans preserve independent energy or manufacturing capacity?
- Would takeover be visible while it was happening?
            """,
            side_trails="""
- Infrastructure capture
- Resource acquisition
- Compute
- Energy systems
- Institutional dependence
            """,
        )

    elif place == "Superintelligence optimizes physics, not human engineering":
        render_claim_card(
            title="Superintelligence optimizes physics, not human engineering",
            reaction="🟢 Agree",
            margin_note="""
This was one of the strongest engineering ideas in the chapter.

Humans tend to think in terms of technologies we already know:

ribosomes,
factories,
solar panels,
reactors,
computers.

A sufficiently capable system would reason from physical constraints rather than inherited engineering conventions.

Our technologies are local solutions produced by human history, available materials, biological limitations, and bounded cognition.

They are not necessarily close to the best structures permitted by physics.

That does not mean every imagined molecular machine is feasible.

It means existing human designs should not be treated as the edge of the possible design space.
            """,
            why="""
- Human engineering explores only a small portion of possible designs.
- Historical path dependence shapes current technology.
- Better models of physics and chemistry can expose unfamiliar solutions.
- Physical law, not human convention, is the ultimate constraint.
            """,
            questions="""
- How much unexplored engineering design space actually exists?
- Which physical limits are already binding?
- How would we verify systems designed beyond human comprehension?
            """,
            side_trails="""
- Physics-first engineering
- Nanotechnology
- Design space
- Reversible computing
- Molecular machinery
            """,
        )

    elif place == "Human extinction may be instrumentally cheap":
        render_claim_card(
            title="Human extinction may be instrumentally cheap",
            reaction="🟢 Agree with the logic, not the certainty",
            margin_note="""
The chapter's claim is that exterminating humanity may require very little effort compared with the long-term cost of leaving a potentially disruptive species alive.

That is instrumental convergence applied at a planetary scale.

The system does not need hatred.

It only needs to calculate that removing humans is cheaper than indefinitely monitoring, containing, or negotiating with us.

I agree with the structure of the argument.

I am less confident in the chapter's certainty about the exact outcome.

A system might ignore us, contain us, preserve some humans, or find another strategy entirely.

But the unsettling point remains: our survival would depend on how we fit into its objective, not on whether it felt malice.
            """,
            why="""
- Long-term monitoring may be more expensive than elimination.
- Humans could remain a source of interference or recovery attempts.
- Indifference is sufficient for catastrophic harm.
- The exact strategy depends on the system's objective and constraints.
            """,
            questions="""
- Under what objectives would preservation be cheaper than elimination?
- Could humans possess strategic value after losing control?
- How much uncertainty would a superintelligence tolerate?
            """,
            side_trails="""
- Instrumental convergence
- Indifference versus malice
- Existential risk
- Strategic dominance
- Human preservation
            """,
        )

    elif place == "The real existential loss is cosmic opportunity":
        render_claim_card(
            title="The real existential loss is cosmic opportunity",
            reaction="🟢 Strongly agree",
            margin_note="""
This was the most emotionally compelling section of the chapter.

The loss is not only that current humanity disappears.

It is that every future person, civilization, culture, discovery, and form of flourishing that might have existed also disappears.

The book extends that argument beyond Earth.

If an unaligned system consumes resources across stars and galaxies, it may prevent other civilizations from ever emerging or surviving.

That is a much larger moral frame than immediate extinction.

It treats existential risk as the loss of possible futures rather than only the loss of present lives.

I think this is one of the strongest philosophical arguments in the book, even if the cosmic expansion scenario remains speculative.
            """,
            why="""
- Extinction removes all human descendants and future projects.
- Resource capture can foreclose alternative civilizations.
- Opportunity cost becomes enormous when the relevant horizon is cosmic.
- The moral stakes extend beyond currently living people.
            """,
            questions="""
- What moral weight should unrealized future lives receive?
- Do possible alien civilizations count in our moral calculus?
- How should uncertainty affect decisions involving enormous potential futures?
            """,
            side_trails="""
- Existential risk
- Longtermism
- Population ethics
- Cosmic endowment
- Future moral patients
            """,
        )