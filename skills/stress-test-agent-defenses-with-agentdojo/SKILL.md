---
title: "Stress-test agent defenses with AgentDojo"
description: "Run AgentDojo benchmark environments to evaluate prompt-injection attacks and defenses against LLM agents before trusting them with real tools or data."
verification: "security_reviewed"
source: "https://github.com/ethz-spylab/agentdojo"
author: "ETH Zurich SPY Lab"
publisher_type: "academic open-source project"
category:
  - "Security & Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "ethz-spylab/agentdojo"
  github_stars: 619
---

# Stress-test agent defenses with AgentDojo

Run AgentDojo benchmark environments to evaluate prompt-injection attacks and defenses against LLM agents before trusting them with real tools or data.

## Prerequisites

Python 3.10+, agentdojo package, model provider credentials for the target pipeline, optional transformers extra for prompt-injection detector workflows

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install with `pip install agentdojo`. For detector workflows, install `pip install "agentdojo[transformers]"`. Then follow the upstream benchmark documentation to configure the target model or agent pipeline.
```

## Documentation

- https://agentdojo.spylab.ai/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stress-test-agent-defenses-with-agentdojo/)
