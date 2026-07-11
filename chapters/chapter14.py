import streamlit as st

from components.claim_card import render_claim_card


def render_chapter14(you) -> None:
    st.header("Chapter 14 — Where There’s Life, There’s Hope")

    st.caption(
        "On uncertain survival, nuclear near misses, political action, "
        "public courage, and choosing hope without pretending the danger is small."
    )

    st.markdown(
        """
### Before you read

The final chapter begins with someone who survived what should have been
unsurvivable.

Vesna Vulović fell more than six miles after an airplane was destroyed
in flight. Any reasonable prediction made beforehand would have said
that she would die.

She lived.

The story gives the chapter its title and its emotional center:
prediction is not destiny while someone is still alive to change the
outcome.

The authors do not soften their central claim. They still believe that
building artificial superintelligence will kill everyone, regardless of
who builds it or how benevolent its creators intend to be.

But this chapter is less interested in repeating the technical argument
than in asking what people should do after hearing it.

Its answer is not passive optimism.

Governments should negotiate. Politicians should prepare the legal
ground. Journalists should investigate. Citizens should speak, vote,
organize, and make concern visible.

And after doing what we can, we should continue living recognizably human
lives rather than allowing fear to consume the entire future we are
trying to protect.

I find that final distinction important.

Hope is not confidence that everything will work out.

Hope is the belief that the outcome is still responsive to action.
        """
    )

    st.markdown(
        """
### The big idea

The authors restate the book's core argument as directly as possible:

If anyone builds artificial superintelligence, everyone dies.

They argue that continued AI escalation should not require critics to
predict the exact date, mechanism, and sequence of catastrophe. In other
high-consequence engineering domains, placing all of humanity at risk
would require evidence that disaster is extremely unlikely—not merely
the observation that critics cannot prove precisely how it will occur.

The chapter then turns to the nuclear age.

After World War II, many informed observers reasonably expected that
nuclear war would eventually destroy civilization. They were wrong about
what humanity would choose, not necessarily about what nuclear weapons
could do.

Nuclear catastrophe was avoided because people treated the trajectory
toward destruction as something that could be changed. Governments built
communication channels, negotiated treaties, monitored weapons, and
worked repeatedly to prevent individual mistakes from becoming an
irreversible war.

The authors argue that AI requires the same seriousness.

Their final message is directed toward different groups: government
leaders, elected officials, uncertain politicians, journalists, and
ordinary citizens. Each has a role in creating the political conditions
for international restraint.

The chapter ends by holding two ideas together:

Humanity may fail.

Humanity can still act.
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

            trajectory [label="A catastrophic trajectory\\nlooks increasingly plausible"]
            recognition [label="People recognize that\\nthe trajectory is not fate"]
            institutions [label="Institutions, treaties,\\nand safeguards are built"]
            public [label="Citizens make action\\npolitically possible"]
            uncertainty [label="The outcome remains\\nuncertain"]
            hope [label="Uncertainty leaves room\\nfor deliberate action"]

            trajectory -> recognition
            recognition -> institutions
            institutions -> public
            public -> uncertainty
            uncertainty -> hope
        }
        """,
        use_container_width=True,
    )

    place = st.radio(
        "📍 Places I paused",
        [
            "An outcome can be highly predictable without being inevitable",
            "The burden of proof should change when all of humanity is exposed",
            "Nuclear war was avoided because people worked to change the trajectory",
            "Human survival depends on institutions, not one heroic intervention",
            "Political leaders may be more persuadable than public silence suggests",
            "Unconvinced officials can still preserve the option to act later",
            "Journalism helps society understand risks before they become disasters",
            "Ordinary people matter by changing what leaders believe is politically possible",
            "Living under existential risk should not mean surrendering ordinary life",
            "Hope is a commitment to action, not a prediction of success",
        ],
        key="chapter14_place",
    )

    if place == (
        "An outcome can be highly predictable without being inevitable"
    ):
        render_claim_card(
            title="An outcome can be highly predictable without being inevitable",
            reaction="🟢 Strongly agree",
            margin_note="""
The story of Vesna Vulović is a useful opening because it separates
prediction from certainty.

Before the fall, nearly any reasonable model would have assigned her
almost no chance of survival.

That prediction would have been rational.

It also would have been wrong.

Rare survival does not mean that falling from an airplane is secretly
safe. It means that even excellent predictions describe a distribution
of possible outcomes rather than writing the future into existence.

The same distinction matters in the opposite direction.

A catastrophic trajectory can be alarming even when catastrophe is not
guaranteed.

The chapter's use of the story works best when it reminds us that
uncertainty leaves room for intervention.

It works less well if it is taken to mean that an extraordinary escape
from danger is a substitute for preventing the danger in the first place.
            """,
            why="""
- Rational forecasts can still be wrong in individual cases.
- Low probability is not the same as impossibility.
- A dangerous trajectory can remain responsive to intervention.
- Exceptional survival does not make the underlying hazard acceptable.
            """,
            questions="""
- When should uncertainty motivate prevention rather than reassurance?
- How do we distinguish genuine hope from dependence on a miracle?
- Can a forecast be actionable even when its confidence is poorly calibrated?
- What does it mean to change a trajectory rather than merely survive it?
            """,
            side_trails="""
- Probabilistic forecasting
- Tail events
- Survivorship bias
- Counterfactual reasoning
- Hope under uncertainty
            """,
        )

    elif place == (
        "The burden of proof should change when all of humanity is exposed"
    ):
        render_claim_card(
            title=(
                "The burden of proof should change when all of humanity "
                "is exposed"
            ),
            reaction="🟢 Agree with the principle",
            margin_note="""
The authors argue that they should not have to predict every detail of
the disaster before society takes the risk seriously.

I agree with the underlying engineering principle.

If a rocket carried every living human, the launch standard would not be
“critics have failed to prove exactly how it will explode.”

The designers would need extraordinary evidence that the system was safe.

Scale and irreversibility should change the burden of proof.

A system with bounded consequences can reasonably be deployed under
uncertainty and improved through experience.

A system that could impose irreversible harm on everyone should face a
much higher evidentiary standard.

My hesitation is that this principle does not resolve the empirical
dispute by itself.

Before reversing the burden of proof, we still need a defensible account
of why a proposed AI system belongs in the category of civilization-scale
hazards.

The authors believe the entire book establishes that bridge.

I think parts of the bridge are strong, while other parts remain
conditional on assumptions about agency, autonomy, strategic behavior,
and control.
            """,
            why="""
- Safety standards should reflect the scale and reversibility of harm.
- Critics cannot always predict the exact mechanism of a novel failure.
- Developers should carry more responsibility when others cannot opt out.
- The high-consequence category still requires an evidence-based definition.
            """,
            questions="""
- What evidence places an AI system in the civilization-scale risk category?
- How should uncertainty affect the burden carried by developers?
- Who represents people exposed to a risk they did not consent to?
- What would constitute affirmative evidence of sufficient safety?
            """,
            side_trails="""
- Burden of proof
- Safety cases
- Catastrophic risk
- Informed consent
- Precautionary principle
            """,
        )

    elif place == (
        "Nuclear war was avoided because people worked to change the trajectory"
    ):
        render_claim_card(
            title=(
                "Nuclear war was avoided because people worked to "
                "change the trajectory"
            ),
            reaction="🟢 Strongly agree",
            margin_note="""
The nuclear section is the strongest source of hope in the chapter.

People who expected nuclear war were not necessarily confused about the
weapons.

They correctly understood that cities could be destroyed, radiation
could kill indiscriminately, defenses could fail, and a single
miscalculation could escalate into something civilization might not
survive.

What they underestimated was humanity's ability to respond to the
danger.

The absence of full-scale nuclear war was not produced by one reassuring
fact about nuclear weapons.

It was produced by decades of diplomacy, monitoring, arms control,
communication systems, military procedures, public pressure, individual
judgment, and repeated luck.

The Cuban Missile Crisis is especially uncomfortable because it shows
both sides of the story.

Humanity created systems capable of bringing us terrifyingly close to
destruction.

Individual people and institutions also prevented the machinery from
completing the trajectory.

That is not evidence that everything naturally works out.

It is evidence that trajectories can be unwritten through sustained,
deliberate work.
            """,
            why="""
- The technical danger of nuclear weapons was real even though global war was avoided.
- Avoidance resulted from repeated institutional and individual intervention.
- Communication and verification reduced the chance of uncontrolled escalation.
- A predicted catastrophe may fail to occur because people act on the prediction.
            """,
            questions="""
- Which nuclear-risk institutions have meaningful analogues in AI governance?
- Which features of AI make the analogy weaker?
- How much of nuclear survival came from design, diplomacy, individuals, or luck?
- Can AI governance be built before a crisis creates broad political attention?
            """,
            side_trails="""
- Nuclear command and control
- Cuban Missile Crisis
- Arms-control treaties
- Vasili Arkhipov
- Self-negating predictions
            """,
        )

    elif place == (
        "Human survival depends on institutions, not one heroic intervention"
    ):
        render_claim_card(
            title=(
                "Human survival depends on institutions, not one "
                "heroic intervention"
            ),
            reaction="🟢 Strongly agree",
            margin_note="""
Stories about survival often concentrate on one person who made the
right decision at the decisive moment.

Those people matter.

But designing safety around the hope that one unusually wise person will
be present is not a serious control strategy.

Nuclear war was not avoided only because of one submarine officer, one
president, or one negotiator.

It was also avoided because there were treaties, monitors, command
procedures, diplomatic channels, verification systems, and people whose
full-time work was preventing individual errors from escalating.

The same should be true for AI.

We should not depend on one conscientious researcher refusing to train a
model, one executive choosing safety over competition, or one employee
raising an alarm.

Institutions should make the safe action ordinary rather than heroic.

The difficulty is that AI governance institutions remain immature while
the technological and commercial systems they would govern are moving
quickly.
            """,
            why="""
- Heroic intervention is unreliable and difficult to reproduce.
- Institutions preserve safety across changes in personnel.
- Communication and verification reduce dependence on individual judgment.
- Durable governance turns exceptional restraint into standard procedure.
            """,
            questions="""
- Which AI safety decisions currently depend on individual courage?
- What institutions would make those choices less personally costly?
- How should whistleblowers and dissenting researchers be protected?
- What must remain independent from companies developing the technology?
            """,
            side_trails="""
- High-reliability organizations
- Institutional design
- Whistleblower protection
- Safety culture
- Defense in depth
            """,
        )

    elif place == (
        "Political leaders may be more persuadable than public silence suggests"
    ):
        render_claim_card(
            title=(
                "Political leaders may be more persuadable than public "
                "silence suggests"
            ),
            reaction="🟢 Agree, cautiously",
            margin_note="""
The chapter suggests that some elected officials understand the concern
but hesitate to say so publicly because the position sounds strange,
extreme, or professionally risky.

That seems plausible.

Public silence is not reliable evidence of private disbelief.

Politicians respond to incentives, coalitions, perceived voter interest,
institutional norms, and the range of positions that can be expressed
without ridicule.

An issue can therefore remain politically invisible even when many
individual decision-makers are privately concerned.

That creates a coordination problem.

Officials wait for public permission.

Citizens wait for officials to treat the issue seriously.

Journalists wait for prominent institutions to legitimize the story.

Experts soften their language so they are not dismissed.

Everyone may be waiting for everyone else to move first.

I do not know how common private concern actually is.

But I agree that making concern socially legible can change what leaders
believe they are allowed to do.
            """,
            why="""
- Public positions do not always reveal private judgments.
- Political actors respond to perceived constituent concern.
- Fear of ridicule can suppress discussion of unfamiliar risks.
- Visible coalitions make previously marginal policies easier to consider.
            """,
            questions="""
- How can private concern be converted into credible public coordination?
- What evidence would show that officials are genuinely open to stronger action?
- How should advocates avoid overstating the level of hidden agreement?
- What makes an unusual risk politically discussable?
            """,
            side_trails="""
- Preference falsification
- Political signaling
- Policy entrepreneurship
- Public opinion
- Coordination problems
            """,
        )

    elif place == (
        "Unconvinced officials can still preserve the option to act later"
    ):
        render_claim_card(
            title=(
                "Unconvinced officials can still preserve the option "
                "to act later"
            ),
            reaction="🟢 Strongly agree",
            margin_note="""
This is one of the most pragmatic arguments in the chapter.

An official does not need to accept the authors' entire extinction
forecast in order to preserve humanity's ability to respond if the
evidence becomes stronger.

Governments can create chip registries, reporting requirements,
international monitoring frameworks, research access, audit authority,
and legal mechanisms before they decide to use the strongest forms of
restraint.

That is option preservation.

It recognizes that future policymakers may understand more than current
policymakers do.

The goal is not necessarily to slam on the brakes today.

It is to make sure the brakes still exist tomorrow.

I find this much easier to support than the claim that the complete
global prohibition proposed in Chapter 13 is already fully specified and
ready to implement.

Institutional preparation can be justified under a broader range of
beliefs about the eventual level of danger.
            """,
            why="""
- Preparation does not require certainty about the worst-case forecast.
- Monitoring systems create information needed for later decisions.
- Legal authority is difficult to build during an active emergency.
- Preserving future options is valuable under deep uncertainty.
            """,
            questions="""
- Which policies preserve options without prematurely imposing a global shutdown?
- What infrastructure would future enforcement require?
- Can preparatory powers be prevented from expanding into unrelated surveillance?
- Which decisions become impossible if governments wait several more years?
            """,
            side_trails="""
- Option value
- Adaptive governance
- Regulatory capacity
- Compute monitoring
- Reversible policy
            """,
        )

    elif place == (
        "Journalism helps society understand risks before they become disasters"
    ):
        render_claim_card(
            title=(
                "Journalism helps society understand risks before they "
                "become disasters"
            ),
            reaction="🟢 Strongly agree",
            margin_note="""
The chapter is right that journalism has a distinct role here.

AI coverage often oscillates between product spectacle, executive
personality, investment enthusiasm, labor panic, and dramatic claims
that receive little technical examination.

Serious risk coverage requires something slower.

It requires investigating company practices, institutional incentives,
employee departures, evaluation results, governance failures, technical
disagreements, and the assumptions underneath catastrophic forecasts.

Journalists should not simply repeat the authors' conclusion.

They should investigate it.

They should also avoid treating the conclusion as inherently unserious
because it sounds socially unusual.

The job is not to make extinction risk popular.

The job is to determine which claims are supported, which are disputed,
which institutions have conflicts of interest, and what evidence the
public is not currently seeing.

This is especially important because the people building the systems are
also shaping much of the public story about what those systems are and
where they are going.
            """,
            why="""
- Public understanding depends on sustained investigation rather than product coverage.
- Companies possess information and incentives that outsiders may not share.
- Unfamiliar claims can be dismissed socially before being evaluated evidentially.
- Journalism can expose disagreements, incentives, incidents, and hidden assumptions.
            """,
            questions="""
- What would rigorous AI-risk journalism investigate first?
- How should journalists represent uncertainty without flattening disagreement?
- Which claims require independent technical replication?
- How can coverage avoid both corporate hype and uncritical catastrophe narratives?
            """,
            side_trails="""
- Investigative journalism
- Risk communication
- Corporate accountability
- Science reporting
- Epistemic institutions
            """,
        )

    elif place == (
        "Ordinary people matter by changing what leaders believe is politically possible"
    ):
        render_claim_card(
            title=(
                "Ordinary people matter by changing what leaders believe "
                "is politically possible"
            ),
            reaction="🟢 Agree",
            margin_note="""
The chapter does not ask individual people to solve alignment or boycott
every AI tool. That is sensible.

Individual consumer purity would impose substantial costs on a person
while doing very little to change a global technological race.

The authors instead emphasize civic action: contacting representatives,
voting, speaking publicly, organizing, supporting institutions, and
making concern visible.

The mechanism is political permission.
A letter does not create a treaty. A protest does not design a verification system. A conversation does not shut down a datacenter.

But collective visibility changes what officials believe their
constituents will tolerate, support, or punish.

That matters most when leaders are privately uncertain and waiting for a
signal that action will not end their careers.

I would still be careful not to imply that public awareness alone solves
the institutional problem.

It helps create the conditions under which technical and diplomatic work
can proceed.
            """,
            why="""
- Individual consumption choices have little leverage over a global race.
- Collective political expression can alter leaders' incentives.
- Public visibility reduces the social cost of discussing unfamiliar risks.
- Civic action supports but does not replace technical governance.
            """,
            questions="""
- Which forms of civic action have the greatest policy leverage?
- What should citizens ask their representatives to do specifically?
- How can concern be organized without amplifying misinformation?
- How do movements preserve credibility when the evidence remains uncertain?
            """,
            side_trails="""
- Civic participation
- Collective action
- Social movements
- Constituent pressure
- Political legitimacy
            """,
        )

    elif place == (
        "Living under existential risk should not mean surrendering ordinary life"
    ):
        render_claim_card(
            title=(
                "Living under existential risk should not mean surrendering "
                "ordinary life"
            ),
            reaction="🟢 Strongly agree",
            margin_note="""
The C. S. Lewis passage gives the chapter something the rest of the book
often lacks: a theory of how to remain human while taking danger
seriously.

Fear can become totalizing.

A person can spend so much time imagining the future's destruction that
they stop inhabiting the life they are supposedly trying to protect.

That does not improve the forecast.

It does not strengthen institutions.

It does not make thoughtful action more likely.

The answer is not denial.

Lewis was not arguing that atomic weapons were imaginary or harmless.
He was arguing against reorganizing one's entire inner life around the
terror.

Do the work.

Speak.

Vote.

Build.

Prepare.

Then read, teach, make dinner, listen to music, care for people, walk the
dogs, argue about books, and remain present.

A future worth saving has to be practiced before it is secured.
            """,
            why="""
- Chronic fear can narrow attention and reduce effective action.
- Ordinary life embodies the values that safety efforts are meant to protect.
- Denial and total preoccupation are not the only available responses.
- Sustained civic work requires psychological endurance.
            """,
            questions="""
- How do we remain informed without becoming consumed?
- What does proportionate concern look like in daily life?
- Can joy be part of resilience rather than avoidance?
- How should communities support people working on catastrophic risks?
            """,
            side_trails="""
- C. S. Lewis
- Existential anxiety
- Resilience
- Meaning under threat
- Sustainable activism
            """,
        )

    elif place == "Hope is a commitment to action, not a prediction of success":
        render_claim_card(
            title="Hope is a commitment to action, not a prediction of success",
            reaction="🟢 Strongly agree",
            margin_note="""
This is where I land at the end of the book.

Hope is not the assertion that the authors must be wrong.

It is not confidence that governments will coordinate, companies will
restrain themselves, or technical researchers will solve alignment in
time.

It is also not the belief that a rare survival story guarantees another
one.

Hope is the refusal to treat the current trajectory as completed history.

The authors ask whether enough people doing their part would be enough.

Their answer is honest: perhaps, perhaps not.

That uncertainty is not a reason to do nothing.

It is the condition that makes action meaningful.

If the outcome were guaranteed, hope would be unnecessary.

If nothing could affect the outcome, action would be pointless.

Hope lives between certainty and futility.
            """,
            why="""
- Hope does not require confidence that success is likely.
- Action matters only when the future remains unsettled.
- Uncertainty can create responsibility rather than passivity.
- Collective effort may change a trajectory even without guaranteeing an outcome.
            """,
            questions="""
- What distinguishes disciplined hope from optimism?
- How much uncertainty is required before action becomes worthwhile?
- Can people coordinate around hope without claiming false confidence?
- What responsibilities follow from believing that the trajectory is still changeable?
            """,
            side_trails="""
- Active hope
- Moral responsibility
- Collective efficacy
- Radical uncertainty
- Agency
            """,
        )

    st.markdown("---")
    st.subheader("What Would Change My Mind?")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            <div class="sage-box">
                <h3>I would become more persuaded by the book if...</h3>
                <p>
                    Evidence increasingly showed that capability growth reliably
                    produces autonomous long-horizon planning, strategic deception,
                    independent replication, resource acquisition, and the ability
                    to accelerate AI research without dense human scaffolding.
                </p>
                <p>
                    I would also update if technically independent researchers
                    converged on the same causal pathways, if proposed control
                    methods repeatedly failed under realistic evaluations, and if
                    governance institutions demonstrated that less restrictive
                    approaches could not preserve meaningful human control.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class="blue-box">
                <h3>I would become less persuaded by the book if...</h3>
                <p>
                    Increasing model capability continued to depend on extensive
                    human direction, fragile scaffolding, bounded infrastructure,
                    and access that could be reliably monitored and revoked.
                </p>
                <p>
                    I would also update if interpretability, control evaluations,
                    containment, staged deployment, and international coordination
                    consistently improved faster than dangerous capability—and if
                    those systems worked outside carefully selected demonstrations.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.subheader("Looking Back")

    st.markdown(
        f"""
        <div class="burgundy-box">
            <h3>Where the book left me</h3>
            <p>
                I did not finish this book agreeing with its full chain of
                certainty.
            </p>
            <p>
                I remain unconvinced that every sufficiently advanced AI system
                necessarily becomes a coherent agent, acquires the relevant goals,
                escapes human control, and eliminates humanity.
            </p>
            <p>
                Too many steps in that sequence still depend on assumptions that
                deserve to be examined separately rather than compressed into one
                inevitable outcome.
            </p>
            <p>
                But I also did not finish the book where I began.
            </p>
            <p>
                I am less willing to treat uncertainty as reassurance. Less willing
                to assume that human oversight remains meaningful merely because a
                person appears somewhere in the workflow. Less willing to believe
                that competition will naturally reward caution. And much less
                willing to accept “we can stop later” without asking who retains the
                ability to stop what, under which conditions, and for how long.
            </p>
            <p>
                The book is strongest when it exposes the structural problem:
                increasingly capable systems are being developed inside institutions
                rewarded for speed, secrecy, scale, and competitive advantage, while
                the relevant harms may be cumulative, difficult to measure, and
                potentially irreversible.
            </p>
            <p>
                It is weakest when uncertainty inside that structure becomes
                certainty about one exact future.
            </p>
            <p>
                I do not think the right response is dismissal.
            </p>
            <p>
                I think it is decomposition.
            </p>
            <p>
                Which capabilities create danger? Which forms of agency are real?
                Which failures are reversible? Which controls remain external?
                Which institutions can verify restraint? Which claims would weaken
                if the evidence changed?
            </p>
            <p>
                Those are not ways of avoiding the argument.
            </p>
            <p>
                They are how I know to take an argument seriously.
            </p>
            <p>
                And the final question I would put in front of {you()} is not
                whether this book successfully proved that everyone dies.
            </p>
            <p>
                It is whether it showed us enough about the trajectory that
                continuing without stronger evidence, stronger controls, and much
                better institutions would itself be an extraordinary gamble.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="lavender-box">
            <h3>My final margin note</h3>
            <p>
                I hope the authors are wrong.
            </p>
            <p>
                Not because the argument was foolish, and not because the risks
                were imaginary.
            </p>
            <p>
                I hope they are wrong because humanity noticed enough, questioned
                enough, built better institutions, and changed the trajectory before
                the prediction had the chance to become history.
            </p>
            <p>
                Where there’s life, there’s still agency.
            </p>
            <p>
                And where there’s agency, there’s hope.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )