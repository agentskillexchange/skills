---
name: "Bridge local coding agents into chat apps with cc-connect"
slug: "bridge-local-coding-agents-into-chat-apps-with-cc-connect"
description: "Let operators control local Claude Code, Codex, Cursor, Gemini CLI, and other coding agents from Slack, Discord, Telegram, Feishu/Lark, DingTalk, LINE, and WeChat Work."
github_stars: 14172
verification: "security_reviewed"
source: "https://github.com/chenhg5/cc-connect"
author: "chenhg5"
publisher_type: "individual"
category: "Integrations & Connectors"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "chenhg5/cc-connect"
  github_stars: 14172
  npm_package: "cc-connect"
  npm_weekly_downloads: 17176
---

# Bridge local coding agents into chat apps with cc-connect

Let operators control local Claude Code, Codex, Cursor, Gemini CLI, and other coding agents from Slack, Discord, Telegram, Feishu/Lark, DingTalk, LINE, and WeChat Work.

## Prerequisites

Node.js/npm or Homebrew, a supported local coding-agent CLI, and at least one supported chat platform account or bot

## Installation

Use the upstream install or setup path that matches your environment:
- npm install -g cc-connect
- brew install cc-connect
- git clone https://github.com/chenhg5/cc-connect.git
- make build

Requirements and caveats from upstream:
- **Multi-user / permissions** — reply-to-unauthorized-IM-senders option, @Bot/permit ≡ /permit keyword matching, Bridge requires token when enabled.
- ⚠️ **Behavior changes (action may be required)**: Telegram/Discord progress_style defaults to compact (set legacy to revert); QQ Bot default intents now include INTERACTION_CREATE (custom values must include 1<<26); D...
- † **QQ (NapCat / OneBot)** — unofficial self-hosted bridge; behaviour depends on your NapCat / network setup.

Basic usage or getting-started notes:
- Thanks to [Kimi](https://www.kimi.com/code/?aff=cc-connect) for sponsoring this project! [Kimi K2.7 Code](https://platform.kimi.ai/docs/guide/kimi-k2-7-code-quickstart) is an open-source, coding-focused agentic model...
- With cc-connect, you can bring Kimi CLI from your local machine into Feishu/Lark, DingTalk, Telegram, Slack, Discord, WeChat Work, and other instant messaging tools. Wherever you are, you can continue working on local...
- **Observability** — blackbox testing framework (P0/P1/P2 + config-switch matrix), CUJ test framework, provider-resume regression suite for codex/opencode/kimi, Pi context-usage reporter in reply footer.

- Source: https://github.com/chenhg5/cc-connect
- Extracted from upstream docs: https://raw.githubusercontent.com/chenhg5/cc-connect/HEAD/README.md

## Documentation

- https://github.com/chenhg5/cc-connect

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/bridge-local-coding-agents-into-chat-apps-with-cc-connect/)
