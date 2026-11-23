# 🤖 Daily Tip Agent

An AI agent that posts one AWS Well-Architected best-practice tip per day into this `README.md`.

The project uses Retrieval-Augmented Generation (RAG) over a committed SQLite vector index built from the [AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf).

<!-- TIP_OF_THE_DAY_START -->

## Tip of the day [Monday, November 23, 2026]

### Make changes small, automated, and reversible

Treat production changes as a first-class release process, not an afterthought. Use infrastructure as code and automated delivery pipelines so updates are repeatable, consistent, and less dependent on manual steps. Prefer frequent, small changes over large batches, because smaller releases are easier to validate, easier to roll back, and less likely to create broad customer impact if something goes wrong. Where possible, add safe rollout patterns such as blue/green, canary, traffic splitting, or feature flags to limit blast radius. Keep configuration and infrastructure definitions in version control so changes are tracked and can be reverted quickly. Also monitor for drift so you can detect when live systems no longer match the approved state.

**Why it matters:** Good change management reduces the risk of failed deployments and shortens recovery time when issues occur. Automation and reversibility help teams ship faster while keeping operational risk under control.

<!-- TIP_OF_THE_DAY_END -->

## How it works

A scheduled GitHub Actions workflow runs `src/update_readme.py` once per day.

The script selects a topic from `src/topics.py`, then generates a new best-practice tip by using an AI agent with access to the local SQLite vector index in `storage/well_architected_index.sqlite`.

The agent searches the index, retrieves relevant source material, and writes one practical tip grounded in the retrieved material. The script then updates only the marked tip section in `README.md`, saves the tip as a dated Markdown file in `tips/`, and commits the change back to the repository.
