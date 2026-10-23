# 🤖 Daily Tip Agent

An AI agent that posts one AWS Well-Architected best-practice tip per day into this `README.md`.

The project uses Retrieval-Augmented Generation (RAG) over a committed SQLite vector index built from the [AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf).

<!-- TIP_OF_THE_DAY_START -->

## Tip of the day [Friday, October 23, 2026]

### Design throttling for retries, load shedding for overload

Use throttling when callers can safely retry, and use load shedding or buffering when they cannot. Before setting limits, analyze the expected demand, rate of change, request size, and required response time so your controls match real traffic patterns. If you expect bursts, configure explicit rate limits and test them under load; don’t rely on default endpoint settings. For retry-capable clients, return clear signals that tell them to back off and try again later instead of letting the workload fail unpredictably. For non-retryable clients, absorb the spike with a queue or similar buffer so you can process requests later and keep the system stable. Make sure your design also accounts for duplicate requests and maximum concurrency on consumers so overload controls do not create new failure modes.

**Why it matters:** Proper throttling and load shedding smooth demand peaks, which helps keep supported requests flowing during spikes, retry storms, or flooding attacks. It also reduces the amount of provisioned capacity you need, lowering cost while improving resilience.

<!-- TIP_OF_THE_DAY_END -->

## How it works

A scheduled GitHub Actions workflow runs `src/update_readme.py` once per day.

The script selects a topic from `src/topics.py`, then generates a new best-practice tip by using an AI agent with access to the local SQLite vector index in `storage/well_architected_index.sqlite`.

The agent searches the index, retrieves relevant source material, and writes one practical tip grounded in the retrieved material. The script then updates only the marked tip section in `README.md`, saves the tip as a dated Markdown file in `tips/`, and commits the change back to the repository.
