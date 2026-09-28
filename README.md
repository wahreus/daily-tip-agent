# 🤖 Daily Tip Agent

An AI agent that posts one AWS Well-Architected best-practice tip per day into this `README.md`.

The project uses Retrieval-Augmented Generation (RAG) over a committed SQLite vector index built from the [AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf).

<!-- TIP_OF_THE_DAY_START -->

## Tip of the day [Monday, September 28, 2026]

### Make changes small, staged, and easy to roll back

Prefer small, incremental deployments over large all-at-once releases so you can validate each change with limited blast radius. Use safe rollout patterns such as canary, rolling, blue/green, traffic splitting, or feature flags to expose changes to a small set of users first. Pair each rollout with monitoring and clear success criteria so you can quickly detect issues before expanding traffic. Automate rollback to a known good version when those criteria are not met, rather than relying on manual recovery during an incident. This keeps deployment risk low while still letting you ship frequently and learn from real production signals.

**Why it matters:** Small reversible changes reduce the chance that a defect affects all customers at once. They also shorten recovery time because you can stop, revert, or adjust a change before it spreads widely.

<!-- TIP_OF_THE_DAY_END -->

## How it works

A scheduled GitHub Actions workflow runs `src/update_readme.py` once per day.

The script selects a topic from `src/topics.py`, then generates a new best-practice tip by using an AI agent with access to the local SQLite vector index in `storage/well_architected_index.sqlite`.

The agent searches the index, retrieves relevant source material, and writes one practical tip grounded in the retrieved material. The script then updates only the marked tip section in `README.md`, saves the tip as a dated Markdown file in `tips/`, and commits the change back to the repository.
