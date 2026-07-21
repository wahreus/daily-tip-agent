# 🤖 Daily Tip Agent

An AI agent that posts one AWS Well-Architected best-practice tip per day into this `README.md`.

The project uses Retrieval-Augmented Generation (RAG) over a committed SQLite vector index built from the [AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf).

<!-- TIP_OF_THE_DAY_START -->

## Tip of the day [Tuesday, July 21, 2026]

### Lock down backups like production data

Treat backups as sensitive systems, not just copies of data. Encrypt backup data at rest and in transit, and make sure the backup environment uses separate access controls from production. Use least-privilege permissions so only the right operators and automation can create, read, or restore backups. Add immutability or logically isolated vaulting for critical backups to reduce the risk of deletion or tampering. Finally, test restores regularly to verify that backups are intact and actually recoverable when you need them.

**Why it matters:** Backups are a common target during ransomware and insider attacks, so protecting them is essential to preserving recovery options. Strong access controls, encryption, and restore validation help ensure your backup strategy delivers real resilience instead of a false sense of security.

<!-- TIP_OF_THE_DAY_END -->

## How it works

A scheduled GitHub Actions workflow runs `src/update_readme.py` once per day.

The script selects a topic from `src/topics.py`, then generates a new best-practice tip by using an AI agent with access to the local SQLite vector index in `storage/well_architected_index.sqlite`.

The agent searches the index, retrieves relevant source material, and writes one practical tip grounded in the retrieved material. The script then updates only the marked tip section in `README.md`, saves the tip as a dated Markdown file in `tips/`, and commits the change back to the repository.
