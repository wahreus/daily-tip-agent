from __future__ import annotations
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-5.4-mini-2026-03-17")
OPENAI_EMBEDDING_MODEL = os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small")

VECTOR_DB_PATH = Path(os.getenv("VECTOR_DB_PATH", "storage/well_architected_index.sqlite"))
README_PATH = Path(os.getenv("README_PATH", "README.md"))
TIPS_DIR = Path(os.getenv("TIPS_DIR", "tips"))

TIP_START_MARKER = "<!-- TIP_OF_THE_DAY_START -->"
TIP_END_MARKER = "<!-- TIP_OF_THE_DAY_END -->"
