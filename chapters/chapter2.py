import streamlit as st
from components.claim_card import render_claim_card


def render_chapter2(you):
    st.header("Part 2")

    st.markdown(
        """
### The big idea

This section argues that modern AI isn't constructed piece by piece like traditional software.

Instead, engineers specify an architecture, a learning objective, and a training process. Intelligence emerges from optimization rather than explicit programming.
That shift changes how we think about prediction, reasoning, interpretability, and ultimately alignment.
"""
    )

    st.markdown("### How I was thinking through this")

    st.graphviz_chart(
        """
        digraph {
            rankdir=LR;
            node [shape=box style="rounded,filled" fillcolor="#1F2937" fontcolor="white" color="#D8A54A"];

            Architecture -> Optimization;
            Optimization -> "Emergent representations";
            "Emergent representations" -> "World models";
            "World models" -> "General capabilities";
            "General capabilities" -> Agency;
        }
        """
    )

    place = st.radio(
        "📍 Places I paused",
        [
            "Next-token prediction isn't 'just autocomplete'",
            "Predicting language forces prediction of the world",
            "AI is grown, not crafted",
            "DNA ↔ weights analogy",
            "We don't fully understand how LLMs work",
        ],
    )

    if place == "Next-token prediction isn't 'just autocomplete'":

        render_claim_card(
            title="Next-token prediction isn't 'just autocomplete'",
            reaction="🟢 Strongly agree",
            margin_note="""
People hear "predict the next token" and imagine glorified phone autocomplete, which stylistically is ok I guess...

That framing dramatically undersells what optimization is actually doing.
Predicting language across trillions of examples forces the model to compress enormous amounts of statistical structure about the world.
The objective looks simple, but he resulting representations are rich, structured, and surprisingly general.
""",
            why="""
- Simple objectives can produce surprisingly rich behavior.
- Prediction rewards internal models of causality and structure.
- Emergent capabilities are a consequence of optimization, not explicit programming.
""",
            questions="""
- Why does such a simple objective scale so well?
- Are richer objectives even necessary?
""",
            side_trails="""
- Compression
- Emergence
- Scaling laws
""",
        )

    elif place == "Predicting language forces prediction of the world":

        render_claim_card(
            title="Predicting language forces prediction of the world",
            reaction="🟢 Agreed",
            margin_note="""
This is one of the strongest NLP arguments in the opening chapters!

To predict language well, a model has to learn something about the world that produced the language.
That includes medicine, physiology, probability, human goals, social dynamics, causality, and common sense.

It reminds me of medicine.
If a model consistently predicts the correct diagnosis or intervention, it must carry some implicit representation of physiology and disease.
Language prediction becomes world-model learning.
""",
            why="""
- Language reflects an underlying world.
- Good prediction requires internal representations of that world.
- Next-token prediction naturally encourages world models.
""",
            questions="""
- When does prediction become understanding?
- Is language alone enough to build robust world models?
""",
            side_trails="""
- World models
- Representation learning
- Embeddings
- Latent space
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
The analogy isn't perfect, but the shift matters. We are no longer writing behavior. We're creating the conditions under which behavior develops.
""",
            why="""
- Engineers define the process rather than the finished behavior.
- Architecture, optimization, and data interact to create intelligence.
- This explains why models sometimes surprise even their creators.
""",
            questions="""
- Does "grown" imply less controllability?
- Is biology really the right analogy?
""",
            side_trails="""
- Gradient descent
- Developmental biology
- Emergence
- Optimization
""",
        )

    elif place == "DNA ↔ weights analogy":

        render_claim_card(
            title="DNA ↔ weights analogy",
            reaction="🟡 Useful analogy, with caveats",
            margin_note="""
I like this analogy because both DNA and neural-network weights are compact encodings that unfold into extraordinarily complex systems.

DNA doesn't look like an organism. Model weights don't look like reasoning.

In both cases, simple underlying components participate in enormous nonlinear processes.

Where the analogy breaks down is mechanistic understanding.

Biology has spent decades mapping genes to proteins to physiology.
Interpretability research is still working toward that kind of mechanistic account for neural networks.
""",
            why="""
- Compact encodings produce complex behavior.
- Neither DNA nor weights transparently reveal the final phenotype.
- Biology currently has much richer mechanistic explanations.
""",
            questions="""
- Will AI interpretability ever resemble molecular biology?
- Is this analogy fundamentally accurate or only useful?
""",
            side_trails="""
- Genotype vs phenotype
- Mechanistic interpretability
- Sparse autoencoders
""",
        )

    elif place == "We don't fully understand how LLMs work":

        render_claim_card(
            title="We don't fully understand how LLMs work",
            reaction="🟡 Overstated",
            margin_note="""
This was another place where I agreed with the spirit but disagreed with the wording.

People often say LLMs are complete black boxes. I don't think that's accurate.

We understand transformers, attention, optimization, tokenization, embeddings, and training remarkably well.
What we lack is a complete mechanistic explanation connecting specific internal computations to specific behaviors.To me, today's models are gray boxes, not black boxes.

We can inspect every weight. The difficult part is interpreting what those weights collectively compute.
""",
            why="""
- We understand architecture far better than behavior.
- Interpretability is incomplete, not nonexistent.
- "Black box" oversimplifies the problem.
""",
            questions="""
- What counts as sufficient mechanistic understanding?
- Is interpretability more like neuroscience or molecular biology?
""",
            side_trails="""
- Mechanistic interpretability
- Gray-box systems
- Anthropic interpretability
- Sparse autoencoders
""",
        )