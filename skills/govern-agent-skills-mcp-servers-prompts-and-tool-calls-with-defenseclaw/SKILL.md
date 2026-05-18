---
name: "Govern agent skills, MCP servers, prompts, and tool calls with DefenseClaw"
slug: "govern-agent-skills-mcp-servers-prompts-and-tool-calls-with-defenseclaw"
description: "Use DefenseClaw as an operator-controlled admission, runtime guardrail, sandbox, and audit layer before untrusted agent capabilities run."
github_stars: 647
verification: "listed"
source: "https://github.com/cisco-ai-defense/defenseclaw"
author: "Cisco AI Defense"
publisher_type: "vendor"
category: "Templates & Workflows"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "cisco-ai-defense/defenseclaw"
  github_stars: 647
---

# Govern agent skills, MCP servers, prompts, and tool calls with DefenseClaw

Use DefenseClaw as an operator-controlled admission, runtime guardrail, sandbox, and audit layer before untrusted agent capabilities run.

## Prerequisites

DefenseClaw CLI, Go gateway sidecar, policy rules, optional OpenClaw plugin, optional OTLP/Splunk/webhook sinks

## Installation

Use the upstream install or setup path that matches your environment:
- make build
- make test
- make lint

Requirements and caveats from upstream:
- <a href="https://www.python.org/downloads/"><img alt="Python 3.10+" src="https://img.shields.io/badge/python-3.10%2B-blue.svg" /></a>
- DefenseClaw combines a Python operator CLI, a Go gateway sidecar, and an OpenClaw TypeScript plugin. Together they enforce a simple operating rule: untrusted agent capabilities are scanned, governed, logged, and block...
- | [CLI Reference](docs/CLI.md) | Python CLI commands and operator workflows |

Basic usage or getting-started notes:
- | Skills, MCP servers, plugins, and generated code before they run | Prompts, completions, tool calls, and sandbox activity at runtime | SQLite audit history, JSONL, OTLP, Splunk, webhooks, and TUI views |
- **Admission control** - scan skills, MCP servers, plugins, and code before they run.
- | [Quick Start](docs/QUICKSTART.md) | First successful local setup and scan flow |

- Source: https://github.com/cisco-ai-defense/defenseclaw
- Extracted from upstream docs: https://raw.githubusercontent.com/cisco-ai-defense/defenseclaw/HEAD/README.md

## Documentation

- https://cisco-ai-defense.github.io/docs/defenseclaw

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/govern-agent-skills-mcp-servers-prompts-and-tool-calls-with-defenseclaw/)
