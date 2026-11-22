# 🤖 Daily Tip Agent

An AI agent that posts one AWS Well-Architected best-practice tip per day into this `README.md`.

The project uses Retrieval-Augmented Generation (RAG) over a committed SQLite vector index built from the [AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf).

<!-- TIP_OF_THE_DAY_START -->

## Tip of the day [Sunday, November 22, 2026]

### Plan for growth, then isolate what should not talk

When designing network topology, start by sizing your VPC CIDR blocks for both current demand and future expansion, including enough space for subnets across Availability Zones. If you expect uncertain growth, choose larger address ranges up front so you avoid disruptive renumbering later. For multi-VPC environments, verify that connected networks use non-overlapping IP ranges and decide early whether you need a Transit Gateway or another multi-VPC connectivity pattern. Use separate subnets or attachments where it helps keep shared infrastructure tidy, and keep routing tables strict so only the networks that truly need to communicate can do so. If you have regulatory or workload-separation requirements, factor that into the topology before deployment rather than trying to bolt it on later.

**Why it matters:** Good topology planning reduces future rework, avoids IP conflicts, and makes it easier to scale without redesigning your network. Tight routing and intentional segmentation also improve fault isolation and help limit unintended east-west access between workloads.

<!-- TIP_OF_THE_DAY_END -->

## How it works

A scheduled GitHub Actions workflow runs `src/update_readme.py` once per day.

The script selects a topic from `src/topics.py`, then generates a new best-practice tip by using an AI agent with access to the local SQLite vector index in `storage/well_architected_index.sqlite`.

The agent searches the index, retrieves relevant source material, and writes one practical tip grounded in the retrieved material. The script then updates only the marked tip section in `README.md`, saves the tip as a dated Markdown file in `tips/`, and commits the change back to the repository.
