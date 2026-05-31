---
name: "Run production multi-agent workflows with Hive"
slug: "run-production-multi-agent-workflows-with-hive"
description: "Use Hive as a model-agnostic harness for long-running multi-agent workflows that need state, recovery, observability, human oversight, and business-system tools."
github_stars: 10461
verification: "security_reviewed"
source: "https://github.com/aden-hive/hive"
author: "Aden Hive"
publisher_type: "organization"
category: "Templates & Workflows"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "aden-hive/hive"
  github_stars: 10461
---

# Run production multi-agent workflows with Hive

Use Hive as a model-agnostic harness for long-running multi-agent workflows that need state, recovery, observability, human oversight, and business-system tools.

## Prerequisites

Hive/OpenHive, Python 3.11+, uv workspace setup, LLM provider credentials, optional MCP business-system tools, optional ripgrep

## Installation

Use the upstream install or setup path that matches your environment:
- git clone https://github.com/aden-hive/hive.git

Requirements and caveats from upstream:
- Require **human-in-the-loop control**, observability, and cost limits
- Python 3.11+ for agent development
- **ripgrep (optional, recommended on Windows):** The search_files tool uses ripgrep for faster file search. If not installed, a Python fallback is used. On Windows: winget install BurntSushi.ripgrep or scoop install ri...

Basic usage or getting-started notes:
- <p align="center"><em>The agent harness for production workloads — state management, failure recovery, observability, and human oversight so your agents actually run.</em></p>
- Plan to run agents in **production** where uptime, cost, and auditability matter
- An LLM provider that powers the agents

- Source: https://github.com/aden-hive/hive
- Extracted from upstream docs: https://raw.githubusercontent.com/aden-hive/hive/HEAD/README.md

## Documentation

- https://docs.adenhq.com/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-production-multi-agent-workflows-with-hive/)
