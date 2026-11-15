# 🤖 Daily Tip Agent

An AI agent that posts one AWS Well-Architected best-practice tip per day into this `README.md`.

The project uses Retrieval-Augmented Generation (RAG) over a committed SQLite vector index built from the [AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf).

<!-- TIP_OF_THE_DAY_START -->

## Tip of the day [Sunday, November 15, 2026]

### Make improvement a standing operational ritual

Set a recurring cadence to review operations metrics with people from engineering, operations, and the business. Use those sessions to look for anomalies, confirm whether recent changes actually improved outcomes, and decide what to tackle next across dev, test, and production. Pair the metric review with post-incident analysis so you can turn customer-impacting events into specific corrective actions, not just notes. Keep the feedback loop tight by validating findings with stakeholders and updating runbooks, dashboards, or automation based on what you learn. Over time, this turns operational improvement into a routine process instead of an occasional cleanup exercise.

**Why it matters:** Continuous operational improvement works best when it is data-driven and shared across teams. Regular review cycles help you spot recurring issues early, prioritize the highest-value fixes, and reinforce changes that measurably improve service health and business outcomes.

<!-- TIP_OF_THE_DAY_END -->

## How it works

A scheduled GitHub Actions workflow runs `src/update_readme.py` once per day.

The script selects a topic from `src/topics.py`, then generates a new best-practice tip by using an AI agent with access to the local SQLite vector index in `storage/well_architected_index.sqlite`.

The agent searches the index, retrieves relevant source material, and writes one practical tip grounded in the retrieved material. The script then updates only the marked tip section in `README.md`, saves the tip as a dated Markdown file in `tips/`, and commits the change back to the repository.
