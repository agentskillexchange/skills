---
name: "Run a mock robotics benchmark and review evidence with Inspect Robots"
slug: "run-mock-robotics-benchmark-review-evidence-inspect-robots"
description: "Run the built-in CubePick benchmark with a scripted policy, inspect resolved configuration and scores, and render saved robotics evaluation logs for review."
github_stars: 757
verification: "security_reviewed"
source: "https://github.com/robocurve/inspect-robots"
author: "Robocurve"
publisher_type: "organization"
category: "Code Quality & Review"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "robocurve/inspect-robots"
  github_stars: 757
---

# Run a mock robotics benchmark and review evidence with Inspect Robots

Run the built-in CubePick benchmark with a scripted policy, inspect resolved configuration and scores, and render saved robotics evaluation logs for review.

## Prerequisites

Python 3.11+; uv or equivalent virtual environment tooling; inspect-robots CLI

## Installation

Install or set up from the source-backed instructions:

Use Python 3.11+ in a fresh project directory. Create a virtual environment with uv venv, then install the verified PyPI release with uv pip install inspect-robots==1.0.0 and activate .venv. Run inspect-robots list, then inspect-robots run --task cubepick-reach --policy scripted --embodiment cubepick. Inspect and render the emitted LOG.json using inspect-robots inspect LOG.json and inspect-robots view LOG.json. No robot plugins, GPU, Rerun extra or model key are needed for this bounded mock workflow. Documentation was inspected at an upstream source revision; packaged-release parity was not runtime-tested.

- Source: https://github.com/robocurve/inspect-robots

## Documentation

- https://github.com/robocurve/inspect-robots/blob/772019598e42ccc7921a043dee3a2ea2692020ea/docs/guide/cli.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-mock-robotics-benchmark-review-evidence-inspect-robots/)
