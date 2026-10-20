# 🤖 Daily Tip Agent

An AI agent that posts one AWS Well-Architected best-practice tip per day into this `README.md`.

The project uses Retrieval-Augmented Generation (RAG) over a committed SQLite vector index built from the [AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf).

<!-- TIP_OF_THE_DAY_START -->

## Tip of the day [Tue, October 20, 2026]

### Pre-assign incident roles and practice the plan

Build your security incident response around a documented plan with clear roles, communication paths, and decision points before an event happens. Make sure the plan covers who is responsible, accountable, consulted, and informed, so your team can move fast without confusion during containment and recovery. Keep logging and observability in place so responders can quickly identify what changed, isolate affected systems, and restore service to a known good state. Pre-provision the tooling and access needed for investigations, including break-glass access and automated response actions where appropriate. Then run regular game days to validate that the plan, permissions, and technical controls still work under pressure.

**Why it matters:** In an incident, speed and clarity reduce impact. A well-practiced plan helps your team contain the issue faster, preserve evidence, and recover safely instead of improvising under stress.

<!-- TIP_OF_THE_DAY_END -->

## How it works

A scheduled GitHub Actions workflow runs `src/update_readme.py` once per day.

The script selects a topic from `src/topics.py`, then generates a new best-practice tip by using an AI agent with access to the local SQLite vector index in `storage/well_architected_index.sqlite`.

The agent searches the index, retrieves relevant source material, and writes one practical tip grounded in the retrieved material. The script then updates only the marked tip section in `README.md`, saves the tip as a dated Markdown file in `tips/`, and commits the change back to the repository.
