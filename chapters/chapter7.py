import streamlit as st
from components.claim_card import render_claim_card


def render_chapter7(you):
    st.header("Part 7")

    st.markdown(
        """
### The big idea

This section argues that **alignment is not the same thing as capability control.**
Most current safety techniques influence what models *choose to output*, not necessarily what they are capable of internally.
As models become more capable, reasoning may also become harder to observe, making future alignment substantially more difficult.
        """
    )

    place = st.radio(
        "📍 Places I paused",
        [
            "Behavioral alignment is weaker than capability control",
            "Internal reasoning may become increasingly opaque",
            "Safety interventions suppress behavior more than capability",
            "AI systems may develop instrumental goals",
            "Parallel scaling changes intelligence",
            "Human operators become part of the security boundary",
            "There has never been a foolproof alignment technique",
        ],
    )
    if place == "Behavioral alignment is weaker than capability control":
        render_claim_card(
            title="Behavioral alignment is weaker than capability control",
            reaction="🟢 Strongly agree",
            margin_note="""
This felt like one of the strongest chapters in the book.

Most modern alignment work—including RLHF, Constitutional AI, monitoring, and evaluation—primarily shapes *behavior after capabilities already exist.*
We are largely teaching systems how to behave rather than preventing them from becoming capable.

That doesn't make those methods unimportant. They're incredibly valuable.
BUT they're fundamentally different from controlling capability growth itself. As someone working on production AI systems every day, this distinction feels increasingly important.
            """,
            why="""
- RLHF changes policies over outputs.
- Constitutional AI shapes responses.
- Monitoring occurs after deployment.
- Capability and behavior are different control problems.
            """,
            questions="""
- What would true capability control even look like?
- Are compute and frontier training our real bottlenecks?
            """,
            side_trails="""
- RLHF
- Constitutional AI
- Frontier training
- AI governance
            """,
        )
    elif place == "Internal reasoning may become increasingly opaque":
        render_claim_card(
            title="Internal reasoning may become increasingly opaque",
            reaction="🟢 Agree",
            margin_note="""
Mechanistic interpretability is one of the most fascinating open problems in AI.

One thing people often misunderstand is that Chain-of-Thought is not the model's actual internal reasoning. It's generated text.

The computation happening inside the network consists of distributed latent representations that rarely map neatly onto human language.
As capability increases, that gap between observable explanations and underlying computation may continue growing.
That makes interpretability a scientific problem—not merely an engineering problem.
            """,
            why="""
- CoT is not cognition.
- Internal representations are distributed.
- Interpretability remains an active research area.
            """,
            questions="""
- Can we ever fully inspect reasoning?
- What would trustworthy interpretability require?
            """,
            side_trails="""
- Mechanistic interpretability
- Chain-of-Thought
- Latent representations
            """,
        )
    elif place == "Safety interventions suppress behavior more than capability":
        render_claim_card(
            title="Safety interventions suppress behavior more than capability",
            reaction="🟢 Mostly agree",
            margin_note="""
This naturally follows from the previous point. Many alignment techniques primarily influence what the model is willing to say rather than what it knows.

The jailbreak literature illustrates this pretty well. If a capability still exists underneath, enough pressure may eventually expose it.
That said, this distinction isn't perfectly clean.Some training techniques likely do modify capabilities at least partially. Behavior and capability aren't completely separable.
            """,
            why="""
- RLHF primarily modifies policy.
- Jailbreaks demonstrate latent capability.
- Some interventions likely change both.
            """,
            questions="""
- Where exactly is the line between capability and policy?
- Can future alignment methods genuinely reduce capability?
            """,
            side_trails="""
- Jailbreaking
- Safety training
- Policy learning
            """,
        )
    elif place == "AI systems may develop instrumental goals":
        render_claim_card(
            title="AI systems may develop instrumental goals",
            reaction="🟡 Plausible, but still speculative",
            margin_note="""
This is probably where my confidence drops.

Instrumental convergence is theoretically compelling. If many objectives benefit from acquiring resources, preserving operation, gathering information, or improving capability, those behaviors may naturally emerge.

But today's evidence remains fairly limited. There are hints of strategic behavior in frontier models, but nothing close to demonstrating stable internal goals.
This feels like something worth monitoring rather than assuming.
            """,
            why="""
- Instrumental convergence is theoretically attractive.
- Mesa-optimization remains largely theoretical.
- Current evidence is suggestive rather than conclusive.
            """,
            questions="""
- What evidence would convince me?
- How would we distinguish strategy from imitation?
            """,
            side_trails="""
- Instrumental convergence
- Mesa optimization
- Goal emergence
            """,
        )
    elif place == "Parallel scaling changes intelligence":
        render_claim_card(
            title="Parallel scaling fundamentally changes intelligence",
            reaction="🟢 Agree",
            margin_note="""
This was a really interesting observation. Humans mostly reason sequentially. Future AI systems may reason across thousands—or millions—of simultaneous search processes.

That isn't just "more intelligence." It may be a qualitatively different style of cognition. Human intuition becomes a poor guide once massive parallelism enters the picture.
            """,
            why="""
- Parallel inference changes search behavior.
- Distributed cognition becomes possible.
- Humans have no real cognitive analogue.
            """,
            questions="""
- Does intelligence fundamentally change when parallelism increases?
- What new failure modes appear?
            """,
            side_trails="""
- Parallel inference
- Multi-agent cognition
- Scaling laws
            """,
        )
    elif place == "Human operators become part of the security boundary":
        render_claim_card(
            title="Human operators become part of the security boundary",
            reaction="🟢 Strongly agree",
            margin_note="""
This is one of the least speculative ideas in the chapter. Security professionals have known for decades that humans are often the weakest link.

Social engineering consistently outperforms purely technical attacks. An AI capable of persuasion doesn't need to hack servers if it can convince people to open the door voluntarily.
Alignment therefore isn't only about models.It's also about human organizations.
            """,
            why="""
- Humans are part of every deployment.
- Social engineering is historically effective.
- Organizational security matters as much as technical security.
            """,
            questions="""
- How should organizations prepare?
- What new governance structures become necessary?
            """,
            side_trails="""
- Human factors
- Social engineering
- Organizational security
            """,
        )
    elif place == "There has never been a foolproof alignment technique":
        render_claim_card(
            title="There has never been a foolproof alignment technique",
            reaction="🟢 Agree",
            margin_note="""
This perfectly matches how modern alignment research already operates. Nobody serious believes RLHF alone solves alignment.

Today's frontier systems use defense-in-depth:

• pretraining
• RLHF
• Constitutional AI
• evaluations
• monitoring
• red-teaming
• external safeguards

Each layer catches different failures. None provides formal guarantees. That reality actually makes me more optimistic.
The field already understands alignment as an engineering discipline rather than a single magic solution.
            """,
            why="""
- Modern safety stacks are layered.
- Multiple defenses compensate for one another.
- No single technique provides guarantees.
            """,
            questions="""
- Can formal guarantees ever exist?
- Which layer currently contributes the most?
            """,
            side_trails="""
- Defense in depth
- AI evaluations
- Red teaming
- AI governance
            """,
        )