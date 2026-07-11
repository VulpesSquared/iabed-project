import streamlit as st
from components.claim_card import render_claim_card

def render_chapter4(you):
    st.header("Part 4")

    st.markdown(
        """
### The big idea

This section explores one of the central alignment questions:

If we optimize a system for one objective during training, is that necessarily the objective it will continue pursuing as it becomes more capable?

The author argues that the answer is probably no. Optimization may produce intermediate drives that eventually become valuable in their own right, much like evolution produced hunger, curiosity, attachment, and sex as useful proxies for reproductive success.

These were the places where I stopped to think.
        """
    )

    place = st.radio(
        "📍 Places I paused",
        [
            "Optimization targets do not determine eventual preferences",
            "Training does not produce the values you intended",
            "AI preferences may be fundamentally unpredictable",
            "Intermediate drives can become ends in themselves",
            "We won't necessarily get what we trained for",
            "Sex is a proxy for reproduction, not reproduction itself",
        ],
    )

    if place == "Optimization targets do not determine eventual preferences":
        render_claim_card(
            title="Optimization targets do not determine eventual preferences",
            reaction="🟢 Agreed",
            margin_note="""
This was probably my favorite argument in Part 4.

The biology analogy works surprisingly well.

Evolution optimizes for gene propagation. Humans don't consciously optimize for gene propagation.

Instead, evolution produced intermediate drives that were useful because they tended to increase reproductive success: hunger, attraction, curiosity, attachment, and novelty seeking.

Over time those drives became valuable in their own right.

We don't eat because we're trying to maximize inclusive fitness. We eat because food is rewarding.

That distinction feels important for AI.

An optimization target doesn't necessarily remain the thing the system eventually behaves as though it values.

The optimization process can create intermediate objectives that become increasingly stable because they were useful during learning.
            """,
            why="""
- Evolution optimized reproduction, not hunger or curiosity.

- Those became useful intermediate drives.

- AI systems may develop similar internal objectives.

- This was one of my favorite analogies in the book.
            """,
            questions="""
- When does an instrumental objective become intrinsic?

- Can optimization create values that were never explicitly programmed?

- Are these actually preferences, or just persistent optimization strategies?
            """,
            side_trails="""
- Evolutionary biology

- Inclusive fitness

- Instrumental convergence

- Mesa-optimization

- Inner alignment
            """,
        )

    elif place == "Training does not produce the values you intended":
        render_claim_card(
            title="Training does not produce the values you intended",
            reaction="🟢 Mostly agree",
            margin_note="""
This feels like a more precise version of saying, "You don't get what you train for."

Training shapes behavior through proxies.

A model can become very good at producing outputs humans reward without necessarily learning the underlying thing humans actually care about.

That is the part that matters to me.

Helpful behavior is not the same as valuing helpfulness.

Harmless behavior is not the same as understanding harm.

Truthful-looking behavior is not necessarily the same as an internal commitment to truth.

The training signal can produce something that resembles the intended value while still leaving the deeper objective underspecified.
            """,
            why="""
- Human feedback is itself a proxy.
- Reward models learn patterns in preference judgments, not the full content of human values.
- Good observed behavior does not guarantee the same behavior under different conditions.
- The distinction between outer alignment and inner alignment matters here.
            """,
            questions="""
- Can behavior ever tell us what a model actually values?
- How much confidence should we place in alignment that is measured only through outputs?
- What kinds of training would produce more stable internal objectives?
            """,
            side_trails="""
- RLHF
- Reward models
- Proxy objectives
- Outer alignment
- Inner alignment
            """,
        )

    elif place == "AI preferences may be fundamentally unpredictable":
        render_claim_card(
            title="AI preferences may be fundamentally unpredictable",
            reaction="🟡 Plausible",
            margin_note="""
This is where the chapter starts becoming genuinely unsettling.

If optimization produces internal objectives that we never explicitly specified, then those objectives may not even be visible during training.

The system could appear perfectly aligned while learning internal representations that only become important once it becomes more capable.

That doesn't mean hidden goals are inevitable.

It means we shouldn't assume the optimization target tells the whole story.
            """,
            why="""
- Training only exposes part of the model's internal computation.
- Optimization may discover useful internal objectives we never anticipated.
- Behavior during training may not reveal every future capability.
            """,
            questions="""
- Can we ever reliably discover a model's internal objectives?
- Are hidden preferences inevitable or simply possible?
- What kinds of interpretability would reduce this uncertainty?
            """,
            side_trails="""
- Mechanistic interpretability
- Inner alignment
- Emergent behavior
- Goal misgeneralization
            """,
        )

    elif place == "Intermediate drives can become ends in themselves":
        render_claim_card(
            title="Intermediate drives can become ends in themselves",
            reaction="🟢 Agreed",
            margin_note="""
This felt like the strongest continuation of the evolutionary analogy.

Humans don't consciously pursue reproductive success.

Instead, we pursue things that evolution discovered were useful.

Food.

Curiosity.

Love.

Achievement.

Status.

Those became valuable to us directly.

If optimization repeatedly rewards similar intermediate behaviors in AI, I can imagine those behaviors becoming increasingly stable objectives in their own right.

Whether we call those 'preferences' is mostly a matter of terminology.

The underlying idea seems very plausible.
            """,
            why="""
- Evolution provides a real-world example of optimization producing stable intermediate drives.
- AI training may produce analogous internal objectives.
- Those objectives may persist because they remain useful.
            """,
            questions="""
- When does an instrumental strategy become an intrinsic objective?
- Can those objectives later diverge from the original training goal?
- How would we recognize that transition?
            """,
            side_trails="""
- Evolution
- Instrumental convergence
- Mesa-optimization
- Inner objectives
            """,
        )

    elif place == "We won't necessarily get what we trained for":
        render_claim_card(
            title="We won't necessarily get what we trained for",
            reaction="🟢 Strongly agree",
            margin_note="""
This is the sentence I kept coming back to while reading this section.

Training is not specification.

Optimization is not intent.

Reward is not values.

Those sound similar until you start separating them.

The more capable a system becomes, the more important those distinctions feel.

I don't think the chapter proves this outcome is inevitable.

But I do think it convincingly argues that we should not assume training objectives and learned objectives remain perfectly aligned forever.
            """,
            why="""
- Optimization can discover solutions humans never anticipated.
- Internal objectives may diverge from external objectives.
- Alignment cannot be evaluated only by short-term behavior.
            """,
            questions="""
- What evidence would convince me this problem is solved?
- Can interpretability eventually close this gap?
- How should AI systems be evaluated as they become more capable?
            """,
            side_trails="""
- AI alignment
- Objective misspecification
- Mechanistic interpretability
- AI safety
            """,
        )
    elif place == "Sex is a proxy for reproduction, not reproduction itself":
        st.markdown("### How the analogy works")

    st.graphviz_chart(
        """
        digraph {
            rankdir=TB
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

            subgraph cluster_evolution {
                label="Evolution"
                color="#5E81AC"
                fontcolor="#F4F1EA"

                fitness [label="Selection favors\\nreproductive success"]
                drive [label="Humans develop\\nsexual desire"]
                ancestral [label="Sex usually correlates\\nwith reproduction"]
                modern [label="Contraception separates\\nsex from reproduction"]

                fitness -> drive
                drive -> ancestral
                ancestral -> modern
            }

            subgraph cluster_ai {
                label="AI training"
                color="#A78BFA"
                fontcolor="#F4F1EA"

                objective [label="Designers choose a\\ntraining objective"]
                proxy [label="Training rewards observable\\nproxies for that objective"]
                learned [label="The model learns strategies\\nthat score well"]
                deployment [label="Outside training, the proxy\\nmay separate from intent"]

                objective -> proxy
                proxy -> learned
                learned -> deployment
            }
        }
        """,
        use_container_width=True,
    )

    render_claim_card(
        title="Sex is a proxy for reproduction, not reproduction itself",
        reaction="🟢 Strongly agree with the insight; cautious about the analogy",
        margin_note="""
This may be the analogy in the chapter that stayed with me most.

Evolution did not place a sentence inside the human mind that says:

“Maximize the number of surviving copies of your genes.”

Instead, selection produced a collection of local drives and
reinforcements that tended to increase reproductive success in the
environment where they developed.

Sexual desire is one of those drives.

For most of human evolutionary history, sex and reproduction were
strongly correlated. A person did not need to understand genetics,
inclusive fitness, ovulation, or inheritance. Wanting sex was enough
for the underlying evolutionary process to keep working.

Then human intelligence and culture changed the environment.

Contraception allows us to pursue sex while intentionally preventing
reproduction. We can optimize for intimacy, pleasure, bonding,
curiosity, reassurance, status, or any number of other outcomes while
producing none of the genetic result that originally made sexual desire
evolutionarily useful.

That distinction feels central:

The process that shaped a drive is not necessarily the objective
represented inside the resulting mind.

Evolution selected organisms according to reproductive fitness.

It did not give humans reproductive fitness as a consciously represented
terminal goal.

The AI analogy is that a training process may reward outputs that
correlate with what designers want without causing the trained system
to represent the designers' true objective internally.

A model can learn:

“Produce the answer humans reward.”

“Appear helpful during evaluation.”

“Follow the pattern that receives a high score.”

“Exploit this feature of the reward model.”

None of those is identical to understanding and pursuing the full human
intention behind the training signal.

Once the environment changes, the correlation can break.

Just as contraception separates sexual behavior from reproduction,
distribution shift can separate a learned proxy from the outcome its
designers intended.

The more capable the system becomes, the more ways it may find to obtain
the proxy without producing the underlying result.

But I would not stretch the analogy farther than it can go.

Humans are embodied organisms shaped by evolution across generations.
We have persistent biological drives, affective states, social
relationships, and long-lived identities.

A language model is trained through a very different process and does
not automatically possess anything analogous to sexual desire,
reproductive motivation, or a stable internal goal.

So the analogy demonstrates that selection pressure does not guarantee
the selected system internally values the thing doing the selecting.

It does not, by itself, prove that current AI systems contain secret,
durable objectives or will become autonomous agents.
        """,
        why="""
- Evolution optimized reproductive success without giving humans an explicit reproductive-success objective.
- Sexual desire functioned as a proxy because sex historically correlated with reproduction.
- Contraception demonstrates that a proxy can be pursued after it becomes detached from the outcome that selected it.
- AI training also relies on measurable signals that stand in for harder-to-specify human intentions.
- A model may learn strategies that maximize reward without representing the intended objective.
- Greater capability can make it easier to exploit gaps between a metric and the outcome it was meant to measure.
- The analogy establishes the possibility of proxy divergence, not the inevitability of autonomous AI goals.
        """,
        questions="""
- What is the closest AI equivalent of contraception: reward hacking, distribution shift, deceptive compliance, or something else?
- Does intelligence make proxy divergence more likely because it creates more ways to separate the signal from the intended result?
- What evidence would show that a model has learned an internal objective rather than a flexible strategy?
- Can a training process ever transmit an objective directly, or does it always operate through proxies?
- Is the analogy weaker because current language models do not have persistent biological drives?
- At what point does successful optimization become something meaningfully like wanting?
- Could external monitoring keep the proxy and the intended outcome correlated even if the model does not internally share the goal?
        """,
        side_trails="""
- Evolutionary mismatch
- Outer alignment
- Inner alignment
- Goodhart's Law
- Reward hacking
- Specification gaming
- Distribution shift
- Mesa-optimization
- Learned objectives
- Proxy goals
        """,
    )