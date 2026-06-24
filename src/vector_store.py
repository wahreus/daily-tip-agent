from __future__ import annotations
import sqlite3
from dataclasses import dataclass
from pathlib import Path
import numpy as np


@dataclass(frozen=True)
class StoredChunk:
    chunk_id: int
    text: str


@dataclass(frozen=True)
class SearchResult:
    chunk_id: int
    score: float
    text: str


def load_embeddings(db_path: Path) -> tuple[list[StoredChunk], np.ndarray]:
    if not db_path.exists():
        raise FileNotFoundError(
            f"Vector index not found at {db_path}. Commit the SQLite index before running the agent."
        )

    with sqlite3.connect(db_path) as connection:
        rows = connection.execute(
            """
            SELECT chunk_id, text, embedding
            FROM chunks
            ORDER BY chunk_id
            """
        ).fetchall()

    if not rows:
        raise ValueError(f"Vector index at {db_path} is empty.")

    chunks = [StoredChunk(chunk_id=int(row[0]), text=str(row[1])) for row in rows]
    embeddings = np.vstack(
        [np.frombuffer(row[2], dtype=np.float32) for row in rows]
    )

    return chunks, embeddings


def cosine_search(
    db_path: Path,
    query_embedding: list[float],
    *,
    limit: int = 5,
) -> list[SearchResult]:
    chunks, embeddings = load_embeddings(db_path)

    query = np.asarray(query_embedding, dtype=np.float32)
    query_norm = np.linalg.norm(query)
    embedding_norms = np.linalg.norm(embeddings, axis=1)

    if query_norm == 0:
        raise ValueError("Query embedding has zero norm.")

    denominator = embedding_norms * query_norm
    scores = np.divide(
        embeddings @ query,
        denominator,
        out=np.zeros_like(embedding_norms, dtype=np.float32),
        where=denominator != 0,
    )

    top_indices = np.argsort(scores)[::-1][:limit]

    return [
        SearchResult(
            chunk_id=chunks[index].chunk_id,
            score=float(scores[index]),
            text=chunks[index].text,
        )
        for index in top_indices
    ]
