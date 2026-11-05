# 🤖 Daily Tip Agent

An AI agent that posts one AWS Well-Architected best-practice tip per day into this `README.md`.

The project uses Retrieval-Augmented Generation (RAG) over a committed SQLite vector index built from the [AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf).

<!-- TIP_OF_THE_DAY_START -->

## Tip of the day [Thursday, November 5, 2026]

### Make performance reviews routine, not reactive

Set a fixed cadence to review workload performance, reliability, and cost metrics, and keep the review aligned to the business impact of the system. Use dashboards and anomaly detection to spot spikes, drops, and trends before they become incidents, then turn findings into prioritized backlog items. Include people from operations, development, and business teams so the review captures both technical symptoms and user-facing impact. Compare current behavior against baselines and recent changes to separate normal variation from real regressions. If the workload is expensive or complex, review it more often and adjust the cadence as the system or business changes.

**Why it matters:** Regular reviews help you catch issues early, make better decisions with data, and continuously improve the workload instead of waiting for outages or budget surprises. They also create shared ownership across teams, which makes remediation faster and more effective.

<!-- TIP_OF_THE_DAY_END -->

## How it works

A scheduled GitHub Actions workflow runs `src/update_readme.py` once per day.

The script selects a topic from `src/topics.py`, then generates a new best-practice tip by using an AI agent with access to the local SQLite vector index in `storage/well_architected_index.sqlite`.

The agent searches the index, retrieves relevant source material, and writes one practical tip grounded in the retrieved material. The script then updates only the marked tip section in `README.md`, saves the tip as a dated Markdown file in `tips/`, and commits the change back to the repository.
