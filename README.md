# 🤖 Daily Tip Agent

An AI agent that posts one AWS Well-Architected best-practice tip per day into this `README.md`.

The project uses Retrieval-Augmented Generation (RAG) over a committed SQLite vector index built from the [AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf).

<!-- TIP_OF_THE_DAY_START -->

## Tip of the day [Tue, June 30, 2026]

### Prefer short-lived access over stored keys

Use temporary credentials for both human and machine access to AWS whenever possible, and reserve long-term access keys only for the rare cases that truly require them. For workforce users, route access through a centralized identity provider and federation or AWS IAM Identity Center so users assume roles instead of receiving permanent keys. For workloads and automation, replace hard-coded or shared access keys with IAM roles so the credentials are short-lived and automatically rotated by AWS. This reduces the chance of secrets being leaked, reused, or left behind when people or systems change. If you still have any long-term credentials in use, treat them as a migration target and remove them as soon as a role-based or federated option is available.

**Why it matters:** Short-lived credentials dramatically reduce the blast radius of exposure because they expire quickly and are harder to abuse if discovered. They also simplify credential management by eliminating most manual storage, sharing, and rotation tasks that commonly lead to operational and security issues.

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