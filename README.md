# 🤖 Daily Tip Agent

An AI agent that posts one AWS Well-Architected best-practice tip per day into this `README.md`.

The project uses Retrieval-Augmented Generation (RAG) over a committed SQLite vector index built from the [AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf).

<!-- TIP_OF_THE_DAY_START -->

## Tip of the day [Wednesday, October 14, 2026]

### Monitor the whole path, not just the server

Treat workload health monitoring as an end-to-end practice: collect logs and metrics from every workload component and its AWS dependencies, then centralize them so you can spot trends and anomalies quickly. Define a small set of meaningful metrics for availability, latency, errors, and saturation, and wire alarms to notify you when thresholds are crossed. Add distributed tracing so you can follow a request through the system and narrow down where failures or slowdowns begin. For external endpoints, use synthetic checks to continuously validate that the user-facing path still works as expected. Review your dashboards and alert rules regularly so they stay aligned with how the workload actually behaves.

**Why it matters:** Good health monitoring helps you detect degradation before users do and reduces the time needed to isolate root cause. It also makes it easier to automate response actions, scale appropriately, and recover faster when a component or dependency starts failing.

<!-- TIP_OF_THE_DAY_END -->

## How it works

A scheduled GitHub Actions workflow runs `src/update_readme.py` once per day.

The script selects a topic from `src/topics.py`, then generates a new best-practice tip by using an AI agent with access to the local SQLite vector index in `storage/well_architected_index.sqlite`.

The agent searches the index, retrieves relevant source material, and writes one practical tip grounded in the retrieved material. The script then updates only the marked tip section in `README.md`, saves the tip as a dated Markdown file in `tips/`, and commits the change back to the repository.
