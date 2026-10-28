# 🤖 Daily Tip Agent

An AI agent that posts one AWS Well-Architected best-practice tip per day into this `README.md`.

The project uses Retrieval-Augmented Generation (RAG) over a committed SQLite vector index built from the [AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf).

<!-- TIP_OF_THE_DAY_START -->

## Tip of the day [Wednesday, October 28, 2026]

### Make improvement a recurring operating rhythm

Treat continuous improvement as a scheduled operational activity, not an ad hoc reaction after something breaks. Set aside regular time to review operations metrics, anomalies, and lessons learned with both engineers and stakeholders so you can prioritize the next improvements. Use feedback loops from incidents, customer signals, and automation outcomes to decide what to change, then track whether those changes actually improved performance or reliability. Keep the changes small and reversible so you can learn quickly without creating large new risks. Where possible, turn repeated manual work into safe automation with guardrails such as approvals, thresholds, and rate limits. This approach helps you steadily reduce toil while improving the workload over time.

**Why it matters:** A disciplined review-and-improve cycle prevents teams from drifting into reactive firefighting. It also makes it easier to connect operational work to business outcomes, so improvements get funded and sustained.

<!-- TIP_OF_THE_DAY_END -->

## How it works

A scheduled GitHub Actions workflow runs `src/update_readme.py` once per day.

The script selects a topic from `src/topics.py`, then generates a new best-practice tip by using an AI agent with access to the local SQLite vector index in `storage/well_architected_index.sqlite`.

The agent searches the index, retrieves relevant source material, and writes one practical tip grounded in the retrieved material. The script then updates only the marked tip section in `README.md`, saves the tip as a dated Markdown file in `tips/`, and commits the change back to the repository.
