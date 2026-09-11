# 🤖 Daily Tip Agent

An AI agent that posts one AWS Well-Architected best-practice tip per day into this `README.md`.

The project uses Retrieval-Augmented Generation (RAG) over a committed SQLite vector index built from the [AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf).

<!-- TIP_OF_THE_DAY_START -->

## Tip of the day [Friday, September 11, 2026]

### Make cost optimization a recurring operating habit

Review cloud spend on a fixed cadence instead of waiting for a budget alert or a month-end surprise. Use dashboards such as AWS Cost Explorer to break down costs by service, account, and day so you can spot trends early and connect spend changes to workload changes. Set AWS Budgets with alerting through email or SNS so you can react quickly when usage crosses thresholds. Include cost and usage in regular operational reporting, and track whether recent scaling or deployment changes improved or worsened efficiency over time. Revisit usage patterns periodically, because shifts in demand can reveal better service choices or opportunities to tune scaling policies.

**Why it matters:** Cost optimization improves when it is continuous rather than reactive. A regular review loop helps teams catch waste early, validate savings actions, and keep workloads aligned with changing demand.

<!-- TIP_OF_THE_DAY_END -->

## How it works

A scheduled GitHub Actions workflow runs `src/update_readme.py` once per day.

The script selects a topic from `src/topics.py`, then generates a new best-practice tip by using an AI agent with access to the local SQLite vector index in `storage/well_architected_index.sqlite`.

The agent searches the index, retrieves relevant source material, and writes one practical tip grounded in the retrieved material. The script then updates only the marked tip section in `README.md`, saves the tip as a dated Markdown file in `tips/`, and commits the change back to the repository.
