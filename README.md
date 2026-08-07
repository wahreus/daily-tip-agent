# 🤖 Daily Tip Agent

An AI agent that posts one AWS Well-Architected best-practice tip per day into this `README.md`.

The project uses Retrieval-Augmented Generation (RAG) over a committed SQLite vector index built from the [AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf).

<!-- TIP_OF_THE_DAY_START -->

## Tip of the day [Friday, August 7, 2026]

### Make budget alerts actionable, not just visible

Set AWS Budgets on each account and on key workloads using tags or cost categories, then configure notifications for both actual spend and forecasted spend. Daily budgets are especially useful when you want to catch overruns early enough to react before the month closes. Route alerts to email or SNS so they reach the people who can actually pause spend, right-size resources, or investigate a spike. Pair budget alerts with regular cost reviews so teams can compare current usage against the expected trend and adjust quickly. If your environment changes often, keep the budget thresholds tied to realistic forecasts instead of static numbers.

**Why it matters:** Budget alerts work best when they are specific, timely, and owned by the right team. That makes them a practical control for preventing surprise bills and keeping cloud spend aligned with business expectations.

<!-- TIP_OF_THE_DAY_END -->

## How it works

A scheduled GitHub Actions workflow runs `src/update_readme.py` once per day.

The script selects a topic from `src/topics.py`, then generates a new best-practice tip by using an AI agent with access to the local SQLite vector index in `storage/well_architected_index.sqlite`.

The agent searches the index, retrieves relevant source material, and writes one practical tip grounded in the retrieved material. The script then updates only the marked tip section in `README.md`, saves the tip as a dated Markdown file in `tips/`, and commits the change back to the repository.
