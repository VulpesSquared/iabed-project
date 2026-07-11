import streamlit as st

from components.claim_card import render_claim_card


def render_chapter13(you) -> None:
    st.header("Chapter 13 — Shut It Down")

    st.caption(
        "On global prohibition, compute governance, international enforcement, "
        "and what humanity would have to sacrifice to stop an AI race."
    )

    st.markdown(
        """
### Before you read

This chapter stops diagnosing the problem and starts prescribing a
solution.

The authors are no longer asking how alignment might work, whether
companies should behave more responsibly, or which technical safeguards
should accompany advanced AI development.

Their answer is much more absolute:

**Stop the development of increasingly powerful AI systems everywhere.**

Not one company. Not one country. Not one voluntary agreement.

Everywhere.

The chapter compares the required response to the Allied mobilization
during World War II. The point of the analogy is not that the situations
are identical. It is that human societies have accepted enormous cost,
centralized authority, rationing, surveillance, and military action when
they believed the alternative was civilizational defeat.

I understand the logic.

I also think this chapter moves from a technical-risk argument into a
political theory of emergency power—and that transition deserves at
least as much scrutiny as the AI systems the authors want to prohibit.
        """
    )

    st.markdown(
        """
### The big idea

The authors argue that preventing artificial superintelligence cannot
be accomplished by shutting down one reckless company, passing ordinary
safety regulations, or asking one country to behave responsibly.

If building superintelligence anywhere threatens everyone, then advanced
AI development must become illegal everywhere.

Their proposed first step is to monitor and control the computing
infrastructure capable of training or running increasingly powerful
systems. Large concentrations of advanced chips would be registered,
observed, and subject to international inspection.

But compute controls alone would not be enough. Algorithmic advances can
make powerful systems cheaper to train, meaning that yesterday's enormous
cluster may become tomorrow's modest laboratory.

The authors therefore argue that research aimed at making AI substantially
more capable or efficient must also be prohibited.

A global prohibition would require credible enforcement. If a company or
state attempted to build an unauthorized frontier datacenter, other
powers would need to demand that it stop and, if necessary, disrupt or
destroy the facility.

The authors acknowledge that this would be expensive, dangerous, and open
to abuse. Their position is that every available alternative is worse if
continued AI escalation ends in human extinction.
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

            premise [label="Superintelligence anywhere\\nthreatens everyone"]
            prohibition [label="Advanced AI must be\\nprohibited everywhere"]
            compute [label="Monitor chips, power,\\nand datacenters"]
            research [label="Restrict capability and\\nefficiency research"]
            enforcement [label="Inspect, disrupt, or\\ndestroy violations"]
            survival [label="Preserve humanity's\\nability to choose later"]

            premise -> prohibition
            prohibition -> compute
            compute -> research
            research -> enforcement
            enforcement -> survival
        }
        """,
        use_container_width=True,
    )

    place = st.radio(
        "📍 Places I paused",
        [
            "Humanity can mobilize at enormous cost when survival is at stake",
            "No single company or country can solve a global AI race",
            "Compute monitoring is more concrete than regulating model behavior",
            "There is no obviously safe computing threshold",
            "Algorithmic progress weakens compute-only governance",
            "A global prohibition requires credible enforcement against defectors",
            "The proposed enforcement regime creates enormous moral hazards",
            "Waiting for a clearer warning may mean waiting too long",
            "Incremental AI policy is not the same as addressing existential risk",
            "A broad coalition should focus on the minimum shared goal",
        ],
        key="chapter13_place",
    )

    if place == (
        "Humanity can mobilize at enormous cost when survival is at stake"
    ):
        render_claim_card(
            title=(
                "Humanity can mobilize at enormous cost when survival "
                "is at stake"
            ),
            reaction="🟢 Agree with the general point",
            margin_note="""
The World War II analogy is doing two things at once.

First, it challenges the claim that international coordination on AI is
simply too expensive, disruptive, or politically difficult to imagine.

Human societies have imposed drafts, rationed essential goods, redirected
industrial production, borrowed staggering sums of money, and accepted
extraordinary state power when leaders and citizens believed the stakes
were high enough.

That part is true.

Political feasibility is not fixed. What sounds impossible under normal
conditions can become ordinary policy during a recognized emergency.

But the analogy also risks smuggling in the very conclusion that needs to
be established.

The Allied powers were responding to visible states, armies, invasions,
and atrocities. The threat was contested politically, but it was not a
hypothetical capability threshold hidden inside an uncertain technological
trajectory.

The chapter is right that humanity can mobilize.

It has not yet shown that people would interpret the AI evidence as
clearly enough to mobilize in the same way.
            """,
            why="""
- Political feasibility changes when a threat becomes socially legible.
- States have previously accepted extraordinary costs for collective survival.
- Emergency mobilization requires more than technical expert concern.
- The comparison depends on whether the AI threat becomes broadly credible.
            """,
            questions="""
- What would make advanced AI risk feel politically real rather than abstract?
- Can democratic mobilization occur before visible catastrophe?
- How much consensus existed before earlier large-scale mobilizations?
- When does an emergency analogy clarify the stakes, and when does it manufacture urgency?
            """,
            side_trails="""
- Wartime mobilization
- Political feasibility
- Risk communication
- Emergency governance
- Securitization
            """,
        )

    elif place == "No single company or country can solve a global AI race":
        render_claim_card(
            title="No single company or country can solve a global AI race",
            reaction="🟢 Strongly agree",
            margin_note="""
This is one of the chapter's strongest claims.

If the danger comes from the existence of a sufficiently capable system,
then it does not matter very much whether most companies behave
responsibly.

It also does not matter whether one country bans the work inside its own
borders while another continues.

A unilateral pause can reduce one actor's contribution to the risk. It
cannot solve a race in which the first successful defector changes the
outcome for everyone.

That makes the problem structurally different from ordinary product
regulation.

A dangerous medical device can be removed from one market. A polluting
factory primarily harms a region. A system capable of replication,
cyber operations, strategic manipulation, or global loss of control
would not respect jurisdictional boundaries.

I agree that national virtue is not a complete strategy.

The unresolved question is whether meaningful international coordination
can exist without the universal and nearly perfect enforcement standard
the authors appear to require.
            """,
            why="""
- Advanced AI development produces cross-border externalities.
- One actor may impose risk on people who never consented to it.
- National regulation does not bind foreign companies or governments.
- A single defector may undermine a broad voluntary agreement.
            """,
            questions="""
- Does survival require universal compliance or merely control of the largest actors?
- Which countries and companies actually possess decisive frontier capability?
- Can partial coordination meaningfully slow the race?
- What happens when a state considers AI development essential to its security?
            """,
            side_trails="""
- Global catastrophic risk
- Cross-border externalities
- Collective action
- Treaty design
- Race dynamics
            """,
        )

    elif place == (
        "Compute monitoring is more concrete than regulating model behavior"
    ):
        render_claim_card(
            title=(
                "Compute monitoring is more concrete than regulating "
                "model behavior"
            ),
            reaction="🟢 Agree, with substantial implementation concerns",
            margin_note="""
I understand why the authors begin with computing infrastructure.

It is easier to count advanced chips, identify major datacenters, monitor
large electrical loads, and audit supply chains than it is to inspect a
model and prove that it will never become dangerous.

Compute is a physical bottleneck.

Models, prompts, intentions, and algorithms are difficult to observe.
Large clusters of specialized hardware are comparatively tangible.

That makes compute governance one of the more plausible components of a
serious international regime.

But physical observability is not the same as political simplicity.

A monitoring system would need chip registries, import controls, power
records, inspections, secure telemetry, supply-chain cooperation, and a
trusted authority capable of distinguishing prohibited activity from
ordinary scientific, commercial, or military computing.

It would also create an extraordinary surveillance infrastructure.

The same system that can identify unauthorized AI training could be used
to monitor universities, companies, dissidents, or less powerful states.

So I see the appeal of the bottleneck.

I do not think the chapter spends enough time on who controls the
monitoring layer—or how the monitored can challenge its decisions.
            """,
            why="""
- Advanced compute is more physically observable than model intent.
- Chip supply chains create potential regulatory choke points.
- Large datacenters may be detectable through procurement and energy use.
- Monitoring infrastructure can itself become a source of concentrated power.
            """,
            questions="""
- Who would operate the international compute registry?
- How would inspectors distinguish dangerous training from legitimate computing?
- What appeal process would exist after a violation is alleged?
- Can monitoring be technically effective without becoming politically abusive?
            """,
            side_trails="""
- Compute governance
- Chip supply chains
- Datacenter monitoring
- Verification technology
- Surveillance infrastructure
            """,
        )

    elif place == "There is no obviously safe computing threshold":
        render_claim_card(
            title="There is no obviously safe computing threshold",
            reaction="🟢 Strongly agree",
            margin_note="""
The authors are unusually candid here.

There is nothing magical about one hundred thousand GPUs.

There is also nothing obviously safe about ninety-nine thousand, one
thousand, or a cluster the size of several consumer machines.

Any threshold would be a governance choice made under uncertainty.

Set it too high and genuinely dangerous systems may remain legal.

Set it too low and ordinary research, gaming hardware, scientific
computing, medical modeling, and local experimentation could become
subject to registration or prohibition.

That is not a minor implementation detail.

The threshold determines how much of society falls inside the emergency
regime.

I agree with the authors that the absence of a precise fatal number is
not evidence that no danger exists.

But the opposite is also true: uncertainty about the danger does not
automatically justify setting the threshold at the lowest technically
enforceable level.

The burden is to explain why a particular threshold is proportionate to
the evidence, revisable as technology changes, and narrow enough not to
criminalize enormous amounts of harmless computation.
            """,
            why="""
- Capability does not map cleanly onto a single hardware count.
- Model architecture and training efficiency alter what a given cluster can do.
- Conservative thresholds reduce false negatives but increase false positives.
- Threshold choices distribute political and economic power.
            """,
            questions="""
- What evidence should determine a regulated compute threshold?
- Should thresholds depend on model type, training objective, or deployment access?
- How often would the threshold need to change?
- What protections should exist for research below the dangerous frontier?
            """,
            side_trails="""
- Regulatory thresholds
- Compute scaling
- False positives
- Proportionality
- Technology-neutral regulation
            """,
        )

    elif place == "Algorithmic progress weakens compute-only governance":
        render_claim_card(
            title="Algorithmic progress weakens compute-only governance",
            reaction="🟢 Strongly agree",
            margin_note="""
This is the chapter's most important technical complication.

A system as capable as last year's frontier model may eventually require
a fraction of last year's computing power.

The transformer itself illustrates the problem.

A conceptual advance can unlock an enormous increase in capability
without requiring a corresponding increase in raw hardware.

That means a governance system built only around today's largest
datacenters will decay over time.

The regulated threshold moves downward as algorithms, data curation,
training procedures, inference methods, and hardware utilization improve.

I agree that compute governance cannot be the entire strategy.

Where the authors lose me is the jump from that observation to making
broad categories of research illegal.

Research into efficiency is not a cleanly separable activity. Work on
optimization, compression, mathematics, hardware, distributed systems,
neuroscience, and energy efficiency can have both ordinary and
capability-enhancing applications.

The danger is real.

The proposed boundary around forbidden knowledge remains extremely hard
to define.
            """,
            why="""
- Algorithmic efficiency can substitute for raw computing power.
- Hardware thresholds become obsolete as methods improve.
- General scientific work may produce unexpected capability gains.
- Research restrictions are harder to define and verify than hardware controls.
            """,
            questions="""
- What counts as capability research rather than ordinary computer science?
- Can research restrictions target experiments rather than ideas?
- How should dual-use work be evaluated?
- Would secrecy make dangerous breakthroughs more difficult to monitor?
            """,
            side_trails="""
- Algorithmic efficiency
- Dual-use research
- Transformer architecture
- Research governance
- Information hazards
            """,
        )

    elif place == (
        "A global prohibition requires credible enforcement against defectors"
    ):
        render_claim_card(
            title=(
                "A global prohibition requires credible enforcement "
                "against defectors"
            ),
            reaction="🟡 Agree with the strategic logic",
            margin_note="""
A prohibition that everyone expects others to violate is not a stable
prohibition.

The authors are right about that.

If one country believes another is secretly building a decisive system,
restraint begins to look like unilateral disarmament.

Verification therefore needs an enforcement mechanism strong enough to
change the expected payoff of defection.

That may include inspections, sanctions, equipment seizure, cyber
disruption, sabotage, or—in the authors' most extreme scenario—
conventional military strikes against unauthorized datacenters.

Strategically, I understand the argument.

A rule without consequences invites the actors most willing to ignore it
to determine the future for everyone else.

But credible enforcement has two sides.

It may deter prohibited activity.

It may also convince states that their datacenters, power systems,
research institutions, and military infrastructure are potential targets,
thereby increasing secrecy, hardening, preemption, and arms-race behavior.

The chapter treats enforcement primarily as the solution to defection.

It may also become one of the mechanisms that makes cooperation harder.
            """,
            why="""
- Agreements fail when violations are profitable and weakly punished.
- Verification is meaningful only when findings produce consequences.
- Strong enforcement may deter hidden frontier development.
- Threats against infrastructure can increase escalation and secrecy.
            """,
            questions="""
- Which enforcement tools are strong enough without becoming acts of war?
- Who determines that a prohibited datacenter actually exists?
- What evidentiary standard should precede destructive action?
- Can enforcement remain credible without creating incentives for preemption?
            """,
            side_trails="""
- Deterrence
- Verification
- Counterproliferation
- Escalation risk
- Commitment problems
            """,
        )

    elif place == (
        "The proposed enforcement regime creates enormous moral hazards"
    ):
        render_claim_card(
            title=(
                "The proposed enforcement regime creates enormous "
                "moral hazards"
            ),
            reaction="🔴 This is where I become deeply uneasy",
            margin_note="""
The authors acknowledge that emergency authority can be abused.

I do not think acknowledgement is enough.

A global institution capable of tracking advanced computation,
investigating private facilities, seizing hardware, imposing sanctions,
conducting cyberattacks, and authorizing physical destruction would be
one of the most powerful governance structures ever created.

That power would not be used by an abstract entity called humanity.

It would be exercised by particular states, agencies, officials,
contractors, intelligence services, and military organizations with
their own interests and biases.

False intelligence happens.

Political opponents are mislabeled.

Rules are enforced unequally.

Temporary emergency powers persist.

Infrastructure intended for one threat is repurposed for another.

The authors' answer is that extinction is worse.

That may be true and still be incomplete.

Expected harm cannot be evaluated by comparing extinction with an ideal
version of global enforcement. It must be compared with the actual
institutions we are likely to build, including their error rates,
incentives, capture risks, and capacity for violence.
            """,
            why="""
- Emergency institutions rarely operate exactly as designed.
- Surveillance and enforcement powers can be redirected toward other goals.
- False positives could carry catastrophic consequences.
- Powerful states may impose unequal rules on weaker states.
            """,
            questions="""
- What constitutional limits could bind an international AI authority?
- Who investigates abuse by the enforcement body itself?
- How would less powerful countries receive equal standing?
- What level of institutional harm becomes unacceptable even under existential risk?
            """,
            side_trails="""
- Moral hazard
- Emergency powers
- Institutional capture
- International law
- Procedural legitimacy
            """,
        )

    elif place == "Waiting for a clearer warning may mean waiting too long":
        render_claim_card(
            title="Waiting for a clearer warning may mean waiting too long",
            reaction="🟢 Agree",
            margin_note="""
The chapter is right to challenge the comforting idea that a dramatic
warning will arrive at exactly the useful moment.

A near-catastrophe is only informative if it is visible, correctly
interpreted, contained, and followed by action.

Advanced systems may improve quietly inside private laboratories.

A dangerous transition may not resemble a public disaster.

Organizations may explain away strange behavior, classify the evidence,
or continue because the anomaly is ambiguous.

Even a highly visible incident may produce only temporary concern before
normal incentives return.

So “we will act when the danger becomes obvious” is not a strategy.

It is a bet that the evidence will become persuasive before the system
becomes difficult to control.

I agree that there may be no universally recognized right time.

The hard question is what evidence is sufficient to justify exceptional
action before certainty is available.
            """,
            why="""
- Dangerous capability growth may occur outside public observation.
- Warning signs can be ambiguous or institutionally suppressed.
- Near misses do not guarantee political action.
- Waiting for certainty may eliminate the opportunity for prevention.
            """,
            questions="""
- Which present-day signals should count as meaningful warning signs?
- Who decides when uncertainty has become intolerable?
- Can predetermined tripwires reduce politically convenient delay?
- How should policy respond when experts disagree about whether a threshold was crossed?
            """,
            side_trails="""
- Warning signals
- Tripwires
- Normalcy bias
- Precautionary action
- Policy windows
            """,
        )

    elif place == (
        "Incremental AI policy is not the same as addressing existential risk"
    ):
        render_claim_card(
            title=(
                "Incremental AI policy is not the same as addressing "
                "existential risk"
            ),
            reaction="🟡 Agree with the distinction; disagree with the dismissal",
            margin_note="""
The authors are frustrated by policy proposals that discuss reporting,
deepfakes, annual safety plans, bias, or limited model behavior while
avoiding the claim that increasingly capable AI could end humanity.

I understand that frustration.

A policy can look serious while leaving the central risk mechanism
untouched.

If the concern is uncontrolled superintelligence, then paperwork,
voluntary commitments, and narrow content rules are not sufficient.

But insufficient is not the same as useless.

Reporting requirements can create visibility.

Incident-disclosure rules can reveal patterns.

Model evaluations can build institutional capacity.

Liability can change incentives.

Compute reporting can become the foundation for stronger verification.

Incremental policy may fail because it is timid.

It may also be how legal systems acquire the authority, technical
knowledge, and political legitimacy needed to do something stronger
later.

I would not confuse small steps with a complete solution.

I also would not discard them merely because they do not begin with the
authors' final conclusion.
            """,
            why="""
- Narrow rules may fail to address frontier capability escalation.
- Symbolic regulation can create the appearance of safety without changing risk.
- Incremental policies can still build information and enforcement capacity.
- Durable governance often develops through cumulative legal infrastructure.
            """,
            questions="""
- Which incremental policies genuinely reduce frontier risk?
- Which policies mainly create regulatory theater?
- Can gradual institution-building move quickly enough?
- How should policymakers communicate limited measures without overstating them?
            """,
            side_trails="""
- Regulatory capacity
- Policy layering
- Safety theater
- Mandatory reporting
- Institutional learning
            """,
        )

    elif place == (
        "A broad coalition should focus on the minimum shared goal"
    ):
        render_claim_card(
            title="A broad coalition should focus on the minimum shared goal",
            reaction="🟢 Strongly agree",
            margin_note="""
This is the most politically useful part of the chapter.

People do not need to agree about automation, employment, military AI,
consciousness, capitalism, abundance, human enhancement, or the long-term
future in order to agree that humanity should not be involuntarily
eliminated.

Bundling every AI dispute into one package makes coordination harder.

Someone may favor automation and oppose extinction.

Someone may oppose autonomous weapons but support medical AI.

Someone may want radical technological progress but reject an
uncontrolled race toward systems no one knows how to govern.

A survival coalition should therefore be narrow enough to include people
with fundamentally different visions of a good future.

That does not resolve the difficult questions about what must be stopped.

But it is a better political starting point than requiring agreement on
every moral and economic consequence of AI before anyone can act.
            """,
            why="""
- Broad package deals create unnecessary ideological barriers.
- Extinction prevention can be separated from many other AI disputes.
- Coalitions are stronger when they organize around a clear shared minimum.
- Other disagreements can continue without blocking survival-oriented action.
            """,
            questions="""
- What is the narrowest principle a broad AI-risk coalition could share?
- Which policies follow directly from that principle?
- Which issues should remain outside the survival coalition?
- How do we prevent a narrow coalition from becoming a vehicle for unrelated goals?
            """,
            side_trails="""
- Coalition building
- Minimum viable consensus
- Existential security
- Political pluralism
- Issue bundling
            """,
        )

    st.markdown("---")
    st.subheader("What Would Change My Mind?")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            <div class="sage-box">
                <h3>I would become more supportive of a global shutdown if...</h3>
                <p>
                    There were reproducible evidence that continued scaling was
                    producing autonomous replication, durable strategic deception,
                    independent resource acquisition, or AI systems capable of
                    accelerating frontier research without meaningful human
                    supervision.
                </p>
                <p>
                    I would also update if multiple technically and politically
                    independent groups converged on enforceable definitions,
                    credible verification methods, and a governance structure with
                    meaningful due-process protections.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class="blue-box">
                <h3>I would become less supportive of a global shutdown if...</h3>
                <p>
                    Capability growth repeatedly remained dependent on dense human
                    scaffolding, narrow deployment environments, and infrastructure
                    that could be reliably monitored, isolated, and revoked.
                </p>
                <p>
                    I would also update if staged deployment, interpretability,
                    external control systems, and international compute governance
                    demonstrated that dangerous capabilities could be bounded
                    without prohibiting broad areas of research.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.subheader("Looking Back")

    st.markdown(
        f"""
        <div class="burgundy-box">
            <h3>Where this chapter moved me</h3>
            <p>
                This chapter makes the book's position much easier to evaluate
                because it finally states what “taking the risk seriously” would
                require in practice.
            </p>
            <p>
                The authors are not proposing better model cards, voluntary safety
                commitments, or a more cautious race.
            </p>
            <p>
                They are proposing a worldwide prohibition backed by surveillance,
                inspection, economic coercion, cyber operations, and potentially
                military force.
            </p>
            <p>
                I agree with several premises underneath that conclusion. One
                responsible company cannot solve a global race. One national ban
                cannot contain a cross-border threat. Compute is more observable
                than intent. Algorithmic progress will weaken static hardware
                thresholds. And waiting for an unmistakable warning may mean
                waiting until prevention is no longer possible.
            </p>
            <p>
                Where I remain unconvinced is the assumption that the enforcement
                system can be treated as a neutral instrument.
            </p>
            <p>
                A global authority powerful enough to stop every prohibited AI
                project would itself become an unprecedented concentration of
                technical, political, and military power.
            </p>
            <p>
                That does not automatically make the proposal wrong.
            </p>
            <p>
                It means the governance system belongs inside the risk model.
                We cannot compare dangerous AI with an idealized shutdown regime.
                We have to compare it with the imperfect, strategic, error-prone,
                and potentially abusive institutions humans would actually build.
            </p>
            <p>
                The question I kept wanting to put in front of {you()} is not simply
                whether humanity could shut the race down.
            </p>
            <p>
                It is whether we could create enough power to enforce that shutdown
                without creating another system that no one can safely control.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )