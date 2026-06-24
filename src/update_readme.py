from __future__ import annotations
import asyncio
from src.config import README_PATH, TIP_END_MARKER, TIP_START_MARKER, TIPS_DIR
from src.daily_tip import generate_tip, today_iso


def replace_tip_section(readme: str, new_tip: str) -> str:
    if TIP_START_MARKER not in readme:
        raise ValueError(f"README.md is missing start marker: {TIP_START_MARKER}")
    if TIP_END_MARKER not in readme:
        raise ValueError(f"README.md is missing end marker: {TIP_END_MARKER}")

    before, rest = readme.split(TIP_START_MARKER, 1)
    _old_tip, after = rest.split(TIP_END_MARKER, 1)

    return (
        before
        + TIP_START_MARKER
        + "\n\n"
        + new_tip.strip()
        + "\n\n"
        + TIP_END_MARKER
        + after
    )


async def update_readme() -> None:
    readme = README_PATH.read_text(encoding="utf-8")
    tip = await generate_tip()

    TIPS_DIR.mkdir(parents=True, exist_ok=True)
    tip_path = TIPS_DIR / f"{today_iso()}.md"
    tip_path.write_text(tip.strip() + "\n", encoding="utf-8")

    updated = replace_tip_section(readme, tip)
    README_PATH.write_text(updated, encoding="utf-8")


def main() -> None:
    asyncio.run(update_readme())
    print(f"Updated {README_PATH} and saved tip to {TIPS_DIR}")


if __name__ == "__main__":
    main()