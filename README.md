# 🤖 Daily Tip Agent

An AI agent that posts one AWS Well-Architected best-practice tip per day into this `README.md`.

The project uses Retrieval-Augmented Generation (RAG) over a committed SQLite vector index built from the [AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf).

<!-- TIP_OF_THE_DAY_START -->

## Tip of the day [Thursday, November 26, 2026]

### Centralize security logs in a protected archive

Capture security-related logs and findings in standardized locations instead of leaving each workload to manage its own copy. A strong pattern is to aggregate sources like CloudTrail, WAF, load balancer logs, Route 53 logs, and other security signals into a dedicated log archive or security tooling account. This reduces the risk of log tampering if a workload is compromised and gives you a single place to integrate SIEM or detection tools. Keep access tightly controlled with cross-account permissions so teams can analyze data without letting workloads alter it. For services with long retention needs, choose storage and lifecycle settings that match your investigation and compliance requirements. If you are using a newer centralized option like Security Lake, include it in your standard collection strategy and make sure it covers the regions and sources you actually use.

**Why it matters:** Centralized logging makes correlation, investigation, and alerting much faster because analysts are working from one normalized data set. It also improves resilience against attackers who might try to delete or modify logs in the affected environment.

<!-- TIP_OF_THE_DAY_END -->

## How it works

A scheduled GitHub Actions workflow runs `src/update_readme.py` once per day.

The script selects a topic from `src/topics.py`, then generates a new best-practice tip by using an AI agent with access to the local SQLite vector index in `storage/well_architected_index.sqlite`.

The agent searches the index, retrieves relevant source material, and writes one practical tip grounded in the retrieved material. The script then updates only the marked tip section in `README.md`, saves the tip as a dated Markdown file in `tips/`, and commits the change back to the repository.
