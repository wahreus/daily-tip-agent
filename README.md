# 🤖 Daily Tip Agent

An AI agent that posts one AWS Well-Architected best-practice tip per day into this `README.md`.

The project uses Retrieval-Augmented Generation (RAG) over a committed SQLite vector index built from the [AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf).

<!-- TIP_OF_THE_DAY_START -->

## Tip of the day [Wednesday, June 24, 2026]

### Centralize and enrich security signals

Make sure your service, application, and cloud control-plane logs are captured in standardized locations so investigators can reliably search them later. Feed key findings and metrics into a common security pipeline rather than leaving them scattered across teams and accounts. Correlate related alerts and enrich them with context such as resource ownership, configuration state, and recent API activity before escalating. This reduces manual triage and helps your team distinguish a real incident from routine noise. When possible, automate the first response for common, repetitive events so analysts can focus on unusual or high-impact cases.

**Why it matters:** Good detection is not just about collecting logs; it is about turning them into actionable signals quickly. Centralization, correlation, and enrichment shorten investigation time and improve severity assessment, which helps you respond before a security event grows into an incident.

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