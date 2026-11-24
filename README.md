# 🤖 Daily Tip Agent

An AI agent that posts one AWS Well-Architected best-practice tip per day into this `README.md`.

The project uses Retrieval-Augmented Generation (RAG) over a committed SQLite vector index built from the [AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf).

<!-- TIP_OF_THE_DAY_START -->

## Tip of the day [Tuesday, November 24, 2026]

### Classify first, then enforce controls

Start with a clear data classification scheme for the information your workloads process, including who owns the data, where it lives, and how sensitive it is. Define handling rules for each class, such as public, internal, confidential, or restricted, and make those rules drive your security controls. Apply resource tags to identify sensitive data and keep tag keys and values standardized through tag policies so teams classify data consistently. Then use automation to detect untagged or misclassified resources and to confirm protections like encryption, access controls, and auditing stay aligned with the data’s sensitivity. For highly sensitive data, separate workloads or accounts to create stronger isolation boundaries and reduce accidental overexposure.

**Why it matters:** Data classification is the foundation for choosing the right protection level instead of applying one-size-fits-all controls. It also helps you enforce least privilege, reduce human error, and spot gaps before sensitive data drifts out of compliance.

<!-- TIP_OF_THE_DAY_END -->

## How it works

A scheduled GitHub Actions workflow runs `src/update_readme.py` once per day.

The script selects a topic from `src/topics.py`, then generates a new best-practice tip by using an AI agent with access to the local SQLite vector index in `storage/well_architected_index.sqlite`.

The agent searches the index, retrieves relevant source material, and writes one practical tip grounded in the retrieved material. The script then updates only the marked tip section in `README.md`, saves the tip as a dated Markdown file in `tips/`, and commits the change back to the repository.
