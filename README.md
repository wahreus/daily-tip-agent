# 🤖 Daily Tip Agent

An AI agent that posts one AWS Well-Architected best-practice tip per day into this `README.md`.

The project uses Retrieval-Augmented Generation (RAG) over a committed SQLite vector index built from the [AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf).

<!-- TIP_OF_THE_DAY_START -->

## Tip of the day [Sunday, September 20, 2026]

### Keep data close to where it is used

Design your workload to avoid moving large datasets farther than necessary. Use shared file systems or object storage for common data, and place frequently accessed data in the same Region or Availability Zone as the services that consume it. Before sending data over the network, reduce its size and choose formats that are efficient to transfer and process. For content delivered to end users, put a CDN or edge service in front so requests do not repeatedly pull the same data from your origin. In hybrid setups, prefer direct private connectivity and avoid unnecessary cross-Region transfers unless the architecture truly needs them.

**Why it matters:** Less data movement usually means lower network cost, lower latency, and fewer bottlenecks between components. It also reduces operational and environmental overhead by cutting the amount of traffic your systems need to push around.

<!-- TIP_OF_THE_DAY_END -->

## How it works

A scheduled GitHub Actions workflow runs `src/update_readme.py` once per day.

The script selects a topic from `src/topics.py`, then generates a new best-practice tip by using an AI agent with access to the local SQLite vector index in `storage/well_architected_index.sqlite`.

The agent searches the index, retrieves relevant source material, and writes one practical tip grounded in the retrieved material. The script then updates only the marked tip section in `README.md`, saves the tip as a dated Markdown file in `tips/`, and commits the change back to the repository.
