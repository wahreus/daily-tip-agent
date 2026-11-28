# 🤖 Daily Tip Agent

An AI agent that posts one AWS Well-Architected best-practice tip per day into this `README.md`.

The project uses Retrieval-Augmented Generation (RAG) over a committed SQLite vector index built from the [AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf).

<!-- TIP_OF_THE_DAY_START -->

## Tip of the day [Saturday, November 28, 2026]

### Turn incidents into shared improvements

Make post-incident analysis a standard part of your operations, and treat near-misses the same way you treat outages. Capture the incident timeline, logs, communications, contributing factors, and the actions taken so you can see what actually happened, not just what was suspected. Focus on root cause and prevention rather than blame, and look for process gaps, missing guardrails, or tests that failed to catch the issue. After each review, convert the findings into concrete follow-up work such as runbook updates, new alerts, automation, or pre-deployment checks. Share the lessons learned across teams so the same failure mode is less likely to repeat elsewhere. Over time, these reviews become a feedback loop that steadily improves operational resilience.

**Why it matters:** Learning from failures is how you reduce repeat incidents and improve response quality. A blameless, structured review process helps teams identify systemic fixes, not just human error, and turns operational pain into lasting reliability gains.

<!-- TIP_OF_THE_DAY_END -->

## How it works

A scheduled GitHub Actions workflow runs `src/update_readme.py` once per day.

The script selects a topic from `src/topics.py`, then generates a new best-practice tip by using an AI agent with access to the local SQLite vector index in `storage/well_architected_index.sqlite`.

The agent searches the index, retrieves relevant source material, and writes one practical tip grounded in the retrieved material. The script then updates only the marked tip section in `README.md`, saves the tip as a dated Markdown file in `tips/`, and commits the change back to the repository.
