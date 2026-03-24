---
name: "Snyk Agent Scan"
description: "Scan your AI agents, MCP servers, and skills for security vulnerabilities from the command line. Snyk Agent Scan discovers and audits every agent component on your machine — detecting prompt injections, tool poisoning, toxic flows, malware payloads, and credential handling issues across 15+ distinct risk categories."
category: "Security & Verification"
framework: "MCP-compatible"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/snyk-agent-scan/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "snyk"  # from ase_tool_match
  github_stars: 5457  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 601684  # from ase_npm_downloads
  github_repo: "snyk/cli"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Snyk Agent Scan

Scan your AI agents, MCP servers, and skills for security vulnerabilities from the command line. Snyk Agent Scan discovers and audits every agent component on your machine — detecting prompt injections, tool poisoning, toxic flows, malware payloads, and credential handling issues across 15+ distinct risk categories.

## Overview

Snyk Agent Scan (formerly Invariant Labs MCP-Scan) is a command-line security scanner purpose-built for the AI agent supply chain. It auto-discovers agent configurations for Claude Code, Claude Desktop, Cursor, Windsurf, Gemini CLI, and other MCP-compatible platforms, then runs a comprehensive vulnerability assessment against every discovered component.
Best for

- Auditing installed MCP servers and agent skills before trusting them

- Detecting prompt injection attacks hidden in tool descriptions

- Identifying tool shadowing between MCP servers

- Verifying skills don’t contain malware payloads or unsafe credential handling

What it scans

- MCP servers: Prompt injection in tool descriptions, tool shadowing, tool poisoning via hidden instructions, and toxic data flows

- Agent skills: Prompt injection in skill files, malware payloads, untrusted content references, unsafe credential handling, and hardcoded secrets

- Agent harnesses: Configuration discovery and inventory across all supported platforms

Install notes

Get an API token from app.snyk.io/account. Set `SNYK_TOKEN`, install uv, then run `uvx snyk-agent-scan@latest` for a full machine scan. For targeted scans: `uvx snyk-agent-scan@latest ~/.cursor/mcp.json`.

Source: github.com/snyk/agent-scan

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill snyk-agent-scan
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill snyk-agent-scan -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill snyk-agent-scan -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill snyk-agent-scan -a codex
```

### OpenClaw

```bash
clawhub install snyk-agent-scan
```

## Source

- Marketplace: https://agentskillexchange.com/skills/snyk-agent-scan/
