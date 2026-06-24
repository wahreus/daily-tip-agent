from __future__ import annotations
import asyncio
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo
from agents import Runner
from src.agent import agent
from src.config import TIPS_DIR
from src.topics import select_topic


def today_iso() -> str:
    return datetime.now(ZoneInfo("Europe/Stockholm")).date().isoformat()


def formatted_today() -> str:
    today = datetime.now(ZoneInfo("Europe/Stockholm")).date()
    return today.strftime("%a, %B %-d, %Y")


async def generate_tip(topic: str | None = None) -> str:
    if topic is None:
        topic = select_topic()

    today = formatted_today()

    prompt = f"""
Today's date: {today}
Topic: {topic}

Generate today's tip. Search the vector index for relevant guidance before writing. Do not switch to another topic. The final output must be markdown only.
""".strip()

    result = await Runner.run(agent, prompt)
    return result.final_output.strip()


async def save_tip(output_dir: Path = TIPS_DIR) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    tip = await generate_tip()
    output_path = output_dir / f"{today_iso()}.md"
    output_path.write_text(tip + "\n", encoding="utf-8")
    return output_path


def main() -> None:
    output_path = asyncio.run(save_tip())
    print(f"Saved tip to {output_path}")


if __name__ == "__main__":
    main()
