# 🤖 Daily Tip Agent

An AI agent that posts one AWS Well-Architected best-practice tip per day into this `README.md`.

The project uses Retrieval-Augmented Generation (RAG) over a committed SQLite vector index built from the [AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf).

<!-- TIP_OF_THE_DAY_START -->

## Tip of the day [Sunday, October 18, 2026]

### Make ORRs a repeatable launch gate

Treat operational readiness reviews as a standard checklist-based gate before launch, not a one-time ceremony. Bring together security, operations, and development stakeholders, and keep the first version focused on a manageable set of requirements. Include items that reflect how you actually operate the workload, such as architectural recommendations, operational processes, event management, and release quality. Use discoveries from incidents and postmortems to evolve the checklist so it prevents repeat failures instead of just confirming good intentions. If a review surfaces a gap without a mitigation, add it to the backlog and close it before launch. Over time, use the same ORR pattern across workloads so teams can self-serve the review and compare readiness consistently.

**Why it matters:** ORRs help you catch operational gaps before they become production incidents. A consistent review process also improves shared accountability across engineering, operations, and security, which lowers launch risk and makes support handoffs smoother.

<!-- TIP_OF_THE_DAY_END -->

## How it works

A scheduled GitHub Actions workflow runs `src/update_readme.py` once per day.

The script selects a topic from `src/topics.py`, then generates a new best-practice tip by using an AI agent with access to the local SQLite vector index in `storage/well_architected_index.sqlite`.

The agent searches the index, retrieves relevant source material, and writes one practical tip grounded in the retrieved material. The script then updates only the marked tip section in `README.md`, saves the tip as a dated Markdown file in `tips/`, and commits the change back to the repository.
