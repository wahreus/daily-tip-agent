# 🤖 Daily Tip Agent

An AI agent that posts one AWS Well-Architected best-practice tip per day into this `README.md`.

The project uses Retrieval-Augmented Generation (RAG) over a committed SQLite vector index built from the [AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf).

<!-- TIP_OF_THE_DAY_START -->

## Tip of the day [Sunday, November 1, 2026]

### Make cost visibility part of your operating model

Start by defining the business categories you want to charge or report against, such as team, project, or environment. Then enforce consistent resource tagging so cost and usage data can be grouped reliably across accounts and workloads. Pair those tags with AWS Budgets, Cost Explorer, and Cost and Usage Reports so teams can review spend trends, receive alerts, and spot unexpected usage early. For shared services, use cost allocation methods based on workload metrics or business outcomes instead of leaving costs unattributed. Review the data on a regular cadence with both engineering and finance so you can act on negative trends before they become budget problems.

**Why it matters:** Good cost and usage visibility turns cloud spend into something teams can actually manage. It improves accountability, supports chargeback or showback, and helps you make faster decisions about right-sizing, shared infrastructure, and optimization priorities.

<!-- TIP_OF_THE_DAY_END -->

## How it works

A scheduled GitHub Actions workflow runs `src/update_readme.py` once per day.

The script selects a topic from `src/topics.py`, then generates a new best-practice tip by using an AI agent with access to the local SQLite vector index in `storage/well_architected_index.sqlite`.

The agent searches the index, retrieves relevant source material, and writes one practical tip grounded in the retrieved material. The script then updates only the marked tip section in `README.md`, saves the tip as a dated Markdown file in `tips/`, and commits the change back to the repository.
