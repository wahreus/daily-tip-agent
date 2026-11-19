# 🤖 Daily Tip Agent

An AI agent that posts one AWS Well-Architected best-practice tip per day into this `README.md`.

The project uses Retrieval-Augmented Generation (RAG) over a committed SQLite vector index built from the [AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf).

<!-- TIP_OF_THE_DAY_START -->

## Tip of the day [Thu, November 19, 2026]

### Automate the cleanup of idle cloud resources

Make unused-resource cleanup a recurring operational task, not a one-time audit. Start by checking utilization data and rightsizing recommendations to find idle or underused components, especially in stable workloads. Then retire resources that are no longer needed, including EBS volumes, snapshots, Elastic IPs, AMIs, and stale Auto Scaling or Elastic Beanstalk infrastructure. For ephemeral environments, rely on utilization metrics and lifecycle policies to catch waste sooner. Before deleting anything, verify the resource is not still needed by another team or workload, and automate deletions where possible with tools like AWS Config, Systems Manager, or lifecycle rules.

**Why it matters:** Unused resources quietly drive up cost and can add operational clutter and risk. Regular cleanup keeps your environment lean, improves efficiency, and reduces the chance that forgotten assets become security or compliance issues.

<!-- TIP_OF_THE_DAY_END -->

## How it works

A scheduled GitHub Actions workflow runs `src/update_readme.py` once per day.

The script selects a topic from `src/topics.py`, then generates a new best-practice tip by using an AI agent with access to the local SQLite vector index in `storage/well_architected_index.sqlite`.

The agent searches the index, retrieves relevant source material, and writes one practical tip grounded in the retrieved material. The script then updates only the marked tip section in `README.md`, saves the tip as a dated Markdown file in `tips/`, and commits the change back to the repository.
