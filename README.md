# 🤖 Daily Tip Agent

An AI agent that posts one AWS Well-Architected best-practice tip per day into this `README.md`.

The project uses Retrieval-Augmented Generation (RAG) over a committed SQLite vector index built from the [AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf).

<!-- TIP_OF_THE_DAY_START -->

## Tip of the day [Wednesday, October 21, 2026]

### Encrypt, isolate, and test backups

Treat backups as a separate security boundary, not just a copy of production data. Encrypt every backup and the underlying data stores so confidentiality and integrity are preserved end to end. Keep backup access tightly scoped with least-privilege permissions, and avoid giving the same people or automation full control over both production and restore paths. For critical systems, use logical isolation such as a separate backup vault or account to reduce the blast radius of ransomware or accidental deletion. Finally, run restore tests on a regular schedule so you know the backups are both readable and actually recoverable when you need them.

**Why it matters:** Backup protection fails if attackers or mistakes can delete, tamper with, or restore from compromised copies. Encryption, isolation, and periodic validation make backups trustworthy for real recovery events and help you meet your RPO/RTO goals.

<!-- TIP_OF_THE_DAY_END -->

## How it works

A scheduled GitHub Actions workflow runs `src/update_readme.py` once per day.

The script selects a topic from `src/topics.py`, then generates a new best-practice tip by using an AI agent with access to the local SQLite vector index in `storage/well_architected_index.sqlite`.

The agent searches the index, retrieves relevant source material, and writes one practical tip grounded in the retrieved material. The script then updates only the marked tip section in `README.md`, saves the tip as a dated Markdown file in `tips/`, and commits the change back to the repository.
