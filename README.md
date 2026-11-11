# 🤖 Daily Tip Agent

An AI agent that posts one AWS Well-Architected best-practice tip per day into this `README.md`.

The project uses Retrieval-Augmented Generation (RAG) over a committed SQLite vector index built from the [AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf).

<!-- TIP_OF_THE_DAY_START -->

## Tip of the day [Wednesday, November 11, 2026]

### Centralize security logs in a dedicated archive

Send security-relevant logs from workloads and AWS services into a standardized, separate log archive account instead of leaving them scattered across individual teams or accounts. Include sources such as CloudTrail, AWS WAF, Elastic Load Balancing, Route 53, and other service logs that help reconstruct security events. Centralizing them gives your security team one place to correlate activity, run investigations, and feed SIEM or analytics tools. Use cross-account permissions so the archive is readable for analysis but harder to tamper with if a workload account is compromised. Make sure you also define retention and lifecycle settings so the archive supports both incident response and compliance needs.

**Why it matters:** A centralized logging pattern reduces blind spots and makes it much easier to detect anomalous activity across distributed systems. It also improves resilience against log tampering and shortens the time needed to perform root-cause analysis during an incident.

<!-- TIP_OF_THE_DAY_END -->

## How it works

A scheduled GitHub Actions workflow runs `src/update_readme.py` once per day.

The script selects a topic from `src/topics.py`, then generates a new best-practice tip by using an AI agent with access to the local SQLite vector index in `storage/well_architected_index.sqlite`.

The agent searches the index, retrieves relevant source material, and writes one practical tip grounded in the retrieved material. The script then updates only the marked tip section in `README.md`, saves the tip as a dated Markdown file in `tips/`, and commits the change back to the repository.
