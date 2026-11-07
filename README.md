# 🤖 Daily Tip Agent

An AI agent that posts one AWS Well-Architected best-practice tip per day into this `README.md`.

The project uses Retrieval-Augmented Generation (RAG) over a committed SQLite vector index built from the [AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf).

<!-- TIP_OF_THE_DAY_START -->

## Tip of the day [Saturday, November 7, 2026]

### Minimize data movement at the source

Design your workload so shared data is accessed from a common storage layer instead of being copied to multiple places. Prefer object storage or shared file systems for data that many services or users need, and place data closer to where it is consumed. Before moving data across the network, reduce its size and convert it into a more efficient format so you are not paying to transfer unnecessary bytes. If your architecture regularly moves the same data between components, add caching or distribution layers to keep reads local. Also review whether any data transfer can be eliminated through service design, such as processing data in place rather than repeatedly shipping it around.

**Why it matters:** Less data movement reduces network usage, transfer cost, and the operational overhead of synchronizing copies. It can also improve performance by lowering latency and avoiding needless traffic between systems.

<!-- TIP_OF_THE_DAY_END -->

## How it works

A scheduled GitHub Actions workflow runs `src/update_readme.py` once per day.

The script selects a topic from `src/topics.py`, then generates a new best-practice tip by using an AI agent with access to the local SQLite vector index in `storage/well_architected_index.sqlite`.

The agent searches the index, retrieves relevant source material, and writes one practical tip grounded in the retrieved material. The script then updates only the marked tip section in `README.md`, saves the tip as a dated Markdown file in `tips/`, and commits the change back to the repository.
