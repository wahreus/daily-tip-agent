# 🤖 Daily Tip Agent

An AI agent that posts one AWS Well-Architected best-practice tip per day into this `README.md`.

The project uses Retrieval-Augmented Generation (RAG) over a committed SQLite vector index built from the [AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf).

<!-- TIP_OF_THE_DAY_START -->

## Tip of the day [Tue, November 10, 2026]

### Standardize cost allocation tags and enforce them early

Define a small, organization-wide set of cost attribution tags such as `CostCenter`, `Project`, `Environment`, and `Owner`, and make sure the key names and allowed values are consistent across accounts. Apply those tags to all billable resources so your cost and usage data can be grouped by business unit, application, or workload. Use AWS Organizations tag policies or similar controls to prevent nonstandard keys and values from creeping in over time. Automate tagging in your provisioning workflows so new resources are tagged at creation instead of being fixed later. Where tagging is not enough, map the same business structure into AWS Cost Categories to improve reporting and chargeback.

**Why it matters:** Consistent cost allocation tags make spend visible to the teams that create it, which improves accountability and helps uncover waste faster. They also make budgeting, forecasting, and internal chargeback more accurate because costs can be attributed to the right workload or owner instead of landing in a generic bucket.

<!-- TIP_OF_THE_DAY_END -->

## How it works

A scheduled GitHub Actions workflow runs `src/update_readme.py` once per day.

The script selects a topic from `src/topics.py`, then generates a new best-practice tip by using an AI agent with access to the local SQLite vector index in `storage/well_architected_index.sqlite`.

The agent searches the index, retrieves relevant source material, and writes one practical tip grounded in the retrieved material. The script then updates only the marked tip section in `README.md`, saves the tip as a dated Markdown file in `tips/`, and commits the change back to the repository.
