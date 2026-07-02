# 🤖 Daily Tip Agent

An AI agent that posts one AWS Well-Architected best-practice tip per day into this `README.md`.

The project uses Retrieval-Augmented Generation (RAG) over a committed SQLite vector index built from the [AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf).

<!-- TIP_OF_THE_DAY_START -->

## Tip of the day [Thu, July 2, 2026]

### Make sustainability reviews a recurring engineering habit

Treat sustainability improvement reviews as a regular cadence, not a one-time design activity. Set up a process and schedule to evaluate new features, instance types, and architecture changes that could reduce resource usage or improve measurement. Before promoting changes to production, test them with low-cost methods and validate that the expected efficiency gains are real. Keep an inventory of the workload components that need updates so you can spot stale areas that block small improvements. If your release process makes minor efficiency changes hard to ship, simplify it so sustainability improvements can land continuously.  

**Why it matters:** Regular reviews help you keep pace with cloud features that can lower energy use and improve efficiency. They also prevent workloads from going stale, where small but valuable sustainability gains are missed because no process exists to adopt them.

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