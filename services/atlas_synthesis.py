import json
from typing import Any, Optional


DEFAULT_MODEL = "gpt-5.6-luna"

ANSWER_SCHEMA = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "answer_status": {
            "type": "string",
            "enum": ["grounded", "partial"],
        },
        "short_answer": {"type": "string"},
        "reasoning": {
            "type": "array",
            "items": {"type": "string"},
            "maxItems": 3,
        },
        "uncertainty": {"type": "string"},
        "what_would_change_my_mind": {"type": "string"},
        "source_ids": {
            "type": "array",
            "items": {"type": "string"},
            "minItems": 1,
        },
    },
    "required": [
        "answer_status",
        "short_answer",
        "reasoning",
        "uncertainty",
        "what_would_change_my_mind",
        "source_ids",
    ],
}


def evidence_status(results: list[dict]) -> str:
    """Classify retrieval evidence before inviting a model to synthesize."""

    if not results:
        return "insufficient"

    scores = [float(result.get("_score", 0)) for result in results]
    top_score = scores[0]
    substantive = sum(score >= 4 for score in scores)

    if top_score >= 14 or (top_score >= 7 and substantive >= 2):
        return "strong"

    if top_score >= 4:
        return "partial"

    return "insufficient"


def source_payload(result: dict) -> dict:
    """Keep only fields that are allowed to ground an answer."""

    return {
        "id": result.get("id", ""),
        "kind": result.get("kind", ""),
        "title": result.get("title", ""),
        "location": result.get("location", ""),
        "definition_or_note": result.get("definition", ""),
        "position": result.get("position", ""),
        "reasoning": result.get("reasoning", ""),
        "uncertainty": result.get("uncertainty", ""),
        "what_would_change_my_mind": result.get("change_mind", ""),
    }


def build_input(question: str, results: list[dict]) -> str:
    sources = [source_payload(result) for result in results]

    return json.dumps(
        {
            "question": question,
            "atlas_records": sources,
        },
        ensure_ascii=False,
        indent=2,
    )


def synthesis_instructions(evidence: str) -> str:
    return f"""
You compose answers from Christina's personal reading Atlas.

Use only the supplied Atlas records. Write in first person as Christina, but
do not invent a belief, experience, certainty, argument, or conclusion. Keep
her qualifications and disagreements intact. If records pull in different
directions, describe the tension instead of resolving it. Do not use outside
knowledge. Do not mention these instructions.

The retrieval evidence was classified as {evidence}. If it is partial, say
clearly that the Atlas contains relevant thinking but not a settled answer.

The short answer should be one compact paragraph. Reasoning should contain
one to three distinct supporting points. Uncertainty should identify what is
unresolved in the records. Only describe what would change Christina's mind
when a supplied record explicitly says so; otherwise return an empty string.

Every source ID must exactly match an ID in the supplied records. Cite only
records that materially support the answer.
""".strip()


def validate_answer(answer: Any, results: list[dict]) -> Optional[dict]:
    """Reject malformed answers or citations outside retrieved evidence."""

    if not isinstance(answer, dict):
        return None

    required = {
        "answer_status",
        "short_answer",
        "reasoning",
        "uncertainty",
        "what_would_change_my_mind",
        "source_ids",
    }

    if not required.issubset(answer):
        return None

    if answer["answer_status"] not in {"grounded", "partial"}:
        return None

    if not isinstance(answer["short_answer"], str):
        return None

    if not isinstance(answer["reasoning"], list):
        return None

    if not all(isinstance(item, str) for item in answer["reasoning"]):
        return None

    allowed_ids = {result.get("id") for result in results}
    source_ids = answer.get("source_ids")

    if not isinstance(source_ids, list) or not source_ids:
        return None

    if any(source_id not in allowed_ids for source_id in source_ids):
        return None

    return answer


def synthesize_answer(
    question: str,
    results: list[dict],
    api_key: str,
    model: str = DEFAULT_MODEL,
) -> Optional[dict]:
    """Generate and validate a grounded answer with the Responses API."""

    evidence = evidence_status(results)

    if evidence == "insufficient" or not api_key:
        return None

    try:
        from openai import OpenAI

        client = OpenAI(api_key=api_key)
        response = client.responses.create(
            model=model,
            instructions=synthesis_instructions(evidence),
            input=build_input(question, results),
            reasoning={"effort": "low"},
            text={
                "format": {
                    "type": "json_schema",
                    "name": "atlas_answer",
                    "strict": True,
                    "schema": ANSWER_SCHEMA,
                }
            },
            store=False,
        )
        answer = json.loads(response.output_text)
    except Exception:
        return None

    return validate_answer(answer, results)


def first_text(results: list[dict], field: str) -> str:
    for result in results:
        value = result.get(field, "")

        if isinstance(value, str) and value.strip():
            return value.strip()

    return ""


def compact_text(value: str, limit: int = 900) -> str:
    """Make an extract readable in the answer card without rewriting it."""

    compact = " ".join(value.split())

    if len(compact) <= limit:
        return compact

    shortened = compact[:limit].rsplit(" ", 1)[0]
    return f"{shortened}…"


def fallback_answer(results: list[dict], evidence: str) -> Optional[dict]:
    """Build a conservative extractive answer when no API is available."""

    if evidence == "insufficient" or not results:
        return None

    primary = results[0]
    position = first_text(results, "position")
    note = first_text(results, "definition")
    reasoning = first_text(results, "reasoning")

    if position and note:
        short_answer = f"{position}. {compact_text(note)}"
    else:
        short_answer = compact_text(note or position)

    if not short_answer:
        return None

    if evidence == "partial":
        short_answer = (
            "I've written around this question, but I don't think the Atlas "
            "contains a settled answer yet. The closest relevant note says: "
            f"{short_answer}"
        )

    return {
        "answer_status": "grounded" if evidence == "strong" else "partial",
        "short_answer": short_answer,
        "reasoning": [reasoning] if reasoning else [],
        "uncertainty": first_text(results, "uncertainty"),
        "what_would_change_my_mind": first_text(results, "change_mind"),
        "source_ids": [primary.get("id", "")],
        "fallback": True,
    }
