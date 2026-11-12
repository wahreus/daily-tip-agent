# 🤖 Daily Tip Agent

An AI agent that posts one AWS Well-Architected best-practice tip per day into this `README.md`.

The project uses Retrieval-Augmented Generation (RAG) over a committed SQLite vector index built from the [AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf).

<!-- TIP_OF_THE_DAY_START -->

## Tip of the day [Thursday, November 12, 2026]

### Set budget alerts for both actual and forecasted spend

Create AWS Budgets with daily granularity so you can catch overspend early instead of waiting until month-end. Set thresholds for both actual costs and forecasted costs; actual alerts tell you when you have already crossed a line, while forecasted alerts give you time to react before the budget is exceeded. Route notifications to a shared email list or SNS topic rather than a single person so the right team always sees the alert. For better coverage, define separate budgets for accounts, workloads, Regions, or services using tags and cost categories. If a budget breach should trigger action, use Budget Actions to enforce controls automatically or with approval.

**Why it matters:** Budget alerts turn cloud spend into an operational signal, not a surprise. They help DevOps teams respond quickly to waste, prevent recurring overruns, and keep costs aligned with workload growth and business expectations.

<!-- TIP_OF_THE_DAY_END -->

## How it works

A scheduled GitHub Actions workflow runs `src/update_readme.py` once per day.

The script selects a topic from `src/topics.py`, then generates a new best-practice tip by using an AI agent with access to the local SQLite vector index in `storage/well_architected_index.sqlite`.

The agent searches the index, retrieves relevant source material, and writes one practical tip grounded in the retrieved material. The script then updates only the marked tip section in `README.md`, saves the tip as a dated Markdown file in `tips/`, and commits the change back to the repository.
