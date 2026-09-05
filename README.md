# 🤖 Daily Tip Agent

An AI agent that posts one AWS Well-Architected best-practice tip per day into this `README.md`.

The project uses Retrieval-Augmented Generation (RAG) over a committed SQLite vector index built from the [AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf).

<!-- TIP_OF_THE_DAY_START -->

## Tip of the day [Saturday, September 5, 2026]

### Make change rollback-ready

Treat every production change as something you may need to reverse quickly. Before deployment, document a rollback or fix-forward plan, test it in a pre-production environment, and make sure the same deployment steps, security controls, and validation checks are used as in production. Favor frequent, small, reversible changes so failures are easier to isolate and recover from. Automate test environments and verification where possible, including functional, integration, load, and health checks. Keep change policies clear so teams know when a change can be preauthorized and when a rollback is required.

**Why it matters:** Good change management reduces the blast radius of failures and makes recovery faster when something goes wrong. It also helps keep changes compliant with governance requirements instead of turning production updates into ad hoc work.

<!-- TIP_OF_THE_DAY_END -->

## How it works

A scheduled GitHub Actions workflow runs `src/update_readme.py` once per day.

The script selects a topic from `src/topics.py`, then generates a new best-practice tip by using an AI agent with access to the local SQLite vector index in `storage/well_architected_index.sqlite`.

The agent searches the index, retrieves relevant source material, and writes one practical tip grounded in the retrieved material. The script then updates only the marked tip section in `README.md`, saves the tip as a dated Markdown file in `tips/`, and commits the change back to the repository.
