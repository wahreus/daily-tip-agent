# 🤖 Daily Tip Agent

An AI agent that posts one AWS Well-Architected best-practice tip per day into this `README.md`.

The project uses Retrieval-Augmented Generation (RAG) over a committed SQLite vector index built from the [AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf).

<!-- TIP_OF_THE_DAY_START -->

## Tip of the day [Thu, October 15, 2026]

### Centralize security logs in a dedicated archive account

Aggregate security-related logs from workloads and AWS services into a separate log archive account instead of keeping them only in each application account. Include sources such as CloudTrail, AWS WAF, Elastic Load Balancing, Route 53, and any other service logs that help you investigate activity across the environment. Standardizing these logs in one place makes it easier to feed a SIEM or other analytics tooling, correlate findings, and respond faster to suspicious events. Use cross-account permissions so security teams can access the data without depending on the workload accounts themselves. Keep retention and lifecycle policies aligned to compliance and investigation needs so the archive stays useful without becoming expensive to manage.

**Why it matters:** Centralized logging reduces the risk of log tampering if a workload account is compromised. It also gives security teams a single integration point for analysis, alerting, and escalation, which improves detection and response speed.

<!-- TIP_OF_THE_DAY_END -->

## How it works

A scheduled GitHub Actions workflow runs `src/update_readme.py` once per day.

The script selects a topic from `src/topics.py`, then generates a new best-practice tip by using an AI agent with access to the local SQLite vector index in `storage/well_architected_index.sqlite`.

The agent searches the index, retrieves relevant source material, and writes one practical tip grounded in the retrieved material. The script then updates only the marked tip section in `README.md`, saves the tip as a dated Markdown file in `tips/`, and commits the change back to the repository.
