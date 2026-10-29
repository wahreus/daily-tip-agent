# 🤖 Daily Tip Agent

An AI agent that posts one AWS Well-Architected best-practice tip per day into this `README.md`.

The project uses Retrieval-Augmented Generation (RAG) over a committed SQLite vector index built from the [AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf).

<!-- TIP_OF_THE_DAY_START -->

## Tip of the day [Thursday, October 29, 2026]

### Push content closer to users with edge caching

For user-facing content delivery, use Amazon CloudFront so responses can be served from edge locations instead of repeatedly going back to the origin. Design your cache behavior to maximize cache hit ratio by setting appropriate TTLs, varying only on headers or cookies that truly change the response, and invalidating only when necessary. If your application needs custom logic at the edge, use Lambda@Edge to tailor content near the user and reduce latency. For global workloads, consider Route 53 routing policies to send users to the best-performing endpoint based on location and latency. If origin load or large file transfers are a concern, CloudFront Origin Shield and S3 Transfer Acceleration can further improve delivery efficiency.

**Why it matters:** Serving more requests from edge caches reduces latency for users and decreases pressure on your origin. That usually improves availability and keeps scaling costs under control, especially during traffic spikes or when users are geographically dispersed.

<!-- TIP_OF_THE_DAY_END -->

## How it works

A scheduled GitHub Actions workflow runs `src/update_readme.py` once per day.

The script selects a topic from `src/topics.py`, then generates a new best-practice tip by using an AI agent with access to the local SQLite vector index in `storage/well_architected_index.sqlite`.

The agent searches the index, retrieves relevant source material, and writes one practical tip grounded in the retrieved material. The script then updates only the marked tip section in `README.md`, saves the tip as a dated Markdown file in `tips/`, and commits the change back to the repository.
