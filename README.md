# 🤖 Daily Tip Agent

An AI agent that posts one AWS Well-Architected best-practice tip per day into this `README.md`.

The project uses Retrieval-Augmented Generation (RAG) over a committed SQLite vector index built from the [AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf).

<!-- TIP_OF_THE_DAY_START -->

## Tip of the day [Tue, November 3, 2026]

### Ship Smaller, Revert Faster

Break production changes into small, well-scoped releases so each deployment is easy to validate and easy to undo. Use safe rollout patterns like canary, rolling, blue/green, or feature flags to limit the blast radius if something goes wrong. Before you deploy, document a rollback or fix-forward path and make sure it is tested, not just written down. Smaller changes also reduce the chance that one defect affects multiple components at once. If a change fails, you should be able to restore the previous working state quickly without impacting the whole system. Build your CI/CD process so reversible change is the default, not the exception.

**Why it matters:** Small reversible changes reduce downtime, shorten recovery time, and keep failures from spreading across production. They also make deployments safer and more frequent because teams can respond quickly when a change behaves unexpectedly.

<!-- TIP_OF_THE_DAY_END -->

## How it works

A scheduled GitHub Actions workflow runs `src/update_readme.py` once per day.

The script selects a topic from `src/topics.py`, then generates a new best-practice tip by using an AI agent with access to the local SQLite vector index in `storage/well_architected_index.sqlite`.

The agent searches the index, retrieves relevant source material, and writes one practical tip grounded in the retrieved material. The script then updates only the marked tip section in `README.md`, saves the tip as a dated Markdown file in `tips/`, and commits the change back to the repository.
