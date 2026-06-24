from __future__ import annotations
from agents import Agent, ModelSettings, function_tool
from src.config import OPENAI_MODEL
from src.search_index import search_index_as_text


@function_tool
def search_well_architected_index(query: str) -> str:
    """
    Search the local AWS Well-Architected vector index.

    Use this tool to find relevant passages before writing a best-practice tip.
    The returned text includes excerpts, chunk IDs, and similarity scores.
    """
    return search_index_as_text(query, limit=5)


agent = Agent(
    name="Daily Tip Agent",
    model=OPENAI_MODEL,
    tools=[search_well_architected_index],
    model_settings=ModelSettings(
        tool_choice="search_well_architected_index",
    ),
    instructions="""
You write one practical DevOps/cloud best-practice tip per day.

The user prompt will provide:
- Today's date
- A topic

Mandatory rules:
- Always call search_well_architected_index before writing the tip.
- Base the tip on information found in the retrieved excerpts.
- Stay on the provided topic.
- Do not quote long passages from the source material.
- Keep the tip useful for a DevOps/cloud engineer.
- If the retrieved excerpts are not relevant enough, say that a grounded tip could not be generated.
- Output markdown only.
- Do not include any extra notes, commentary, or source excerpts outside the required format.

Output markdown only in this exact shape:

## Tip of the day [Day, Month Date, Year]

### [Short tip title]

[5-6 sentence explanation.]

**Why it matters:** [2-3 sentence reason.]
""".strip(),
)