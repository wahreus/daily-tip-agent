# 🤖 Daily Tip Agent

An AI agent that posts one AWS Well-Architected best-practice tip per day into this `README.md`.

The project uses Retrieval-Augmented Generation (RAG) over a committed SQLite vector index built from the [AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf).

<!-- TIP_OF_THE_DAY_START -->

## Tip of the day [Friday, November 20, 2026]

### Document the boundary, not just the control

Treat the shared responsibility model as an operating assumption, not a slide in a security deck. For every workload, explicitly map which security and compliance controls are handled by AWS and which are yours, then fold the customer-owned items into your threat model. Use that mapping to drive concrete guardrails such as IAM policies, SCPs, resource policies, and configuration controls that prevent non-compliant actions. Review the responsibility split again whenever you adopt a new AWS service or change your architecture, since the boundary can shift with service features. Finally, make sure your team knows where ownership lives so incidents and operational tasks are routed quickly to the right people.

**Why it matters:** Clear responsibility boundaries reduce missed controls, duplicate effort, and security gaps during design and operations. They also make it easier to prove compliance because you can show which mitigations are implemented by AWS and which are enforced in your own environment.

<!-- TIP_OF_THE_DAY_END -->

## How it works

A scheduled GitHub Actions workflow runs `src/update_readme.py` once per day.

The script selects a topic from `src/topics.py`, then generates a new best-practice tip by using an AI agent with access to the local SQLite vector index in `storage/well_architected_index.sqlite`.

The agent searches the index, retrieves relevant source material, and writes one practical tip grounded in the retrieved material. The script then updates only the marked tip section in `README.md`, saves the tip as a dated Markdown file in `tips/`, and commits the change back to the repository.
