# 🤖 Daily Tip Agent

An AI agent that posts one AWS Well-Architected best-practice tip per day into this `README.md`.

The project uses Retrieval-Augmented Generation (RAG) over a committed SQLite vector index built from the [AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf).

<!-- TIP_OF_THE_DAY_START -->

## Tip of the day [Friday, September 18, 2026]

### Tighten IAM with roles, not one-off user permissions

Grant each identity only the actions it needs on the specific resources and conditions required for the task. Prefer IAM roles and groups over attaching permissions directly to individual users, because that makes access easier to manage and revoke when responsibilities change. Use resource-level scoping and policy conditions so a policy cannot be used more broadly than intended. Review permissions regularly and remove anything that is no longer needed, using tools like IAM Access Analyzer or AWS Config to spot overbroad access. For elevated access, require temporary, approved permissions instead of leaving powerful rights attached all the time.

**Why it matters:** Least privilege reduces the blast radius if credentials are compromised or a policy is misused. It also improves auditability, since your access model stays closer to actual job functions and project boundaries.

<!-- TIP_OF_THE_DAY_END -->

## How it works

A scheduled GitHub Actions workflow runs `src/update_readme.py` once per day.

The script selects a topic from `src/topics.py`, then generates a new best-practice tip by using an AI agent with access to the local SQLite vector index in `storage/well_architected_index.sqlite`.

The agent searches the index, retrieves relevant source material, and writes one practical tip grounded in the retrieved material. The script then updates only the marked tip section in `README.md`, saves the tip as a dated Markdown file in `tips/`, and commits the change back to the repository.
