---
name: "Statically scan agent repos for prompt injection and unsafe MCP configs with Agent Audit"
slug: "statically-scan-agent-repos-for-prompt-injection-and-unsafe-mcp-configs-with-agent-audit"
description: "Audit agent code, prompts, and MCP configuration for prompt-injection surfaces, taint issues, and unsafe tool exposure before shipping."
github_stars: 149
verification: "listed"
source: "https://github.com/HeadyZhang/agent-audit"
author: "Agent Security Team"
publisher_type: "individual"
category: "Security & Verification"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "HeadyZhang/agent-audit"
  github_stars: 149
---

# Statically scan agent repos for prompt injection and unsafe MCP configs with Agent Audit

Audit agent code, prompts, and MCP configuration for prompt-injection surfaces, taint issues, and unsafe tool exposure before shipping.

## Prerequisites

agent-audit, local agent repository or config tree

## Installation

Use the upstream install or setup path that matches your environment:
- pip install agent-audit
- git clone https://github.com/HeadyZhang/agent-audit

Requirements and caveats from upstream:
- [![Python](https://img.shields.io/pypi/pyversions/agent-audit.svg)](https://pypi.org/project/agent-audit/)
- | T6 | [openai-agents-python](https://github.com/openai/openai-agents-python) | 25 | ASI-01, ASI-02 |
- | T7 | [adk-python](https://github.com/google/adk-python) | 40 | ASI-02, ASI-04, ASI-10 |

Basic usage or getting-started notes:
- Install
- bash
- Scan your project

- Source: https://github.com/HeadyZhang/agent-audit
- Extracted from upstream docs: https://raw.githubusercontent.com/HeadyZhang/agent-audit/HEAD/README.md

## Documentation

- https://headyzhang.github.io/agent-audit/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/statically-scan-agent-repos-for-prompt-injection-and-unsafe-mcp-configs-with-agent-audit/)
