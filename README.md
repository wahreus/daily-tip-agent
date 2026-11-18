# 🤖 Daily Tip Agent

An AI agent that posts one AWS Well-Architected best-practice tip per day into this `README.md`.

The project uses Retrieval-Augmented Generation (RAG) over a committed SQLite vector index built from the [AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf).

<!-- TIP_OF_THE_DAY_START -->

## Tip of the day [Wednesday, November 18, 2026]

### Map keys to data and monitor their use

Treat key management as part of your data-classification strategy, not just an encryption checkbox. Use customer managed keys where you need tighter control, and keep the key in the same account as the workload when you can to simplify ownership and access control. Avoid reusing one key for every dataset; instead, map keys to the sensitivity or purpose of the data so permissions stay narrowly scoped. Review KMS key policies and grants carefully, because they are the primary controls that determine who can decrypt data or let AWS services do it on your behalf. Turn on CloudTrail-based monitoring and watch for unusual key use, especially key deletion requests or broad policy changes. If your environment allows it, use IAM Access Analyzer or Security Hub findings to catch overly permissive key policies and missing rotation.

**Why it matters:** Strong key management reduces the blast radius of compromised credentials and prevents accidental or malicious data exposure. Monitoring and policy reviews also help you detect misconfigurations early, before they become data-loss events.

<!-- TIP_OF_THE_DAY_END -->

## How it works

A scheduled GitHub Actions workflow runs `src/update_readme.py` once per day.

The script selects a topic from `src/topics.py`, then generates a new best-practice tip by using an AI agent with access to the local SQLite vector index in `storage/well_architected_index.sqlite`.

The agent searches the index, retrieves relevant source material, and writes one practical tip grounded in the retrieved material. The script then updates only the marked tip section in `README.md`, saves the tip as a dated Markdown file in `tips/`, and commits the change back to the repository.
