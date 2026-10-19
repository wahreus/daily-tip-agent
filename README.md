# 🤖 Daily Tip Agent

An AI agent that posts one AWS Well-Architected best-practice tip per day into this `README.md`.

The project uses Retrieval-Augmented Generation (RAG) over a committed SQLite vector index built from the [AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf).

<!-- TIP_OF_THE_DAY_START -->

## Tip of the day [Monday, October 19, 2026]

### Segment and inspect network traffic

Design your network in layers so internet-facing components are separated from internal systems like databases and admin services. Then enforce traffic flow between those layers with explicit controls such as security groups, route tables, and firewall rules. Add inspection points where traffic crosses boundaries so you can validate both allowed and denied flows against expected behavior, not just ports and protocols. For public endpoints, use edge protections like AWS WAF and AWS Shield, and consider AWS Network Firewall for deeper VPC-level inspection. Automate these controls through centralized policy management so new services inherit the same protection pattern by default.

**Why it matters:** Network threats often succeed by moving laterally after an initial foothold, so layered segmentation limits blast radius. Inspection and centralized enforcement also make it easier to detect abnormal traffic early and respond consistently across workloads.

<!-- TIP_OF_THE_DAY_END -->

## How it works

A scheduled GitHub Actions workflow runs `src/update_readme.py` once per day.

The script selects a topic from `src/topics.py`, then generates a new best-practice tip by using an AI agent with access to the local SQLite vector index in `storage/well_architected_index.sqlite`.

The agent searches the index, retrieves relevant source material, and writes one practical tip grounded in the retrieved material. The script then updates only the marked tip section in `README.md`, saves the tip as a dated Markdown file in `tips/`, and commits the change back to the repository.
