---
name: "Run supervised MCP browser automation with Auto Browser"
slug: "run-supervised-mcp-browser-automation-with-auto-browser"
description: "Give an MCP-capable agent a local Playwright browser with human takeover, reusable auth profiles, approvals, audit trails, and repeatable browser workflow evidence."
github_stars: 565
verification: "security_reviewed"
source: "https://github.com/LvcidPsyche/auto-browser"
author: "LvcidPsyche"
publisher_type: "open_source"
category: "Browser Automation"
framework: "MCP"
tool_ecosystem:
  github_repo: "LvcidPsyche/auto-browser"
  github_stars: 565
---

# Run supervised MCP browser automation with Auto Browser

Give an MCP-capable agent a local Playwright browser with human takeover, reusable auth profiles, approvals, audit trails, and repeatable browser workflow evidence.

## Prerequisites

Docker Compose, Auto Browser, MCP-compatible client or bundled stdio bridge, Playwright browser stack, optional noVNC operator dashboard

## Installation

Use the upstream install or setup path that matches your environment:
- git clone https://github.com/LvcidPsyche/auto-browser.git
- docker compose up --build
- make doctor
- Run make doctor from a normal terminal with local Docker access and permission to open localhost sockets.

Requirements and caveats from upstream:
- **Local-first by default.** Run the full stack on your own box with Docker Compose, or use Codespaces for a quick hosted demo.
- **Fresh dependency floor.** Playwright 1.60 (controller and browser-node aligned), uvicorn 0.49, and a unified, current user-agent pool replacing the stale Chrome 122-era defaults.
- **Release gates in CI** continue to enforce dependency audits, fixture evals, client tests, Python wheel builds, and the 80% controller coverage gate — now on Python 3.11 and 3.14.

Basic usage or getting-started notes:
- **On PyPI.** pip install auto-browser-client for the SDK, pip install auto-browser-langchain for the LangChain/LangGraph/CrewAI adapters, and uvx auto-browser-mcp to run the MCP stdio bridge with zero setup. Releases...
- | Playwright-backed sessions with screenshots, DOM summaries, OCR excerpts, tab controls, downloads, and network inspection | approval gates, operator identity headers, audit events, PII scrubbing, Witness receipts, a...
- cd auto-browser

- Source: https://github.com/LvcidPsyche/auto-browser
- Extracted from upstream docs: https://raw.githubusercontent.com/LvcidPsyche/auto-browser/HEAD/README.md

## Documentation

- https://github.com/LvcidPsyche/auto-browser

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-supervised-mcp-browser-automation-with-auto-browser/)
