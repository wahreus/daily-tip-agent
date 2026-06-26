# 🤖 Daily Tip Agent

An AI agent that posts one AWS Well-Architected best-practice tip per day into this `README.md`.

The project uses Retrieval-Augmented Generation (RAG) over a committed SQLite vector index built from the [AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf).

<!-- TIP_OF_THE_DAY_START -->

## Tip of the day [Friday, June 26, 2026]

### Scale to the shape of demand

Treat capacity as something that should follow workload patterns, not a fixed number you set once. Use demand-based scaling for unpredictable spikes and time-based scaling for traffic you can forecast, so you can add capacity quickly when needed and remove it when demand drops. If your application has bursts, place a queue or buffer in front of the work to smooth short-lived peaks and avoid overprovisioning. Make sure your scaling policy considers how long it takes to provision new resources and tests the workload’s ability to recover from failures as capacity changes. After a scaling event, verify that excess capacity is removed promptly so you do not keep paying for resources you no longer need.

**Why it matters:** Matching supply to demand reduces waste while protecting performance during spikes. It also lowers the risk of manual scaling mistakes and keeps your architecture elastic enough to respond to real usage patterns.

<!-- TIP_OF_THE_DAY_END -->

## How it works

A scheduled GitHub Actions workflow runs `src/update_readme.py` once per day.

The script selects a topic from `src/topics.py`, then generates a new best-practice tip by using an AI agent with access to the local SQLite vector index in `storage/well_architected_index.sqlite`.

The agent searches the index, retrieves relevant source material, and writes one practical tip grounded in the retrieved material. The script then updates only the marked tip section in `README.md`, saves the tip as a dated Markdown file in `tips/`, and commits the change back to the repository.

## GitHub Actions

The workflow is defined in:

```text
.github/workflows/daily-tip.yml
```

It runs daily and can also be triggered manually from the GitHub Actions tab.