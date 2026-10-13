# 🤖 Daily Tip Agent

An AI agent that posts one AWS Well-Architected best-practice tip per day into this `README.md`.

The project uses Retrieval-Augmented Generation (RAG) over a committed SQLite vector index built from the [AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf).

<!-- TIP_OF_THE_DAY_START -->

## Tip of the day [Tuesday, October 13, 2026]

### Automate retention, tiering, and deletion

Treat data lifecycle management as an automated policy, not a manual cleanup task. Classify datasets by sensitivity, retention needs, and access patterns, then define rules for how long each type should stay in hot storage, when it should move to lower-cost tiers, and when it should be deleted. Use native lifecycle features where possible, such as S3 lifecycle policies, EBS snapshot automation, EFS lifecycle management, or ECR cleanup policies. Also make sure the process includes monitored, automated destruction for data that has outlived its business, legal, or regulatory purpose. Regularly review the policies and use configuration checks to catch resources that are missing lifecycle automation.

**Why it matters:** Well-defined lifecycle management improves compliance, reduces security risk, and lowers storage cost. It also keeps teams from relying on manual deletion or retaining data longer than necessary, which increases operational overhead and environmental impact.

<!-- TIP_OF_THE_DAY_END -->

## How it works

A scheduled GitHub Actions workflow runs `src/update_readme.py` once per day.

The script selects a topic from `src/topics.py`, then generates a new best-practice tip by using an AI agent with access to the local SQLite vector index in `storage/well_architected_index.sqlite`.

The agent searches the index, retrieves relevant source material, and writes one practical tip grounded in the retrieved material. The script then updates only the marked tip section in `README.md`, saves the tip as a dated Markdown file in `tips/`, and commits the change back to the repository.
