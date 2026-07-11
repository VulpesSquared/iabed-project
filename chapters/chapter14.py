import streamlit as st


def render_chapter14(you) -> None:
    st.header("Chapter 14 — Where There’s Life, There’s Hope")

    st.caption(
        "On uncertainty, nuclear near-misses, political action, "
        "and how to live while taking catastrophic risk seriously."
    )

    # ------------------------------------------------------------------
    # BEFORE YOU READ
    # ------------------------------------------------------------------

    st.subheader("Before You Read")

    st.markdown(
        """
        This is the final chapter, and it is doing two things at once.

        First, the authors restate the argument they have spent the entire book
        building:

        **If anyone creates artificial superintelligence, everyone dies.**

        They do not retreat to “maybe,” “possibly,” or “there is some risk.”
        Their position remains absolute.

        But the chapter is also trying to leave the reader somewhere other than
        paralysis.

        The authors turn to nuclear history, political organizing, journalism,
        public pressure, and ordinary life to argue that a predicted catastrophe
        is not the same thing as an unavoidable one.

        Humanity has lived beneath credible threats of annihilation before.
        People changed institutions, negotiated treaties, built monitoring
        systems, and sometimes prevented disaster through individual acts of
        judgment.

        I appreciate that movement from warning toward responsibility.

        I am still not convinced by the certainty of the underlying prediction.
        But I agree with the broader idea that uncertainty about whether a
        catastrophe will occur is not the same thing as evidence that no action
        is needed.
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
                Humanity should not continue developing artificial
                superintelligence merely because the exact timing of disaster
                cannot be predicted.
            </p>

            <p>
                In other safety-critical fields, placing the entire human species
                at risk would require strong evidence that catastrophe is
                extraordinarily unlikely. The authors argue that current AI
                development proceeds under the opposite standard: companies and
                governments continue unless critics can prove exactly when and how
                disaster will occur.
            </p>

            <p>
                They compare the situation to the nuclear age. Nuclear war once
                appeared highly plausible, and humanity came dangerously close to
                it. Civilization survived not because the danger was imaginary,
                but because people recognized the trajectory and worked to change
                it through diplomacy, monitoring, communication, arms agreements,
                political leadership, and individual restraint.
            </p>

            <p>
                The authors therefore ask governments, politicians, journalists,
                and ordinary citizens to help build support for international
                restrictions on advanced AI development.
            </p>

            <p>
                Their final message is that action and ordinary life are not
                opposites. People should do what they can to reduce the danger,
                then continue living rather than allowing fear to consume the life
                they are trying to protect.
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
            <h3>1. An apparently certain death can still fail to occur</h3>

            <p><strong>My initial reaction:</strong> Agree, but the lesson is
            narrower than the chapter sometimes makes it sound.</p>

            <p><strong>Here’s what I wrote in the margin:</strong></p>

            <p>
                “A confident prediction can be wrong. That does not mean every
                extraordinary survival teaches us the same thing about policy.”
            </p>

            <p><strong>Why I think this:</strong></p>

            <p>
                The chapter opens with Vesna Vulović, who survived a fall that
                almost anyone would have predicted was fatal. The example separates
                a probable outcome from an inevitable one.
            </p>

            <p>
                That is an important epistemic reminder. Even an “easy call” can be
                wrong in an individual case.
            </p>

            <p>
                But rare survival does not tell us that the original risk estimate
                was unreasonable. Nor does it establish how we should govern a
                different threat involving different mechanisms.
            </p>

            <p>
                The story works best as a statement about hope: while an outcome has
                not occurred, there remains some possibility of changing it.
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
                When an unlikely survival occurs, should it make us question the
                original risk estimate, or simply remind us that high probability
                is not the same thing as fate?
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <span class="tag">probability</span>
        <span class="tag">uncertainty</span>
        <span class="tag">survivorship</span>
        <span class="tag">hope</span>
        """,
        unsafe_allow_html=True,
    )

    # CLAIM 2 -----------------------------------------------------------

    st.markdown(
        """
        <div class="card">
            <h3>2. The book ends with the same absolute claim it began with</h3>

            <p><strong>My initial reaction:</strong> Still disagree.</p>

            <p><strong>Here’s what I wrote in the margin:</strong></p>

            <p>
                “The argument has become more detailed, but the conclusion is still
                doing more work than the evidence can carry: if anyone builds it,
                everyone dies.”
            </p>

            <p><strong>Why I think this:</strong></p>

            <p>
                The authors explicitly reject the language of possibility and risk.
                They argue that the disaster is predictable and that the identity,
                intentions, location, and values of the builders do not matter.
            </p>

            <p>
                I think the book makes a serious case that sufficiently capable,
                autonomous, misaligned systems could create catastrophic and
                potentially irreversible harm.
            </p>

            <p>
                I do not think it demonstrates that every sufficiently advanced
                artificial intelligence must become a unified strategic agent,
                escape meaningful human control, overcome competing systems and
                institutions, and eliminate all human life.
            </p>

            <p>
                Those are connected hypotheses, not one established result.
            </p>

            <p>
                The authors’ certainty makes the policy recommendation cleaner. It
                does not make the empirical uncertainty disappear.
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
                Does the moral force of the book depend on certainty, or would its
                case for drastic precaution remain strong if the authors admitted a
                wide range of possible outcomes?
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <span class="tag">existential risk</span>
        <span class="tag">certainty</span>
        <span class="tag">argument structure</span>
        <span class="tag">burden of proof</span>
        """,
        unsafe_allow_html=True,
    )

    # CLAIM 3 -----------------------------------------------------------

    st.markdown(
        """
        <div class="card">
            <h3>3. Humanity should not need a catastrophe to be precisely predictable before acting</h3>

            <p><strong>My initial reaction:</strong> Strongly agree.</p>

            <p><strong>Here’s what I wrote in the margin:</strong></p>

            <p>
                “Requiring critics to provide the exact date, mechanism, and failure
                sequence is an impossible standard—and a convenient way to keep
                moving.”
            </p>

            <p><strong>Why I think this:</strong></p>

            <p>
                The authors compare AI development to launching a rocket carrying
                the entire human species. In an ordinary safety-critical system,
                designers would not demand that someone predict the exact moment of
                failure before requiring evidence that the vehicle was safe.
            </p>

            <p>
                This is one of the book’s stronger reversals of the burden of proof.
                When the possible harm is extreme and irreversible, uncertainty
                should not automatically favor deployment.
            </p>

            <p>
                I would still avoid the authors’ binary framing. We do not have to
                choose only between complete confidence in safety and a universal
                halt to all relevant research.
            </p>

            <p>
                But developers making increasingly consequential systems should bear
                more responsibility for demonstrating control, containment,
                security, and recoverability than critics bear for predicting an
                exact catastrophe.
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
                What level of evidence should a developer have to provide before
                deploying a system whose worst plausible failure may be
                irreversible?
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <span class="tag">safety case</span>
        <span class="tag">risk asymmetry</span>
        <span class="tag">precautionary principle</span>
        <span class="tag">deployment standards</span>
        """,
        unsafe_allow_html=True,
    )

    # CLAIM 4 -----------------------------------------------------------

    st.markdown(
        """
        <div class="card">
            <h3>4. Nuclear catastrophe was not avoided because the warnings were foolish</h3>

            <p><strong>My initial reaction:</strong> Strongly agree.</p>

            <p><strong>Here’s what I wrote in the margin:</strong></p>

            <p>
                “When prevention succeeds, the original warning can look
                exaggerated precisely because the warned-about event did not
                happen.”
            </p>

            <p><strong>Why I think this:</strong></p>

            <p>
                The chapter argues that people who predicted nuclear catastrophe
                were not necessarily wrong about the danger. Nuclear weapons could
                destroy cities, penetrate defenses, trigger escalation, and produce
                mass death.
            </p>

            <p>
                What some forecasts underestimated was humanity’s ability to alter
                the trajectory.
            </p>

            <p>
                Diplomats negotiated. Governments established direct communication.
                Monitoring systems and arms agreements were developed. People
                worked repeatedly to prevent errors, misunderstandings, and local
                crises from escalating.
            </p>

            <p>
                This creates a difficult evaluation problem. If the catastrophe does
                not happen because people responded to the warning, the warning may
                later be dismissed as alarmism.
            </p>

            <p>
                Successful prevention often removes the observable counterfactual
                that would have proven the intervention was necessary.
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
                How do we evaluate whether a warning was excessive when the actions
                motivated by that warning may be part of why the predicted disaster
                never occurred?
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <span class="tag">prevention paradox</span>
        <span class="tag">counterfactuals</span>
        <span class="tag">nuclear risk</span>
        <span class="tag">institutional learning</span>
        """,
        unsafe_allow_html=True,
    )

    # CLAIM 5 -----------------------------------------------------------

    st.markdown(
        """
        <div class="card">
            <h3>5. Civilization survives when people work to “un-write” an apparently fixed future</h3>

            <p><strong>My initial reaction:</strong> Agree.</p>

            <p><strong>Here’s what I wrote in the margin:</strong></p>

            <p>
                “This is the version of hope I trust: not optimism that everything
                will work out, but organized effort based on the belief that the
                trajectory can still be changed.”
            </p>

            <p><strong>Why I think this:</strong></p>

            <p>
                The authors distinguish passive reassurance from active hope. The
                people working to avoid nuclear war did not treat the danger as a
                remote accident. They behaved as though destruction was the path the
                world was already traveling and their job was to redirect it.
            </p>

            <p>
                That framing avoids two failures.
            </p>

            <p>
                One is fatalism: the belief that catastrophe is inevitable, so
                action is pointless.
            </p>

            <p>
                The other is complacency: the belief that civilization has survived
                so far because the danger was never serious.
            </p>

            <p>
                Hope becomes a practice rather than a forecast.
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
                Is hope more useful when it means confidence in a good outcome, or
                when it means believing that effort can still influence an uncertain
                one?
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <span class="tag">active hope</span>
        <span class="tag">collective agency</span>
        <span class="tag">fatalism</span>
        <span class="tag">resilience</span>
        """,
        unsafe_allow_html=True,
    )

    # CLAIM 6 -----------------------------------------------------------

    st.markdown(
        """
        <div class="card">
            <h3>6. Different institutions have different responsibilities</h3>

            <p><strong>My initial reaction:</strong> Agree with the structure, not
            necessarily every requested action.</p>

            <p><strong>Here’s what I wrote in the margin:</strong></p>

            <p>
                “Responsibility should follow power, access, and institutional
                function—not be flattened into the claim that everyone is equally
                responsible for everything.”
            </p>

            <p><strong>Why I think this:</strong></p>

            <p>
                The chapter addresses governments, elected officials, journalists,
                and ordinary citizens separately.
            </p>

            <p>
                Governments can negotiate treaties and establish verification
                systems. Legislators can create reporting, licensing, monitoring,
                and enforcement authority. Journalists can investigate claims,
                incentives, failures, and contradictions. Citizens can communicate
                political concern, vote, organize, and influence the legitimacy of
                action.
            </p>

            <p>
                I appreciate this role-specific approach because it resists the
                tendency to turn structural problems into consumer guilt.
            </p>

            <p>
                A person choosing not to use an AI writing tool does not meaningfully
                govern frontier model development. A regulator, cloud provider,
                chip manufacturer, laboratory executive, or head of state occupies
                a very different causal position.
            </p>

            <p>
                The chapter sometimes overstates the certainty of what these actors
                should support. But it is right that their responsibilities differ.
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
                How should responsibility for AI risk be distributed among
                developers, infrastructure providers, governments, journalists,
                researchers, and ordinary users?
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <span class="tag">institutional responsibility</span>
        <span class="tag">governance</span>
        <span class="tag">journalism</span>
        <span class="tag">collective action</span>
        """,
        unsafe_allow_html=True,
    )

    # CLAIM 7 -----------------------------------------------------------

    st.markdown(
        """
        <div class="card">
            <h3>7. Journalism should treat catastrophic AI claims as an investigative subject, not a personality conflict</h3>

            <p><strong>My initial reaction:</strong> Strongly agree.</p>

            <p><strong>Here’s what I wrote in the margin:</strong></p>

            <p>
                “The relevant story is not which CEO is charismatic or which
                researcher sounds dramatic. It is whether the claims, incentives,
                evaluations, and technical evidence hold up.”
            </p>

            <p><strong>Why I think this:</strong></p>

            <p>
                The authors ask journalists to move beyond product announcements,
                executive profiles, and simplified debates between optimists and
                pessimists.
            </p>

            <p>
                That request is reasonable.
            </p>

            <p>
                AI reporting often collapses technical and institutional questions
                into personalities: the visionary founder, the frightened former
                employee, the accelerationist, the doomer, the regulator who does
                not understand technology.
            </p>

            <p>
                Serious reporting should instead examine what systems can do, how
                those claims were tested, what incidents occurred, who has access,
                which incentives shape disclosure, and whether governance promises
                are enforceable.
            </p>

            <p>
                It should also interrogate catastrophic-risk advocates with the same
                care. Taking a claim seriously does not require treating it as true.
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
                What would genuinely rigorous AI-risk journalism investigate that
                personality-driven coverage usually misses?
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <span class="tag">technology journalism</span>
        <span class="tag">accountability</span>
        <span class="tag">evidence</span>
        <span class="tag">institutional incentives</span>
        """,
        unsafe_allow_html=True,
    )

    # CLAIM 8 -----------------------------------------------------------

    st.markdown(
        """
        <div class="card">
            <h3>8. People who are not persuaded by the full argument can still support building brakes</h3>

            <p><strong>My initial reaction:</strong> Strongly agree.</p>

            <p><strong>Here’s what I wrote in the margin:</strong></p>

            <p>
                “This is the most useful political move in the chapter: preserving
                future options does not require agreeing today that the worst-case
                forecast is certain.”
            </p>

            <p><strong>Why I think this:</strong></p>

            <p>
                The authors ask skeptical politicians to support infrastructure that
                would make later restraint possible: concentrating advanced
                computing resources, making large clusters legible, establishing
                monitoring arrangements, and preventing uncontrolled proliferation.
            </p>

            <p>
                I do not accept every element of their preferred regime. But the
                underlying concept is important.
            </p>

            <p>
                Governance often arrives after a crisis, when the institutions
                needed to respond do not yet exist. Building measurement,
                registration, evaluation, incident-reporting, audit, and coordination
                capacity now preserves options later.
            </p>

            <p>
                This is different from accepting an immediate permanent prohibition.
                It is creating the ability to slow down if stronger evidence
                emerges.
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
                Which governance mechanisms function as reversible preparedness,
                and which ones quietly commit society to a much broader control
                regime?
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <span class="tag">option value</span>
        <span class="tag">governance capacity</span>
        <span class="tag">monitoring</span>
        <span class="tag">reversibility</span>
        """,
        unsafe_allow_html=True,
    )

    # CLAIM 9 -----------------------------------------------------------

    st.markdown(
        """
        <div class="card">
            <h3>9. Ordinary users are not asked to achieve purity through individual abstention</h3>

            <p><strong>My initial reaction:</strong> Agree.</p>

            <p><strong>Here’s what I wrote in the margin:</strong></p>

            <p>
                “Good. A global coordination problem cannot be solved by asking
                individuals to become symbolically blameless while institutions
                continue unchanged.”
            </p>

            <p><strong>Why I think this:</strong></p>

            <p>
                The authors explicitly say that ordinary people do not need to stop
                using every AI tool. They acknowledge that refusing these tools may
                place an individual at a disadvantage without meaningfully changing
                the development race.
            </p>

            <p>
                This avoids a common moral displacement in technology debates.
                Responsibility is transferred from organizations with enormous
                resources and decision-making power to users making constrained
                choices inside the system those organizations created.
            </p>

            <p>
                Consumer choices can occasionally support broader movements, but
                they are not substitutes for law, infrastructure, governance, or
                collective coordination.
            </p>

            <p>
                The relevant question is not whether an individual has ever used an
                AI system. It is what political and institutional arrangements they
                are willing to support.
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
                When does personal abstention contribute to collective change, and
                when does it mainly turn a structural problem into an individual
                test of moral purity?
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <span class="tag">consumer responsibility</span>
        <span class="tag">structural change</span>
        <span class="tag">collective action</span>
        <span class="tag">moral purity</span>
        """,
        unsafe_allow_html=True,
    )

    # CLAIM 10 ----------------------------------------------------------

    st.markdown(
        """
        <div class="card">
            <h3>10. After doing what you can, live your life</h3>

            <p><strong>My initial reaction:</strong> Strongly agree.</p>

            <p><strong>Here’s what I wrote in the margin:</strong></p>

            <p>
                “Fear is not the same thing as responsibility. Protecting life also
                means continuing to inhabit it.”
            </p>

            <p><strong>Why I think this:</strong></p>

            <p>
                The chapter closes with C. S. Lewis’s argument about living under
                the threat of atomic war. The danger may be real, but organizing
                every belief, relationship, and ordinary activity around terror
                does not prevent it.
            </p>

            <p>
                People should work, teach, read, make music, raise children, spend
                time with friends, and continue doing the human things that make
                survival worth wanting.
            </p>

            <p>
                I think this is the healthiest distinction in the book.
            </p>

            <p>
                Taking a risk seriously does not require performing fear
                continuously. Constant dread is not evidence of intellectual
                seriousness, and it does not automatically produce useful action.
            </p>

            <p>
                Do the work available to you. Preserve room for joy, curiosity,
                intimacy, and ordinary life. Otherwise the feared future begins
                consuming the present before it has even arrived.
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
                What does it look like to take an existential risk seriously without
                allowing it to colonize every part of the life one is trying to
                preserve?
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <span class="tag">living with uncertainty</span>
        <span class="tag">fear</span>
        <span class="tag">meaning</span>
        <span class="tag">ordinary life</span>
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
                <h3>I would move closer to the authors’ conclusion if...</h3>

                <p>
                    Evidence showed that increasingly capable systems reliably
                    developed persistent autonomous goals, concealed capabilities,
                    improved their own research process, acquired resources, or
                    resisted meaningful intervention across different architectures
                    and training methods.
                </p>

                <p>
                    I would also update if independent technical teams repeatedly
                    concluded that proposed containment and alignment methods failed
                    before systems reached the capabilities required for autonomous
                    replication or strategic control.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class="blue-box">
                <h3>I would move farther from the authors’ conclusion if...</h3>

                <p>
                    Advanced capabilities continued to depend heavily on human
                    scaffolding, fragmented tools, restricted access, and
                    organization-specific deployment conditions rather than
                    producing durable autonomous agency.
                </p>

                <p>
                    I would also update if monitoring, interpretability, containment,
                    secure deployment, and international coordination demonstrated
                    that catastrophic pathways could be governed without the global
                    prohibition and coercive enforcement proposed by the authors.
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
            <h3>Where the book leaves me</h3>

            <p>
                I did not finish this book convinced that artificial
                superintelligence necessarily kills everyone.
            </p>

            <p>
                I remain unconvinced that capability automatically becomes agency,
                that agency inevitably becomes power-seeking, or that every
                sufficiently advanced system converges on one catastrophic
                trajectory.
            </p>

            <p>
                I also do not think uncertainty gives us permission to be careless.
            </p>

            <p>
                The book succeeds in making several weaker—but still extremely
                important—claims difficult to dismiss:
            </p>

            <p>
                We do not understand advanced model internals well enough.
                Competitive incentives reward capability before understanding.
                Voluntary corporate restraint is structurally fragile.
                National rules cannot fully govern a transnational technology.
                Some failures may be difficult or impossible to reverse.
                And “we will stop when it becomes dangerous” is not a plan unless we
                can define danger, detect it, and retain the ability to stop.
            </p>

            <p>
                I disagree most strongly when the authors turn uncertainty into
                certainty and certainty into permission for extraordinary
                centralized or military power.
            </p>

            <p>
                But I think they are right that surviving a dangerous trajectory is
                not evidence the trajectory was safe. Sometimes disaster does not
                occur because people noticed the path, took the warning seriously,
                and changed direction.
            </p>

            <p>
                So I leave the book neither reassured nor converted.
            </p>

            <p>
                I leave it more interested in the space between dismissal and
                certainty: the place where serious risk analysis, measurement,
                institutional design, technical research, and democratic legitimacy
                actually have to live.
            </p>

            <p>
                And I leave it agreeing with the final sentence more than I expected.
            </p>

            <p><strong>Where there’s life, there’s hope.</strong></p>
        </div>
        """,
        unsafe_allow_html=True,
    )