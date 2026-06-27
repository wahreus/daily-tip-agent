# 🤖 Daily Tip Agent

An AI agent that posts one AWS Well-Architected best-practice tip per day into this `README.md`.

The project uses Retrieval-Augmented Generation (RAG) over a committed SQLite vector index built from the [AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf).

<!-- TIP_OF_THE_DAY_START -->

## Tip of the day [Saturday, June 27, 2026]

### Build escalation paths that trigger the right responders fast

For event response, define clear escalation paths before an incident happens so alarms can route directly to the right on-call people or contacts. Use CloudWatch alarms or EventBridge events to create incidents in AWS Systems Manager Incident Manager, then map those incidents to escalation plans and on-call schedules. Make sure each escalation path states when to escalate, who owns each step, and what actions are pre-approved to avoid delays during high-severity events. Pair this with runbooks so responders have immediate, consistent next steps instead of inventing a process under pressure. Keep permissions and tools ready for the people in the schedule so they can act without waiting for access changes.

**Why it matters:** Clear escalation reduces time to engage the right team and shortens mean time to resolution. It also prevents confusion during outages by removing guesswork about ownership, communication, and response actions.

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