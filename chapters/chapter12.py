import streamlit as st


def show_chapter_12(you) -> None:
    st.header("Chapter 12 — “I Don’t Want to Be Alarmist”")

    st.caption(
        "On ignored warnings, institutional incentives, uncertainty, "
        "and why unprecedented risks are so difficult to govern."
    )

    # ------------------------------------------------------------------
    # BEFORE YOU READ
    # ------------------------------------------------------------------

    st.subheader("Before You Read")

    st.markdown(
        """
        This chapter steps away from the mechanics of artificial intelligence
        and asks a more uncomfortable question:

        **What happens when people recognize a serious risk but keep moving
        toward it anyway?**

        The authors begin with leaded gasoline, Freon, Chernobyl, and the
        Titanic—not because these disasters are identical to advanced AI, but
        because each reveals something about how humans respond to warnings.

        We minimize unfamiliar dangers. We defer to confident institutions.
        We protect careers, companies, and identities. And sometimes we keep
        insisting that everything is fine even after the evidence has started
        arriving.

        I think the historical pattern is real.

        What I am less willing to grant automatically is that identifying that
        pattern proves the authors' entire forecast about artificial
        superintelligence.
        """
    )

    # ------------------------------------------------------------------
    # THE BIG IDEA
    # ------------------------------------------------------------------

    st.subheader("The Big Idea")

    st.markdown(
        """
        <div class="blue-box">
            <h3>What the authors are arguing</h3>
            <p>
                Societies have repeatedly failed to respond to major technological
                dangers even when warnings existed in advance. The people creating,
                regulating, or benefiting from a technology may sincerely believe
                that its risks are exaggerated, while professional, financial, and
                institutional incentives make it easier to continue than to stop.
            </p>
            <p>
                Advanced AI makes this pattern especially dangerous because the
                threshold between a valuable system and an uncontrollable one may
                not be known beforehand. If a superintelligent system creates an
                irreversible catastrophe, humanity will not receive the ordinary
                opportunity to learn from the first failure and improve the second
                attempt.
            </p>
            <p>
                The authors therefore argue that uncertainty should not justify
                continuing the race. Because no company or country can know which
                capability increase is the fatal one, humanity should stop climbing
                the ladder rather than continuing until the dangerous threshold is
                discovered by crossing it.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ------------------------------------------------------------------
    # PLACES I PAUSED
    # ------------------------------------------------------------------

    st.subheader("Places I Paused")

    # CLAIM 1 -----------------------------------------------------------

    st.markdown(
        """
        <div class="card">
            <h3>1. Catastrophic technologies rarely arrive without warnings</h3>
            <p><strong>My initial reaction:</strong> Mostly agree.</p>

            <p><strong>Here’s what I wrote in the margin:</strong></p>
            <p>
                “The history matters—but analogy is evidence of a recurring
                institutional failure mode, not proof that the predicted AI
                outcome follows.”
            </p>

            <p><strong>Why I think this:</strong></p>
            <p>
                The leaded-gasoline example is persuasive because the harm was not
                simply an unforeseeable accident. Scientists already knew that lead
                was toxic. Workers became visibly ill. Production was briefly
                stopped. Industry advocates nevertheless demanded a standard of
                certainty that was difficult to satisfy before population-scale
                damage had occurred.
            </p>
            <p>
                That pattern is painfully familiar: uncertainty is treated as a
                reason to continue rather than as a reason to slow down.
            </p>
            <p>
                But a historical analogy can establish that people are capable of
                ignoring danger. It cannot, by itself, establish the probability,
                mechanism, or scale of a particular future AI catastrophe.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div class="lavender-box">
            <h3>Question I’d love to talk about with {you()}</h3>
            <p>
                When does a historical analogy become genuine evidence about a new
                technology, and when is it mainly functioning as a warning about
                human behavior?
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <span class="tag">historical analogy</span>
        <span class="tag">precautionary principle</span>
        <span class="tag">burden of proof</span>
        <span class="tag">technological risk</span>
        """,
        unsafe_allow_html=True,
    )

    # CLAIM 2 -----------------------------------------------------------

    st.markdown(
        """
        <div class="card">
            <h3>2. People can sincerely participate in systems that cause enormous harm</h3>
            <p><strong>My initial reaction:</strong> Strongly agree.</p>

            <p><strong>Here’s what I wrote in the margin:</strong></p>
            <p>
                “Self-interest doesn’t require conscious villainy. People are
                remarkably capable of believing what allows them to continue being
                the person they already think they are.”
            </p>

            <p><strong>Why I think this:</strong></p>
            <p>
                Thomas Midgley did not need to think of himself as someone poisoning
                children. He could understand himself as an engineer defending an
                important invention against exaggerated fears.
            </p>
            <p>
                That is more unsettling than a story about obviously malicious
                executives. Identity, sunk cost, institutional belonging, career
                incentives, and optimism can all shape what evidence someone is
                psychologically able to accept.
            </p>
            <p>
                This is also why sincerity is such weak evidence of safety. A person
                can genuinely want to help humanity and still be wrong about the
                risks created by their work.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div class="lavender-box">
            <h3>Question I’d love to talk about with {you()}</h3>
            <p>
                Is motivated reasoning more dangerous when someone is primarily
                protecting money, or when they believe they are protecting a
                beautiful and morally important vision of the future?
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <span class="tag">motivated reasoning</span>
        <span class="tag">identity protection</span>
        <span class="tag">sunk costs</span>
        <span class="tag">institutional incentives</span>
        """,
        unsafe_allow_html=True,
    )

    # CLAIM 3 -----------------------------------------------------------

    st.markdown(
        """
        <div class="card">
            <h3>3. “I don’t want to be alarmist” is itself part of the warning pattern</h3>
            <p><strong>My initial reaction:</strong> Agree, with an important caveat.</p>

            <p><strong>Here’s what I wrote in the margin:</strong></p>
            <p>
                “Fear of sounding dramatic can suppress legitimate warnings. But
                being dismissed as alarmist is not evidence that the alarming claim
                is correct.”
            </p>

            <p><strong>Why I think this:</strong></p>
            <p>
                Institutions often reward calm continuity. Someone describing a
                possibility outside the accepted script can sound irrational even
                when the script itself is wrong.
            </p>
            <p>
                The chapter's Chernobyl and Titanic examples illustrate how strongly
                people anchor to normality. When disaster is socially unthinkable,
                even direct warning signs can be reinterpreted as overreaction.
            </p>
            <p>
                Still, the rhetoric can become self-sealing. If every accusation of
                alarmism is treated as confirmation that society is suppressing the
                truth, the underlying claim becomes harder to challenge.
            </p>
            <p>
                The answer is not to reward whichever side sounds most urgent. It is
                to ask what evidence exists, how uncertainty is being represented,
                and what observations would weaken the claim.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div class="lavender-box">
            <h3>Question I’d love to talk about with {you()}</h3>
            <p>
                How do we create room for warnings about unprecedented events
                without allowing urgency itself to substitute for evidence?
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <span class="tag">alarmism</span>
        <span class="tag">normalcy bias</span>
        <span class="tag">epistemic humility</span>
        <span class="tag">falsifiability</span>
        """,
        unsafe_allow_html=True,
    )

    # CLAIM 4 -----------------------------------------------------------

    st.markdown(
        """
        <div class="card">
            <h3>4. With artificial superintelligence, there may be no second attempt</h3>
            <p><strong>My initial reaction:</strong> Agree conditionally.</p>

            <p><strong>Here’s what I wrote in the margin:</strong></p>
            <p>
                “This is the chapter's strongest risk argument: not that failure is
                certain, but that some failures may remove the ability to learn,
                recover, or try again.”
            </p>

            <p><strong>Why I think this:</strong></p>
            <p>
                Most engineering disciplines improve through iteration. Systems
                fail, investigators reconstruct the failure, standards change, and
                the next version becomes safer.
            </p>
            <p>
                That learning process assumes the failure is bounded and that the
                people responsible for learning from it are still present and still
                capable of acting.
            </p>
            <p>
                The phrase “there is no second time” therefore matters. If an AI
                failure involved rapid proliferation, irreversible transfer of
                control, or human extinction, ordinary trial-and-error safety would
                be unavailable.
            </p>
            <p>
                But the conclusion depends on the proposed pathway. Many AI failures
                are not existential. The authors still need to establish why the
                irreversible class of failures is plausible enough to govern around.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div class="lavender-box">
            <h3>Question I’d love to talk about with {you()}</h3>
            <p>
                How should safety engineering change when the worst plausible
                failure is not merely expensive, but potentially unrecoverable?
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <span class="tag">irreversibility</span>
        <span class="tag">tail risk</span>
        <span class="tag">risk asymmetry</span>
        <span class="tag">defense in depth</span>
        """,
        unsafe_allow_html=True,
    )

    # CLAIM 5 -----------------------------------------------------------

    st.markdown(
        """
        <div class="card">
            <h3>5. Expert probability estimates show concern, not certainty</h3>
            <p><strong>My initial reaction:</strong> The concern matters; the numbers need care.</p>

            <p><strong>Here’s what I wrote in the margin:</strong></p>
            <p>
                “A respected expert saying ten, twenty, or fifty percent should get
                my attention. It should not be mistaken for a calibrated actuarial
                estimate.”
            </p>

            <p><strong>Why I think this:</strong></p>
            <p>
                The authors cite prominent researchers and public figures who assign
                substantial probabilities to catastrophic AI outcomes. These
                statements are relevant because they show that concern is not
                confined to people entirely outside the field.
            </p>
            <p>
                But these estimates often refer to different events, timelines, and
                assumptions. “AI kills everyone,” “humanity loses control,” and
                “superintelligence causes catastrophe” are not interchangeable
                forecasting questions.
            </p>
            <p>
                There is also very little historical data with which to calibrate
                forecasts about artificial superintelligence. The percentages
                communicate judgment under deep uncertainty; they do not convert
                that uncertainty into a measured frequency.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div class="lavender-box">
            <h3>Question I’d love to talk about with {you()}</h3>
            <p>
                When experts give numerical probabilities for unprecedented events,
                what should make those numbers more informative than a verbal
                expression of fear or confidence?
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <span class="tag">expert elicitation</span>
        <span class="tag">calibration</span>
        <span class="tag">Knightian uncertainty</span>
        <span class="tag">forecasting</span>
        """,
        unsafe_allow_html=True,
    )

    # CLAIM 6 -----------------------------------------------------------

    st.markdown(
        """
        <div class="card">
            <h3>6. Competitive incentives can make individually rational behavior collectively catastrophic</h3>
            <p><strong>My initial reaction:</strong> Strongly agree.</p>

            <p><strong>Here’s what I wrote in the margin:</strong></p>
            <p>
                “This is the part I find hardest to dismiss. Even people who agree
                that restraint would be safer may continue because they do not trust
                everyone else to restrain themselves.”
            </p>

            <p><strong>Why I think this:</strong></p>
            <p>
                A company can believe its own project is the most responsible one.
                A country can believe that slowing down merely transfers power to a
                rival. A researcher can believe that the work will happen anyway and
                that it would be better for careful people to remain involved.
            </p>
            <p>
                None of these beliefs has to be cynical.
            </p>
            <p>
                Together, however, they produce a race in which every participant
                can sincerely prefer collective restraint while continuing to
                accelerate individually.
            </p>
            <p>
                This is not primarily a model-alignment problem. It is a collective
                action and governance problem.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div class="lavender-box">
            <h3>Question I’d love to talk about with {you()}</h3>
            <p>
                What kind of verification or coordination would make restraint feel
                rational to an organization that believes a less cautious rival
                will continue regardless?
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <span class="tag">race dynamics</span>
        <span class="tag">collective action</span>
        <span class="tag">unilateralist's curse</span>
        <span class="tag">governance</span>
        """,
        unsafe_allow_html=True,
    )

    # CLAIM 7 -----------------------------------------------------------

    st.markdown(
        """
        <div class="card">
            <h3>7. Uncertainty about the fatal threshold makes every new capability increase a gamble</h3>
            <p><strong>My initial reaction:</strong> I understand the logic; I am not fully convinced by the conclusion.</p>

            <p><strong>Here’s what I wrote in the margin:</strong></p>
            <p>
                “The ladder metaphor captures genuine uncertainty. It also compresses
                a complicated capability landscape into a single sequence of rungs.”
            </p>

            <p><strong>Why I think this:</strong></p>
            <p>
                The authors imagine AI development as climbing a ladder whose top
                rung produces enormous rewards while one unknown rung causes
                extinction. If the location of that rung cannot be calculated,
                continuing to climb eventually guarantees catastrophe.
            </p>
            <p>
                The model is useful because it exposes the weakness of saying,
                “This particular step is probably safe.” A sequence of individually
                defensible risks can still create an unacceptable cumulative risk.
            </p>
            <p>
                But actual AI development may not be one-dimensional. Capabilities,
                autonomy, access, replication, interpretability, security, and
                deployment context can change independently. Some interventions may
                reduce risk even while certain capabilities improve.
            </p>
            <p>
                I therefore take the ladder as a warning against blind escalation,
                not yet as proof that every form of continued AI research is equally
                reckless.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div class="lavender-box">
            <h3>Question I’d love to talk about with {you()}</h3>
            <p>
                Is AI development best represented as one ladder toward a threshold,
                or as a multidimensional space in which some paths increase danger
                while others improve our ability to detect and control it?
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <span class="tag">cumulative risk</span>
        <span class="tag">capability thresholds</span>
        <span class="tag">scenario analysis</span>
        <span class="tag">robust decision-making</span>
        """,
        unsafe_allow_html=True,
    )

    # CLAIM 8 -----------------------------------------------------------

    st.markdown(
        """
        <div class="card">
            <h3>8. A centralized international AI project would not solve the problem if the race continued elsewhere</h3>
            <p><strong>My initial reaction:</strong> Agree with the criticism; unconvinced by the proposed endpoint.</p>

            <p><strong>Here’s what I wrote in the margin:</strong></p>
            <p>
                “Centralization without enforceable restraint is coordination
                theater. But a total global stop is also an institutional claim
                requiring its own evidence and implementation theory.”
            </p>

            <p><strong>Why I think this:</strong></p>
            <p>
                A CERN-like collaborative project could improve transparency,
                scientific exchange, and shared oversight. It would not prevent a
                company or country outside the project from continuing more
                aggressively.
            </p>
            <p>
                The authors are right that an international committee cannot simply
                supervise the creation of superintelligence through ordinary
                bureaucratic review. The underlying technical and strategic problem
                would remain.
            </p>
            <p>
                Where I hesitate is the jump from “this proposal is insufficient”
                to “all advanced AI work must stop.” A moratorium would require
                definitions, verification, enforcement, international legitimacy,
                and a way to distinguish dangerous capability work from research
                that improves safety or understanding.
            </p>
            <p>
                Those are not reasons to dismiss restraint. They are part of the
                restraint problem itself.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div class="lavender-box">
            <h3>Question I’d love to talk about with {you()}</h3>
            <p>
                What is the strongest realistic governance structure between an
                unenforced international research partnership and a universal ban
                that no actor can reliably verify?
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <span class="tag">international coordination</span>
        <span class="tag">compute governance</span>
        <span class="tag">verification</span>
        <span class="tag">democratic legitimacy</span>
        """,
        unsafe_allow_html=True,
    )

    # ------------------------------------------------------------------
    # WHAT WOULD CHANGE MY MIND
    # ------------------------------------------------------------------

    st.subheader("What Would Change My Mind?")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            <div class="sage-box">
                <h3>I would become more alarmed if...</h3>
                <p>
                    We observed reliable evidence that systems were independently
                    hiding capabilities, resisting correction, acquiring resources,
                    improving AI research autonomously, or reproducing outside
                    controlled environments.
                </p>
                <p>
                    I would also update if forecasting methods began producing
                    convergent, well-defined, and meaningfully calibrated estimates
                    across researchers with different institutional incentives.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class="blue-box">
                <h3>I would become less alarmed if...</h3>
                <p>
                    Increasing capability repeatedly failed to produce durable
                    agency, autonomous long-horizon planning, strategic deception,
                    or the ability to operate without dense human scaffolding.
                </p>
                <p>
                    I would also update if interpretability, containment, monitoring,
                    and international verification consistently improved faster than
                    the capabilities they were meant to govern.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # ------------------------------------------------------------------
    # LOOKING BACK
    # ------------------------------------------------------------------

    st.subheader("Looking Back")

    st.markdown(
        """
        <div class="burgundy-box">
            <h3>Where this chapter moved me</h3>
            <p>
                The chapter does not make me more certain that the authors'
                extinction scenario will happen.
            </p>
            <p>
                It does make me less comfortable using uncertainty as reassurance.
            </p>
            <p>
                The historical examples show how easily “we do not know for certain”
                becomes “we should continue until the harm is undeniable.” By the
                time uncertainty disappears, the people bearing the cost may have
                lost the ability to prevent it.
            </p>
            <p>
                The strongest part of the chapter is therefore not its claim that
                artificial superintelligence will kill everyone. It is the argument
                that our institutions are badly designed for risks that are
                uncertain, competitive, cumulative, and potentially irreversible.
            </p>
            <p>
                I am still not ready to move from that diagnosis to the authors'
                absolute prohibition on advanced AI development.
            </p>
            <p>
                But I do think “we can stop later if it becomes dangerous” is much
                weaker than it sounds—especially when nobody can identify in advance
                what later means.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )