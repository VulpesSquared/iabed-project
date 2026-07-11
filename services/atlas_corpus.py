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


def chapter_documents() -> list[dict]:
    chapter_dir = DATA_DIR / "chapters"

    if not chapter_dir.exists():
        return []

    documents = []

    for path in sorted(chapter_dir.glob("chapter_*.json")):
        chapter = read_json(path)

        if not chapter:
            continue

        chapter_label = (
            f"Chapter {chapter.get('chapter')} — "
            f"{chapter.get('title', '')}"
        )

        if chapter.get("big_idea"):
            documents.append(
                {
                    "id": f"chapter::{chapter.get('chapter')}::big_idea",
                    "kind": "chapter",
                    "title": chapter_label,
                    "location": chapter_label,
                    "definition": chapter.get("big_idea", ""),
                    "position": "",
                    "reasoning": "",
                    "uncertainty": "",
                    "change_mind": "",
                    "related": [],
                    "appears_in": [chapter_label],
                    "sources": [],
                }
            )

        for claim in chapter.get("claims", []):
            documents.append(
                {
                    "id": (
                        f"chapter::{chapter.get('chapter')}::"
                        f"{claim.get('id', claim.get('title', 'claim'))}"
                    ),
                    "kind": "chapter_claim",
                    "title": claim.get("title", "Untitled Claim"),
                    "location": chapter_label,
                    "definition": claim.get("claim", ""),
                    "position": claim.get("reaction", ""),
                    "reasoning": claim.get("reasoning", ""),
                    "uncertainty": " ".join(
                        claim.get("questions", [])
                    ),
                    "change_mind": claim.get(
                        "what_would_change_my_mind",
                        "",
                    ),
                    "related": claim.get("tags", []),
                    "appears_in": [chapter_label],
                    "sources": claim.get("sources", []),
                }
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