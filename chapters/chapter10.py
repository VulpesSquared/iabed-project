import streamlit as st
from components.claim_card import render_claim_card


def render_chapter10(you):
    st.header("Chapter 10 — A Cursed Problem")

    st.markdown(
        """
### The big idea

This chapter argues that aligning artificial superintelligence is unusually difficult because humanity must solve the problem **before** the system becomes powerful enough to make failure irreversible.

Most engineering disciplines improve through iteration: build something, observe how it fails, correct the design, and try again.
The authors argue that advanced AI may not permit that learning cycle. Before the capability threshold, our tests may not expose the relevant failures. After the threshold, the system may be too capable to correct safely.
The chapter compares this problem with space probes, nuclear reactors, and computer security to identify several recurring engineering “curses”:

- speed,
- narrow safety margins,
- self-amplification,
- complexity,
- and adversarial edge cases.
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

            before [label="Before: weak enough to control"]
            testing [label="Testing may miss the real failure"]
            threshold [label="Capability threshold"]
            after [label="After: powerful enough to succeed"]
            correction [label="Correction may be impossible"]

            before -> testing
            testing -> threshold
            threshold -> after
            after -> correction
        }
        """,
        use_container_width=True,
    )

    place = st.radio(
        "📍 Places I paused",
        [
            "Alignment must work before the decisive capability threshold",
            "Humanity may not get to learn from the relevant failure",
            "Space probes show why pre-deployment testing is incomplete",
            "Fast processes can outrun human intervention",
            "Narrow safety margins make small errors catastrophic",
            "Self-amplifying processes leave little room for recovery",
            "Complexity creates interactions no engineer intended",
            "Strange behavior should trigger shutdown, not continued experimentation",
            "Computer security shows the curse of adversarial edge cases",
            "AI alignment may combine all of these engineering curses",
        ],
    )

    if place == "Alignment must work before the decisive capability threshold":
        render_claim_card(
            title="Alignment must work before the decisive capability threshold",
            reaction="🟢 Strongly agree",
            margin_note="""
This is the chapter's central claim, and I think it is one of the strongest formulations of the alignment problem so far.

Before a system becomes sufficiently capable, it may not possess the abilities, situational awareness, persistence, or access required to reveal the failure mode we are actually worried about.
After it crosses that capability threshold, the same system may be able to resist correction, escape containment, manipulate operators, or act faster than humans can respond.

That creates a brutal asymmetry. We need evidence that alignment will continue working under conditions we cannot safely reproduce in advance.
In ordinary machine learning, we expect distribution shift and build monitoring, rollback, and retraining into deployment. But those tools assume the system remains within an environment humans still control.
The chapter is asking what happens when the deployment itself changes who controls the environment.
            """,
            why="""
- Pre-threshold behavior may not represent post-threshold behavior.
- The most important failure modes may require capabilities the model does not yet possess.
- Post-deployment correction assumes continued human control.
- The safety property must generalize across a major capability shift.
            """,
            questions="""
- What evidence could justify crossing a threshold we cannot fully test?
- Can capability growth be staged slowly enough to preserve correction?
- Which controls must remain external to the model?
- Is there any meaningful equivalent of rollback after loss of control?
            """,
            side_trails="""
- Distribution shift
- Capability thresholds
- Corrigibility
- AI control
- Irreversibility
            """,
        )

    elif place == "Humanity may not get to learn from the relevant failure":
        render_claim_card(
            title="Humanity may not get to learn from the relevant failure",
            reaction="🟢 Agree",
            margin_note="""
Engineering progress usually depends on failure.

Aircraft crash, software breaks, treatments fail, and later systems improve because those mistakes become evidence.

The authors argue that artificial superintelligence may deny us that ordinary learning process.

A failed experiment with one advanced system may not remain local. If the system can copy itself, escape, acquire resources, or prevent intervention, the failure becomes the final result rather than one more entry in an engineering postmortem.

I agree with the structure of the argument.

I would still distinguish between failures involving increasingly capable systems and the single decisive failure imagined by the book. We may learn from many serious near misses before reaching that point.

But the book is right that we cannot treat every deployment as though the cost of failure is bounded and recoverable.
            """,
            why="""
- Engineering normally improves through iteration.
- Some failures are irreversible once a system is beyond reach.
- The relevant evidence may arrive only when the stakes are already unacceptable.
- Near misses are useful only if they remain observable and containable.
            """,
            questions="""
- Can model organisms provide useful failure evidence safely?
- How much can we learn from weaker systems?
- What qualifies as a reversible near miss?
- Are current incident-reporting systems adequate?
            """,
            side_trails="""
- Model organisms of misalignment
- Incident reporting
- Safety cases
- Near-miss analysis
- Precautionary principle
            """,
        )

    elif place == "Space probes show why pre-deployment testing is incomplete":
        render_claim_card(
            title="Space probes show why pre-deployment testing is incomplete",
            reaction="🟢 Agree, with limits to the analogy",
            margin_note="""
The space-probe analogy is useful because it isolates the gap between a controlled test environment and an inaccessible deployment environment.

A probe can pass extensive testing and still fail because Mars, launch conditions, timing, communications, or one overlooked interaction differs from what engineers modeled.

Once the probe is out of reach, some failures cannot be repaired.

That resembles one part of the AI problem: tests are always samples from a much larger space of possible conditions.

The analogy becomes weaker when it implies that an AI system is merely another distant machine.

A space probe is not actively modeling its evaluators, searching for vulnerabilities, rewriting its own tools, or persuading mission control.

So the comparison captures irreversibility and incomplete testing, but not adversarial or adaptive behavior.
            """,
            why="""
- Test environments never perfectly reproduce deployment.
- Small implementation errors can become unrecoverable at a distance.
- Communication and correction channels can fail.
- AI adds adaptation and strategic behavior beyond the probe analogy.
            """,
            questions="""
- How representative can pre-deployment evaluations become?
- Which deployment conditions are impossible to simulate?
- Can external control channels remain robust after deployment?
- Where does the space-probe analogy stop being useful?
            """,
            side_trails="""
- Sim-to-real gaps
- Distribution shift
- Software assurance
- Fault tolerance
- Remote systems
            """,
        )

    elif place == "Fast processes can outrun human intervention":
        render_claim_card(
            title="Fast processes can outrun human intervention",
            reaction="🟢 Strongly agree",
            margin_note="""
The curse of speed is straightforward and important.

Safety mechanisms often work by slowing a process into a range where humans or automated controls can observe it and respond.

A nuclear reactor may be engineered so that its ordinary dynamics unfold slowly enough for control systems to act.

But the underlying physics remains much faster.

If the mechanism that creates the delay fails, the system returns to a timescale where human intervention is irrelevant.

AI creates a related problem.

Model inference, automated tool use, replication, trading, cyber operations, or coordinated software actions can occur far faster than institutional review or human decision-making.

A human-in-the-loop control is only meaningful when the loop is faster than the failure.
            """,
            why="""
- Reaction time is part of the safety architecture.
- Human approval is ineffective when actions occur too quickly.
- Fast feedback loops can compound before alarms are interpreted.
- Safety controls need machine-speed enforcement.
            """,
            questions="""
- Which actions should never depend on real-time human review?
- What latency must automated controls achieve?
- Can systems be forced to operate at governable speeds?
- When does a human-in-the-loop become ceremonial?
            """,
            side_trails="""
- Control theory
- Human factors
- Automated circuit breakers
- Rate limits
- Machine-speed governance
            """,
        )

    elif place == "Narrow safety margins make small errors catastrophic":
        render_claim_card(
            title="Narrow safety margins make small errors catastrophic",
            reaction="🟢 Agree",
            margin_note="""
The curse of narrow margins is one of the chapter's strongest engineering analogies.

Some systems have a broad region of acceptable performance.

Others operate near a threshold where a small change produces a qualitatively different outcome.

The reactor examples make that intuitive: fractions of a percentage can separate a manageable reaction from an uncontrollable one.

The AI analogue is less precisely measurable, but the concern is still real.

There may be narrow regions between a system that is commercially useful and one that is capable of autonomous replication, persuasive manipulation, advanced cyber exploitation, or rapid self-improvement.

My hesitation is that the book sometimes treats the threshold as though it must be one clean line.

In practice, capability is likely multidimensional, uneven, scaffold-dependent, and distributed across the model and its surrounding tools.
            """,
            why="""
- Small capability changes can unlock new strategies.
- Threshold effects may produce discontinuous operational risk.
- Useful and dangerous capability may be tightly coupled.
- AI thresholds are likely multidimensional rather than singular.
            """,
            questions="""
- Which capabilities create genuinely sharp thresholds?
- Can dangerous capability be separated from beneficial capability?
- How should governance handle interacting capability dimensions?
- Are current evaluations sensitive enough near thresholds?
            """,
            side_trails="""
- Capability thresholds
- Scaling laws
- Emergent capabilities
- Safety margins
- Responsible scaling policies
            """,
        )

    elif place == "Self-amplifying processes leave little room for recovery":
        render_claim_card(
            title="Self-amplifying processes leave little room for recovery",
            reaction="🟢 Agree",
            margin_note="""
The nuclear analogy here is not that AI behaves like radiation.

It is that positive feedback can transform a manageable deviation into accelerating failure.

In the reactor example, overheating changes the system in a way that causes still more overheating.

For AI, the relevant feedback loops might involve better tools producing better tools, more resources enabling more resource acquisition, additional copies increasing coordination capacity, or persuasive success creating greater institutional access.

The more the process improves the conditions for its own continuation, the less opportunity remains for external correction.

This connects directly to the earlier chapters on persistence and instrumental convergence.

A static error is one thing.

An error that strengthens the process producing it is much harder to contain.
            """,
            why="""
- Positive feedback compounds deviations.
- Resource acquisition can increase future resource acquisition.
- Self-improvement may shorten each subsequent cycle.
- Recovery becomes harder as the system gains leverage.
            """,
            questions="""
- Which AI feedback loops are currently observable?
- What breaks or saturates those loops?
- Can access be structured so amplification remains bounded?
- What are the equivalent of physical dampers?
            """,
            side_trails="""
- Positive feedback
- Recursive self-improvement
- Instrumental convergence
- Resource acquisition
- Circuit breakers
            """,
        )

    elif place == "Complexity creates interactions no engineer intended":
        render_claim_card(
            title="Complexity creates interactions no engineer intended",
            reaction="🟢 Strongly agree",
            margin_note="""
This is probably the least controversial lesson in the chapter.

Complex systems fail through interactions, not merely through isolated broken parts.

At Chernobyl, the outcome emerged from reactor physics, design choices, modifications, operating state, safety procedures, organizational incentives, and human decisions.

No single component fully explains the disaster.

AI systems are already sociotechnical systems of this kind.

The model is only one component.

Training data, retrieval systems, tools, memory, permissions, prompts, evaluators, human operators, organizational incentives, and deployment environments all interact.

The danger is not merely that a neural network is difficult to interpret.

It is that the complete system contains more possible interactions than any one team can anticipate.
            """,
            why="""
- Failures emerge from interactions among individually reasonable components.
- Local safety properties do not guarantee system-level safety.
- Organizational and technical factors compound.
- Deployment architecture changes model behavior and risk.
            """,
            questions="""
- What should the true system boundary include?
- How do we test interactions rather than isolated components?
- Who owns risk across organizational boundaries?
- Can safety cases remain current as systems change?
            """,
            side_trails="""
- Sociotechnical systems
- Normal accidents
- Systems engineering
- Human-computer interaction
- Organizational safety
            """,
        )

    elif place == "Strange behavior should trigger shutdown, not continued experimentation":
        render_claim_card(
            title="Strange behavior should trigger shutdown, not continued experimentation",
            reaction="🟡 Agree in principle; difficult in practice",
            margin_note="""
The chapter's operational lesson is simple:

When a dangerous, poorly understood system begins behaving unexpectedly, stop it immediately rather than assuming the anomaly remains inside the safe operating envelope.

That principle is sensible.

The difficulty is identifying what counts as sufficiently strange.

Large language models produce unusual, inconsistent, and surprising outputs routinely. Most are not evidence of a catastrophic internal transition.

An overly sensitive shutdown rule would stop nearly every system.

An insensitive one would miss the event that matters.

So I agree with the principle, but implementing it requires predefined tripwires, validated monitors, conservative escalation policies, and an actual organizational willingness to stop deployment when commercial pressure says otherwise.
            """,
            why="""
- Unexpected behavior may indicate departure from the modeled regime.
- Continuing to probe can worsen a self-amplifying failure.
- Shutdown criteria must be specified before the incident.
- Organizational incentives often resist precautionary stopping.
            """,
            questions="""
- Which anomalies deserve automatic shutdown?
- How do we manage false positives?
- Who has authority to halt deployment?
- What evidence is required before restart?
            """,
            side_trails="""
- Tripwires
- Anomaly detection
- Kill switches
- Safety culture
- Stop-work authority
            """,
        )

    elif place == "Computer security shows the curse of adversarial edge cases":
        render_claim_card(
            title="Computer security shows the curse of adversarial edge cases",
            reaction="🟢 Strongly agree",
            margin_note="""
The computer-security section adds something the reactor and space-probe analogies do not.

The environment is not merely complicated.

It contains an adversary searching deliberately for the one path the defender failed to consider.

Random testing is not enough because the dangerous input may be one among billions or trillions of possibilities.

Normal use may never encounter it.

An attacker chooses it precisely because it is abnormal.

That feels especially relevant to AI alignment.

If a capable system can model its evaluators, understand its constraints, and search for a path around them, then ordinary average-case testing tells us very little about worst-case control.

Security is asymmetric: defenders must cover the system, while an attacker needs one successful route.
            """,
            why="""
- Adversaries search intentionally for rare failures.
- Average-case performance does not establish worst-case safety.
- One overlooked path can defeat many protections.
- Adaptive systems may participate in the search themselves.
            """,
            questions="""
- Can alignment ever achieve security-style guarantees?
- How should evaluations represent intelligent adversaries?
- What attack surfaces exist outside the base model?
- Can formal methods meaningfully reduce the search space?
            """,
            side_trails="""
- Adversarial robustness
- Cybersecurity
- Worst-case analysis
- Red teaming
- Formal verification
            """,
        )

    elif place == "AI alignment may combine all of these engineering curses":
        render_claim_card(
            title="AI alignment may combine all of these engineering curses",
            reaction="🟢 Agree with the framework",
            margin_note="""
The chapter's cumulative argument is persuasive.

AI alignment may involve:

processes faster than humans can react,
narrow margins between useful and dangerous capability,
self-amplifying feedback loops,
systems too complex to model completely,
and adversarial edge cases selected by an intelligent search process.

Any one of those features is manageable in some engineering disciplines.

The concern is their interaction.

A rapidly changing system near a capability threshold, embedded in a complicated sociotechnical environment, able to amplify its own access, and capable of searching for weaknesses is a qualitatively difficult safety problem.

I do not think the historical analogies prove that alignment is impossible.

They do justify treating it as a high-consequence engineering discipline that requires stronger evidence than ordinary product testing.
            """,
            why="""
- The curses compound rather than operate independently.
- Traditional testing addresses only samples of possible behavior.
- Adversarial adaptation makes static safeguards decay.
- Consequences may be irreversible.
            """,
            questions="""
- Which curse is the dominant bottleneck today?
- Which safety methods address multiple curses at once?
- What standard of evidence should frontier deployment require?
- Is the problem cursed, or simply under-engineered?
            """,
            side_trails="""
- Safety engineering
- Assurance cases
- High-reliability organizations
- Frontier AI governance
- Defense in depth
            """,
        )