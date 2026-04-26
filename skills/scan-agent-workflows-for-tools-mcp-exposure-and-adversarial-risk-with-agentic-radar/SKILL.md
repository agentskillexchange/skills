---
title: "Scan agent workflows for tools, MCP exposure, and adversarial risk with Agentic Radar"
description: "Use Agentic Radar to statically scan agent workflows, map tools and MCP servers, generate shareable security reports, and optionally run adversarial runtime tests before rollout."
verification: "security_reviewed"
source: "https://github.com/splx-ai/agentic-radar"
category:
  - "Security & Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "splx-ai/agentic-radar"
  github_stars: 953
---

# Scan agent workflows for tools, MCP exposure, and adversarial risk with Agentic Radar

Use Agentic Radar when the job is to inspect an agent workflow before release, inventory its tools and MCP servers, map likely vulnerabilities, and produce a reviewable report for security or engineering follow-up. The upstream project supports explicit framework-targeted scan commands such as `agentic-radar scan langgraph`, `scan crewai`, `scan n8n`, `scan openai-agents`, and `scan autogen`, plus a runtime `test` mode for adversarial checks in supported workflows.

Invoke this instead of using the product normally when you need a repeatable pre-deployment review step, not just a generic security platform. The operator workflow is concrete: point Agentic Radar at a workflow, choose the framework, generate the HTML report, inspect MCP and tool findings, and optionally run the built-in vulnerability test suite against an entrypoint.

The scope boundary that keeps this skill-shaped is narrow and operational: workflow security inspection and targeted agent testing. It is not a generic agent framework listing, not a plain product card, and not a broad SDK entry. The user is invoking a specific audit workflow with clear inputs, outputs, and stop conditions.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/scan-agent-workflows-for-tools-mcp-exposure-and-adversarial-risk-with-agentic-radar/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/scan-agent-workflows-for-tools-mcp-exposure-and-adversarial-risk-with-agentic-radar
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/scan-agent-workflows-for-tools-mcp-exposure-and-adversarial-risk-with-agentic-radar`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/scan-agent-workflows-for-tools-mcp-exposure-and-adversarial-risk-with-agentic-radar/)
