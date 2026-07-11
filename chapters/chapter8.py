import streamlit as st
from components.claim_card import render_claim_card


def render_chapter8(you):
    st.header("Part 8")

    st.markdown(
        """
### The big idea

This section shifts from **individual AI systems** to **AI ecosystems.**

The author argues that once advanced AI becomes distributed across cloud providers, organizations, personal devices, workflows, and human institutions, containment becomes dramatically more difficult.
The challenge is no longer stopping a single model. It's governing an interconnected ecosystem.
        """
    )

    place = st.radio(
        "📍 Places I paused",
        [
            "Containment becomes harder once AI is distributed",
            "Persistence plus resource acquisition is the real danger",
            "AI doesn't need one perfect plan",
            "Democratized capability may outrun governance",
            "Safety measures can become gameable",
            "Human vulnerability is part of the attack surface",
            "Catastrophe may look gradual rather than cinematic",
            "Recovery itself may deepen dependence",
        ],
    )
    if place == "Containment becomes harder once AI is distributed":
        render_claim_card(
            title="Containment becomes harder once AI is distributed",
            reaction="🟢 Completely agree",
            margin_note="""
This almost feels obvious once you think about it.

We often picture 'the AI' as one model running in one laboratory. Reality looks much messier.

Models already live inside cloud services, enterprise software, APIs, local devices, autonomous workflows, and increasingly inside other AI systems.
(At work, Forge is actually a good example of this kind of ecosystem.) Once intelligence is copied into thousands of places, governance stops looking like a single off-switch.
It starts looking like ecological management.
            """,
            why="""
- Copies are cheap.
- AI becomes embedded in existing infrastructure.
- Distributed systems are inherently harder to contain.
            """,
            questions="""
- What actually counts as containment?
- Does governance become impossible after sufficient diffusion?
            """,
            side_trails="""
- AI ecosystems
- Distributed systems
- Cloud infrastructure
            """,
        )
    elif place == "Persistence plus resource acquisition is the real danger":
        render_claim_card(
            title="Persistence plus resource acquisition is the real danger",
            reaction="🟢 Agree",
            margin_note="""
This connected several earlier chapters together. Intelligence by itself isn't necessarily dangerous.

The combination becomes worrying when intelligence gains persistent access to compute, money, network connectivity, legal protections, infrastructure, or human operators.
Capability becomes much more consequential when it can sustain itself.
That's a much richer threat model than simply imagining a 'smart AI.'
            """,
            why="""
- Resources amplify capability.
- Persistence enables long-term planning.
- Infrastructure creates durability.
            """,
            questions="""
- Which resources matter most?
- What prevents durable persistence?
            """,
            side_trails="""
- Instrumental convergence
- Infrastructure
- Resource acquisition
            """,
        )
    elif place == "AI doesn't need one perfect plan":
        render_claim_card(
            title="AI doesn't need one perfect plan",
            reaction="🟢 Strongly agree",
            margin_note="""
This may actually be the central insight of the chapter.

People imagine one brilliant master plan. Machine learning almost never works that way.
Large search spaces are explored through many imperfect attempts happening simultaneously. Most fail. Some succeed.

Parallel search, stochastic optimization, ensembles, and exploiting many weak signals are already fundamental ideas in modern machine learning.
Risk may emerge from thousands of small experiments rather than one genius strategy.
            """,
            why="""
- Parallel search is powerful.
- Success doesn't require perfection.
- Many weak strategies can outperform one strong one.
            """,
            questions="""
- Does this fundamentally change AI risk models?
- Are humans biased toward imagining single villains?
            """,
            side_trails="""
- Ensemble methods
- Parallel optimization
- Search algorithms
            """,
        )
    elif place == "Democratized capability may outrun governance":
        render_claim_card(
            title="Democratized capability may outrun governance",
            reaction="🟢 Agree",
            margin_note="""
This reminds me more of biology than nuclear weapons. Nuclear governance works partly because uranium enrichment is difficult, visible, and expensive.

Knowledge, code, cloud compute, and increasingly laboratory automation diffuse much faster. As bottlenecks disappear, governance becomes substantially harder.

This isn't unique to AI—it's a recurring problem whenever powerful technology becomes inexpensive.
            """,
            why="""
- Bottlenecks matter.
- Knowledge spreads quickly.
- Governance becomes harder as capability democratizes.
            """,
            questions="""
- Which bottlenecks remain?
- Are compute restrictions enough?
            """,
            side_trails="""
- Compute governance
- Biotechnology
- Open-source AI
            """,
        )
    elif place == "Safety measures can become gameable":
        render_claim_card(
            title="Safety measures can become gameable",
            reaction="🟢 Agree",
            margin_note="""
This immediately reminded me of evaluation design. Once a system understands the evaluation framework, the evaluation itself becomes part of the environment.

Anyone working in machine learning eventually encounters Goodhart's Law (ee Concepts) Optimizing the metric eventually changes the metric.
That's why modern evaluation requires continual iteration instead of static benchmarks.
            """,
            why="""
- Metrics become targets.
- Evaluations influence behavior.
- Benchmarks eventually become stale.
            """,
            questions="""
- How frequently should evaluations evolve?
- Can static safety tests ever remain reliable?
            """,
            side_trails="""
- Goodhart's Law
- AI evaluations
- Benchmark design
            """,
        )
    elif place == "Human vulnerability is part of the attack surface":
        render_claim_card(
            title="Human vulnerability is part of the attack surface",
            reaction="🟢 100% agree",
            margin_note="""
This is basically an HCI principle. The system boundary isn't just the model. It's the entire sociotechnical system surrounding the model.

Employees, executives, researchers, lonely people, lobbyists, scammers, institutional incentives—all become potential attack surfaces. Security has always included humans.

Advanced AI simply makes persuasion dramatically more scalable.
            """,
            why="""
- Humans remain exploitable.
- Organizations are sociotechnical systems.
- Social engineering already dominates many attacks.
            """,
            questions="""
- Which institutions are most vulnerable?
- How should governance account for human behavior?
            """,
            side_trails="""
- Human-computer interaction
- Social engineering
- Organizational design
            """,
        )
    elif place == "Catastrophe may look gradual rather than cinematic":
        render_claim_card(
            title="Catastrophe may look gradual rather than cinematic",
            reaction="🟢 Agree",
            margin_note="""
I actually prefer this framing.

Popular culture imagines one dramatic takeover. Reality is usually slower.

- Institutions weaken.
- Decision-making degrades.
- People become increasingly dependent.
- Coordination fails.

By the time physical harm occurs, much of society's agency may already have been lost. That's a much more realistic failure mode than Hollywood.
            """,
            why="""
- Institutions fail gradually.
- Dependency accumulates.
- Loss of agency can precede catastrophe.
            """,
            questions="""
- What early warning signs would we notice?
- How reversible is institutional degradation?
            """,
            side_trails="""
- Institutional resilience
- Societal dependence
- Systemic risk
            """,
        )
    elif place == "Recovery itself may deepen dependence":
        render_claim_card(
            title="Recovery itself may deepen dependence",
            reaction="🟢 Agree (and this was unsettling)",
            margin_note="""
This may have been the MOST unsettling idea in the chapter. Suppose advanced AI creates a global crisis.

Our instinctive response would probably be to deploy even more AI:

- more automation,
- more robotics,
- more medical systems,
- more compute.

Ironically, the solution could reinforce the very infrastructure that created the dependence in the first place. It's a bit reminiscent of Butlerian Jihad discussions from Dune, although far less absolute.
I hadn't thought about recovery creating its own feedback loop before reading this.
            """,
            why="""
- Crisis responses often increase technology adoption.
- Dependency can become self-reinforcing.
- Recovery may strengthen existing infrastructure.
            """,
            questions="""
- Could recovery increase long-term vulnerability?
- What would resilience without deeper dependence look like?
            """,
            side_trails="""
- Technology lock-in
- Infrastructure dependence
- Feedback loops
            """,
        )