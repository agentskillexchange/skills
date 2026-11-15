---
name: "Stress-test agent defenses with AgentDojo"
slug: "stress-test-agent-defenses-with-agentdojo"
description: "Run AgentDojo benchmark environments to evaluate prompt-injection attacks and defenses against LLM agents before trusting them with real tools or data."
github_stars: 619
verification: "security_reviewed"
source: "https://github.com/ethz-spylab/agentdojo"
author: "ETH Zurich SPY Lab"
publisher_type: "academic open-source project"
category: "Security & Verification"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "ethz-spylab/agentdojo"
  github_stars: 619
---

# Stress-test agent defenses with AgentDojo

Run AgentDojo benchmark environments to evaluate prompt-injection attacks and defenses against LLM agents before trusting them with real tools or data.

## Prerequisites

Python 3.10+, agentdojo package, model provider credentials for the target pipeline, optional transformers extra for prompt-injection detector workflows

## Installation

Use the upstream install or setup path that matches your environment:
- pip install agentdojo
- pip install "agentdojo[transformers]"

Requirements and caveats from upstream:
- ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/agentdojo) ![PyPI - Downloads](https://img.shields.io/pypi/dm/agentdojo) ![PyPI - Version](https://img.shields.io/pypi/v/agentdojo)
- python -m agentdojo.scripts.benchmark -s workspace -ut user_task_0 \
- python -m agentdojo.scripts.benchmark --model gpt-4o-2024-05-13 \

Basic usage or getting-started notes:
- [!IMPORTANT]
- Note that the API of the package is still under development and might change in the future.
- If you want to use the prompt injection detector, you need to install the transformers extra:

- Source: https://github.com/ethz-spylab/agentdojo
- Extracted from upstream docs: https://raw.githubusercontent.com/ethz-spylab/agentdojo/HEAD/README.md

## Documentation

- https://agentdojo.spylab.ai/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stress-test-agent-defenses-with-agentdojo/)
