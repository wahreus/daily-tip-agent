# 🤖 Daily Tip Agent

An AI agent that posts one AWS Well-Architected best-practice tip per day into this `README.md`.

The project uses Retrieval-Augmented Generation (RAG) over a committed SQLite vector index built from the [AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf).

<!-- TIP_OF_THE_DAY_START -->

## Tip of the day [Monday, November 9, 2026]

### Test recovery to prove your RTO and RPO

Don’t treat backups or failover plans as “done” until you’ve actually recovered data and verified it is usable. Periodically restore backups to a new location and run a real application-level check so you confirm the data is complete, readable, and not corrupted. Measure how long the recovery takes and compare it against your RTO to make sure the workload can be restored in time. Also verify that the amount of data lost during the test stays within the defined RPO for the workload. If the process fails or runs too slowly, use the test to tighten the recovery mechanism before an incident forces you to rely on it.

**Why it matters:** Recovery objectives are only meaningful if your implementation can meet them under test conditions. Regular recovery testing reduces the risk of discovering broken backups, inaccessible data, or slow restore paths during an outage.

<!-- TIP_OF_THE_DAY_END -->

## How it works

A scheduled GitHub Actions workflow runs `src/update_readme.py` once per day.

The script selects a topic from `src/topics.py`, then generates a new best-practice tip by using an AI agent with access to the local SQLite vector index in `storage/well_architected_index.sqlite`.

The agent searches the index, retrieves relevant source material, and writes one practical tip grounded in the retrieved material. The script then updates only the marked tip section in `README.md`, saves the tip as a dated Markdown file in `tips/`, and commits the change back to the repository.
