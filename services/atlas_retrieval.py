import math
import re
from collections import Counter

from services.atlas_corpus import searchable_text


STOP_WORDS = {
    "a", "an", "and", "are", "as", "at", "be", "because",
    "but", "by", "do", "does", "for", "from", "how", "i",
    "in", "is", "it", "me", "my", "of", "on", "or", "that",
    "the", "their", "this", "to", "was", "what", "when",
    "where", "which", "who", "why", "with", "would", "you",
}


def tokenize(text: str) -> list[str]:
    tokens = re.findall(r"[a-z0-9][a-z0-9\-']+", text.lower())

    return [
        token
        for token in tokens
        if token not in STOP_WORDS and len(token) > 1
    ]


def score_document(query: str, document: dict) -> float:
    query_tokens = tokenize(query)
    document_tokens = tokenize(searchable_text(document))

    if not query_tokens or not document_tokens:
        return 0.0

    query_counts = Counter(query_tokens)
    document_counts = Counter(document_tokens)

    score = 0.0

    for token, query_count in query_counts.items():
        document_count = document_counts.get(token, 0)

        if document_count:
            score += (
                query_count
                * (1 + math.log(document_count))
            )

    title_tokens = set(tokenize(document.get("title", "")))
    related_tokens = set(
        tokenize(" ".join(document.get("related", [])))
    )

    for token in query_tokens:
        if token in title_tokens:
            score += 4.0

        if token in related_tokens:
            score += 2.0

    normalized_query = " ".join(query_tokens)
    normalized_document = " ".join(document_tokens)

    if normalized_query and normalized_query in normalized_document:
        score += 8.0

    return score


def retrieve(
    query: str,
    corpus: list[dict],
    limit: int = 6,
) -> list[dict]:
    scored = []

    for document in corpus:
        score = score_document(query, document)

        if score > 0:
            scored.append(
                {
                    **document,
                    "_score": round(score, 3),
                }
            )

    scored.sort(
        key=lambda item: item["_score"],
        reverse=True,
    )

    return scored[:limit]