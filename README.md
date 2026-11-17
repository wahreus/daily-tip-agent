# 🤖 Daily Tip Agent

An AI agent that posts one AWS Well-Architected best-practice tip per day into this `README.md`.

The project uses Retrieval-Augmented Generation (RAG) over a committed SQLite vector index built from the [AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf).

<!-- TIP_OF_THE_DAY_START -->

## Tip of the day [Tuesday, November 17, 2026]

### Pick the region that meets both business and sustainability goals

When selecting an AWS Region, treat sustainability as a first-class requirement alongside compliance, latency, available services, and cost. Start by shortlisting regions that satisfy your data sovereignty and feature needs, then compare how each option affects performance, cost, and carbon footprint. Use AWS Regional Services Lists to verify that the services you depend on are available in the candidate regions. If your workload has clear user or network locality, prefer the region that reduces travel distance and network resource use rather than defaulting to the region closest to your team. For reporting and target-setting, align your region choice with the emissions method you use so your sustainability measurements stay consistent over time.

**Why it matters:** Region choice directly influences both operational efficiency and environmental impact. Choosing deliberately can lower latency and cost while also helping reduce carbon emissions, instead of optimizing one KPI at the expense of the others.

<!-- TIP_OF_THE_DAY_END -->

## How it works

A scheduled GitHub Actions workflow runs `src/update_readme.py` once per day.

The script selects a topic from `src/topics.py`, then generates a new best-practice tip by using an AI agent with access to the local SQLite vector index in `storage/well_architected_index.sqlite`.

The agent searches the index, retrieves relevant source material, and writes one practical tip grounded in the retrieved material. The script then updates only the marked tip section in `README.md`, saves the tip as a dated Markdown file in `tips/`, and commits the change back to the repository.
