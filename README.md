# 🤖 Daily Tip Agent

An AI agent that posts one AWS Well-Architected best-practice tip per day into this `README.md`.

The project uses Retrieval-Augmented Generation (RAG) over a committed SQLite vector index built from the [AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf).

<!-- TIP_OF_THE_DAY_START -->

## Tip of the day [Friday, November 6, 2026]

### Test recovery against your real RTO and RPO

Define the workload’s RTO and RPO first, then run recovery tests that prove your backup and failover process can actually meet those targets. Don’t stop at confirming that backups exist; perform a restore and validate that the recovered system is usable, data is intact, and the elapsed recovery time stays within the agreed objective. If your workload uses a disaster recovery strategy such as backup and restore, pilot light, or warm standby, test the exact runbook you would use in an incident. Automate as much of the recovery workflow as possible so you can repeat the test consistently and reduce human error. Revisit the test results whenever the workload changes, because a strategy that met objectives last quarter may no longer do so today.

**Why it matters:** Recovery objectives are only useful if they are achievable in practice. Regular testing exposes gaps in backup integrity, data consistency, and restore timing before a real outage forces you to discover them.

<!-- TIP_OF_THE_DAY_END -->

## How it works

A scheduled GitHub Actions workflow runs `src/update_readme.py` once per day.

The script selects a topic from `src/topics.py`, then generates a new best-practice tip by using an AI agent with access to the local SQLite vector index in `storage/well_architected_index.sqlite`.

The agent searches the index, retrieves relevant source material, and writes one practical tip grounded in the retrieved material. The script then updates only the marked tip section in `README.md`, saves the tip as a dated Markdown file in `tips/`, and commits the change back to the repository.
