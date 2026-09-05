---
name: "Run supervised browser automation workflows with AIHawk"
slug: "run-one-shot-and-supervised-browser-automation-workflows-with-aihawk"
description: "Use AIHawk's local supervised browser UI for bounded web research and extraction, with human review before external actions."
github_stars: 30305
verification: "security_reviewed"
source: "https://github.com/feder-cr/AIHawk"
author: "feder-cr"
publisher_type: "individual"
category: "Browser Automation"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "feder-cr/AIHawk"
  github_stars: 30305
---

# Run supervised browser automation workflows with AIHawk

Use AIHawk's local supervised browser UI for bounded web research and extraction, with human review before external actions.

These instructions target AIHawk 0.6.0. That release exposes `ui`, not the former `do` command. The existing ASE slug is retained for link compatibility.

## Prerequisites

Python 3.11+, uv/uvx, Windows x86_64 or Linux x86_64/arm64, an OpenRouter API key, and space for the separate browser download (approximately 250 MB). Current upstream does not support macOS. Install uv using its [official installation guide](https://docs.astral.sh/uv/getting-started/installation/).

## Installation

Use a dedicated working directory and a test browser profile without sensitive saved sessions. Configure the `OPENROUTER_API_KEY` environment variable, or add it to an uncommitted `.env` file in that directory. Never put the real key in command arguments, published examples, or logs.

Download the browser before starting the UI, then launch the reviewed AIHawk release:

```bash
uvx invisible-playwright fetch
uvx --from aihawk==0.6.0 aihawk ui
```

Open `http://127.0.0.1:8765`. Keep the default localhost binding: the UI has no authentication and must not be exposed through a public host or tunnel.

- Source: https://github.com/feder-cr/AIHawk

## Usage and Verification

Ask the UI: "Open https://example.com and report the page title and first heading. Do not submit forms, download files, or follow external links."

Confirm the local UI loads, the browser visibly reaches the requested URL, and its reported title and heading match the visible page. A loading screen or a model-written answer without observed browser evidence is not a successful test. Model-backed use consumes OpenRouter credits.

Require human approval before sending messages, submitting forms, making purchases, or changing external data. Treat persistent profile directories as sensitive because they can retain cookies and logins. Follow the target site's access rules and rate limits.

## Documentation

- https://github.com/feder-cr/AIHawk

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-one-shot-and-supervised-browser-automation-workflows-with-aihawk/)
