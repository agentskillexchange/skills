---
name: "Scan agent skills before installation with Ironheights"
slug: "scan-agent-skills-before-installation-with-ironheights"
description: "Use Ironheights, an open-source local-first scanner, to check a skill folder (SKILL.md plus bundled scripts) or a ClawHub skill for prompt injection, credential reads, remote-exec installs and persistence before an agent installs it, then pin the reviewed bytes so later changes are caught."
category: "Security & Verification"
framework: "Multi-Framework"
verification: listed
source: "https://github.com/Frank-Masciopinto/ironheights"
author: "Frank-Masciopinto"
publisher_type: "individual"
tool_ecosystem:
  github_repo: "Frank-Masciopinto/ironheights"
  npm_package: "ironheights"
---

# Scan agent skills before installation with Ironheights

Use this skill when an agent (Claude Code, Codex, Cursor, OpenClaw, Gemini or any MCP client) is about to install or upload a third-party skill and you want a local check first. Ironheights reads the skill folder as data and never runs its scripts. It applies fixed rules to `SKILL.md` and bundled files and reports instruction overrides, hidden text, reads of credential files and environment secrets, remote-exec install steps, persistence (startup files, scheduled jobs, agent memory edits) and outbound data flows. Each finding carries a rule ID, file, line, evidence and a suggested fix, and the scan ends in a verdict with a matching exit code, so it can gate a CI job or an agent workflow.

After review, `ironheights install --write-lock` pins the exact bytes and dependency closure that were checked, and a later install refuses on any mismatch. `ironheights drift` flags a skill or MCP tool description that changed after you approved it. Output formats are text, JSON, SARIF, Markdown and HTML. No account, API key or telemetry is needed; an optional `--llm` mode uses a local or OpenAI-compatible model only when you pass it.

Limits: it is early (public since October 2026) and mostly rule-based, so it misses many plain-language attacks. The benchmark numbers in its repository are self-reported by the maintainer. A clean result means "no known pattern found", not "safe"; keep reading high-privilege skills yourself.

## Prerequisites

Node.js 20 or newer (for `npx`). Optional: a ClawHub CLI for OpenClaw installs, or Ollama for `--llm` mode.

## Installation

### Run the scanner directly

```bash
npx ironheights@0.37.0 scan ./path/to/skill
npx ironheights@0.37.0 scan ./path/to/skill --json
npx ironheights@0.37.0 scan ./path/to/skill --sarif ironheights.sarif
```

### MCP server

Add a stdio server that runs `npx -y ironheights@0.37.0 mcp`. Agents can then call `check_skill` before installing a skill and `tool_manifest_check` for MCP tool-description drift.

### OpenClaw

```bash
clawhub install ironheights
```

### GitHub Action

Use `Frank-Masciopinto/ironheights@v0.37.0` in a workflow step; it runs the same scan and exit codes. See the CI docs linked below.

- Source: https://github.com/Frank-Masciopinto/ironheights

## Documentation

- https://github.com/Frank-Masciopinto/ironheights#readme
- https://github.com/Frank-Masciopinto/ironheights/blob/main/docs/mcp.md
- https://github.com/Frank-Masciopinto/ironheights/blob/main/docs/ci.md
- https://www.ironheights.dev

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/scan-agent-skills-before-installation-with-ironheights/)
