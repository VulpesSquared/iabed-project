import html
import json
from pathlib import Path

import streamlit as st


PROJECT_DIR = Path(__file__).resolve().parents[1]
DATA_FILE = PROJECT_DIR / "data" / "side_trails.json"


CONCENTRATION_DETAILS = {
    "Minds, Models, and Intelligence": {
        "icon": "🧠",
        "description": (
            "What intelligence, agency, cognition, and consciousness "
            "actually mean."
        ),
    },
    "Building and Understanding AI": {
        "icon": "⚙️",
        "description": (
            "How models learn, how objectives fail, and what "
            "interpretability can reveal."
        ),
    },
    "Humans Inside the System": {
        "icon": "🫂",
        "description": (
            "How people understand, use, trust, govern, and become "
            "part of AI systems."
        ),
    },
    "Risk, Governance, and the Future": {
        "icon": "🌍",
        "description": (
            "How to reason and act when capabilities, consequences, "
            "and values are uncertain."
        ),
    },
}


@st.cache_data
def load_side_trails() -> list[dict]:
    """Load the Side Trails curriculum from JSON."""

    if not DATA_FILE.exists():
        return []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
    except json.JSONDecodeError as error:
        st.error(
            "`side_trails.json` contains invalid JSON. "
            f"Check line {error.lineno}, column {error.colno}."
        )
        return []

    if not isinstance(data, list):
        st.error("`side_trails.json` must contain a JSON list.")
        return []

    return sorted(
        data,
        key=lambda trail: (
            trail.get("concentration", ""),
            trail.get("number", 999),
        ),
    )


def set_concentration(concentration: str) -> None:
    st.session_state.side_trails_concentration = concentration
    st.session_state.side_trails_trail_id = None


def set_trail(trail_id: str) -> None:
    st.session_state.side_trails_trail_id = trail_id


def return_to_curriculum() -> None:
    st.session_state.side_trails_concentration = None
    st.session_state.side_trails_trail_id = None


def return_to_concentration() -> None:
    st.session_state.side_trails_trail_id = None


def render_tags(items: list[str]) -> None:
    if not items:
        return

    tag_html = "".join(
        f'<span class="tag">{html.escape(str(item))}</span>'
        for item in items
    )

    st.markdown(tag_html, unsafe_allow_html=True)


def render_curriculum_home(trails: list[dict]) -> None:
    st.markdown(
        """
        Some questions don’t fit neatly inside a chapter.

        They lead into cognitive science, philosophy of mind, machine learning,
        HCI, organizational theory, governance, and occasionally somewhere
        much stranger.

        These are the Side Trails: structured reading paths for following those
        questions properly.
        """
    )

    st.markdown(
        """
        <div class="lavender-box">
            <h3>How this works</h3>
            <p>
                Choose a concentration, open a seminar, follow the readings,
                argue with the questions, and disappear into the methods lab
                for a while.
            </p>
            <p>
                This is less “recommended reading list” and more “tiny,
                unofficial doctoral curriculum that got slightly out of hand.”
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    concentrations_in_data = {
        trail.get("concentration")
        for trail in trails
        if trail.get("concentration")
    }

    ordered_concentrations = [
        name
        for name in CONCENTRATION_DETAILS
        if name in concentrations_in_data
    ]

    extra_concentrations = sorted(
        concentrations_in_data - set(ordered_concentrations)
    )

    ordered_concentrations.extend(extra_concentrations)

    for index in range(0, len(ordered_concentrations), 2):
        columns = st.columns(2)

        for column, concentration in zip(
            columns,
            ordered_concentrations[index:index + 2],
        ):
            details = CONCENTRATION_DETAILS.get(
                concentration,
                {
                    "icon": "🧭",
                    "description": "A guided research path through the Atlas.",
                },
            )

            trail_count = sum(
                1
                for trail in trails
                if trail.get("concentration") == concentration
            )

            with column:
                st.markdown(
                    f"""
                    <div class="card">
                        <h3>
                            {details["icon"]}
                            {html.escape(concentration)}
                        </h3>
                        <p>{html.escape(details["description"])}</p>
                        <p><strong>{trail_count} seminars</strong></p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

                st.button(
                    f"Explore {concentration}",
                    key=f"open_concentration_{concentration}",
                    use_container_width=True,
                    on_click=set_concentration,
                    args=(concentration,),
                )


def render_concentration(
    concentration: str,
    trails: list[dict],
) -> None:
    details = CONCENTRATION_DETAILS.get(
        concentration,
        {
            "icon": "🧭",
            "description": "A guided research path through the Atlas.",
        },
    )

    st.button(
        "← Back to all concentrations",
        on_click=return_to_curriculum,
    )

    st.header(f'{details["icon"]} {concentration}')
    st.markdown(details["description"])

    concentration_trails = [
        trail
        for trail in trails
        if trail.get("concentration") == concentration
    ]

    if not concentration_trails:
        st.info("No seminars have been added to this concentration yet.")
        return

    for trail in concentration_trails:
        trail_id = trail.get("id", "")
        number = trail.get("number", "")
        icon = trail.get("icon", "🧭")
        title = trail.get("title", "Untitled Seminar")
        question = trail.get("question", "")
        objectives = trail.get("learning_objectives", [])
        readings = trail.get("core_readings", [])

        metadata = []

        if objectives:
            metadata.append(f"{len(objectives)} learning objectives")

        if readings:
            metadata.append(f"{len(readings)} core readings")

        metadata_text = " · ".join(metadata)

        st.markdown(
            f"""
            <div class="card">
                <h3>
                    {html.escape(str(number))}.
                    {html.escape(icon)}
                    {html.escape(title)}
                </h3>
                <p><strong>{html.escape(question)}</strong></p>
                <p>{html.escape(metadata_text)}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.button(
            f"Open seminar: {title}",
            key=f"open_trail_{trail_id}",
            use_container_width=True,
            on_click=set_trail,
            args=(trail_id,),
        )


def render_reading(reading: dict) -> None:
    title = reading.get("title", "Untitled Reading")
    authors = reading.get("authors", "")
    year = reading.get("year", "")
    source_type = reading.get("type", "")
    role = reading.get("role", "")
    why_read_it = reading.get("why_read_it", "")
    url = reading.get("url", "")

    heading = title

    if year:
        heading = f"{title} · {year}"

    with st.expander(heading):
        if authors:
            st.markdown(f"**Authors:** {authors}")

        if source_type:
            st.markdown(f"**Source type:** {source_type}")

        if role:
            st.markdown(f"**Role in this seminar:** {role}")

        if why_read_it:
            st.markdown(f"**Why read it:** {why_read_it}")

        if url:
            st.link_button("Open reading", url)


def render_trail(trail: dict, all_trails: list[dict]) -> None:
    st.button(
        "← Back to concentration",
        on_click=return_to_concentration,
    )

    number = trail.get("number", "")
    icon = trail.get("icon", "🧭")
    title = trail.get("title", "Untitled Seminar")
    question = trail.get("question", "")

    st.header(f"{number}. {icon} {title}")

    if question:
        st.markdown(
            f"""
            <div class="lavender-box">
                <h3>The Question</h3>
                <p>{html.escape(question)}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    why_i_followed_this = trail.get("why_i_followed_this", "")

    if why_i_followed_this:
        st.subheader("Why I Followed This Trail")
        st.markdown(why_i_followed_this)

    learning_objectives = trail.get("learning_objectives", [])

    if learning_objectives:
        st.subheader("Learning Objectives")

        for objective in learning_objectives:
            st.markdown(f"- {objective}")

    prerequisites = trail.get("prerequisite_concepts", [])

    if prerequisites:
        st.subheader("Concepts to Know First")
        render_tags(prerequisites)

    core_readings = trail.get("core_readings", [])

    st.subheader("Core Readings")

    if core_readings:
        for reading in core_readings:
            render_reading(reading)
    else:
        st.info(
            "The core reading list for this seminar is still being curated."
        )

    further_reading = trail.get("further_reading", [])

    if further_reading:
        st.subheader("Further Reading")

        for reading in further_reading:
            render_reading(reading)

    seminar_questions = trail.get("seminar_questions", [])

    if seminar_questions:
        st.subheader("Seminar Questions")

        for question_number, seminar_question in enumerate(
            seminar_questions,
            start=1,
        ):
            st.markdown(
                f"**{question_number}.** {seminar_question}"
            )

    methods_lab = trail.get("methods_lab", {})

    if methods_lab:
        lab_title = methods_lab.get("title", "Methods Lab")
        prompt = methods_lab.get("prompt", "")
        deliverable = methods_lab.get("deliverable", "")

        st.markdown(
            f"""
            <div class="blue-box">
                <h3>Methods Lab: {html.escape(lab_title)}</h3>
                <p>{html.escape(prompt)}</p>
                {
                    f'<p><strong>Deliverable:</strong> '
                    f'{html.escape(deliverable)}</p>'
                    if deliverable
                    else ''
                }
            </div>
            """,
            unsafe_allow_html=True,
        )

    position_memo = trail.get("position_memo", {})

    if position_memo:
        memo_prompt = position_memo.get("prompt", "")
        memo_length = position_memo.get("length", "")

        st.markdown(
            f"""
            <div class="card">
                <h3>Position Memo</h3>
                <p>{html.escape(memo_prompt)}</p>
                {
                    f'<p><strong>Suggested length:</strong> '
                    f'{html.escape(memo_length)}</p>'
                    if memo_length
                    else ''
                }
            </div>
            """,
            unsafe_allow_html=True,
        )

    my_current_position = trail.get("my_current_position", "")

    if my_current_position:
        st.markdown(
            f"""
            <div class="sage-box">
                <h3>My Current Position</h3>
                <p>{html.escape(my_current_position)}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    what_would_change_my_mind = trail.get(
        "what_would_change_my_mind",
        "",
    )

    if what_would_change_my_mind:
        st.markdown(
            f"""
            <div class="burgundy-box">
                <h3>What Would Change My Mind?</h3>
                <p>{html.escape(what_would_change_my_mind)}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    appears_in = trail.get("appears_in", [])

    if appears_in:
        st.subheader("Appears In")
        render_tags(appears_in)

    connected_trails = trail.get("connected_trails", [])

    if connected_trails:
        st.subheader("Continue Down the Trail")

        trail_by_title = {
            item.get("title"): item
            for item in all_trails
        }

        available_connections = [
            trail_by_title[title]
            for title in connected_trails
            if title in trail_by_title
        ]

        if not available_connections:
            render_tags(connected_trails)
            return

        columns = st.columns(
            min(len(available_connections), 3)
        )

        for column, connected_trail in zip(
            columns,
            available_connections,
        ):
            connected_id = connected_trail.get("id", "")
            connected_title = connected_trail.get(
                "title",
                "Untitled Seminar",
            )
            connected_icon = connected_trail.get("icon", "🧭")

            with column:
                st.button(
                    f"{connected_icon} {connected_title}",
                    key=f"connected_trail_{connected_id}",
                    use_container_width=True,
                    on_click=set_trail,
                    args=(connected_id,),
                )


def show() -> None:
    st.title("🧭 Side Trails")

    trails = load_side_trails()

    if not trails:
        st.warning(
            "No Side Trails could be loaded. Check "
            "`data/side_trails.json`."
        )
        return

    if "side_trails_concentration" not in st.session_state:
        st.session_state.side_trails_concentration = None

    if "side_trails_trail_id" not in st.session_state:
        st.session_state.side_trails_trail_id = None

    selected_concentration = (
        st.session_state.side_trails_concentration
    )
    selected_trail_id = st.session_state.side_trails_trail_id

    if selected_trail_id:
        selected_trail = next(
            (
                trail
                for trail in trails
                if trail.get("id") == selected_trail_id
            ),
            None,
        )

        if selected_trail:
            render_trail(selected_trail, trails)
            return

        st.session_state.side_trails_trail_id = None

    if selected_concentration:
        render_concentration(
            selected_concentration,
            trails,
        )
        return

    render_curriculum_home(trails)