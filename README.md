# 🤖 Daily Tip Agent

An AI agent that posts one AWS Well-Architected best-practice tip per day into this `README.md`.

The project uses Retrieval-Augmented Generation (RAG) over a committed SQLite vector index built from the [AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf).

<!-- TIP_OF_THE_DAY_START -->

## Tip of the day [Saturday, October 24, 2026]

### Centralize and correlate security signals fast

Capture security-relevant logs, findings, and metrics in standardized locations so investigators can reliably search and compare events across services. Enable service and application logging, then route alerts and findings into a central workflow or SIEM where they can be correlated with identity, network, and resource context. Use managed detections such as GuardDuty, CloudTrail, CloudWatch alarms, and AWS Config history to provide multiple angles on the same event. Enrich alerts with asset, user, and policy data so teams can quickly tell whether an issue is routine noise or a real incident. Where possible, automate initial triage and repetitive response steps to reduce manual effort and shorten time to investigation.

**Why it matters:** Centralized, enriched detections reduce alert fatigue and help responders understand severity faster. That leads to quicker containment decisions and a lower chance that a real security incident is missed or misclassified.

<!-- TIP_OF_THE_DAY_END -->

## How it works

A scheduled GitHub Actions workflow runs `src/update_readme.py` once per day.

The script selects a topic from `src/topics.py`, then generates a new best-practice tip by using an AI agent with access to the local SQLite vector index in `storage/well_architected_index.sqlite`.

The agent searches the index, retrieves relevant source material, and writes one practical tip grounded in the retrieved material. The script then updates only the marked tip section in `README.md`, saves the tip as a dated Markdown file in `tips/`, and commits the change back to the repository.
