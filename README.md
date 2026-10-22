# 🤖 Daily Tip Agent

An AI agent that posts one AWS Well-Architected best-practice tip per day into this `README.md`.

The project uses Retrieval-Augmented Generation (RAG) over a committed SQLite vector index built from the [AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf).

<!-- TIP_OF_THE_DAY_START -->

## Tip of the day [Thursday, October 22, 2026]

### Use separate AWS accounts as your isolation boundary

Organize AWS workloads into multiple accounts so production, development, test, and unrelated applications are separated by default. AWS Well-Architected recommends account-level separation because it creates a strong boundary for security, billing, and access, and it reduces the blast radius if something is misconfigured or compromised. Design your organizational unit hierarchy so guardrails can be applied consistently and inherited by member accounts. Keep workload resources only in member accounts, not in the management account, and make the account structure reflect how your teams own costs and operations. Avoid putting workloads with different sensitivity levels into the same account, even if they are technically related. A clean multi-account structure also makes it easier to centralize governance while still allowing teams to move quickly.

**Why it matters:** Good account structure improves security isolation and makes policy enforcement much simpler at scale. It also helps with cost allocation and operational clarity, which reduces risk as your AWS footprint grows.

<!-- TIP_OF_THE_DAY_END -->

## How it works

A scheduled GitHub Actions workflow runs `src/update_readme.py` once per day.

The script selects a topic from `src/topics.py`, then generates a new best-practice tip by using an AI agent with access to the local SQLite vector index in `storage/well_architected_index.sqlite`.

The agent searches the index, retrieves relevant source material, and writes one practical tip grounded in the retrieved material. The script then updates only the marked tip section in `README.md`, saves the tip as a dated Markdown file in `tips/`, and commits the change back to the repository.
