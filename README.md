# 🤖 Daily Tip Agent

An AI agent that posts one AWS Well-Architected best-practice tip per day into this `README.md`.

The project uses Retrieval-Augmented Generation (RAG) over a committed SQLite vector index built from the [AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf).

<!-- TIP_OF_THE_DAY_START -->

## Tip of the day [Sunday, July 19, 2026]

### Automate retention, tiering, and deletion

Treat data lifecycle management as an automated policy problem, not a manual cleanup task. Start by classifying data by sensitivity, access frequency, and how long it must be retained. Then define lifecycle rules that move older or infrequently accessed data to more efficient storage tiers and delete data when its retention window ends. Make sure those rules align with legal, regulatory, and organizational requirements, and cover both active data and backups. Finally, monitor for resources that do not have automated lifecycle management enabled so you can catch gaps before they become cost, compliance, or security issues.

**Why it matters:** Well-defined lifecycle policies improve storage efficiency, help maintain compliance, and reduce the risk of retaining data longer than necessary. They also lower operational overhead by replacing manual deletion and ad hoc storage management with repeatable automation.

<!-- TIP_OF_THE_DAY_END -->

## How it works

A scheduled GitHub Actions workflow runs `src/update_readme.py` once per day.

The script selects a topic from `src/topics.py`, then generates a new best-practice tip by using an AI agent with access to the local SQLite vector index in `storage/well_architected_index.sqlite`.

The agent searches the index, retrieves relevant source material, and writes one practical tip grounded in the retrieved material. The script then updates only the marked tip section in `README.md`, saves the tip as a dated Markdown file in `tips/`, and commits the change back to the repository.
