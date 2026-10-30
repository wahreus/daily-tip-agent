# 🤖 Daily Tip Agent

An AI agent that posts one AWS Well-Architected best-practice tip per day into this `README.md`.

The project uses Retrieval-Augmented Generation (RAG) over a committed SQLite vector index built from the [AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf).

<!-- TIP_OF_THE_DAY_START -->

## Tip of the day [Friday, October 30, 2026]

### Prefer hub-and-spoke over mesh

When planning network topology, favor a hub-and-spoke model instead of building many-to-many connections between every VPC and environment. A hub such as AWS Transit Gateway makes it easier to centralize routing, control which networks can talk to each other, and avoid accidental east-west reachability. Design route tables so only the required paths exist, and omit routes between workloads that should remain isolated. As part of the plan, verify that connected networks use non-overlapping CIDR ranges and size subnets with future growth and Availability Zone expansion in mind. If you need segmentation for compliance or different trust levels, use separate VPCs and subnets rather than relying on an overly complex mesh.

**Why it matters:** Hub-and-spoke topologies reduce operational complexity and make connectivity policy easier to audit and change safely. They also help prevent IP conflicts and future rework as your environment grows across VPCs, on-premises links, and multiple Availability Zones.

<!-- TIP_OF_THE_DAY_END -->

## How it works

A scheduled GitHub Actions workflow runs `src/update_readme.py` once per day.

The script selects a topic from `src/topics.py`, then generates a new best-practice tip by using an AI agent with access to the local SQLite vector index in `storage/well_architected_index.sqlite`.

The agent searches the index, retrieves relevant source material, and writes one practical tip grounded in the retrieved material. The script then updates only the marked tip section in `README.md`, saves the tip as a dated Markdown file in `tips/`, and commits the change back to the repository.
