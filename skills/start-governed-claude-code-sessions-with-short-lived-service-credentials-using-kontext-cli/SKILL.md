---
name: "Start governed Claude Code sessions with short-lived service credentials using Kontext CLI"
slug: "start-governed-claude-code-sessions-with-short-lived-service-credentials-using-kontext-cli"
description: "Inject short-lived, scoped service credentials into Claude Code sessions so agents can reach approved systems without exposing raw secrets."
github_stars: 143
verification: "listed"
source: "https://github.com/kontext-security/kontext-cli"
author: "kontext-security"
publisher_type: "organization"
category: "Security & Verification"
framework: "Claude Code"
tool_ecosystem:
  github_repo: "kontext-security/kontext-cli"
  github_stars: 143
---

# Start governed Claude Code sessions with short-lived service credentials using Kontext CLI

Inject short-lived, scoped service credentials into Claude Code sessions so agents can reach approved systems without exposing raw secrets.

## Prerequisites

Claude Code, supported service accounts, browser login for first-run auth

## Installation

Use the upstream install or setup path that matches your environment:
- brew install kontext-security/tap/kontext
- pnpm install --frozen-lockfile
- pnpm build

Requirements and caveats from upstream:
- | Local evaluation | Default kontext start does not require hosted login or trace upload. |

Basic usage or getting-started notes:
- Kontext is an authorization platform for AI agents. It helps teams control what agents can access and do with scoped credentials, policy enforcement, approvals, and audit trails. Kontext can run local-first for develo...
- For enterprise identity, audit retention, organization controls, deployment planning, custom usage volume, and onboarding for security and platform teams, contact [michel@kontext.security](mailto:michel@kontext.securi...
- | No reasoning capture | Kontext captures tool events and outcomes, not LLM reasoning, token usage, or full conversation history. |

- Source: https://github.com/kontext-security/kontext-cli
- Extracted from upstream docs: https://raw.githubusercontent.com/kontext-security/kontext-cli/HEAD/README.md

## Documentation

- https://github.com/kontext-security/kontext-cli

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/start-governed-claude-code-sessions-with-short-lived-service-credentials-using-kontext-cli/)
