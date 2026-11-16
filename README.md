# 🤖 Daily Tip Agent

An AI agent that posts one AWS Well-Architected best-practice tip per day into this `README.md`.

The project uses Retrieval-Augmented Generation (RAG) over a committed SQLite vector index built from the [AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf).

<!-- TIP_OF_THE_DAY_START -->

## Tip of the day [Monday, November 16, 2026]

### Make cost optimization a recurring operating habit

Treat cost optimization as an ongoing process, not a one-time cleanup. Review usage and spend regularly with AWS Cost Explorer and AWS Budgets so you can spot idle, underutilized, or unexpectedly growing resources early. Build a cadence for reporting on cost performance, such as weekly or monthly reviews, and track progress against budgets and alerts. Use recurring reports to surface rightsizing recommendations plus Savings Plans and Reserved Instances opportunities, then apply commitments in small batches and re-evaluate after a month or two. For workloads with predictable downtime, stop compute resources after hours or pause them when possible so you only pay for storage while they are idle.  

**Why it matters:** Costs drift over time as workloads, teams, and usage patterns change. A regular review cycle helps you catch waste quickly, keep unit costs down, and make better purchasing decisions as your steady-state usage becomes clearer.

<!-- TIP_OF_THE_DAY_END -->

## How it works

A scheduled GitHub Actions workflow runs `src/update_readme.py` once per day.

The script selects a topic from `src/topics.py`, then generates a new best-practice tip by using an AI agent with access to the local SQLite vector index in `storage/well_architected_index.sqlite`.

The agent searches the index, retrieves relevant source material, and writes one practical tip grounded in the retrieved material. The script then updates only the marked tip section in `README.md`, saves the tip as a dated Markdown file in `tips/`, and commits the change back to the repository.
