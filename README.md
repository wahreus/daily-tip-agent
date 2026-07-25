# 🤖 Daily Tip Agent

An AI agent that posts one AWS Well-Architected best-practice tip per day into this `README.md`.

The project uses Retrieval-Augmented Generation (RAG) over a committed SQLite vector index built from the [AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf).

<!-- TIP_OF_THE_DAY_START -->

## Tip of the day [Saturday, July 25, 2026]

### Rightsize and schedule away idle capacity

Start by inventorying your AWS resources and monitoring utilization for key signals like CPU, memory, and network throughput. Use AWS Compute Optimizer or similar rightsizing tools at regular intervals to spot idle or underutilized components, especially in stable workloads. For resources that do not need to run continuously, use scheduled stop/start patterns with AWS Instance Scheduler or equivalent automation to avoid paying for unused hours. Where possible, pair this with Auto Scaling so capacity follows demand instead of staying provisioned for peak load. Finally, remove components that are no longer needed and consider consolidating low-use resources to improve overall utilization.  

**Why it matters:** Idle resources quietly inflate cloud spend without adding value. Reducing them lowers cost while also simplifying operations and making your environment easier to manage.

<!-- TIP_OF_THE_DAY_END -->

## How it works

A scheduled GitHub Actions workflow runs `src/update_readme.py` once per day.

The script selects a topic from `src/topics.py`, then generates a new best-practice tip by using an AI agent with access to the local SQLite vector index in `storage/well_architected_index.sqlite`.

The agent searches the index, retrieves relevant source material, and writes one practical tip grounded in the retrieved material. The script then updates only the marked tip section in `README.md`, saves the tip as a dated Markdown file in `tips/`, and commits the change back to the repository.
