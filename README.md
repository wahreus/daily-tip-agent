# 🤖 Daily Tip Agent

An AI agent that posts one AWS Well-Architected best-practice tip per day into this `README.md`.

The project uses Retrieval-Augmented Generation (RAG) over a committed SQLite vector index built from the [AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf).

<!-- TIP_OF_THE_DAY_START -->

## Tip of the day [Saturday, November 14, 2026]

### Make cost optimization a recurring operating habit

Treat cost optimization as an ongoing review cycle, not a one-time cleanup. Set a regular cadence to review spend, usage trends, and budget variance alongside your normal operational reporting. Use cost and usage reports with the right level of granularity so you can spot drift, identify inefficient resources, and catch negative trends early. Tag workloads and accounts consistently so you can track costs by owner, service, or business unit over time. Pair those reviews with alerts from budgets so teams can respond quickly when spend moves outside expected bounds.

**Why it matters:** Costs usually creep up gradually as workloads change, new resources are added, and old ones are left behind. A repeatable review process helps teams stay ahead of waste and continuously improve the cost efficiency of the workload.

<!-- TIP_OF_THE_DAY_END -->

## How it works

A scheduled GitHub Actions workflow runs `src/update_readme.py` once per day.

The script selects a topic from `src/topics.py`, then generates a new best-practice tip by using an AI agent with access to the local SQLite vector index in `storage/well_architected_index.sqlite`.

The agent searches the index, retrieves relevant source material, and writes one practical tip grounded in the retrieved material. The script then updates only the marked tip section in `README.md`, saves the tip as a dated Markdown file in `tips/`, and commits the change back to the repository.
