---
name: "HOL Guard"
slug: "hol-guard"
description: "Protect local AI coding-agent harnesses before tools run, review approvals and evidence, and scan agent plugins, skills, MCP servers, and marketplace packages with HOL Guard."
verification: "listed"
source: "https://github.com/hashgraph-online/hol-guard-plugin"
category: "Security & Verification"
framework: "Custom Agents"
tool_ecosystem:
  github_repo: "hashgraph-online/hol-guard-plugin"
---

# HOL Guard

HOL Guard is a local security runtime for AI coding agents. Use this skill when a user wants to put a supported local harness behind Guard before tools execute, inspect a blocked or approval-gated action, produce receipts or audit evidence, or verify an agent package before release. The `hol-guard` CLI owns harness setup and runtime protection; `plugin-scanner` is a separate scanner distribution for plugins, skills, MCP server packages, and mixed agent workspaces. Do not claim a harness is protected until HOL Guard reports that state, and never bypass a Guard approval. Supported local harness targets include Codex, Claude Code, Copilot CLI, Cursor, Gemini CLI, Hermes, OpenClaw, OpenCode, and Antigravity.

## Installation

No source-backed install or usage instructions could be extracted automatically. Review the upstream project before running this skill in a sensitive workflow.

- Source: https://github.com/hashgraph-online/hol-guard-plugin

## Protect a local harness

Use Guard-owned setup rather than editing agent configuration by hand:

```bash
hol-guard bootstrap
hol-guard install <harness>
hol-guard run <harness> --dry-run
hol-guard run <harness>
hol-guard status
```

For example, use `codex`, `claude-code`, `cursor`, `gemini`, `openclaw`, or `opencode` as the harness name. If Guard queues work, inspect it before approving or denying:

```bash
hol-guard approvals
hol-guard approvals open
hol-guard receipts
hol-guard diff <harness>
```

For diagnostics and evidence:

```bash
hol-guard doctor <harness> --json
hol-guard inventory
hol-guard events
```

## Scan agent packages

Run scanner mode from the package or workspace root so relevant plugin, skill, MCP, and harness configuration surfaces can be discovered together:

```bash
plugin-scanner lint .
plugin-scanner verify . --json
```

Treat scanner failures as real until inspected. Do not mark a package release-ready or a workspace protected without command output proving it.

## Source

- HOL Guard skill and runtime guidance: https://github.com/hashgraph-online/hol-guard-plugin
- HOL Guard: https://hol.org/guard
