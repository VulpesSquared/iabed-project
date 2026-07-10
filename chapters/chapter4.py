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