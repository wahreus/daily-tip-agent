# 🤖 Daily Tip Agent

An AI agent that posts one AWS Well-Architected best-practice tip per day into this `README.md`.

The project uses Retrieval-Augmented Generation (RAG) over a committed SQLite vector index built from the [AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf).

<!-- TIP_OF_THE_DAY_START -->

## Tip of the day [Wednesday, November 4, 2026]

### Pick the region that balances carbon, compliance, and latency

When choosing an AWS Region, treat sustainability as one of the core decision factors alongside business requirements like compliance, latency, available services, and cost. Start by shortlisting Regions that meet your data sovereignty and feature needs, then compare their sustainability fit rather than defaulting to the nearest or cheapest option. If you track emissions, align the Region choice with the carbon accounting method your organization uses so your reporting stays consistent year over year. For global workloads, consider whether placing resources closer to users can reduce latency and unnecessary data movement while still meeting sustainability goals. This approach helps you avoid optimizing one KPI at the expense of another.

**Why it matters:** Region choice directly affects performance, cost, and carbon footprint, so it has an outsized impact on the sustainability profile of a workload. Making the decision explicitly and consistently helps teams reduce emissions without creating compliance or user-experience tradeoffs.

<!-- TIP_OF_THE_DAY_END -->

## How it works

A scheduled GitHub Actions workflow runs `src/update_readme.py` once per day.

The script selects a topic from `src/topics.py`, then generates a new best-practice tip by using an AI agent with access to the local SQLite vector index in `storage/well_architected_index.sqlite`.

The agent searches the index, retrieves relevant source material, and writes one practical tip grounded in the retrieved material. The script then updates only the marked tip section in `README.md`, saves the tip as a dated Markdown file in `tips/`, and commits the change back to the repository.
