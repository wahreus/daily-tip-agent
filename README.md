# 🤖 Daily Tip Agent

An AI agent that posts one AWS Well-Architected best-practice tip per day into this `README.md`.

The project uses Retrieval-Augmented Generation (RAG) over a committed SQLite vector index built from the [AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf).

<!-- TIP_OF_THE_DAY_START -->

## Tip of the day [Friday, October 16, 2026]

### Make health visible before incidents escalate

Build a small set of dashboards that show your team’s key operational metrics in one place, and make them easy to access for both operators and leaders. Include the signals that define operational health for your services, not just infrastructure noise, so you can spot trends and prioritize improvement work. Pair those dashboards with alarms that notify the right people and can trigger incident workflows when thresholds are crossed. Add a simple status page that can be updated quickly during an event, including ownership, coordination details, and any user workarounds. Review the reports regularly so they reflect current KPIs and business needs, and use them to drive conversations about operational gaps. If you also surface AWS Health events, teams can distinguish internal issues from cloud-provider events faster.

**Why it matters:** Clear health visibility reduces manual reporting and speeds up incident detection and response. It also builds trust with stakeholders by showing current status and trends, not just after-action summaries.

<!-- TIP_OF_THE_DAY_END -->

## How it works

A scheduled GitHub Actions workflow runs `src/update_readme.py` once per day.

The script selects a topic from `src/topics.py`, then generates a new best-practice tip by using an AI agent with access to the local SQLite vector index in `storage/well_architected_index.sqlite`.

The agent searches the index, retrieves relevant source material, and writes one practical tip grounded in the retrieved material. The script then updates only the marked tip section in `README.md`, saves the tip as a dated Markdown file in `tips/`, and commits the change back to the repository.
