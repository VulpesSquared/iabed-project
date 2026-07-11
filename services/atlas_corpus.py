import ast
import json
from pathlib import Path
from typing import Any


PROJECT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_DIR / "data"

CONCEPT_FILES = [
    ("Tier 0", "tier0_concepts.json"),
    ("Tier 1", "tier1_concepts.json"),
    ("Tier 2", "tier2_concepts.json"),
    ("Tier 3", "tier3_concepts.json"),
]


def read_json(path: Path) -> Any:
    if not path.exists():
        return None

    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def concept_documents() -> list[dict]:
    documents = []

    for tier, filename in CONCEPT_FILES:
        concepts = read_json(DATA_DIR / filename) or []

        for concept in concepts:
            name = concept.get("name", "Untitled Concept")

            documents.append(
                {
                    "id": f"concept::{tier}::{name}",
                    "kind": "concept",
                    "title": name,
                    "location": tier,
                    "definition": concept.get("definition", ""),
                    "position": concept.get("my_take", ""),
                    "reasoning": concept.get("why_it_matters", ""),
                    "uncertainty": "",
                    "change_mind": "",
                    "related": concept.get("related_concepts", []),
                    "appears_in": concept.get("appears_in", []),
                    "sources": concept.get("sources", []),
                }
            )

    return documents


def side_trail_documents() -> list[dict]:
    documents = []
    trails = read_json(DATA_DIR / "side_trails.json") or []

    for trail in trails:
        documents.append(
            {
                "id": f"trail::{trail.get('id', '')}",
                "kind": "side_trail",
                "title": trail.get("title", "Untitled Side Trail"),
                "location": trail.get("concentration", "Side Trails"),
                "definition": trail.get("question", ""),
                "position": trail.get("my_current_position", ""),
                "reasoning": trail.get("why_i_followed_this", ""),
                "uncertainty": " ".join(
                    trail.get("seminar_questions", [])
                ),
                "change_mind": trail.get(
                    "what_would_change_my_mind",
                    "",
                ),
                "related": (
                    trail.get("prerequisite_concepts", [])
                    + trail.get("connected_trails", [])
                ),
                "appears_in": trail.get("appears_in", []),
                "sources": (
                    trail.get("core_readings", [])
                    + trail.get("further_reading", [])
                ),
            }
        )

    return documents


def literal_value(node: ast.AST, default: Any = "") -> Any:
    """Return a literal argument value without executing chapter code."""

    try:
        return ast.literal_eval(node)
    except (ValueError, TypeError):
        return default


def bullet_items(value: str) -> list[str]:
    """Convert a multiline bullet field into relationship labels."""

    if not value:
        return []

    items = []

    for line in value.splitlines():
        item = line.strip().lstrip("-•").strip()

        if item:
            items.append(item)

    return items


def chapter_label(tree: ast.AST, fallback: str) -> str:
    """Read the visible chapter heading from the first st.header call."""

    for node in ast.walk(tree):
        if not isinstance(node, ast.Call) or not node.args:
            continue

        function = node.func

        if (
            isinstance(function, ast.Attribute)
            and isinstance(function.value, ast.Name)
            and function.value.id == "st"
            and function.attr == "header"
        ):
            heading = literal_value(node.args[0])

            if isinstance(heading, str) and heading.strip():
                return heading.strip()

    return fallback


def claim_card_document(
    call: ast.Call,
    chapter_name: str,
    chapter_id: str,
    claim_number: int,
) -> dict:
    """Normalize one render_claim_card call for the Atlas corpus."""

    values = {
        keyword.arg: literal_value(keyword.value)
        for keyword in call.keywords
        if keyword.arg
    }

    return {
        "id": f"chapter::{chapter_id}::claim_{claim_number}",
        "kind": "chapter_claim",
        "title": values.get("title", "Untitled Claim"),
        "location": chapter_name,
        "definition": values.get("margin_note", ""),
        "position": values.get("reaction", ""),
        "reasoning": values.get("why", ""),
        "uncertainty": values.get("questions", ""),
        "change_mind": "",
        "related": bullet_items(values.get("side_trails", "")),
        "appears_in": [chapter_name],
        "sources": [],
    }


def chapter_documents() -> list[dict]:
    """Extract claims directly from the existing Python chapter files."""

    chapter_dir = PROJECT_DIR / "chapters"

    if not chapter_dir.exists():
        return []

    documents = []

    for path in sorted(chapter_dir.glob("chapter*.py")):
        try:
            source = path.read_text(encoding="utf-8")
            tree = ast.parse(source, filename=str(path))
        except (OSError, SyntaxError):
            continue

        chapter_id = path.stem
        fallback = chapter_id.replace("_", " ").replace(
            "chapter", "Chapter "
        )
        location = chapter_label(tree, fallback.strip())
        claim_number = 0

        for node in ast.walk(tree):
            if not isinstance(node, ast.Call):
                continue

            function = node.func

            if not (
                isinstance(function, ast.Name)
                and function.id == "render_claim_card"
            ):
                continue

            claim_number += 1
            documents.append(
                claim_card_document(
                    call=node,
                    chapter_name=location,
                    chapter_id=chapter_id,
                    claim_number=claim_number,
                )
            )

    return documents


def build_corpus() -> list[dict]:
    return (
        concept_documents()
        + side_trail_documents()
        + chapter_documents()
    )


def searchable_text(document: dict) -> str:
    fields = [
        document.get("title", ""),
        document.get("location", ""),
        document.get("definition", ""),
        document.get("position", ""),
        document.get("reasoning", ""),
        document.get("uncertainty", ""),
        document.get("change_mind", ""),
        " ".join(document.get("related", [])),
        " ".join(document.get("appears_in", [])),
    ]

    return "\n".join(str(field) for field in fields if field)
