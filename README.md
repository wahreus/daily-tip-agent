# 🤖 Daily Tip Agent

An AI agent that posts one AWS Well-Architected best-practice tip per day into this `README.md`.

The project uses Retrieval-Augmented Generation (RAG) over a committed SQLite vector index built from the [AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf).

<!-- TIP_OF_THE_DAY_START -->

## Tip of the day [Sunday, November 8, 2026]

### Right-size hardware from workload data, not guesswork

Start by collecting concrete workload requirements such as CPU cores, memory, storage type and size, and network bandwidth. Use that data to choose the instance family and size that best matches the workload instead of defaulting to a larger general-purpose option. For variable demand, use attribute-based instance selection and Auto Scaling so the fleet can adapt as needs change without overprovisioning. If the workload is stable, review utilization metrics and rightsizing recommendations to find smaller or better-fit instances. For specialized workloads like ML inference, consider purpose-built hardware that is designed for that task rather than forcing the workload onto generic compute. This approach helps you balance performance and cost while reducing wasted capacity.

**Why it matters:** Efficient hardware selection improves both cost efficiency and performance by matching resources to actual demand. It also makes scaling and operations easier because your fleet is sized around measured usage rather than estimates.

<!-- TIP_OF_THE_DAY_END -->

## How it works

A scheduled GitHub Actions workflow runs `src/update_readme.py` once per day.

The script selects a topic from `src/topics.py`, then generates a new best-practice tip by using an AI agent with access to the local SQLite vector index in `storage/well_architected_index.sqlite`.

The agent searches the index, retrieves relevant source material, and writes one practical tip grounded in the retrieved material. The script then updates only the marked tip section in `README.md`, saves the tip as a dated Markdown file in `tips/`, and commits the change back to the repository.
