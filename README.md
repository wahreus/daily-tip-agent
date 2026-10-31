# 🤖 Daily Tip Agent

An AI agent that posts one AWS Well-Architected best-practice tip per day into this `README.md`.

The project uses Retrieval-Augmented Generation (RAG) over a committed SQLite vector index built from the [AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf).

<!-- TIP_OF_THE_DAY_START -->

## Tip of the day [Saturday, October 31, 2026]

### Design for fast, automated horizontal scaling

Treat horizontal scaling as a built-in behavior, not an emergency action. Keep application nodes stateless where possible so new instances or containers can be added without migration work or session surprises. Use load balancing to spread requests across targets, and pair it with autoscaling policies that react to demand rather than manual intervention. Choose a scaling signal that reflects real user load, such as request latency, throughput, or CPU, and test both scale-out and scale-in behavior under load. Also make sure your system can shrink back down after spikes so you do not pay for unused capacity. If your workload has predictable patterns, combine demand-based scaling with scheduled or predictive policies to stay ahead of growth.

**Why it matters:** Horizontal scaling only helps if the workload can expand and contract cleanly. Automated scale-out protects performance during traffic spikes, while scale-in avoids overprovisioning and unnecessary cost.

<!-- TIP_OF_THE_DAY_END -->

## How it works

A scheduled GitHub Actions workflow runs `src/update_readme.py` once per day.

The script selects a topic from `src/topics.py`, then generates a new best-practice tip by using an AI agent with access to the local SQLite vector index in `storage/well_architected_index.sqlite`.

The agent searches the index, retrieves relevant source material, and writes one practical tip grounded in the retrieved material. The script then updates only the marked tip section in `README.md`, saves the tip as a dated Markdown file in `tips/`, and commits the change back to the repository.
