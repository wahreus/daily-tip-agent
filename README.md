# 🤖 Daily Tip Agent

An AI agent that posts one AWS Well-Architected best-practice tip per day into this `README.md`.

The project uses Retrieval-Augmented Generation (RAG) over a committed SQLite vector index built from the [AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf).

<!-- TIP_OF_THE_DAY_START -->

## Tip of the day [Sunday, July 5, 2026]

### Define ownership and escalation before the alert fires

For event response, make sure every actionable alert maps to a specific owner, a runbook or playbook, and a clear escalation path. Use on-call schedules and escalation plans so CloudWatch or other alerts can route incidents to the right responders immediately, instead of relying on ad hoc triage. Prioritize response based on business and customer impact, and pre-identify who has the authority to approve decisions when an incident could affect service or risk. Keep runbooks for well-understood events and playbooks for investigation and resolution so responders can act consistently under pressure. This reduces confusion, speeds up response, and helps ensure that important events do not get lost in alert noise.

**Why it matters:** Clear ownership and escalation cut mean time to investigate and resolve incidents, which improves reliability during both planned and unplanned events. They also make responses more uniform and scalable, so the team can handle incidents without scrambling for the right people or decisions.

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