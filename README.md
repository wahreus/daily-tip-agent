# 🤖 Daily Tip Agent

An AI agent that posts one AWS Well-Architected best-practice tip per day into this `README.md`.

The project uses Retrieval-Augmented Generation (RAG) over a committed SQLite vector index built from the [AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf).

<!-- TIP_OF_THE_DAY_START -->

## Tip of the day [Saturday, October 17, 2026]

### Match storage to access patterns, not habits

Choose your storage service based on how the workload actually reads, writes, retains, and serves data. Start by classifying the data as structured, semi-structured, or unstructured, then check whether it is persistent, ephemeral, or transient. Next, compare the workload’s latency, throughput, IOPS, durability, and retention needs against purpose-built options instead of defaulting to a familiar database or a single storage tier. If the access pattern is read-heavy, write-heavy, bursty, archival, or online versus offline, pick storage that fits that pattern or adjust the application to better align with the storage model. Revisit the choice over time, because access patterns often change as features, traffic, and data growth evolve.

**Why it matters:** Proper storage selection reduces wasted compute and storage capacity while improving performance efficiency. It also lowers the risk of using an overbuilt or underperforming service for the workload’s real needs.

<!-- TIP_OF_THE_DAY_END -->

## How it works

A scheduled GitHub Actions workflow runs `src/update_readme.py` once per day.

The script selects a topic from `src/topics.py`, then generates a new best-practice tip by using an AI agent with access to the local SQLite vector index in `storage/well_architected_index.sqlite`.

The agent searches the index, retrieves relevant source material, and writes one practical tip grounded in the retrieved material. The script then updates only the marked tip section in `README.md`, saves the tip as a dated Markdown file in `tips/`, and commits the change back to the repository.
