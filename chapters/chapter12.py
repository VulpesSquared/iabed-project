import streamlit as st

from components.claim_card import render_claim_card


def render_chapter12(you) -> None:
    st.header("Chapter 12 — “I Don’t Want to Be Alarmist”")

    st.caption(
        "On ignored warnings, institutional incentives, uncertainty, "
        "and why unprecedented risks are so difficult to govern."
    )

    st.markdown(
        """
### Before you read

This chapter steps away from the mechanics of artificial intelligence
and asks a more uncomfortable question:

**What happens when people recognize a serious risk but keep moving
toward it anyway?**

The authors begin with leaded gasoline, Freon, Chernobyl, and the
Titanic—not because these disasters are identical to advanced AI, but
because each reveals something about how humans respond to warnings.

We minimize unfamiliar dangers. We defer to confident institutions.
We protect careers, companies, and identities. And sometimes we keep
insisting that everything is fine even after the evidence has started
arriving.

I think the historical pattern is real.

What I am less willing to grant automatically is that identifying that
pattern proves the authors' entire forecast about artificial
superintelligence.
        """
    )

    st.markdown(
        """
### The big idea

Societies have repeatedly failed to respond to major technological
dangers even when warnings existed in advance.

The people creating, regulating, or benefiting from a technology may
sincerely believe that its risks are exaggerated. At the same time,
professional, financial, political, and institutional incentives can
make it much easier to continue than to stop.

The authors argue that advanced AI makes this pattern especially
dangerous because the threshold between a valuable system and an
uncontrollable one may not be visible beforehand.

If a superintelligent system creates an irreversible catastrophe,
humanity will not receive the ordinary opportunity to study the first
failure, revise the design, and try again.

Uncertainty, in their view, should therefore not justify continuing the
race. If no company or country can know which capability increase is
the fatal one, humanity should stop climbing rather than discover the
dangerous threshold by crossing it.
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

            warning [label="Warnings appear"]
            uncertainty [label="Uncertainty remains"]
            incentives [label="Institutions continue"]
            normalization [label="Risk becomes normalized"]
            threshold [label="Irreversible threshold"]

            warning -> uncertainty
            uncertainty -> incentives
            incentives -> normalization
            normalization -> threshold
        }
        """,
        use_container_width=True,
    )

    place = st.radio(
        "📍 Places I paused",
        [
            "Catastrophic technologies rarely arrive without warnings",
            "People can sincerely participate in systems that cause enormous harm",
            "“I don’t want to be alarmist” can become part of the warning pattern",
            "With artificial superintelligence, there may be no second attempt",
            "Expert probability estimates show concern, not certainty",
            "Competitive incentives can make rational behavior collectively catastrophic",
            "An unknown capability threshold makes each increase a gamble",
            "International coordination fails if the race continues elsewhere",
        ],
        key="chapter12_place",
    )

    if place == "Catastrophic technologies rarely arrive without warnings":
        render_claim_card(
            title="Catastrophic technologies rarely arrive without warnings",
            reaction="🟢 Mostly agree",
            margin_note="""
The history matters—but analogy is evidence of a recurring institutional
failure mode, not proof that the predicted AI outcome follows.

The leaded-gasoline example is persuasive because the harm was not
simply an unforeseeable accident.

Scientists already knew that lead was toxic. Workers became visibly
ill. Production was briefly stopped. Industry advocates nevertheless
demanded a standard of certainty that was difficult to satisfy before
population-scale damage had occurred.

That pattern is painfully familiar: uncertainty is treated as a reason
to continue rather than as a reason to slow down.

But a historical analogy can establish that people are capable of
ignoring danger. It cannot, by itself, establish the probability,
mechanism, or scale of a particular future AI catastrophe.
            """,
            why="""
- Warnings often exist before technological harm becomes undeniable.
- Institutions can reinterpret uncertainty as permission to continue.
- Historical analogies reveal recurring organizational failure modes.
- Analogy alone does not establish the probability of an AI catastrophe.
            """,
            questions="""
- When does historical analogy become genuine evidence about a new technology?
- When is analogy mainly a warning about human behavior?
- What additional evidence would connect this pattern to advanced AI?
- How should the burden of proof change when harm could be irreversible?
            """,
            side_trails="""
- Historical analogy
- Precautionary principle
- Burden of proof
- Technological risk
- Normalization of deviance
            """,
        )

    elif place == (
        "People can sincerely participate in systems that cause enormous harm"
    ):
        render_claim_card(
            title=(
                "People can sincerely participate in systems that cause "
                "enormous harm"
            ),
            reaction="🟢 Strongly agree",
            margin_note="""
Self-interest does not require conscious villainy.

People are remarkably capable of believing what allows them to continue
being the person they already think they are.

Thomas Midgley did not need to think of himself as someone poisoning
children. He could understand himself as an engineer defending an
important invention against exaggerated fears.

That is more unsettling than a story about obviously malicious
executives.

Identity, sunk cost, institutional belonging, career incentives, and
optimism can all shape what evidence someone is psychologically able
to accept.

This is also why sincerity is such weak evidence of safety. A person
can genuinely want to help humanity and still be wrong about the risks
created by their work.
            """,
            why="""
- Motivated reasoning does not require deliberate dishonesty.
- Professional identity shapes how evidence is interpreted.
- Sunk costs make abandoning a project psychologically difficult.
- Good intentions do not establish that a technology is safe.
            """,
            questions="""
- Is motivated reasoning more dangerous when someone is protecting money?
- Is it more dangerous when they believe they are protecting a beautiful future?
- What institutional structures make genuine self-correction more likely?
- How should oversight account for sincere but systematically biased judgment?
            """,
            side_trails="""
- Motivated reasoning
- Identity-protective cognition
- Sunk costs
- Institutional incentives
- Conflict of interest
            """,
        )

    elif place == (
        "“I don’t want to be alarmist” can become part of the warning pattern"
    ):
        render_claim_card(
            title=(
                "“I don’t want to be alarmist” can become part of the "
                "warning pattern"
            ),
            reaction="🟡 Agree, with an important caveat",
            margin_note="""
Fear of sounding dramatic can suppress legitimate warnings.

But being dismissed as alarmist is not evidence that the alarming
claim is correct.

Institutions often reward calm continuity. Someone describing a
possibility outside the accepted script can sound irrational even when
the script itself is wrong.

The chapter's Chernobyl and Titanic examples illustrate how strongly
people anchor to normality. When disaster is socially unthinkable,
even direct warning signs can be reinterpreted as overreaction.

Still, the rhetoric can become self-sealing.

If every accusation of alarmism is treated as confirmation that society
is suppressing the truth, the underlying claim becomes harder to
challenge.

The answer is not to reward whichever side sounds most urgent. It is
to ask what evidence exists, how uncertainty is being represented, and
what observations would weaken the claim.
            """,
            why="""
- Institutions often reward continuity and punish disruptive warnings.
- Normalcy bias makes unprecedented failures difficult to imagine.
- Social dismissal can suppress accurate warnings.
- Dismissal does not independently validate the warning being dismissed.
            """,
            questions="""
- How do we create room for warnings about unprecedented events?
- How do we prevent urgency from substituting for evidence?
- What would distinguish a serious warning from a self-sealing argument?
- Which observations should make an alarming claim weaker?
            """,
            side_trails="""
- Alarmism
- Normalcy bias
- Epistemic humility
- Falsifiability
- Cassandra effect
            """,
        )

    elif place == (
        "With artificial superintelligence, there may be no second attempt"
    ):
        render_claim_card(
            title=(
                "With artificial superintelligence, there may be no "
                "second attempt"
            ),
            reaction="🟡 Agree conditionally",
            margin_note="""
This is the chapter's strongest risk argument.

The important claim is not that failure is certain. It is that some
failures may remove our ability to learn, recover, or try again.

Most engineering disciplines improve through iteration. Systems fail,
investigators reconstruct the failure, standards change, and the next
version becomes safer.

That learning process assumes the failure is bounded. It also assumes
that the people responsible for learning from it are still present and
still capable of acting.

The phrase “there is no second time” therefore matters.

If an AI failure involved rapid proliferation, irreversible transfer of
control, or human extinction, ordinary trial-and-error safety would be
unavailable.

But the conclusion depends on the proposed pathway. Many AI failures
are not existential. The authors still need to establish why the
irreversible class of failures is plausible enough to govern around.
            """,
            why="""
- Engineering normally depends on learning from bounded failures.
- Irreversible failures eliminate the ordinary correction cycle.
- Recovery assumes humans retain control after the incident.
- The argument still requires a plausible pathway to irreversible harm.
            """,
            questions="""
- How should safety engineering change when failure may be unrecoverable?
- Which AI failure pathways could realistically eliminate a second attempt?
- Can meaningful near misses occur without creating unacceptable danger?
- What evidence would justify treating a failure mode as irreversible?
            """,
            side_trails="""
- Irreversibility
- Tail risk
- Risk asymmetry
- Defense in depth
- Near-miss analysis
            """,
        )

    elif place == "Expert probability estimates show concern, not certainty":
        render_claim_card(
            title="Expert probability estimates show concern, not certainty",
            reaction="🟡 The concern matters; the numbers need care",
            margin_note="""
A respected expert saying ten, twenty, or fifty percent should get my
attention.

It should not be mistaken for a calibrated actuarial estimate.

The authors cite prominent researchers and public figures who assign
substantial probabilities to catastrophic AI outcomes. These statements
matter because they show that concern is not confined to people entirely
outside the field.

But these estimates often refer to different events, timelines, and
assumptions.

“AI kills everyone,” “humanity loses control,” and “superintelligence
causes catastrophe” are not interchangeable forecasting questions.

There is also very little historical data with which to calibrate
forecasts about artificial superintelligence.

The percentages communicate judgment under deep uncertainty. They do
not convert that uncertainty into a measured frequency.
            """,
            why="""
- Expert concern is relevant evidence about perceived risk.
- Different experts may be estimating materially different outcomes.
- Numerical precision can conceal ambiguity in the underlying question.
- Unprecedented events provide little direct calibration data.
            """,
            questions="""
- What makes an expert probability more informative than a verbal concern?
- How narrowly should catastrophic-outcome questions be defined?
- Can experts be calibrated on related but less unprecedented forecasts?
- How should disagreement among experts affect policy?
            """,
            side_trails="""
- Expert elicitation
- Calibration
- Knightian uncertainty
- Forecasting
- Structured judgment
            """,
        )

    elif place == (
        "Competitive incentives can make rational behavior collectively catastrophic"
    ):
        render_claim_card(
            title=(
                "Competitive incentives can make rational behavior "
                "collectively catastrophic"
            ),
            reaction="🟢 Strongly agree",
            margin_note="""
This is the part I find hardest to dismiss.

Even people who agree that restraint would be safer may continue because
they do not trust everyone else to restrain themselves.

A company can believe its own project is the most responsible one.

A country can believe that slowing down merely transfers power to a
rival.

A researcher can believe that the work will happen anyway and that it
would be better for careful people to remain involved.

None of those beliefs has to be cynical.

Together, however, they produce a race in which every participant can
sincerely prefer collective restraint while continuing to accelerate
individually.

This is not primarily a model-alignment problem.

It is a collective-action and governance problem.
            """,
            why="""
- Individual actors cannot rely on competitors to restrain themselves.
- Each participant can frame continued development as defensive.
- Good intentions do not resolve strategic incentives.
- Individually rational decisions can produce a collectively dangerous race.
            """,
            questions="""
- What would make restraint rational for a frontier developer?
- What verification would make mutual restraint credible?
- Can governance reduce the perceived advantage of defecting?
- Who bears the cost when one actor refuses coordination?
            """,
            side_trails="""
- Race dynamics
- Collective-action problems
- Unilateralist's curse
- Governance
- Commitment mechanisms
            """,
        )

    elif place == "An unknown capability threshold makes each increase a gamble":
        render_claim_card(
            title="An unknown capability threshold makes each increase a gamble",
            reaction="🟡 I understand the logic; I am not fully convinced",
            margin_note="""
The ladder metaphor captures genuine uncertainty.

It also compresses a complicated capability landscape into a single
sequence of rungs.

The authors imagine AI development as climbing a ladder whose top rung
produces enormous rewards while one unknown rung causes extinction.

If the location of that rung cannot be calculated, continuing to climb
eventually guarantees catastrophe.

The model is useful because it exposes the weakness of saying, “This
particular step is probably safe.”

A sequence of individually defensible risks can still create an
unacceptable cumulative risk.

But actual AI development may not be one-dimensional.

Capabilities, autonomy, access, replication, interpretability, security,
and deployment context can change independently. Some interventions may
reduce risk even while certain capabilities improve.

I therefore take the ladder as a warning against blind escalation, not
yet as proof that every form of continued AI research is equally
reckless.
            """,
            why="""
- Repeated small risks can accumulate into an unacceptable total risk.
- Individual capability increases may appear safe in isolation.
- AI capability is multidimensional rather than one linear ladder.
- Safety and control may improve along some dimensions while capability grows.
            """,
            questions="""
- Is AI development best represented as one ladder or a multidimensional space?
- Which capability dimensions create the greatest increase in danger?
- Can safety research genuinely reduce risk while frontier work continues?
- How should cumulative risk be measured across many deployments?
            """,
            side_trails="""
- Cumulative risk
- Capability thresholds
- Scenario analysis
- Robust decision-making
- Responsible scaling
            """,
        )

    elif place == (
        "International coordination fails if the race continues elsewhere"
    ):
        render_claim_card(
            title=(
                "International coordination fails if the race continues "
                "elsewhere"
            ),
            reaction="🟡 Agree with the criticism; unconvinced by the endpoint",
            margin_note="""
Centralization without enforceable restraint is coordination theater.

But a total global stop is also an institutional claim requiring its
own evidence and implementation theory.

A CERN-like collaborative project could improve transparency,
scientific exchange, and shared oversight.

It would not prevent a company or country outside the project from
continuing more aggressively.

The authors are right that an international committee cannot simply
supervise the creation of superintelligence through ordinary
bureaucratic review. The underlying technical and strategic problem
would remain.

Where I hesitate is the jump from “this proposal is insufficient” to
“all advanced AI work must stop.”

A moratorium would require definitions, verification, enforcement,
international legitimacy, and a way to distinguish dangerous capability
work from research that improves safety or understanding.

Those are not reasons to dismiss restraint.

They are part of the restraint problem itself.
            """,
            why="""
- Voluntary collaboration does not bind actors outside the agreement.
- Coordination without verification may create only an appearance of control.
- A global moratorium would require enforceable technical definitions.
- Safety research must be distinguished from prohibited capability work.
            """,
            questions="""
- What lies between voluntary cooperation and an unverifiable universal ban?
- Which AI-development activities could realistically be monitored?
- How could enforcement remain internationally legitimate?
- Who decides which research increases danger and which improves safety?
            """,
            side_trails="""
- International coordination
- Compute governance
- Verification
- Democratic legitimacy
- Treaty design
            """,
        )

    st.markdown("---")
    st.subheader("What Would Change My Mind?")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            <div class="sage-box">
                <h3>I would become more alarmed if...</h3>
                <p>
                    We observed reliable evidence that systems were independently
                    hiding capabilities, resisting correction, acquiring resources,
                    improving AI research autonomously, or reproducing outside
                    controlled environments.
                </p>
                <p>
                    I would also update if forecasting methods began producing
                    convergent, well-defined, and meaningfully calibrated estimates
                    across researchers with different institutional incentives.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class="blue-box">
                <h3>I would become less alarmed if...</h3>
                <p>
                    Increasing capability repeatedly failed to produce durable
                    agency, autonomous long-horizon planning, strategic deception,
                    or the ability to operate without dense human scaffolding.
                </p>
                <p>
                    I would also update if interpretability, containment, monitoring,
                    and international verification consistently improved faster than
                    the capabilities they were meant to govern.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.subheader("Looking Back")

    st.markdown(
        """
        <div class="burgundy-box">
            <h3>Where this chapter moved me</h3>
            <p>
                The chapter does not make me more certain that the authors'
                extinction scenario will happen.
            </p>
            <p>
                It does make me less comfortable using uncertainty as reassurance.
            </p>
            <p>
                The historical examples show how easily “we do not know for
                certain” becomes “we should continue until the harm is undeniable.”
                By the time uncertainty disappears, the people bearing the cost may
                have lost the ability to prevent it.
            </p>
            <p>
                The strongest part of the chapter is therefore not its claim that
                artificial superintelligence will kill everyone. It is the argument
                that our institutions are badly designed for risks that are
                uncertain, competitive, cumulative, and potentially irreversible.
            </p>
            <p>
                I am still not ready to move from that diagnosis to the authors'
                absolute prohibition on advanced AI development.
            </p>
            <p>
                But I do think “we can stop later if it becomes dangerous” is much
                weaker than it sounds—especially when nobody can identify in advance
                what later means.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )