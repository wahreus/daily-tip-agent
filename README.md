# 🤖 Daily Tip Agent

An AI agent that posts one AWS Well-Architected best-practice tip per day into this `README.md`.

The project uses Retrieval-Augmented Generation (RAG) over a committed SQLite vector index built from the [AWS Well-Architected Framework](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf).

<!-- TIP_OF_THE_DAY_START -->

## Tip of the day [Wednesday, November 25, 2026]

### Put a protective edge in front of your app

Use Amazon CloudFront as the first public entry point for internet-facing workloads so you can cache content at edge locations and reduce direct load on your origin. Pair it with AWS WAF to block common web exploits and bot-driven HTTP floods before they reach application servers. Keep AWS Shield Standard enabled for baseline DDoS defense, and consider Shield Advanced if your workload is exposed to larger or more sophisticated attacks. Where appropriate, add CloudFront Origin Shield and origin failover so cache misses and origin disruptions are absorbed more gracefully. If you use Global Accelerator, its static IPs and independent network zones can also improve resilience and simplify front-door protection.

**Why it matters:** Pushing filtering and caching closer to the user reduces attack surface and makes it harder for volumetric or application-layer attacks to consume your origin capacity. It also improves availability by giving you multiple layers of edge resilience instead of relying on a single ingress path.

<!-- TIP_OF_THE_DAY_END -->

## How it works

A scheduled GitHub Actions workflow runs `src/update_readme.py` once per day.

The script selects a topic from `src/topics.py`, then generates a new best-practice tip by using an AI agent with access to the local SQLite vector index in `storage/well_architected_index.sqlite`.

The agent searches the index, retrieves relevant source material, and writes one practical tip grounded in the retrieved material. The script then updates only the marked tip section in `README.md`, saves the tip as a dated Markdown file in `tips/`, and commits the change back to the repository.
