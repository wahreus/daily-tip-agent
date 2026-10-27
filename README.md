# 🤖 Daily Tip Agent

An AI agent that posts one AWS Well-Architected best-practice tip per day into this `README.md`.

The project uses Retrieval-Augmented Generation (RAG) over a committed SQLite vector index built from the [AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf).

<!-- TIP_OF_THE_DAY_START -->

## Tip of the day [Tuesday, October 27, 2026]

### Automate classification and enforce it with tags

Define a simple data classification scheme, such as public, internal, confidential, and restricted, and apply it consistently across your workloads. Use automation to identify sensitive data and reduce the risk of manual misclassification as data volumes grow. Where supported, encode the classification in resource tags like `Classification=PHI` or `Sensitivity=High`, but avoid putting sensitive details in the tag values themselves. Pair those tags with monitoring and governance so you can detect drift, such as encryption settings changing or untagged data appearing in your environment. Periodically audit for unclassified data and update tags and handling rules as data moves or changes over time.

**Why it matters:** Clear classification helps you apply the right controls for access, encryption, retention, and monitoring without guessing. It also reduces human error and makes compliance and incident response much easier because you can quickly see which data needs the strongest protections.

<!-- TIP_OF_THE_DAY_END -->

## How it works

A scheduled GitHub Actions workflow runs `src/update_readme.py` once per day.

The script selects a topic from `src/topics.py`, then generates a new best-practice tip by using an AI agent with access to the local SQLite vector index in `storage/well_architected_index.sqlite`.

The agent searches the index, retrieves relevant source material, and writes one practical tip grounded in the retrieved material. The script then updates only the marked tip section in `README.md`, saves the tip as a dated Markdown file in `tips/`, and commits the change back to the repository.
