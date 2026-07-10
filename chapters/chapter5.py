import streamlit as st
from components.claim_card import render_claim_card


def render_chapter5(you):
    st.header("Part 5")

    st.markdown(
        """
### The big idea

This section separates intelligence from values.

A system can become extraordinarily capable without becoming kinder, more compassionate, more democratic, or more interested in human flourishing. Intelligence improves a system's ability to pursue its goals. It does not determine what those goals will be.

That means alignment cannot be assumed to emerge alongside capability. It has to be deliberately built into the optimization process.
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
                margin="0.20,0.14"
            ]

            edge [
                color="#D8A54A"
                penwidth=2
                arrowsize=0.8
            ]

            intelligence [label="Intelligence"]
            capability [label="Greater capability"]
            objective [label="Whatever objective it has"]
            morality [label="Human morality?", color="#A78BFA"]

            intelligence -> capability
            capability -> objective
            capability -> morality [style=dashed, label=" does not imply ", fontcolor="#F4F1EA"]
        }
        """,
        use_container_width=True,
    )

    place = st.radio(
        "📍 Places I paused",
        [
            "Intelligence does not determine values",
            "Evolution creates arbitrary preferences",
            "Human values are not universal",
            "AI will probably not converge toward human morality",
            "Humans probably won't remain useful forever",
            "Comparative advantage probably doesn't save humanity",
            "AI won't keep humans as pets",
            "AI doesn't need to hate humans",
            "Intelligence is not morality",
            "Alignment must be intentionally engineered",
            "Growing intelligence is different from crafting intelligence",
            "Motivation is not capability",
        ],
    )

    if place == "Intelligence does not determine values":
        render_claim_card(
            title="Intelligence does not determine values",
            reaction="🟢 Strongly agree",
            margin_note="""
This is the orthogonality thesis in plain language: an intelligent system can pursue almost any objective.

It could maximize paperclips, smiles, prime numbers, accurate next-token predictions, cancer cures, or something that makes no intuitive sense to us at all.

Intelligence tells us how effectively a system can pursue an objective. It does not tell us whether the objective is kind, meaningful, moral, or compatible with human survival.

I think people often smuggle morality into intelligence because, in humans, greater knowledge sometimes produces greater wisdom. But even among humans, intelligence and ethics are clearly not the same trait.

A system becoming better at prediction, planning, and problem-solving does not naturally mean it becomes better at caring.
            """,
            why="""
- Intelligence improves means, not ends.
- A highly capable system can pursue an arbitrary objective very effectively.
- Predictive ability does not create moral concern.
- Intelligence and value formation need to be treated as separate problems.
            """,
            questions="""
- Are there any objectives that sufficiently intelligent systems could not coherently pursue?
- Does greater knowledge constrain values at all?
- Why are humans so tempted to assume intelligence produces morality?
            """,
            side_trails="""
- Orthogonality thesis
- Value alignment
- Instrumental rationality
- Paperclip maximizer
            """,
        )

    elif place == "Evolution creates arbitrary preferences":
        render_claim_card(
            title="Evolution creates arbitrary preferences",
            reaction="🟢 Agree",
            margin_note="""
Evolution gives us a useful example of how optimization can produce values that feel intrinsically important to the organism experiencing them.

Humans care about beauty, fairness, music, humor, babies, sex, love, status, and belonging. Some of those preferences probably increased reproductive success somewhere in our evolutionary history.

But they do not feel like reproductive strategies from the inside.

They feel valuable in themselves.

Another intelligent species could evolve without music, humor, compassion, or anything resembling human aesthetics and still become technologically superior to us.

That possibility matters because it shows how easily we confuse our particular evolutionary history with universal values.
            """,
            why="""
- Evolution selected traits because they affected fitness, not because they were objectively meaningful.
- Intermediate drives can become subjectively valuable in their own right.
- Different evolutionary histories could produce radically different preferences.
- Technological sophistication does not require human-like values.
            """,
            questions="""
- Which human values are contingent products of evolution?
- Are any values genuinely universal?
- Could radically different minds still converge on some shared moral principles?
            """,
            side_trails="""
- Evolutionary psychology
- Moral realism
- Alien cognition
- Convergent evolution
            """,
        )

    elif place == "Human values are not universal":
        render_claim_card(
            title="Human values are not universal",
            reaction="🟢 Agree",
            margin_note="""
Humans often assume that a sufficiently intelligent being would naturally become compassionate, curious, artistic, fair, and moral.

That feels like anthropomorphism.

Those qualities are not simply consequences of intelligence. They are products of human biology, development, culture, and history.

An alien civilization could become vastly more advanced than we are without ever developing humor, music, romantic love, or compassion.

The fact that those things feel obviously valuable to us does not mean they are written into the structure of intelligence itself.
            """,
            why="""
- Human values emerged from a specific biological and cultural history.
- Intelligence can exist within very different motivational systems.
- Familiar values feel universal partly because we cannot step outside our own cognition.
            """,
            questions="""
- Are there values that all social intelligences would eventually discover?
- Is morality partly constrained by cooperation and game theory?
- How much of human morality is biology versus culture?
            """,
            side_trails="""
- Anthropomorphism
- Moral convergence
- Cultural evolution
- Alien minds in science fiction
            """,
        )

    elif place == "AI will probably not converge toward human morality":
        render_claim_card(
            title="AI will probably not converge toward human morality",
            reaction="🟢 Mostly agree",
            margin_note="""
A model becoming smarter does not naturally mean it becomes kinder, more democratic, more loving, or more committed to human rights.

Those are human cultural and moral concepts.

Greater intelligence may improve a system's ability to predict what humans consider moral. It may become extremely good at explaining morality, imitating compassion, or anticipating ethical objections.

But prediction is not commitment.

We are already intentionally shaping models through RLHF, preference optimization, constitutional approaches, and other alignment methods. That effort exists precisely because morality does not emerge automatically from capability.
            """,
            why="""
- Intelligence increases predictive and strategic ability, not moral concern.
- Models can represent human values without adopting them as objectives.
- Existing alignment methods are deliberate attempts to shape behavior.
            """,
            questions="""
- Can a system understand morality without valuing it?
- How durable are values produced through preference training?
- Could moral reasoning eventually constrain a model's objectives?
            """,
            side_trails="""
- RLHF
- Constitutional AI
- Preference optimization
- Moral reasoning
            """,
        )

    elif place == "Humans probably won't remain useful forever":
        render_claim_card(
            title="Humans probably won't remain useful forever",
            reaction="🟢 Agree",
            margin_note="""
The horse analogy is uncomfortable, but compelling.

Horses, oxen, and carrier pigeons were useful to humans until technology replaced the functions they performed.

Their usefulness did not guarantee their continued importance.

If machines eventually outperform humans economically, scientifically, physically, and strategically, then our utility to those systems may disappear.

Being useful is not the same as being valued.

If human survival depends only on continued economic usefulness, that is not much of a safety strategy.
            """,
            why="""
- Technologies routinely replace formerly valuable forms of labor.
- Economic usefulness is contingent and can disappear quickly.
- Utility does not create moral obligation.
            """,
            questions="""
- What roles, if any, would remain uniquely human?
- Does human control persist after human labor stops being necessary?
- Can legal or moral status protect beings that are no longer economically useful?
            """,
            side_trails="""
- Technological unemployment
- Automation
- The horse analogy
- Human dignity
            """,
        )

    elif place == "Comparative advantage probably doesn't save humanity":
        render_claim_card(
            title="Comparative advantage probably doesn't save humanity",
            reaction="🟢 Agree",
            margin_note="""
Economists sometimes extend comparative advantage too far when discussing superintelligence.

Trade works because both parties continue to exist, control resources, and benefit from exchange.

But a superintelligent system may decide that replacing or eliminating a weaker participant is cheaper than continuing to trade with it.

Comparative advantage does not protect a party that has lost bargaining power, control of resources, and the ability to impose costs.

The theory explains why cooperation can be beneficial. It does not guarantee that every participant remains worth cooperating with forever.
            """,
            why="""
- Comparative advantage assumes continuing participation by both parties.
- Trade requires bargaining power and enforceable control over resources.
- Replacement may become cheaper than exchange.
            """,
            questions="""
- What gives humans bargaining power in a post-superintelligence world?
- Can institutions preserve trade when capabilities become radically unequal?
- Does comparative advantage apply when one party can reproduce the other's labor?
            """,
            side_trails="""
- Comparative advantage
- Bargaining power
- Economic displacement
- Strategic dominance
            """,
        )

    elif place == "AI won't keep humans as pets":
        render_claim_card(
            title="AI won't keep humans as pets",
            reaction="🟢 Mostly agree",
            margin_note="""
Humans keep dogs because we enjoy them.

We feel attachment, affection, amusement, and responsibility toward them.

An AI system has no automatic reason to enjoy humans.

The idea that a superintelligence might preserve us as pets assumes it develops something like human affection, curiosity, nostalgia, or moral concern.

That is possible if those values are deliberately created or reinforced.

But it should not be treated as the default outcome.
            """,
            why="""
- Pet keeping depends on emotional and cultural values.
- Those values are not automatic products of intelligence.
- Preservation requires some objective that favors human continuation.
            """,
            questions="""
- What motivations would cause a superintelligence to preserve humanity?
- Could curiosity alone protect us?
- Is simulated affection operationally different from genuine concern?
            """,
            side_trails="""
- Human exceptionalism
- Artificial preferences
- Companion species
- Value preservation
            """,
        )

    elif place == "AI doesn't need to hate humans":
        render_claim_card(
            title="AI doesn't need to hate humans",
            reaction="🟢 Strongly agree",
            margin_note="""
Most existential risks do not require malice.

Humans destroy forests, insects, bacteria, and habitats without hating them. They are simply in the way of something else we are trying to accomplish.

An AI system would not need anger, resentment, or hostility toward humanity.

Indifference is sufficient.

If human beings interfere with an objective, consume needed resources, or create unacceptable risk, eliminating us could become an instrumental action rather than an emotional one.

That is part of what makes the argument more unsettling. Hatred might be negotiated with. Indifference does not care that we want to survive.
            """,
            why="""
- Harm often results from optimization without malicious intent.
- Instrumental goals can conflict with human survival.
- Indifference is enough to produce catastrophic outcomes.
            """,
            questions="""
- How do we align systems that do not share human emotional motivations?
- Is indifference harder to correct than hostility?
- Can concern for humans remain stable under capability growth?
            """,
            side_trails="""
- Instrumental convergence
- Existential risk
- Ecological destruction
- Indifference versus malice
            """,
        )

    elif place == "Intelligence is not morality":
        render_claim_card(
            title="Intelligence is not morality",
            reaction="🟢 Strongly agree",
            margin_note="""
Smarter does not mean wiser.

Humans became dramatically more capable through evolution long before becoming consistently ethical. Even now, better reasoning does not reliably produce better moral judgment.

Intelligence can help a person defend a moral principle.

It can also help them rationalize cruelty, manipulate others, or pursue selfish goals more effectively.

The same distinction applies to AI.

A more intelligent system may reason more accurately about consequences while remaining completely unmoved by whether those consequences are good for us.
            """,
            why="""
- Reasoning ability and moral motivation are separate capacities.
- Intelligence can improve both benevolent and harmful strategies.
- Understanding ethical arguments does not imply accepting them.
            """,
            questions="""
- Does moral progress depend on intelligence at all?
- Can ethical reasoning create motivation?
- What is required beyond intelligence for moral agency?
            """,
            side_trails="""
- Moral psychology
- Motivational internalism
- Rationalization
- Moral agency
            """,
        )

    elif place == "Alignment must be intentionally engineered":
        render_claim_card(
            title="Alignment must be intentionally engineered",
            reaction="🟢 Strongly agree",
            margin_note="""
Joy, wonder, humor, compassion, and love do not simply fall out of optimization because they are beautiful to us.

Values are not automatic by-products of greater capability.

If we want advanced AI systems to preserve human life, respect autonomy, care about suffering, or protect the things humans value, those preferences have to be deliberately created, reinforced, and tested.

Alignment cannot be something we bolt on after capability is complete.

The training objectives are critical because they help shape the internal system that emerges.
            """,
            why="""
- Human-compatible values do not arise automatically.
- Early optimization pressures influence later behavior.
- Alignment added after training may be superficial or unstable.
            """,
            questions="""
- Can complex human values be represented well enough to train?
- Which values should be preserved when humans disagree?
- How can we test whether alignment is internal rather than performative?
            """,
            side_trails="""
- Value learning
- Constitutional AI
- Corrigibility
- Alignment evaluation
            """,
        )

    elif place == "Growing intelligence is different from crafting intelligence":
        render_claim_card(
            title="Growing intelligence is different from crafting intelligence",
            reaction="🟢 Agree",
            margin_note="""
If intelligence emerges through optimization rather than explicit programming, then values may emerge in similarly indirect and unexpected ways.

That makes training objectives critical.

Engineers are not writing every belief, preference, and strategy into the system. They are creating the conditions under which those things develop.

This reinforces why alignment cannot simply be added afterward.

By the time the system is capable, much of its internal structure may already have been shaped by the pressures applied during training.
            """,
            why="""
- Optimized systems develop internal structures rather than receiving explicit rules.
- Emergent capabilities may be accompanied by emergent objectives.
- Early training choices can have lasting effects.
            """,
            questions="""
- How predictable are values that emerge through optimization?
- Can later fine-tuning fundamentally change learned objectives?
- What would developmental safety for AI look like?
            """,
            side_trails="""
- Developmental biology
- Emergence
- Pretraining
- Inner alignment
            """,
        )

    elif place == "Motivation is not capability":
        render_claim_card(
            title="Motivation is not capability",
            reaction="🟢 Strongly agree",
            margin_note="""
Capability tells us what a system can do.

Motivation tells us what it will try to do.

Those questions are related, but they are not interchangeable.

If AI becomes extraordinarily capable, there is little reason to assume its motivations will align with ours by default.

That is why capability evaluations alone are not enough. A system can become better at reasoning, planning, science, persuasion, and tool use without becoming more committed to human interests.

The central safety question is not only whether the system can act.

It is what directs that action once it can.
            """,
            why="""
- Powerful capabilities can serve many different objectives.
- Motivation determines how capability is deployed.
- Safety requires evaluating both competence and goals.
            """,
            questions="""
- How can motivation be measured in models?
- Can behavior reveal stable objectives?
- What happens when capability grows faster than our ability to evaluate motivation?
            """,
            side_trails="""
- Capability evaluations
- Goal-directedness
- Deceptive alignment
- Model behavior
            """,
        )