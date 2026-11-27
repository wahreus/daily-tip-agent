# 🤖 Daily Tip Agent

An AI agent that posts one AWS Well-Architected best-practice tip per day into this `README.md`.

The project uses Retrieval-Augmented Generation (RAG) over a committed SQLite vector index built from the [AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf).

<!-- TIP_OF_THE_DAY_START -->

## Tip of the day [Friday, November 27, 2026]

### Build recovery to be automated, observable, and stoppable

Design recovery so it can repair common failures without human intervention, but keep it standardized and tested so it behaves predictably during an incident. Use infrastructure as code for the recovery environment and orchestration tools like AWS Systems Manager Automation or AWS Step Functions to coordinate multi-step failover or repair workflows. Make sure your automation is observable while it runs, so you can confirm it is making the situation better rather than worse. Just as important, include a fast way to halt the automation if it starts to create additional downtime or data loss. Test recovery paths regularly against your real RTO and RPO targets so you know they work before you need them.

**Why it matters:** Automated recovery reduces the business impact of failures by shortening response time and eliminating manual, error-prone steps. Observability and a stop mechanism help prevent recovery automation from turning a bad incident into a worse one.

<!-- TIP_OF_THE_DAY_END -->

## How it works

A scheduled GitHub Actions workflow runs `src/update_readme.py` once per day.

The script selects a topic from `src/topics.py`, then generates a new best-practice tip by using an AI agent with access to the local SQLite vector index in `storage/well_architected_index.sqlite`.

The agent searches the index, retrieves relevant source material, and writes one practical tip grounded in the retrieved material. The script then updates only the marked tip section in `README.md`, saves the tip as a dated Markdown file in `tips/`, and commits the change back to the repository.
