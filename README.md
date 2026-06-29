# 🤖 Daily Tip Agent

An AI agent that posts one AWS Well-Architected best-practice tip per day into this `README.md`.

The project uses Retrieval-Augmented Generation (RAG) over a committed SQLite vector index built from the [AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf).

<!-- TIP_OF_THE_DAY_START -->

## Tip of the day [Mon, June 29, 2026]

### Prefer asynchronous contracts for non-blocking dependencies

When two services do not need an immediate response, switch from direct point-to-point calls to asynchronous messaging. Use events, queues, or topics so the producer only needs to know that the request was accepted, not how or when it will be processed. Keep interfaces versioned and published so consumers depend on a stable contract instead of an implementation detail. Avoid sharing databases between services, because that can quietly reintroduce tight coupling and make scaling or failure isolation harder. If a downstream component can’t keep up, apply back pressure, throttle intake, or fail fast rather than letting queues grow without control.

**Why it matters:** Loose coupling reduces the blast radius of failures and lets teams change, deploy, and scale services independently. It also improves resilience because one component can degrade or fail without taking down the whole workflow.

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