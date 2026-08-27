# 🤖 Daily Tip Agent

An AI agent that posts one AWS Well-Architected best-practice tip per day into this `README.md`.

The project uses Retrieval-Augmented Generation (RAG) over a committed SQLite vector index built from the [AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf).

<!-- TIP_OF_THE_DAY_START -->

## Tip of the day [Thursday, August 27, 2026]

### Make improvement a scheduled operational habit

Treat continuous operational improvement as a recurring part of your delivery process, not an occasional cleanup task. Set aside dedicated time each cycle to review operations metrics, post-incident findings, and feedback from both automated signals and stakeholders. Use that input to prioritize a small set of concrete improvements, then implement them and measure whether the change actually moved the outcome you wanted. Keep the loop closed by documenting lessons learned and sharing them with the teams that can act on them. If an improvement does not deliver the expected result, try an alternative approach rather than leaving the issue open-ended.

**Why it matters:** This keeps operational excellence from becoming aspirational and makes it repeatable. Regular feedback loops help you catch recurring issues early, validate fixes, and steadily reduce risk and toil over time.

<!-- TIP_OF_THE_DAY_END -->

## How it works

A scheduled GitHub Actions workflow runs `src/update_readme.py` once per day.

The script selects a topic from `src/topics.py`, then generates a new best-practice tip by using an AI agent with access to the local SQLite vector index in `storage/well_architected_index.sqlite`.

The agent searches the index, retrieves relevant source material, and writes one practical tip grounded in the retrieved material. The script then updates only the marked tip section in `README.md`, saves the tip as a dated Markdown file in `tips/`, and commits the change back to the repository.
