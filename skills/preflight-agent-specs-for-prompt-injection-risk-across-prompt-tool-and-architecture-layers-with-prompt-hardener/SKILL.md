---
name: "Preflight agent specs for prompt-injection risk across prompt, tool, and architecture layers with Prompt Hardener"
slug: "preflight-agent-specs-for-prompt-injection-risk-across-prompt-tool-and-architecture-layers-with-prompt-hardener"
description: "Describe an agent in `agent_spec.yaml`, run deterministic prompt-injection analysis, generate mitigations, and validate defenses before rollout."
github_stars: 50
verification: "listed"
source: "https://github.com/cybozu/prompt-hardener"
author: "Cybozu"
publisher_type: "organization"
category: "Security & Verification"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "cybozu/prompt-hardener"
  github_stars: 50
---

# Preflight agent specs for prompt-injection risk across prompt, tool, and architecture layers with Prompt Hardener

Describe an agent in `agent_spec.yaml`, run deterministic prompt-injection analysis, generate mitigations, and validate defenses before rollout.

## Prerequisites

Python 3, pipx or uv optional

## Installation

Use the upstream install or setup path that matches your environment:
- pipx install https://github.com/cybozu/prompt-hardener/releases/download/v0.6.0/prompt_hardener-0.6.0-py3-none-any.whl
- Recommended if you already use uv for Python tooling.
- uv tool install https://github.com/cybozu/prompt-hardener/releases/download/v0.6.0/prompt_hardener-0.6.0-py3-none-any.whl
- pip install https://github.com/cybozu/prompt-hardener/releases/download/v0.6.0/prompt_hardener-0.6.0-py3-none-any.whl

Requirements and caveats from upstream:
- **Deterministic first**: init, validate, analyze, report, and diff do not require an LLM API key
- Use this if you prefer a standard Python environment.

Basic usage or getting-started notes:
- run deterministic security analysis across prompt, tool, and architecture layers
- Choose the installation method that fits how you want to use Prompt Hardener.
- ### Using [pipx](https://pipx.pypa.io/)

- Source: https://github.com/cybozu/prompt-hardener
- Extracted from upstream docs: https://raw.githubusercontent.com/cybozu/prompt-hardener/HEAD/README.md

## Documentation

- https://github.com/cybozu/prompt-hardener

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/preflight-agent-specs-for-prompt-injection-risk-across-prompt-tool-and-architecture-layers-with-prompt-hardener/)
