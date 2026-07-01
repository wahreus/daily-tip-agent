# 🤖 Daily Tip Agent

An AI agent that posts one AWS Well-Architected best-practice tip per day into this `README.md`.

The project uses Retrieval-Augmented Generation (RAG) over a committed SQLite vector index built from the [AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf).

<!-- TIP_OF_THE_DAY_START -->

## Tip of the day [Wednesday, July 1, 2026]

### Automate quota monitoring before growth becomes an outage

Treat service quotas like any other operational dependency: continuously monitor usage, alert when you approach thresholds, and have a documented path for requesting increases. Use AWS Service Quotas, Trusted Advisor, or your own automation to track limits across accounts and Regions instead of relying on spreadsheets or occasional manual checks. Set alerts early enough that soft quota increases can be approved before traffic growth hits the limit, and remember that some requests may take time to process. Where the workload is business-critical, you can automate quota increase requests, but test that automation carefully to avoid runaway feedback loops. Also review hard limits and service-specific constraints so you don’t assume every quota can be raised.

**Why it matters:** Quota exhaustion can cause throttling, failed deployments, or even a production outage when demand spikes. Proactive monitoring and controlled automation help keep workloads stable and resilient as they grow.

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