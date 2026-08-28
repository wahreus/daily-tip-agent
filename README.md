# 🤖 Daily Tip Agent

An AI agent that posts one AWS Well-Architected best-practice tip per day into this `README.md`.

The project uses Retrieval-Augmented Generation (RAG) over a committed SQLite vector index built from the [AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf).

<!-- TIP_OF_THE_DAY_START -->

## Tip of the day [Friday, August 28, 2026]

### Use a multi-account structure as your main isolation boundary

Design AWS account structure so production, non-production, and unrelated workloads live in separate member accounts under AWS Organizations. Keep workload resources out of the management account, and use organizational units to group accounts by business need, data sensitivity, or environment. This makes it easier to apply consistent guardrails with inherited policies while still allowing different controls where needed. It also reduces the blast radius if a workload is misconfigured or compromised. For teams that are growing, a landing zone approach helps standardize new account creation and keeps governance from becoming ad hoc.

**Why it matters:** Account-level separation improves security, billing clarity, and access control at the same time. It also makes cost allocation and policy management much easier as your environment scales.

<!-- TIP_OF_THE_DAY_END -->

## How it works

A scheduled GitHub Actions workflow runs `src/update_readme.py` once per day.

The script selects a topic from `src/topics.py`, then generates a new best-practice tip by using an AI agent with access to the local SQLite vector index in `storage/well_architected_index.sqlite`.

The agent searches the index, retrieves relevant source material, and writes one practical tip grounded in the retrieved material. The script then updates only the marked tip section in `README.md`, saves the tip as a dated Markdown file in `tips/`, and commits the change back to the repository.
