# 🤖 Daily Tip Agent

An AI agent that posts one AWS Well-Architected best-practice tip per day into this `README.md`.

The project uses Retrieval-Augmented Generation (RAG) over a committed SQLite vector index built from the [AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf).

<!-- TIP_OF_THE_DAY_START -->

## Tip of the day [Sunday, July 26, 2026]

### Design for loose coupling and safe retries

In distributed systems, make component interactions resilient to latency and partial failure by keeping dependencies loosely coupled. Prefer asynchronous patterns like queues or event-driven flows when a synchronous hop would otherwise block the whole request path. If you must use mutating operations, make them idempotent so retries do not create duplicate side effects. Also, avoid tight shared-data dependencies that let one failing service cascade into others. Build in back pressure so a slow downstream component can signal the caller to slow down instead of overwhelming the system.

**Why it matters:** Loose coupling helps isolate failures and improves overall resilience when networks are unreliable or services become slow. Idempotency and back pressure make retries safer and reduce the chance that a transient issue turns into an outage or data corruption.

<!-- TIP_OF_THE_DAY_END -->

## How it works

A scheduled GitHub Actions workflow runs `src/update_readme.py` once per day.

The script selects a topic from `src/topics.py`, then generates a new best-practice tip by using an AI agent with access to the local SQLite vector index in `storage/well_architected_index.sqlite`.

The agent searches the index, retrieves relevant source material, and writes one practical tip grounded in the retrieved material. The script then updates only the marked tip section in `README.md`, saves the tip as a dated Markdown file in `tips/`, and commits the change back to the repository.
