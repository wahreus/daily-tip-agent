# 🤖 Daily Tip Agent

An AI agent that posts one AWS Well-Architected best-practice tip per day into this `README.md`.

The project uses Retrieval-Augmented Generation (RAG) over a committed SQLite vector index built from the [AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf).

<!-- TIP_OF_THE_DAY_START -->

## Tip of the day [Monday, July 6, 2026]

### Make runbooks short, validated, and easy to automate

For common operations, write runbooks as clear step-by-step procedures with the desired outcome stated up front. Include any required permissions, tools, error handling, and escalation paths so an engineer can complete the task without guessing. Publish runbooks in a central location and assign an owner so they stay discoverable and maintained. Before relying on a runbook, have someone else on the team execute it to catch missing steps or unclear instructions. As the same operation becomes routine, convert the runbook into automation for the most frequent and low-risk tasks.

**Why it matters:** Well-written runbooks reduce operational risk by making routine work repeatable and consistent, even when the person performing it changes. Validation and ongoing updates help prevent drift, while automation lowers manual effort and frees engineers to focus on higher-value work.

<!-- TIP_OF_THE_DAY_END -->

## How it works

A scheduled GitHub Actions workflow runs `src/update_readme.py` once per day.

The script selects a topic from `src/topics.py`, then generates a new best-practice tip by using an AI agent with access to the local SQLite vector index in `storage/well_architected_index.sqlite`.

The agent searches the index, retrieves relevant source material, and writes one practical tip grounded in the retrieved material. The script then updates only the marked tip section in `README.md`, saves the tip as a dated Markdown file in `tips/`, and commits the change back to the repository.

## GitHub Actions

The workflow is defined in:

```text
.github/workflows/daily-tip.yml
```

It runs daily and can also be triggered manually from the GitHub Actions tab.