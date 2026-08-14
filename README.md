# 🤖 Daily Tip Agent

An AI agent that posts one AWS Well-Architected best-practice tip per day into this `README.md`.

The project uses Retrieval-Augmented Generation (RAG) over a committed SQLite vector index built from the [AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf).

<!-- TIP_OF_THE_DAY_START -->

## Tip of the day [Friday, August 14, 2026]

### Ship in small slices with automatic rollback

Break changes into smaller releases so each deployment is easier to validate and, if needed, undo. Use safe rollout patterns such as canary, rolling, blue/green, or feature flags to limit the blast radius of a defect. Pair each change with automated testing in the pipeline so you can confirm expected behavior before expanding traffic or promoting the release. If the deployment does not meet pre-defined success criteria, trigger an automated rollback to a known good version rather than relying on manual recovery steps. This approach reduces customer impact, shortens recovery time, and makes frequent delivery safer.

**Why it matters:** Small, reversible changes lower the risk of wide-scale outages and remove a lot of pressure from the deployment process. They also let teams release more often with more confidence, because failures are contained and recovery is built into the workflow.

<!-- TIP_OF_THE_DAY_END -->

## How it works

A scheduled GitHub Actions workflow runs `src/update_readme.py` once per day.

The script selects a topic from `src/topics.py`, then generates a new best-practice tip by using an AI agent with access to the local SQLite vector index in `storage/well_architected_index.sqlite`.

The agent searches the index, retrieves relevant source material, and writes one practical tip grounded in the retrieved material. The script then updates only the marked tip section in `README.md`, saves the tip as a dated Markdown file in `tips/`, and commits the change back to the repository.
