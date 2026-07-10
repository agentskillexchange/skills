---
name: "Run a self-improving personal agent with Hermes Agent"
slug: "run-a-self-improving-personal-agent-with-hermes-agent"
description: "Deploy Hermes Agent as a persistent personal agent that learns skills from experience, searches past sessions, schedules automations, and coordinates work across CLI and chat channels."
github_stars: 177610
verification: "security_reviewed"
source: "https://github.com/NousResearch/hermes-agent"
author: "Nous Research"
publisher_type: "open_source"
category: "Templates & Workflows"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "NousResearch/hermes-agent"
  github_stars: 177610
---

# Run a self-improving personal agent with Hermes Agent

Deploy Hermes Agent as a persistent personal agent that learns skills from experience, searches past sessions, schedules automations, and coordinates work across CLI and chat channels.

## Prerequisites

Hermes Agent; model provider API key or compatible endpoint; optional Telegram/Discord/Slack/WhatsApp/Signal gateways

## Installation

Install Hermes Agent from the official repository installer.

Linux, macOS, WSL2, or Termux:

```bash
curl -fsSLO https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh
less install.sh
bash install.sh
source ~/.bashrc
hermes
```

Windows PowerShell:

```powershell
iex (irm https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.ps1)
```

After installation, use the documented CLI commands to configure and operate the agent:

```bash
hermes setup        # Run the full setup wizard
hermes model        # Choose the model provider and model
hermes tools        # Configure enabled tools
hermes gateway      # Start messaging gateway setup/runtime
hermes doctor       # Diagnose environment or configuration issues
```

Contributor setup, when you need to work from source:

```bash
git clone https://github.com/NousResearch/hermes-agent.git
cd hermes-agent
./setup-hermes.sh
./hermes
```

- Source: https://github.com/NousResearch/hermes-agent
- Extracted from upstream docs: https://raw.githubusercontent.com/NousResearch/hermes-agent/HEAD/README.md

## Documentation

- https://hermes-agent.nousresearch.com/docs/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-a-self-improving-personal-agent-with-hermes-agent/)
