# 🤖 Daily Tip Agent

An AI agent that posts one AWS Well-Architected best-practice tip per day into this `README.md`.

The project uses Retrieval-Augmented Generation (RAG) over a committed SQLite vector index built from the [AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf).

<!-- TIP_OF_THE_DAY_START -->

## Tip of the day [Thursday, October 1, 2026]

### Turn incidents into system improvements

After every operational failure or near-miss, run a structured post-incident review that looks past the immediate symptom and traces the root causes and contributing factors. Use a blameless approach so the team can focus on what failed in the system, process, or automation—not on who made the mistake. Document the incident thoroughly, including logs, communications, and actions taken, then capture the lessons learned in a shared knowledge base. If testing did not catch the issue, add or improve tests, guardrails, or runbooks so the same failure is less likely to recur. Make sure follow-up actions have clear ownership and are tracked to completion.

**Why it matters:** Operational failures become valuable only when they change future behavior. A consistent review process helps teams reduce repeat incidents, improve resilience, and build a culture that learns from mistakes instead of hiding them.

<!-- TIP_OF_THE_DAY_END -->

## How it works

A scheduled GitHub Actions workflow runs `src/update_readme.py` once per day.

The script selects a topic from `src/topics.py`, then generates a new best-practice tip by using an AI agent with access to the local SQLite vector index in `storage/well_architected_index.sqlite`.

The agent searches the index, retrieves relevant source material, and writes one practical tip grounded in the retrieved material. The script then updates only the marked tip section in `README.md`, saves the tip as a dated Markdown file in `tips/`, and commits the change back to the repository.
