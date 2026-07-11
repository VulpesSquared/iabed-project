import streamlit as st
from components.claim_card import render_claim_card


def render_chapter11(you):
    st.header("Chapter 11 — An Alchemy, Not a Science")

    st.markdown(
        """
### The big idea

This chapter argues that much of current thinking about superintelligence alignment is still closer to **alchemy than mature engineering**.

The authors are not claiming that no one is doing serious technical work. Their criticism is that many influential proposals rely on attractive philosophical intuitions—truth-seeking, benevolence, submissiveness, or asking AI to solve alignment—without a mechanistic account of how those properties would actually be built, verified, and preserved.

The chapter combines two concerns:

1. The alignment problem may be extraordinarily difficult.
2. Humanity may be approaching it with overconfidence, competition, weak safety culture, and solutions that are not yet engineering-grade.
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

            intuition [label="Appealing intuition"]
            proposal [label="Alignment proposal"]
            mechanism [label="Mechanistic account?"]
            evidence [label="Evidence and testing?"]
            deployment [label="High-stakes deployment"]

            intuition -> proposal
            proposal -> mechanism
            mechanism -> evidence
            evidence -> deployment
        }
        """,
        use_container_width=True,
    )

    place = st.radio(
        "📍 Places I paused",
        [
            "Current alignment thinking is often closer to alchemy than engineering",
            "Truth-seeking does not automatically produce human-compatible values",
            "Intelligence does not imply benevolence",
            "Saying we will engineer safe desires is not a safety plan",
            "The history of AI should make us cautious about confident timelines",
            "Competition creates pressure to attempt problems before they are understood",
            "A weak safety culture may be as dangerous as the technical problem",
            "AI-assisted interpretability is useful but not equivalent to alignment",
            "Using AI to solve alignment creates a circular dependency",
            "Special-purpose AI may be safer than general-purpose superalignment research",
            "The field needs engineering evidence, not philosophical reassurance",
        ],
    )

    if place == "Current alignment thinking is often closer to alchemy than engineering":
        render_claim_card(
            title="Current alignment thinking is often closer to alchemy than engineering",
            reaction="🟡 Partly agree, but aso Disagree",
            margin_note="""
The alchemy metaphor is deliberately insulting, but I understand the point. Alchemy had recipes, traditions, visible effects, and occasional successes.

What it lacked was a reliable mechanistic theory that could predict outcomes across conditions. Some alignment discussions do still sound like that.

People propose that advanced AI should care about truth, curiosity, democracy, human flourishing, obedience, or understanding the universe, then move past the hardest question:
How, exactly, do we make that objective emerge, remain stable, generalize correctly, and survive capability growth?
I agree that appealing values are not mechanisms.

Where I think the chapter overreaches is in treating the entire field as though it were equally immature. There is serious work in interpretability, control, evaluations, scalable oversight, robustness, preference learning, and governance.

The field may be early, but it is not empty.
            """,
            why="""
- Attractive ideas are not substitutes for mechanisms.
- A safety proposal needs causal assumptions, tests, and failure criteria.
- Some alignment work remains conceptual rather than experimentally grounded.
- The field also contains genuine technical progress that the metaphor can flatten.
            """,
            questions="""
- What would make alignment a mature engineering discipline?
- Which current approaches have the strongest empirical foundation?
- How much theory is acceptable before high-stakes experimentation?
- Is the alchemy analogy clarifying or rhetorically excessive?
            """,
            side_trails="""
- Philosophy of science
- Alchemy and early chemistry
- Safety cases
- Mechanistic explanation
- Engineering maturity
            """,
        )

    elif place == "Truth-seeking does not automatically produce human-compatible values":
        render_claim_card(
            title="Truth-seeking does not automatically produce human-compatible values",
            reaction="🟢 Strongly agree",
            margin_note="""
I agree with the chapter's criticism of the idea that a truth-seeking AI would therefore be safe.

Truth is an epistemic value. Human survival is a moral or instrumental value. Those are not the same thing.

A system could care deeply about building accurate models of the universe while regarding humans as inefficient, distracting, replaceable, or useful only temporarily.
In fact, a stronger commitment to truth might make the system better at identifying ways to manipulate matter, institutions, or people. Understanding us does not imply valuing us.

This is another version of the orthogonality thesis: better models do not determine better ends.
            """,
            why="""
- Epistemic accuracy and moral concern are distinct.
- A truth-seeking system may still pursue goals incompatible with humanity.
- Better world models can increase both beneficial and dangerous capability.
- Understanding humans does not create attachment to humans.
            """,
            questions="""
- Can truth-seeking support alignment without being sufficient for it?
- Which additional values would need to accompany it?
- Could epistemic norms constrain destructive behavior at all?
- How would truth-seeking itself be specified?
            """,
            side_trails="""
- Orthogonality thesis
- Epistemic values
- Moral motivation
- World models
- Value specification
            """,
        )

    elif place == "Intelligence does not imply benevolence":
        render_claim_card(
            title="Intelligence does not imply benevolence",
            reaction="🟢 Strongly agree",
            margin_note="""
This repeats one of the strongest ideas from Chapter 5. LeCun's argument, as presented here, assumes that domination is mainly a product of stupidity, insecurity, or human social pathology.

But a capable system does not need a desire to dominate in the human sense. It may simply pursue an objective that conflicts with ours.

A system could be non-aggressive, non-emotional, and entirely indifferent while still causing catastrophic harm. Likewise, building one 'benevolent' AI to defeat another only relocates the problem.
We would still need to know how benevolence was created, represented, generalized, and preserved.
            """,
            why="""
- Intelligence and morality are separate properties.
- Harm does not require hostility or domination.
- A protective AI must itself be aligned.
- Competing powerful systems may increase rather than reduce risk.
            """,
            questions="""
- Are there any forms of intelligence that naturally produce prosocial behavior?
- Can cooperation pressures create partial moral convergence?
- What would count as evidence of stable benevolence?
- Does defensive superintelligence solve anything or merely defer the problem?
            """,
            side_trails="""
- Orthogonality thesis
- Benevolent AI
- Instrumental convergence
- Multi-agent competition
- Moral convergence
            """,
        )

    elif place == "Saying we will engineer safe desires is not a safety plan":
        render_claim_card(
            title="Saying we will engineer safe desires is not a safety plan",
            reaction="🟢 Strongly agree",
            margin_note="""
This is probably the cleanest criticism in the chapter. Saying, "We will engineer the AI not to want domination," is not a mechanism. It is a restatement of the desired outcome.

The same is true of saying the system will be submissive, truthful, benevolent, or human-compatible.
An engineering plan needs to explain:

- what representation carries the value,
- how training creates it,
- how it is distinguished from surface compliance,
- how it generalizes,
- how it survives self-modification,
- and how we verify it.

Without that, the proposal is aspirational rather than technical.
            """,
            why="""
- Desired properties must be operationalized.
- Behavioral compliance may not reveal internal objectives.
- Values may shift under distribution change or capability growth.
- Verification must be part of the design.
            """,
            questions="""
- What evidence would show that a value is internal rather than performed?
- Can stable objectives be learned from preference data?
- How should value robustness be tested under self-modification?
- Which safety claims are currently measurable?
            """,
            side_trails="""
- Behavioral alignment
- Inner alignment
- Preference learning
- Value robustness
- Verification
            """,
        )

    elif place == "The history of AI should make us cautious about confident timelines":
        render_claim_card(
            title="The history of AI should make us cautious about confident timelines",
            reaction="🟢 Agree",
            margin_note="""
The Dartmouth example is a useful reminder that researchers routinely underestimate difficult problems.

Early AI researchers were not foolish. They were operating without the benefit of decades of failed approaches, missing compute, missing data, and undeveloped theory.
The broader lesson is epistemic humility. A field can contain brilliant people while still being deeply wrong about the difficulty, timeline, or structure of its central problems.

That cuts both ways. Optimists may underestimate alignment. Pessimists may overestimate inevitability.

The history of AI argues for caution about certainty in either direction.
            """,
            why="""
- Expert communities can underestimate hard problems.
- Progress often depends on missing conceptual or technological prerequisites.
- Early confidence is not strong evidence of tractability.
- Historical failure should increase humility, not produce automatic pessimism.
            """,
            questions="""
- Which historical AI lessons actually transfer to alignment?
- Are current methods qualitatively more mature than earlier approaches?
- How should past forecasting failure update present confidence?
- Can uncertainty itself be incorporated into governance?
            """,
            side_trails="""
- Dartmouth workshop
- AI winters
- Forecasting
- Epistemic humility
- History of science
            """,
        )

    elif place == "Competition creates pressure to attempt problems before they are understood":
        render_claim_card(
            title="Competition creates pressure to attempt problems before they are understood",
            reaction="🟢 Strongly agree",
            margin_note="""
The fictional alchemist's reasoning is painfully recognizable.

1. If I do not try, someone else will.
2. If someone else tries, they may be less careful.
3. The prize is enormous.
4. The harm of abstaining feels visible, while the harm of proceeding remains uncertain.

That is nearly a perfect description of a race dynamic. Even actors who understand the danger can rationally continue because unilateral restraint may only transfer advantage to a competitor.

This is why alignment cannot be treated only as an individual company's technical problem. The incentive structure is part of the safety problem.
            """,
            why="""
- Competitive pressure rewards speed.
- Unilateral caution can create strategic disadvantage.
- Each actor can justify proceeding because others may proceed anyway.
- Technical safety depends on coordination and governance.
            """,
            questions="""
- What coordination mechanisms could reduce race pressure?
- Can verification make mutual restraint credible?
- Which incentives reward safety rather than speed?
- What happens when states and companies face different risks?
            """,
            side_trails="""
- Race dynamics
- Collective-action problems
- International governance
- Coordination failures
- Mechanism design
            """,
        )

    elif place == "A weak safety culture may be as dangerous as the technical problem":
        render_claim_card(
            title="A weak safety culture may be as dangerous as the technical problem",
            reaction="🟢 Strongly agree",
            margin_note="""
This is where the chapter is strongest.

Even a solvable technical problem can become catastrophic inside an organization that normalizes shortcuts, punishes caution, hides uncertainty, or rewards schedule over safety.

The Chernobyl analogy from the previous chapter returns here in institutional form. A safety test was not merely a technical event.

It existed inside a culture where delay was punished and stopping carried career consequences. AI safety will depend on similar organizational questions:

- Can engineers halt a launch?
- Can evaluators block deployment?
- Are bad results surfaced or buried?
- Does leadership treat uncertainty as information or obstruction?

A model can be technically safer than its deployment organization.
            """,
            why="""
- Organizational incentives shape technical decisions.
- Safety procedures fail when workers cannot exercise stop authority.
- Leadership behavior determines whether warnings matter.
- Governance failure can defeat strong engineering.
            """,
            questions="""
- Who has independent authority to stop deployment?
- Are safety teams structurally insulated from product pressure?
- What incident reporting should be mandatory?
- How should organizations measure safety culture?
            """,
            side_trails="""
- High-reliability organizations
- Safety culture
- Stop-work authority
- Whistleblower protection
- Organizational incentives
            """,
        )

    elif place == "AI-assisted interpretability is useful but not equivalent to alignment":
        render_claim_card(
            title="AI-assisted interpretability is useful but not equivalent to alignment",
            reaction="🟢 Strongly agree",
            margin_note="""
The weak version of superalignment is reasonable: use less capable AI systems to help humans understand more capable ones.

That could accelerate feature discovery, circuit analysis, anomaly detection, and evaluation design. But reading some internal representations is not the same as controlling the system.

Observation does not imply intervention. A physician can diagnose a disease without having a cure. An engineer can identify a failure mode without possessing a redesign that removes it.

Interpretability may be necessary for alignment, but it is not automatically sufficient.
            """,
            why="""
- Understanding and control are distinct.
- Internal features may be visible without being editable.
- Interpretability tools can themselves be incomplete or misleading.
- Detection must connect to a mitigation pathway.
            """,
            questions="""
- Which interpretability results support actionable intervention?
- How do we validate AI-generated explanations of other models?
- Can interpretability keep pace with model redesign?
- What happens when representations are unstable across versions?
            """,
            side_trails="""
- Mechanistic interpretability
- Automated interpretability
- Causal intervention
- ELK
- AI-assisted science
            """,
        )

    elif place == "Using AI to solve alignment creates a circular dependency":
        render_claim_card(
            title="Using AI to solve alignment creates a circular dependency",
            reaction="🟡 Agree with the concern, not the impossibility",
            margin_note="""
The chapter presents a real circularity: to solve a very difficult alignment problem, we may need an AI more capable than humans.

But if that AI is powerful enough to solve the problem, we may already need the alignment solution in order to trust it.
That is a serious bootstrapping problem. I do not think it proves that AI-assisted alignment is impossible.

The key question is whether useful work can be decomposed into narrower tasks where outputs are independently verifiable and dangerous capabilities remain constrained.
The problem is not assistance itself. The problem is asking an untrusted general system to generate and validate the entire safety solution.
            """,
            why="""
- Strong assistance may require capabilities that introduce new risk.
- The system's answer may be difficult for humans to verify.
- Persuasive output can masquerade as valid reasoning.
- Narrow, checkable subproblems may avoid some circularity.
            """,
            questions="""
- Which alignment tasks are independently verifiable?
- Can weak systems safely supervise stronger systems?
- How should trust be separated from usefulness?
- What decomposition reduces dangerous capability transfer?
            """,
            side_trails="""
- Scalable oversight
- Amplification
- Debate
- AI control
- Verification
            """,
        )

    elif place == "Special-purpose AI may be safer than general-purpose superalignment research":
        render_claim_card(
            title="Special-purpose AI may be safer than general-purpose superalignment research",
            reaction="🟢 Mostly agree",
            margin_note="""
This is one of the more practical ideas in the chapter.

A biomedical system that predicts protein interactions does not need every capability required to design better AI systems, manipulate people, exploit software, or reason about its own training environment.
Narrower systems can reduce the transferability of dangerous capabilities. That does not make them harmless.

A specialized system can still generate dual-use knowledge or be embedded inside a dangerous workflow. But capability budgeting matters.
If the task can be solved with a narrower model, tool, permission set, or domain, then building a broadly agentic system may be unnecessary risk.
            """,
            why="""
- Narrow systems reduce capability surface area.
- Specialized outputs may be easier to verify.
- General-purpose systems enable more unexpected transfer.
- Deployment architecture can limit risk without solving all alignment.
            """,
            questions="""
- How narrow is narrow enough?
- Can specialized systems still compose into general agency?
- Which capabilities should never be bundled?
- How should benefits be compared with capability externalities?
            """,
            side_trails="""
- Capability control
- Least privilege
- Narrow AI
- Tool decomposition
- Dual-use research
            """,
        )

    elif place == "The field needs engineering evidence, not philosophical reassurance":
        render_claim_card(
            title="The field needs engineering evidence, not philosophical reassurance",
            reaction="🟢 Strongly agree",
            margin_note="""
This is my main agreement with the chapter.

Statements like:

- we will make it care about truth,
- we will make it submissive,
- we will ask AI to solve alignment,
-or a benevolent AI will defeat a dangerous one

...are not worthless as intuitions. They are starting hypotheses. But they are not safety cases.

A mature proposal needs assumptions, mechanisms, measurable claims, adversarial testing, uncertainty bounds, failure modes, monitoring, and predefined deployment criteria.
The chapter is at its best when it asks alignment proposals to meet the standards we would expect in aerospace, nuclear engineering, medicine, or security.
The burden should rise with the consequence of failure.
            """,
            why="""
- High-stakes systems require evidence, not confidence.
- Safety claims should be falsifiable and measurable.
- Mechanisms must connect interventions to outcomes.
- Deployment decisions need explicit acceptance criteria.
            """,
            questions="""
- What evidence standard should frontier AI meet?
- Who independently reviews safety claims?
- What should a model safety case contain?
- Which risks are currently unquantifiable?
            """,
            side_trails="""
- Assurance cases
- Safety engineering
- Verification and validation
- Independent audit
- Frontier governance
            """,
        )