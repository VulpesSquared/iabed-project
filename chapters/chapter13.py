import streamlit as st


def render_chapter13(you) -> None:
    st.header("Chapter 13 — Shut It Down")

    st.caption(
        "On global prohibition, compute governance, coercive enforcement, "
        "and what the authors believe survival would require."
    )

    # ------------------------------------------------------------------
    # BEFORE YOU READ
    # ------------------------------------------------------------------

    st.subheader("Before You Read")

    st.markdown(
        """
        Chapter 12 argued that people routinely minimize unfamiliar dangers,
        especially when acknowledging them would require sacrifice.

        Chapter 13 is where the authors stop describing that failure and tell us
        what they believe should happen instead.

        Their answer is not ordinary AI regulation.

        It is not better evaluations, stricter licensing, more interpretability,
        or one unusually responsible company winning the race.

        Their answer is a worldwide prohibition on advancing toward
        superintelligence, backed by compute monitoring, international
        enforcement, and—if necessary—sabotage or military force.

        This is the chapter where I most clearly separate two questions:

        **Are the authors right that current governance proposals are too weak for
        the risk they describe?**

        and

        **Have they justified the extraordinary political and coercive system
        they propose in response?**

        I think the first question deserves serious attention.

        I am much less persuaded by their answer to the second.
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
                If the creation of artificial superintelligence would kill
                everyone, then humanity cannot safely permit any company, country,
                military, or independent actor to continue advancing toward it.
            </p>
            <p>
                National regulation is insufficient because the consequences would
                be global. A cautious country would remain vulnerable if another
                country continued. A responsible company would not protect humanity
                if a less responsible competitor built the dangerous system first.
            </p>
            <p>
                The authors therefore propose restricting the computing power and
                research needed to create increasingly capable AI systems. Advanced
                chips would be registered, concentrated in monitored facilities,
                and subject to international verification. Research that could make
                powerful systems dramatically cheaper or more efficient would also
                need to be prohibited.
            </p>
            <p>
                If an actor refused to comply and attempted to construct a dangerous
                datacenter, the authors argue that other states should be prepared
                to stop it through cyberattacks, sabotage, or conventional military
                action.
            </p>
            <p>
                They present this not as an ideal political arrangement, but as the
                minimum response appropriate to a technology they believe would
                otherwise cause human extinction.
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
            <h3>1. The authors frame AI governance as a wartime mobilization problem</h3>

            <p><strong>My initial reaction:</strong> I understand the logic, but I
            do not think the analogy is neutral.</p>

            <p><strong>Here’s what I wrote in the margin:</strong></p>

            <p>
                “Once the Axis powers become the comparison, almost any sacrifice
                or expansion of authority can be made to sound proportionate.”
            </p>

            <p><strong>Why I think this:</strong></p>

            <p>
                The chapter begins with World War II because the authors want to
                establish that humanity can coordinate, ration resources, suspend
                ordinary expectations, and accept enormous costs when survival is
                genuinely at stake.
            </p>

            <p>
                That historical point is true. Governments and populations are
                capable of extraordinary mobilization when they perceive a shared
                existential threat.
            </p>

            <p>
                But the analogy also performs substantial argumentative work. The
                Axis threat was observable, embodied in identifiable states and
                armies, and already producing mass violence. The danger described
                here is a forecast about a class of systems that does not yet exist.
            </p>

            <p>
                If those two situations are treated as morally equivalent before
                the probability and mechanism of the AI threat have been
                established, skepticism can begin to look like appeasement rather
                than disagreement about evidence.
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
                At what point does an emergency analogy clarify the scale of a risk,
                and at what point does it pre-load the moral conclusion before the
                evidence has done enough work?
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <span class="tag">wartime mobilization</span>
        <span class="tag">historical analogy</span>
        <span class="tag">emergency politics</span>
        <span class="tag">securitization</span>
        """,
        unsafe_allow_html=True,
    )

    # CLAIM 2 -----------------------------------------------------------

    st.markdown(
        """
        <div class="card">
            <h3>2. A global risk cannot be solved by one virtuous company or country</h3>

            <p><strong>My initial reaction:</strong> Strongly agree.</p>

            <p><strong>Here’s what I wrote in the margin:</strong></p>

            <p>
                “If the externality is global, voluntary restraint by one actor
                mostly changes who gets there first.”
            </p>

            <p><strong>Why I think this:</strong></p>

            <p>
                The authors are right that unilateral caution does not resolve a
                competitive problem. A company can slow down while another company
                accelerates. One country can regulate domestic labs while foreign
                actors continue. A military can abstain while assuming that its
                rivals will not.
            </p>

            <p>
                This creates a familiar collective-action problem: nearly everyone
                may prefer a safer equilibrium while still believing that continued
                development is individually rational.
            </p>

            <p>
                Even without accepting the authors’ extinction certainty, this
                argument applies to many AI risks. Cyber capability, biological
                design assistance, autonomous weapons, scalable persuasion, and
                model proliferation all cross borders.
            </p>

            <p>
                The chapter is strongest when it insists that “our company is
                careful” and “our country has rules” are not complete answers to a
                technology with transnational consequences.
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
                What would make restraint stable when every actor believes that
                restraint is only safe if everyone else adopts it too?
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <span class="tag">collective action</span>
        <span class="tag">global externalities</span>
        <span class="tag">race dynamics</span>
        <span class="tag">international governance</span>
        """,
        unsafe_allow_html=True,
    )

    # CLAIM 3 -----------------------------------------------------------

    st.markdown(
        """
        <div class="card">
            <h3>3. Compute is the most governable chokepoint available</h3>

            <p><strong>My initial reaction:</strong> Cautiously agree.</p>

            <p><strong>Here’s what I wrote in the margin:</strong></p>

            <p>
                “Compute is attractive to govern because chips, datacenters, and
                power draw are more legible than algorithms or intentions.”
            </p>

            <p><strong>Why I think this:</strong></p>

            <p>
                The authors propose concentrating advanced computing hardware in
                monitored locations and using chip registration, electricity
                monitoring, and international inspection to detect unauthorized
                training runs.
            </p>

            <p>
                This is more concrete than asking regulators to inspect whether an
                AI system is “too intelligent” or whether a developer has “good
                intentions.” Large training runs currently require physical
                infrastructure, specialized chips, energy, cooling, networking, and
                capital.
            </p>

            <p>
                Those physical dependencies create possible points of observation
                and control.
            </p>

            <p>
                But governable does not mean simple. Hardware can be smuggled,
                workloads can be distributed, monitoring can be evaded, governments
                can conceal military programs, and verification systems can become
                instruments of industrial surveillance.
            </p>

            <p>
                Compute governance is therefore plausible as one layer of control.
                I am not convinced it can carry the entire burden the authors place
                on it.
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
                Is compute governance a durable safety mechanism, or merely the most
                visible control point available during the current technological
                phase?
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <span class="tag">compute governance</span>
        <span class="tag">chip monitoring</span>
        <span class="tag">verification</span>
        <span class="tag">legibility</span>
        """,
        unsafe_allow_html=True,
    )

    # CLAIM 4 -----------------------------------------------------------

    st.markdown(
        """
        <div class="card">
            <h3>4. Because no safe compute threshold is known, the threshold should be set extremely low</h3>

            <p><strong>My initial reaction:</strong> This is where precaution starts
            to become prohibition by assumption.</p>

            <p><strong>Here’s what I wrote in the margin:</strong></p>

            <p>
                “The uncertainty is real. But ‘we cannot identify a safe boundary’
                does not automatically tell us that the only defensible boundary is
                near zero.”
            </p>

            <p><strong>Why I think this:</strong></p>

            <p>
                The authors acknowledge that there is nothing scientifically magical
                about a threshold such as 100,000 GPUs. They therefore recommend
                setting the legal limit dramatically lower rather than risking that
                an apparently moderate amount of compute is already enough.
            </p>

            <p>
                This follows a strict precautionary logic: when the harm is
                extinction and the threshold is unknown, err as far as possible on
                the side of restraint.
            </p>

            <p>
                The problem is that this reasoning can become difficult to falsify.
                Any threshold can be described as potentially too high because the
                dangerous system has not yet been built. The absence of a known safe
                boundary becomes evidence for choosing the most restrictive one.
            </p>

            <p>
                A defensible threshold would need to connect compute to measurable
                capabilities, deployment conditions, autonomy, access, and evidence
                of dangerous behavior. Compute alone is an imperfect proxy for all
                of them.
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
                How should policymakers choose a safety threshold when the relevant
                capability boundary is unknown and the proposed proxy is only
                indirectly related to the feared harm?
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <span class="tag">precautionary principle</span>
        <span class="tag">threshold uncertainty</span>
        <span class="tag">proxy measures</span>
        <span class="tag">burden of proof</span>
        """,
        unsafe_allow_html=True,
    )

    # CLAIM 5 -----------------------------------------------------------

    st.markdown(
        """
        <div class="card">
            <h3>5. Algorithmic efficiency can undermine hardware-based limits</h3>

            <p><strong>My initial reaction:</strong> Agree. This is one of the most
            technically important points in the chapter.</p>

            <p><strong>Here’s what I wrote in the margin:</strong></p>

            <p>
                “Controlling today’s quantity of compute does not control tomorrow’s
                capability if algorithms keep making each unit of compute more
                productive.”
            </p>

            <p><strong>Why I think this:</strong></p>

            <p>
                A system with the capabilities of last year’s frontier model may be
                trainable later using a fraction of the original hardware.
                Improvements in architectures, data efficiency, optimization,
                inference methods, distillation, and hardware utilization can move
                capability beneath a fixed compute threshold.
            </p>

            <p>
                This means that a static hardware rule decays over time.
            </p>

            <p>
                The authors respond by arguing that some algorithmic research would
                also have to become illegal. Their example is the transformer:
                apparently abstract research can unexpectedly unlock broad new
                capabilities.
            </p>

            <p>
                I agree with the diagnosis more than the prescription. Algorithmic
                progress complicates compute governance profoundly. But prohibiting
                research because the next paper might be dangerous raises enormous
                questions about scope, enforcement, scientific freedom, and how one
                distinguishes safety-enhancing work from capability-enhancing work.
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
                Can research governance meaningfully distinguish capability work
                from safety work when the same technical discovery may contribute
                to both?
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <span class="tag">algorithmic efficiency</span>
        <span class="tag">compute overhang</span>
        <span class="tag">dual-use research</span>
        <span class="tag">capability diffusion</span>
        """,
        unsafe_allow_html=True,
    )

    # CLAIM 6 -----------------------------------------------------------

    st.markdown(
        """
        <div class="card">
            <h3>6. The authors endorse sabotage or military force against noncompliant AI infrastructure</h3>

            <p><strong>My initial reaction:</strong> Strongly disagree.</p>

            <p><strong>Here’s what I wrote in the margin:</strong></p>

            <p>
                “This is not a minor implementation detail. It is a proposal to make
                speculative AI risk a possible justification for interstate
                violence.”
            </p>

            <p><strong>Why I think this:</strong></p>

            <p>
                The authors argue that if a country attempted to construct a
                prohibited AI datacenter, other powers should communicate that the
                project frightened them and demand that it stop. If diplomacy
                failed, they propose cyberattacks, sabotage, or conventional
                airstrikes.
            </p>

            <p>
                They frame this as equivalent to stopping nuclear proliferation and
                argue that datacenters may ultimately be more dangerous than nuclear
                weapons.
            </p>

            <p>
                I do not think the chapter has earned that conclusion.
            </p>

            <p>
                Preventive violence requires extraordinarily reliable intelligence,
                shared definitions, legitimate authority, evidence of imminent
                danger, and confidence that intervention will reduce rather than
                escalate the risk.
            </p>

            <p>
                A mistaken attribution, ambiguous research program, intelligence
                failure, or politically motivated accusation could create war
                between nuclear powers. Cyberattacks could spread beyond their
                intended target. Destruction of datacenters could harm civilians or
                critical infrastructure.
            </p>

            <p>
                The authors repeatedly emphasize the danger of handing control to a
                powerful unaccountable optimizer. That concern should also apply to
                states empowered to destroy infrastructure based on predictions
                about what a future AI system might become.
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
                What evidentiary standard could ever justify preventive military
                action against a computing facility, especially when the feared
                capability may not yet exist and cannot be directly observed?
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <span class="tag">preventive force</span>
        <span class="tag">state power</span>
        <span class="tag">escalation risk</span>
        <span class="tag">legitimacy</span>
        """,
        unsafe_allow_html=True,
    )

    # CLAIM 7 -----------------------------------------------------------

    st.markdown(
        """
        <div class="card">
            <h3>7. Small or incremental regulation may create the appearance of action without changing the trajectory</h3>

            <p><strong>My initial reaction:</strong> Agree with the criticism, but
            not with dismissing incremental policy altogether.</p>

            <p><strong>Here’s what I wrote in the margin:</strong></p>

            <p>
                “A policy can be politically achievable and still be irrelevant to
                the risk it claims to address.”
            </p>

            <p><strong>Why I think this:</strong></p>

            <p>
                The authors criticize proposals focused on reporting requirements,
                deepfakes, annual safety plans, or regulation of obviously weaker
                systems. Their concern is that these measures allow institutions to
                say they acted while leaving frontier capability development
                untouched.
            </p>

            <p>
                That is a legitimate governance failure mode. Regulation can become
                symbolic, fragmented, or aimed at harms that are easier to explain
                rather than those that are hardest to control.
            </p>

            <p>
                I am less convinced that incremental policy is inherently useless.
                Reporting, incident disclosure, model evaluations, chip tracking,
                liability, licensing, security requirements, and audit authority can
                create institutional capacity that does not currently exist.
            </p>

            <p>
                The relevant question is not whether a policy stops extinction by
                itself. It is whether the policy measurably improves visibility,
                accountability, coordination, or the ability to intervene later.
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
                How can we tell the difference between incremental regulation that
                builds real governing capacity and incremental regulation that
                merely reassures the public?
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <span class="tag">regulatory theater</span>
        <span class="tag">incremental governance</span>
        <span class="tag">institutional capacity</span>
        <span class="tag">accountability</span>
        """,
        unsafe_allow_html=True,
    )

    # CLAIM 8 -----------------------------------------------------------

    st.markdown(
        """
        <div class="card">
            <h3>8. The anti-extinction coalition should remain broader than any single political package</h3>

            <p><strong>My initial reaction:</strong> Agree.</p>

            <p><strong>Here’s what I wrote in the margin:</strong></p>

            <p>
                “Coalitions collapse when survival becomes conditional on agreeing
                about every other disputed consequence of technology.”
            </p>

            <p><strong>Why I think this:</strong></p>

            <p>
                The authors argue that people do not need to agree about employment,
                productivity, autonomous weapons, digital minds, human enhancement,
                or the long-term future in order to cooperate against extinction.
            </p>

            <p>
                This is one of the more politically realistic arguments in the
                chapter.
            </p>

            <p>
                AI policy is often bundled with broader ideological programs. That
                may create a coherent platform for one group while making
                cooperation impossible with anyone who rejects one part of the
                package.
            </p>

            <p>
                A narrow agreement—humanity should retain the ability to continue
                existing—does not resolve the technical or evidentiary dispute. But
                it does provide a possible common value across otherwise incompatible
                political positions.
            </p>

            <p>
                I would still phrase the coalition around preventing catastrophic
                loss of control rather than assuming extinction is the inevitable
                result of any sufficiently advanced system.
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
                What is the narrowest shared principle that could support meaningful
                AI governance without requiring agreement about the entire future of
                technology or society?
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <span class="tag">coalition building</span>
        <span class="tag">minimum consensus</span>
        <span class="tag">political pluralism</span>
        <span class="tag">catastrophic risk</span>
        """,
        unsafe_allow_html=True,
    )

    # CLAIM 9 -----------------------------------------------------------

    st.markdown(
        """
        <div class="card">
            <h3>9. Stopping AI development is presented as only the first step</h3>

            <p><strong>My initial reaction:</strong> This exposes an unresolved
            tension in the book.</p>

            <p><strong>Here’s what I wrote in the margin:</strong></p>

            <p>
                “The authors want an indefinite global halt now, followed eventually
                by a safe path to something like superintelligence. The bridge
                between those two states is doing a lot of invisible work.”
            </p>

            <p><strong>Why I think this:</strong></p>

            <p>
                The authors do not claim that humanity should permanently abandon
                intelligence enhancement or an abundant technological future. They
                say the current path should stop until humanity becomes capable of
                solving alignment correctly.
            </p>

            <p>
                They briefly suggest improving humans themselves so that people are
                smart enough to solve the problem without optimistically trusting a
                plan that will fail.
            </p>

            <p>
                That leaves several enormous questions unanswered.
            </p>

            <p>
                Who determines when humanity is ready? What research remains legal
                during the pause? How are safety theories tested without building
                increasingly capable systems? How does a temporary emergency regime
                avoid becoming permanent? And why should human enhancement be easier
                to align, govern, or distribute fairly?
            </p>

            <p>
                “Shut it down” is clearer than the authors’ theory of what happens
                afterward.
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
                What would a legitimate and testable exit condition from a global AI
                moratorium actually look like?
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <span class="tag">moratorium</span>
        <span class="tag">exit conditions</span>
        <span class="tag">human enhancement</span>
        <span class="tag">institutional permanence</span>
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
                <h3>I would become more supportive of a broad shutdown if...</h3>

                <p>
                    Multiple independently governed evaluations showed that frontier
                    systems were approaching autonomous replication, persistent
                    strategic deception, rapid AI research acceleration, or the
                    ability to evade meaningful human control.
                </p>

                <p>
                    I would also update if safety researchers demonstrated that
                    narrower controls consistently failed because capabilities
                    crossed technical, national, and organizational boundaries too
                    quickly to contain.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class="blue-box">
                <h3>I would become more opposed to a broad shutdown if...</h3>

                <p>
                    The proposed enforcement regime required pervasive surveillance,
                    indefinite emergency powers, preventive violence, or unreviewable
                    authority without producing reliable evidence that it reduced
                    catastrophic risk.
                </p>

                <p>
                    I would also update if capability-specific regulation,
                    containment, interpretability, licensing, and international
                    verification repeatedly controlled dangerous behavior without
                    requiring a prohibition on the broader field.
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
                This chapter makes the governance problem feel more concrete.
            </p>

            <p>
                If advanced AI creates genuinely global and irreversible risks, then
                voluntary commitments, company-level safety promises, and purely
                domestic regulation are not enough. Compute infrastructure,
                algorithmic efficiency, international competition, and verification
                all matter.
            </p>

            <p>
                I agree with the authors that a system cannot be called safe merely
                because its creators are sincere, and that one responsible actor
                cannot compensate for a race involving many others.
            </p>

            <p>
                But the chapter asks the reader to move from that diagnosis to an
                extraordinary political order: worldwide restrictions on computing
                hardware, prohibition of broad categories of research, intrusive
                monitoring, and possible military attacks on noncompliant
                infrastructure.
            </p>

            <p>
                I do not think the book has established enough confidence in either
                its forecast or its proposed institutions to justify that leap.
            </p>

            <p>
                There is also a tension I cannot ignore. The authors warn us that no
                powerful system should be trusted merely because its objective sounds
                benevolent. Yet their solution requires concentrating enormous power
                in governments and international enforcement bodies whose objective
                would also be described as benevolent: saving humanity.
            </p>

            <p>
                Human institutions are not superintelligences, but they are still
                optimizers. They pursue incentives, expand mandates, protect
                authority, make classification errors, and impose costs unevenly.
            </p>

            <p>
                So I leave this chapter more convinced that weak and fragmented AI
                governance is inadequate—but not convinced that “shut it down,” as
                described here, is either the only possible response or a safe one.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )