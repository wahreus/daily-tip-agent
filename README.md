# 🤖 Daily Tip Agent

An AI agent that posts one AWS Well-Architected best-practice tip per day into this `README.md`.

The project uses Retrieval-Augmented Generation (RAG) over a committed SQLite vector index built from the [AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf).

<!-- TIP_OF_THE_DAY_START -->

## Tip of the day [Tue, July 7, 2026]

### Turn incidents into durable fixes

After a customer-impacting event or near-miss, run a structured post-incident review that looks past the immediate trigger to the underlying process, tooling, and automation gaps. Capture what happened, how it was detected, what worked, and what did not, then keep digging until you identify root causes and contributing factors. Avoid stopping at “human error”; look for missing safeguards, weak tests, unclear procedures, or alerting gaps that allowed the failure to happen. Add corrective actions that reduce the chance of recurrence, such as new tests, guardrails, runbooks, or automation. Store the lessons learned in a shared knowledge base so future changes and incident response improve over time. Treat near-misses the same way you would outages, because they often expose the same failure modes before customers feel them.

**Why it matters:** Operational failures only become valuable if they change how you build and run systems. A blameless, repeatable review process helps teams learn faster, prevent repeat incidents, and strengthen reliability without creating fear or finger-pointing.

<!-- TIP_OF_THE_DAY_END -->

## How it works

A scheduled GitHub Actions workflow runs `src/update_readme.py` once per day.

The script selects a topic from `src/topics.py`, then generates a new best-practice tip by using an AI agent with access to the local SQLite vector index in `storage/well_architected_index.sqlite`.

The agent searches the index, retrieves relevant source material, and writes one practical tip grounded in the retrieved material. The script then updates only the marked tip section in `README.md`, saves the tip as a dated Markdown file in `tips/`, and commits the change back to the repository.
