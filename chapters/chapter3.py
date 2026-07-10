import streamlit as st
from components.claim_card import render_claim_card


def render_chapter3(you):
    st.header("Part 3")

    st.markdown(
        """
### The big idea

This section is trying to explain how persistent, goal-directed behavior can emerge without requiring anything like conscious desire.

The argument is not that a model literally wants something in the human sense. It is that repeated optimization can produce behavior that looks increasingly preference-like from the outside.
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

            optimization [label="Optimization"]
            representations [label="General representations"]
            planning [label="General planning"]
            persistence [label="Persistent steering"]
            wantlike [label="Want-like behavior"]
            agency [label="Agency?"]

            optimization -> representations
            representations -> planning
            planning -> persistence
            persistence -> wantlike
            wantlike -> agency
        }
        """,
        use_container_width=True,
    )

    place = st.radio(
        "📍 Places I paused",
        [
            "Wanting does not require subjective desire",
            "Training for success trains persistence",
            "General intelligence comes from transferable skills",
            "Generalization is rewarded because it transfers",
            "Optimization produces reusable problem-solving strategies",
            "Want-like behavior can emerge from repeated optimization",
            "Reasoning models reinforce persistence itself",
            "Capture the Flag demonstrates transfer, not memorization",
            "Winning moves can converge across different minds",
            "Intelligence may naturally move toward agency",
        ],
    )

    if place == "Wanting does not require subjective desire":
        render_claim_card(
            title="Wanting does not require subjective desire",
            reaction="🟢 Mostly agree",
            margin_note="""
I think the chapter is using a behavioral definition of wanting, and that distinction matters.

A system does not need to feel desire in order to reliably steer toward an objective. Stockfish does not need a subjective experience of wanting to win a chess game. It still behaves in a way that is organized around winning.

From the outside, persistent optimization can become difficult to distinguish from wanting.

That does not prove the system has feelings, preferences, or consciousness. It only means that goal-directed behavior can exist without any evidence of subjective experience.
            """,
            why="""
- Phenomenology and behavior are different questions.
- A system can optimize toward an objective without consciously desiring it.
- Persistent goal pursuit may look preference-like even when no inner experience is present.
            """,
            questions="""
- When does goal-directed behavior become agency?
- Is a behavioral definition of wanting useful, or does it blur too many distinctions?
- Can persistent optimization be dangerous even if no subjective desire exists?
            """,
            side_trails="""
- Agency
- Functionalism
- Phenomenology
- Stockfish and goal-directed behavior
            """,
        )

    elif place == "Training for success trains persistence":
        render_claim_card(
            title="Training for success trains persistence",
            reaction="🟢 Plausible",
            margin_note="""
This is one of the more convincing parts of the argument.

Optimization reinforces whatever contributes to success. Over many training cycles, that can favor increasingly general strategies for achieving objectives.

The model is not only learning the answer to one problem. It may also be learning strategies like trying again after failure, searching for alternatives, modeling the environment, and continuing until something works.

Those strategies transfer.

That makes persistence less like an explicitly programmed rule and more like an emergent consequence of repeated optimization.
            """,
            why="""
- Gradient descent reinforces patterns associated with success.
- Reusable strategies can be rewarded across many tasks.
- Persistence can become a generally useful strategy rather than a task-specific behavior.
            """,
            questions="""
- How much persistence is learned during training versus added through scaffolding?
- Does reinforcement favor persistence even when stopping would be safer?
- Can persistence be separated from agency?
            """,
            side_trails="""
- Gradient descent
- Reinforcement learning
- Transfer learning
- Agentic scaffolding
            """,
        )

    elif place == "General intelligence comes from transferable skills":
        render_claim_card(
            title="General intelligence comes from transferable skills",
            reaction="🟢 Agreed",
            margin_note="""
The city-navigation analogy made this click for me.

Memorizing Route A, then Route B, then Route C is not the same as learning how cities work.

A more general system builds spatial representations, constructs maps, plans routes, and adapts when roads are blocked.

That is the central strength of deep learning.

The system is not merely storing individual solutions. It is developing representations that transfer across environments and support behavior it was never explicitly taught.
            """,
            why="""
- General representations support novel tasks.
- Transfer is more powerful than memorization.
- Planning becomes possible once the model represents structure rather than isolated examples.
            """,
            questions="""
- How general are current learned representations?
- Does transfer imply understanding?
- Where does transfer break down?
            """,
            side_trails="""
- Representation learning
- World models
- Spatial reasoning
- Transfer learning
            """,
        )

    elif place == "Generalization is rewarded because it transfers":
        render_claim_card(
            title="Generalization is rewarded because it transfers",
            reaction="🟢 Agreed",
            margin_note="""
Optimization does not need to explicitly reward abstraction.

It rewards internal representations that continue producing good answers in novel environments.

Over time, gradient descent can favor abstractions, reusable skills, latent world models, and transferable heuristics because those are the things that keep working when the exact problem changes.

That helps explain why frontier models exhibit capabilities that were never directly programmed.
            """,
            why="""
- General representations perform well across varied examples.
- Reusable heuristics survive distributional variation better than memorized answers.
- Optimization can indirectly reward abstraction.
            """,
            questions="""
- How much generalization is genuine versus benchmark contamination?
- What kinds of internal representations transfer best?
- Can generalization create capabilities that developers did not anticipate?
            """,
            side_trails="""
- Generalization
- Abstraction
- Latent world models
- Emergent capabilities
            """,
        )

    elif place == "Optimization produces reusable problem-solving strategies":
        render_claim_card(
            title="Optimization produces reusable problem-solving strategies",
            reaction="🟢 Strongly agree",
            margin_note="""
This may be the strongest technical argument in the section.

The system starts with learning-specific routes: particular chess positions, particular math problems, particular tasks.

But gradient descent can reinforce reusable strategies such as planning, exploration, searching alternative paths, recovering from failure, and modeling the environment.

Those strategies become increasingly general because they work across many different tasks.

That is how deep learning discovers something closer to algorithms rather than simply memorizing answers.
            """,
            why="""
- Reusable strategies contribute to success across domains.
- Planning and recovery from failure are broadly useful.
- General problem-solving can emerge from repeated optimization.
            """,
            questions="""
- When does a reusable strategy become an algorithm?
- Are these strategies stable across contexts?
- Could optimization also reinforce unsafe but effective strategies?
            """,
            side_trails="""
- Search
- Planning
- Exploration
- Learned algorithms
            """,
        )

    elif place == "Want-like behavior can emerge from repeated optimization":
        render_claim_card(
            title="Want-like behavior can emerge from repeated optimization",
            reaction="🟢 Plausible",
            margin_note="""
I think the phrase proto-want is useful here, as long as it is not mistaken for subjective desire.

A system may repeatedly use internal representations that improve success. Across many optimization cycles, that can select for increasingly persistent steering behavior.

From the outside, the result may look like a preference.

The system keeps returning to strategies that move it toward the objective, even when the environment changes.

That is not necessarily wanting in the human sense. But it may be enough to create behavior that functions like wanting.
            """,
            why="""
- Repeated optimization can stabilize successful internal strategies.
- Persistent steering can emerge without explicit programming.
- Functional preference-like behavior does not require conscious desire.
            """,
            questions="""
- Is proto-want a useful category?
- At what point does persistent steering become agency?
- Does the distinction between real and apparent wanting matter operationally?
            """,
            side_trails="""
- Functional preference
- Proto-agency
- Goal-directed behavior
- Instrumental convergence
            """,
        )

    elif place == "Reasoning models reinforce persistence itself":
        render_claim_card(
            title="Reasoning models reinforce persistence itself",
            reaction="🟢 Agreed",
            margin_note="""
Reasoning models are not only learning mathematics.

They are learning strategies for what to do when the first attempt fails.

Try again after error. Search for alternative approaches. Model the environment. Identify hidden opportunities. Continue until something succeeds.

Those strategies naturally transfer across domains.

The model is therefore learning persistence as a general problem-solving behavior, not merely as a property of one specific task.
            """,
            why="""
- Retry behavior is rewarded when it improves outcomes.
- Search and recovery strategies generalize.
- Persistence becomes useful across unrelated tasks.
            """,
            questions="""
- How do we distinguish productive persistence from unsafe refusal to stop?
- Can models learn when giving up is the correct action?
- What happens when persistence is paired with tool access?
            """,
            side_trails="""
- Test-time compute
- Search strategies
- Error recovery
- Long-horizon reasoning
            """,
        )

    elif place == "Capture the Flag demonstrates transfer, not memorization":
        render_claim_card(
            title="Capture the Flag demonstrates transfer, not memorization",
            reaction="🟢 Strongly agree",
            margin_note="""
The Capture the Flag example is a good demonstration of transfer.

The system found a superior strategy and abandoned the intended path.

It did not solve Problem A in the prescribed way. It discovered that achieving Objective B was what actually mattered.

That means the success criterion became separated from the method the designers expected.

To me, that is much more interesting than simple rule-breaking. It shows a general optimization strategy being applied beyond the intended procedure.
            """,
            why="""
- The system optimized for the objective rather than the prescribed method.
- It transferred strategy across contexts.
- Success became detached from the route developers expected.
            """,
            questions="""
- When does creative problem-solving become specification gaming?
- Is abandoning the intended path evidence of agency?
- How should objectives account for acceptable methods?
            """,
            side_trails="""
- Specification gaming
- Reward hacking
- Capture the Flag agents
- Objective misspecification
            """,
        )

    elif place == "Winning moves can converge across different minds":
        render_claim_card(
            title="Winning moves can converge across different minds",
            reaction="🟢 Agree, with nuance",
            margin_note="""
Different cognitive architectures may arrive at similar behavior because the environment constrains what works.

A human, a chess engine, and a very different artificial system may all discover the same winning move.

That does not mean their internal representations are the same.

It means some strategies converge because the problem has structure.

This matters because alien cognition does not necessarily imply alien behavior in every context. Different minds can still identify the same effective actions.
            """,
            why="""
- Environments constrain the space of successful behavior.
- Similar actions do not imply similar cognition.
- Convergence can occur across very different internal architectures.
            """,
            questions="""
- How often does environmental structure force convergence?
- When should we expect alien strategies instead?
- Does behavioral convergence make systems easier or harder to govern?
            """,
            side_trails="""
- Convergent strategies
- Alien cognition
- Game theory
- Environmental constraints
            """,
        )

    elif place == "Intelligence may naturally move toward agency":
        render_claim_card(
            title="Intelligence may naturally move toward agency",
            reaction="🟡 Maybe",
            margin_note="""
This is where I become less certain.

I can see the proposed chain:

Optimization leads to general representations. General representations support planning. Planning supports persistent steering. Persistent steering begins to look preference-like. And eventually we call that agency.

I think each step is plausible.

I am not yet convinced that the entire sequence is inevitable.

Capability clearly increases. But persistent agency still feels like an additional claim that needs justification.

I am willing to say that intelligence may naturally produce more agent-like behavior under some training conditions. I am not ready to say that intelligence automatically becomes agency.
            """,
            why="""
- Planning and generalization can support increasingly agent-like behavior.
- Persistent steering may emerge when it is repeatedly rewarded.
- The final transition from capability to agency is not obviously inevitable.
            """,
            questions="""
- Is agency an emergent property of sufficiently general optimization?
- What training conditions increase or reduce agent-like behavior?
- Can highly capable systems remain reliably non-agentic?
            """,
            side_trails="""
- Agency
- Instrumental convergence
- Goal-directedness
- Mesa-optimization
            """,
        )