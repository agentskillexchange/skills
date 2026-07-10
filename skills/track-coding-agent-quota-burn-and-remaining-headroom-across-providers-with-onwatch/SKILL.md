---
name: "Track coding-agent quota burn and remaining headroom across providers with onWatch"
slug: "track-coding-agent-quota-burn-and-remaining-headroom-across-providers-with-onwatch"
description: "Monitor quota, spend, resets, and alerts across multiple coding-agent providers from one local dashboard before a long run hits throttling or budget limits."
github_stars: 580
verification: "security_reviewed"
source: "https://github.com/onllm-dev/onWatch"
author: "onllm-dev"
publisher_type: "organization"
category: "Monitoring & Alerts"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "onllm-dev/onWatch"
  github_stars: 580
---

# Track coding-agent quota burn and remaining headroom across providers with onWatch

Monitor quota, spend, resets, and alerts across multiple coding-agent providers from one local dashboard before a long run hits throttling or budget limits.

## Prerequisites

onWatch binary or Homebrew install, local shell access, provider credentials for one or more supported services, and optional browser access for the local dashboard

## Installation

Use the upstream install or setup path that matches your environment:
- docker run -d --name onwatch -p 9211:9211 \
- git clone https://github.com/onllm-dev/onwatch.git && cd onwatch
- docker-compose up -d
- docker-compose logs -f

Requirements and caveats from upstream:
- | GEMINI_REFRESH_TOKEN | Gemini OAuth refresh token (for Docker/headless) |
- | GEMINI_ACCESS_TOKEN | Gemini OAuth access token (for Docker/headless) |
- | ANTIGRAVITY_BASE_URL | Antigravity base URL (for Docker/manual config) |

Basic usage or getting-started notes:
- Track usage across [Synthetic](https://synthetic.new), [Z.ai](https://z.ai), [Anthropic](https://anthropic.com), [Codex](https://openai.com/codex), [GitHub Copilot](https://github.com/features/copilot), [MiniMax](http...
- See history, get alerts, and open a local web dashboard before you hit throttling or run over budget. Additionally, you can ingest local telemetry from your own API-driven workflows with API Integrations, keeping trac...
- onWatch fills the gap between "current usage snapshot" and the historical, per-cycle, cross-session view that developers actually need. It runs as a lightweight background agent (<50 MB RAM with all nine providers pol...

- Source: https://github.com/onllm-dev/onWatch
- Extracted from upstream docs: https://raw.githubusercontent.com/onllm-dev/onWatch/HEAD/README.md

## Documentation

- https://onwatch.onllm.dev

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/track-coding-agent-quota-burn-and-remaining-headroom-across-providers-with-onwatch/)
