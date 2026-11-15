---
name: "Review-gate OpenClaw memory hygiene with openclaw-mem"
slug: "review-gate-openclaw-memory-hygiene-with-openclaw-mem"
description: "Pack trusted context and review memory writes before long OpenClaw sessions drift or accumulate low-quality memory."
github_stars: 28
verification: "security_reviewed"
source: "https://github.com/phenomenoner/openclaw-mem"
author: "phenomenoner"
publisher_type: "individual"
category: "Templates & Workflows"
framework: "OpenClaw"
tool_ecosystem:
  github_repo: "phenomenoner/openclaw-mem"
  github_stars: 28
---

# Review-gate OpenClaw memory hygiene with openclaw-mem

Pack trusted context and review memory writes before long OpenClaw sessions drift or accumulate low-quality memory.

## Prerequisites

OpenClaw, SQLite, local filesystem access

## Installation

Use the upstream install or setup path that matches your environment:
- pip install openclaw-context-pack
- git clone https://github.com/phenomenoner/openclaw-mem.git
- uv sync --locked
- uv run --python 3.13 --frozen -- \

Requirements and caveats from upstream:
- python -m venv .venv
- python benchmarks/trust_policy_synthetic_proof.py --json

Basic usage or getting-started notes:
- **Run the synthetic proof:** [Trust-policy synthetic proof](docs/showcase/trust-policy-synthetic-proof.md)
- **Pack**: run pack to get a bounded bundle_text and context_pack (schema: openclaw-mem.context-pack.v1), with citations, trust policy, and trace receipts.
- openclaw-mem self-curator verify --receipt .state/self-curator/apply-runs/<run>/apply-receipt.json --json

- Source: https://github.com/phenomenoner/openclaw-mem
- Extracted from upstream docs: https://raw.githubusercontent.com/phenomenoner/openclaw-mem/HEAD/README.md

## Documentation

- https://phenomenoner.github.io/openclaw-mem/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/review-gate-openclaw-memory-hygiene-with-openclaw-mem/)
