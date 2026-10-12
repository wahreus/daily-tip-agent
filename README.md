# 🤖 Daily Tip Agent

An AI agent that posts one AWS Well-Architected best-practice tip per day into this `README.md`.

The project uses Retrieval-Augmented Generation (RAG) over a committed SQLite vector index built from the [AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf).

<!-- TIP_OF_THE_DAY_START -->

## Tip of the day [Monday, October 12, 2026]

### Store secrets in a managed vault and automate rotation

Use a purpose-built secrets manager to store API keys, passwords, and tokens instead of embedding them in source code, config files, or long-lived environment values. Keep secrets encrypted at rest and in transit, and grant access through fine-grained IAM roles rather than broad human access. Where possible, enable automated rotation so credential changes happen centrally without app teams manually updating every dependent service. Add auditing and monitoring for secret reads, writes, rotation events, and deletion attempts so you can spot unexpected usage quickly. For workloads that retrieve secrets frequently, use client-side caching to reduce latency and lower API costs while still keeping the source of truth in the managed service.

**Why it matters:** Secrets exposure is a high-risk failure mode because leaked credentials can be reused quickly and widely. Centralized storage, rotation, and auditability reduce the chance of accidental disclosure and make compromise easier to detect and contain.

<!-- TIP_OF_THE_DAY_END -->

## How it works

A scheduled GitHub Actions workflow runs `src/update_readme.py` once per day.

The script selects a topic from `src/topics.py`, then generates a new best-practice tip by using an AI agent with access to the local SQLite vector index in `storage/well_architected_index.sqlite`.

The agent searches the index, retrieves relevant source material, and writes one practical tip grounded in the retrieved material. The script then updates only the marked tip section in `README.md`, saves the tip as a dated Markdown file in `tips/`, and commits the change back to the repository.
