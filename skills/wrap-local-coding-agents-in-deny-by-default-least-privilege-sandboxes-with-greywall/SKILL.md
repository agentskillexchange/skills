---
name: "Wrap local coding agents in deny-by-default least-privilege sandboxes with Greywall"
slug: "wrap-local-coding-agents-in-deny-by-default-least-privilege-sandboxes-with-greywall"
description: "Run Claude Code, Codex, Cursor, or similar local agent CLIs inside a host-local sandbox that learns required access and blocks everything else by default."
github_stars: 158
verification: "security_reviewed"
source: "https://github.com/GreyhavenHQ/greywall"
author: "GreyhavenHQ"
publisher_type: "organization"
category: "Security & Verification"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "GreyhavenHQ/greywall"
  github_stars: 158
---

# Wrap local coding agents in deny-by-default least-privilege sandboxes with Greywall

Run Claude Code, Codex, Cursor, or similar local agent CLIs inside a host-local sandbox that learns required access and blocks everything else by default.

## Prerequisites

Greywall CLI, local shell access, a supported local coding agent such as Claude Code, Codex, Cursor, Aider, Gemini CLI, or OpenCode, Linux or macOS host

## Installation

Use the upstream install or setup path that matches your environment:
- brew tap greyhavenhq/tap
- brew install greywall
- go install github.com/GreyhavenHQ/greywall/cmd/greywall@latest
- git clone https://github.com/GreyhavenHQ/greywall

Requirements and caveats from upstream:
- **No containers required** — kernel-enforced sandboxing without Docker overhead
- Greywall ships with built-in sandbox profiles for popular AI coding agents (Claude Code, Codex, Cursor, Aider, Goose, Gemini CLI, OpenCode, Amp, Cline, Copilot, Kilo, Auggie, Droid) and toolchains (Node, Python, Go, R...

Basic usage or getting-started notes:
- greywall -- curl https://example.com
- **Homebrew (macOS):**
- bash

- Source: https://github.com/GreyhavenHQ/greywall
- Extracted from upstream docs: https://raw.githubusercontent.com/GreyhavenHQ/greywall/HEAD/README.md

## Documentation

- https://docs.greywall.io/greywall/platform-support

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wrap-local-coding-agents-in-deny-by-default-least-privilege-sandboxes-with-greywall/)
