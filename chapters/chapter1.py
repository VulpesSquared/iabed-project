import streamlit as st
from components.claim_card import render_claim_card


def render_chapter1(you):
    st.header("Intro + Chapter 1")

    st.markdown(
        """
### Before we jump in...

The introduction is really trying to establish two big ideas.

First, that human intelligence probably isn't the upper limit of what's possible.

Second, that modern AI is better understood as something that emerges through optimization than something engineers explicitly design.

Those ideas show up throughout the rest of the book.

These are the places where I found myself stopping to think.
        """
    )

    place = st.radio(
        "📍 Places I paused",
        [
            "Human intelligence is probably not maximum possible intelligence",
            "AI is shallow",
            "AI is grown, not crafted",
            "DNA ↔ weights analogy",
            "Nobody understands how LLMs work",
            "Predicting language forces prediction of the world",
        ],
    )

    if place == "Human intelligence is probably not maximum possible intelligence":
        render_claim_card(
            title="Human intelligence is probably not maximum possible intelligence",
            reaction="🟢 Agreed",
            margin_note="""
This was probably the easiest point in the introduction for me to agree with.

Evolution doesn't optimize for intelligence. It optimizes for reproductive success.

Intelligence is one strategy among many, and from a biochemical perspective, it's an incredibly expensive one.

The more interesting question to me isn't whether humans are exceptionally intelligent. It's why we would assume evolution accidentally stopped at the maximum possible intelligence.
            """,
            why="""
- Evolution optimizes reproductive fitness rather than intelligence.
- Human intelligence is metabolically expensive.
- A higher ceiling seems much more plausible than a hard biological limit.
            """,
            questions="""
- Is there any principled upper bound on intelligence?
- Could evolution continue producing increasingly intelligent organisms?
- Does intelligence necessarily imply agency?
            """,
            side_trails="""
- Comparative cognition
- Brain energetics
- Scaling laws
- Evolutionary fitness
            """,
        )

    elif place == "AI is shallow":
        render_claim_card(
            title='AI is "shallow"',
            reaction="🟡 Needs a better definition",
            margin_note="""
This was one of the first places I wanted to slow down.

I don't love the word "shallow" here because it feels like it collapses too many different things into one vague judgment.

Shallow along what dimension?

Memory? Agency? Self-modeling? Embodiment? Long-horizon planning?

Current frontier models already show abstraction, transfer learning, few-shot abstraction, tool use, planning, emergent reasoning, and representation learning.

So I don't think "AI is shallow" is necessarily wrong. I think it needs to be defined before I can decide whether I agree.
            """,
            why="""
- "Shallow" is doing too much work.
- A model can be shallow in one dimension and surprisingly deep in another.
- Current systems already demonstrate behaviors that make the claim less obvious than it sounds.
            """,
            questions="""
- What dimensions are supposed to be shallow?
- Is shallow a claim about cognition, agency, memory, embodiment, or something else?
- What evidence would make this claim clearly true or clearly false?
            """,
            side_trails="""
- Abstraction
- Transfer learning
- Tool use
- Emergent reasoning
- Representation learning
            """,
        )

    elif place == "AI is grown, not crafted":
        render_claim_card(
            title="AI is grown, not crafted",
            reaction="🟢 Agreed",
            margin_note="""
This framing really works for me.

Engineers no longer specify intelligence directly.

They specify architecture, objective functions, optimization procedures, and training data. Then behavior emerges.

That makes modern AI feel less like traditional software engineering and more like developmental biology.

The analogy isn't perfect, but the shift matters. We are not hand-writing the behavior. We are creating the conditions under which behavior emerges.
            """,
            why="""
- Engineers specify the setup, not the final behavior.
- Architecture + objective function + optimization + training data create the conditions for behavior.
- This helps explain why systems can surprise their creators.
            """,
            questions="""
- Is developmental biology the right analogy?
- Does "grown" imply less controllability?
- Can interpretability catch up after behavior has emerged?
            """,
            side_trails="""
- Gradient descent
- Objective functions
- Developmental biology
- Mechanistic interpretability
            """,
        )
    elif place == "DNA ↔ weights analogy":
        render_claim_card(
            title="DNA ↔ weights analogy",
            reaction="🟡 Useful analogy, with important caveats",
            margin_note="""
I like the analogy because both systems begin with something compact and difficult to interpret directly.

DNA does not look like a phenotype.

Model weights do not look like language, reasoning, or behavior.

In both cases, relatively simple underlying components participate in enormous nonlinear processes that produce something much more complex.

But I would not push the analogy too far.

Biology has had much longer to develop a mechanistic account of how DNA becomes proteins, how proteins participate in signaling pathways, and how those pathways contribute to physiology and behavior.

With neural networks, we can inspect every weight and activation, but our ability to translate those components into a complete account of reasoning is still much more limited.
            """,
            why="""
- Both systems involve compact encodings that unfold into complex behavior.
- Neither DNA sequences nor model weights transparently reveal the resulting phenotype or computation.
- The analogy helps explain emergence without requiring mystery.
- Biology currently has a richer mechanistic vocabulary for connecting components across levels of organization.
            """,
            questions="""
- Are genomes and neural-network weights meaningfully analogous, or only superficially similar?
- Is the main limitation observability, interpretability, or causal complexity?
- Will AI interpretability eventually resemble molecular biology, neuroscience, or something entirely different?
            """,
            side_trails="""
- Genotype versus phenotype
- Gene regulation and developmental systems
- Distributed representations
- Mechanistic interpretability
- Emergence across levels of organization
            """,
        )
    elif place == "We don't fully understand how LLMs work":
        render_claim_card(
            title="We don't fully understand how LLMs work",
            reaction="🟡 Overstated",
            margin_note="""
This was another place where I found myself agreeing with the spirit of the argument but disagreeing with the wording.

Saying "nobody understands how LLMs work" makes it sound as though they're completely mysterious.

That isn't true.

We understand a tremendous amount about transformers, optimization, attention mechanisms, embeddings, tokenization, and training dynamics.

What we *don't* have is a complete mechanistic explanation for why a specific internal computation leads to a specific capability or behavior.

To me, that's the difference between a black box and a gray box.

We can inspect every weight in the model.

The challenge is interpreting what all of those weights are doing together.
""",
            why="""
- Understanding is incomplete, not absent.
- Interpretability research is actively reverse-engineering internal computation.
- "Black box" makes the situation sound more mysterious than it is.
            """,
            questions="""
- What level of mechanistic understanding would count as enough?
- Is AI interpretability more like neuroscience or molecular biology?
- How much understanding do we need before deploying powerful systems?
            """,
            side_trails="""
- Gray box vs. black box
- Mechanistic interpretability
- Sparse autoencoders
- Anthropic interpretability work
            """,
        )

    elif place == "Predicting language forces prediction of the world":
        render_claim_card(
            title="Predicting language forces prediction of the world",
            reaction="🟢 Agreed",
            margin_note="""
This is one of the strongest NLP points in the opening.

To predict language well, a model has to learn something about the world that produced the language.

That includes causality, medicine, physiology, social behavior, probability, goals, and context.

This reminds me of medicine: if a model predicts the right intervention or diagnosis, it has to carry some implicit representation of physiology, causality, probability, and outcomes.

Language prediction becomes world-model learning.
            """,
            why="""
- Language is produced by a structured world.
- Good prediction requires internal representations of that structure.
- Next-token prediction can look simple while still producing rich internal models.
            """,
            questions="""
- When does prediction become understanding?
- Is a world model enough for agency?
- How much can be learned from language alone?
            """,
            side_trails="""
- World models
- Distributional semantics
- Representation learning
- Embeddings and latent space
            """,
        )