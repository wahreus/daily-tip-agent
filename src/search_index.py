from __future__ import annotations
import argparse
from pathlib import Path
from openai import OpenAI
from src.config import OPENAI_EMBEDDING_MODEL, VECTOR_DB_PATH
from src.vector_store import SearchResult, cosine_search


def embed_query(query: str) -> list[float]:
    client = OpenAI()
    response = client.embeddings.create(
        model=OPENAI_EMBEDDING_MODEL,
        input=query,
    )
    return response.data[0].embedding


def search_index(
    query: str,
    *,
    db_path: Path = VECTOR_DB_PATH,
    limit: int = 5,
) -> list[SearchResult]:
    query_embedding = embed_query(query)
    return cosine_search(db_path, query_embedding, limit=limit)


def format_results(
    results: list[SearchResult],
    *,
    max_chars_per_result: int = 1000,
) -> str:
    if not results:
        return "No matching passages found."

    formatted = []
    for result in results:
        excerpt = result.text.strip()
        if len(excerpt) > max_chars_per_result:
            excerpt = excerpt[:max_chars_per_result].rstrip() + "..."

        formatted.append(
            f"[chunk {result.chunk_id}; score {result.score:.3f}]\n{excerpt}"
        )

    return "\n\n---\n\n".join(formatted)


def search_index_as_text(query: str, *, limit: int = 5) -> str:
    results = search_index(query, limit=limit)
    return format_results(results)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Search the local Well-Architected vector index.")
    parser.add_argument("query", help="Search query.")
    parser.add_argument("--limit", type=int, default=5, help="Number of results to return.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    print(search_index_as_text(args.query, limit=args.limit))


if __name__ == "__main__":
    main()
