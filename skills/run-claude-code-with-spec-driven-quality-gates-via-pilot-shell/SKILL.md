---
name: "Run Claude Code with spec-driven quality gates via Pilot Shell"
slug: "run-claude-code-with-spec-driven-quality-gates-via-pilot-shell"
description: "Wrap Claude Code sessions in a spec, approval, and verification workflow before risky implementation work lands."
github_stars: 1645
verification: "security_reviewed"
source: "https://github.com/maxritter/pilot-shell"
author: "Max Ritter"
publisher_type: "individual"
category: "Templates & Workflows"
framework: "Claude Code"
tool_ecosystem:
  github_repo: "maxritter/pilot-shell"
  github_stars: 1645
---

# Run Claude Code with spec-driven quality gates via Pilot Shell

Wrap Claude Code sessions in a spec, approval, and verification workflow before risky implementation work lands.

## Prerequisites

Claude Code, curl, bash, macOS/Linux/WSL2

## Installation

Requirements and caveats from upstream:
- **RED:** Write the failing test via an existing public entry point → run, must fail with the documented symptom.
- | [**Language Servers**](https://pilot-shell.com/docs/features/language-servers) | Real-time diagnostics for Python (basedpyright), TypeScript (vtsls), Go (gopls). Auto-installed, auto-configured |

Basic usage or getting-started notes:
- ### How real engineers run Claude Code.
- Run pilot for Spec-Driven Development with /spec, or pilot bot for 24/7 automations.
- **Verify End-to-End:** The primary correctness signal. Run the actual program with the original input (Claude Code Chrome → Chrome DevTools MCP → playwright-cli → agent-browser for UI; CLI / API / REPL / job trigger f...

- Source: https://github.com/maxritter/pilot-shell
- Extracted from upstream docs: https://raw.githubusercontent.com/maxritter/pilot-shell/HEAD/README.md

## Documentation

- https://pilot-shell.com/docs

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-claude-code-with-spec-driven-quality-gates-via-pilot-shell/)
