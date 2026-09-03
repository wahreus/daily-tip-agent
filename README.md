# 🤖 Daily Tip Agent

An AI agent that posts one AWS Well-Architected best-practice tip per day into this `README.md`.

The project uses Retrieval-Augmented Generation (RAG) over a committed SQLite vector index built from the [AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf).

<!-- TIP_OF_THE_DAY_START -->

## Tip of the day [Thursday, September 3, 2026]

### Make retries safe, bounded, and idempotent

In distributed systems, assume network calls can fail, duplicate, or arrive late, and design your interactions accordingly. Use retries only where the operation is idempotent or otherwise safe to repeat, and prefer SDK retry behavior with exponential backoff and jitter instead of rolling your own. Set explicit timeouts and maximum retry limits so one dependency cannot consume all client resources or create a retry storm. Test retry scenarios deliberately, including failure modes that should not be retried, such as permission or configuration errors. For mutating operations, confirm the backend can tolerate duplicate requests before enabling automatic retries.

**Why it matters:** This reduces cascading failures and keeps transient issues from turning into outages. It also protects both your workload and the downstream service from unnecessary load during partial failures.

<!-- TIP_OF_THE_DAY_END -->

## How it works

A scheduled GitHub Actions workflow runs `src/update_readme.py` once per day.

The script selects a topic from `src/topics.py`, then generates a new best-practice tip by using an AI agent with access to the local SQLite vector index in `storage/well_architected_index.sqlite`.

The agent searches the index, retrieves relevant source material, and writes one practical tip grounded in the retrieved material. The script then updates only the marked tip section in `README.md`, saves the tip as a dated Markdown file in `tips/`, and commits the change back to the repository.
