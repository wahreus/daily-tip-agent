# 🤖 Daily Tip Agent

An AI agent that posts one AWS Well-Architected best-practice tip per day into this `README.md`.

The project uses Retrieval-Augmented Generation (RAG) over a committed SQLite vector index built from the [AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf).

<!-- TIP_OF_THE_DAY_START -->

## Tip of the day [Sunday, October 25, 2026]

### Match commitment level to workload shape

Choose your AWS pricing model based on how predictable each workload is, not just on the headline discount. Use Savings Plans or Reserved Instances for steady, always-on components where you can commit to consistent usage over time. Use Spot Instances for stateless or interruptible jobs that can tolerate capacity changes. Keep On-Demand for short-lived or irregular workloads that do not run long enough to benefit from a commitment. A practical approach is to start with a small commitment, review the top recommendations, and then adjust as your usage patterns become clearer.

**Why it matters:** The best savings come from aligning pricing model to actual usage patterns, which reduces waste without creating unnecessary commitment risk. This also helps you keep flexibility where the workload needs it while still capturing discounts on predictable capacity.

<!-- TIP_OF_THE_DAY_END -->

## How it works

A scheduled GitHub Actions workflow runs `src/update_readme.py` once per day.

The script selects a topic from `src/topics.py`, then generates a new best-practice tip by using an AI agent with access to the local SQLite vector index in `storage/well_architected_index.sqlite`.

The agent searches the index, retrieves relevant source material, and writes one practical tip grounded in the retrieved material. The script then updates only the marked tip section in `README.md`, saves the tip as a dated Markdown file in `tips/`, and commits the change back to the repository.
