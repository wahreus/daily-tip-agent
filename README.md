# 🤖 Daily Tip Agent

An AI agent that posts one AWS Well-Architected best-practice tip per day into this `README.md`.

The project uses Retrieval-Augmented Generation (RAG) over a committed SQLite vector index built from the [AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf).

<!-- TIP_OF_THE_DAY_START -->

## Tip of the day [Thursday, August 13, 2026]

### Make changes small and easy to undo

Design your delivery process so each deployment changes as little as possible and can be reversed quickly if needed. Use safe rollout patterns like canary, rolling, blue/green, traffic splitting, or feature flags to limit impact while you validate the change in production. Keep rollback or fix-forward plans documented and tested before release, and automate them in the pipeline wherever possible. Smaller, repeatable, standardized changes are easier to recover from than large bulk updates. If a change fails, automated rollback should stop the problem from spreading to all users at once.

**Why it matters:** Small reversible changes reduce blast radius and shorten recovery time when something goes wrong. They also let teams ship more frequently without requiring a risky all-at-once release.

<!-- TIP_OF_THE_DAY_END -->

## How it works

A scheduled GitHub Actions workflow runs `src/update_readme.py` once per day.

The script selects a topic from `src/topics.py`, then generates a new best-practice tip by using an AI agent with access to the local SQLite vector index in `storage/well_architected_index.sqlite`.

The agent searches the index, retrieves relevant source material, and writes one practical tip grounded in the retrieved material. The script then updates only the marked tip section in `README.md`, saves the tip as a dated Markdown file in `tips/`, and commits the change back to the repository.
