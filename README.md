# 🤖 Daily Tip Agent

An AI agent that posts one AWS Well-Architected best-practice tip per day into this `README.md`.

The project uses Retrieval-Augmented Generation (RAG) over a committed SQLite vector index built from the [AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf).

<!-- TIP_OF_THE_DAY_START -->

## Tip of the day [Sat, November 21, 2026]

### Centralize security logs in a dedicated archive account

Capture security logs and findings from AWS services and applications into a standardized, separate Log Archive account rather than leaving them spread across workloads. Include sources like CloudTrail, WAF, Route 53, VPC Flow Logs, and other service logs that are relevant to security analysis. This makes it much easier to correlate events, reduces the operational overhead of ETL and scattered permissions, and gives you a single place to integrate SIEM or other analytics tools. Keep the Security Tooling account separate from the Log Archive account so your analysis tools do not share the same blast radius as the data they inspect. If possible, use standardized formats and ingestion paths so the data is ready for querying without extra transformation. Protect the archive with cross-account permissions and controls that make tampering from compromised workloads harder.

**Why it matters:** Centralized logging improves incident detection because security teams can analyze one consistent data set instead of chasing logs across many accounts and services. It also strengthens resilience and auditability by making log tampering more difficult and preserving evidence for response and compliance.

<!-- TIP_OF_THE_DAY_END -->

## How it works

A scheduled GitHub Actions workflow runs `src/update_readme.py` once per day.

The script selects a topic from `src/topics.py`, then generates a new best-practice tip by using an AI agent with access to the local SQLite vector index in `storage/well_architected_index.sqlite`.

The agent searches the index, retrieves relevant source material, and writes one practical tip grounded in the retrieved material. The script then updates only the marked tip section in `README.md`, saves the tip as a dated Markdown file in `tips/`, and commits the change back to the repository.
