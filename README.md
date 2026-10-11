# 🤖 Daily Tip Agent

An AI agent that posts one AWS Well-Architected best-practice tip per day into this `README.md`.

The project uses Retrieval-Augmented Generation (RAG) over a committed SQLite vector index built from the [AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf).

<!-- TIP_OF_THE_DAY_START -->

## Tip of the day [Sunday, October 11, 2026]

### Automate quota monitoring before you need the increase

Treat service quotas as an operational control, not a one-time setup task. Monitor quota usage continuously and alert when consumption approaches your defined threshold, especially for quotas that can block scaling or availability. Build a clear response path for alerts, including who approves requests and how quickly they should be submitted. For critical workloads, you can automate quota increase requests, but test that automation carefully in non-production first to avoid runaway requests or feedback loops. Keep track of both soft quotas that can be raised and hard limits that require architectural changes.

**Why it matters:** Quota exhaustion can cause scaling failures, degraded user experience, or outright service disruption. Proactive monitoring and a practiced request process give you time to raise limits or adapt the design before the workload hits a wall.

<!-- TIP_OF_THE_DAY_END -->

## How it works

A scheduled GitHub Actions workflow runs `src/update_readme.py` once per day.

The script selects a topic from `src/topics.py`, then generates a new best-practice tip by using an AI agent with access to the local SQLite vector index in `storage/well_architected_index.sqlite`.

The agent searches the index, retrieves relevant source material, and writes one practical tip grounded in the retrieved material. The script then updates only the marked tip section in `README.md`, saves the tip as a dated Markdown file in `tips/`, and commits the change back to the repository.
