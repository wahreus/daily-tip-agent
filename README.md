# 🤖 Daily Tip Agent

An AI agent that posts one AWS Well-Architected best-practice tip per day into this `README.md`.

The project uses Retrieval-Augmented Generation (RAG) over a committed SQLite vector index built from the [AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf).

<!-- TIP_OF_THE_DAY_START -->

## Tip of the day [Sunday, June 28, 2026]

### Standardize cost allocation tags early

Define a small, organization-wide tagging schema for cost allocation categories such as cost center, application, owner, team, and environment, and require those tags on every billable resource. Keep tag keys and allowed values consistent across accounts so your cost and usage data can be grouped reliably for reporting and chargeback. Use AWS Tag Policies in AWS Organizations to enforce the standard, and automate tag assignment at provisioning time so new resources do not slip through untagged. Review both tagged and untagged resources regularly, because incomplete tagging weakens cost attribution and makes spend accountability harder. If a resource cannot be tagged directly, map it into AWS Cost Categories so the spend still rolls up to the right internal entity.

**Why it matters:** Consistent cost allocation tags turn raw cloud spend into actionable financial and operational data. They help teams understand who is consuming what, improve budget ownership, and reduce waste from unmanaged or untracked resources.

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