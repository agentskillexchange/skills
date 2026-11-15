---
name: "Investigate telemetry incidents with Monoscope MCP and agent-mode CLI"
slug: "investigate-telemetry-incidents-with-monoscope-mcp-and-agent-mode-cli"
description: "Connect agents to Monoscope so they can query logs, traces, metrics, monitors, and issues through stable JSON CLI output or MCP tools for incident triage."
github_stars: 1130
verification: "security_reviewed"
source: "https://github.com/monoscope-tech/monoscope"
author: "monoscope-tech"
publisher_type: "open_source"
category: "Monitoring & Alerts"
framework: "MCP"
tool_ecosystem:
  github_repo: "monoscope-tech/monoscope"
  github_stars: 1130
---

# Investigate telemetry incidents with Monoscope MCP and agent-mode CLI

Connect agents to Monoscope so they can query logs, traces, metrics, monitors, and issues through stable JSON CLI output or MCP tools for incident triage.

## Prerequisites

Monoscope cloud or self-hosted stack, S3-compatible storage, OpenTelemetry or test telemetry data, Monoscope CLI or MCP-capable client, API key for MCP access

## Installation

Use the upstream install or setup path that matches your environment:
- git clone https://github.com/monoscope-tech/monoscope.git
- docker-compose up
- npx skills add monoscope-tech/skills
- pip install opentelemetry-distro opentelemetry-exporter-otlp

Requirements and caveats from upstream:
- <summary><b>Python</b></summary>
- opentelemetry-instrument python myapp.py
- <summary><b>Node.js</b></summary>

Basic usage or getting-started notes:
- <a href="#what-is-monoscope">What is Monoscope?</a> • <a href="#cloud-vs-self-hosted">Cloud vs Self-hosted</a> • <a href="#quick-start">Quick Start</a> • <a href="#ai-agents--reports">AI Agents</a> • <a href="#roadmap...
- 🤖 **AI agents** — Create agents that run on a schedule to detect anomalies and surface insights
- | **Pricing** | [Usage-based](https://monoscope.tech/pricing) | Free (AGPL-3.0) |

- Source: https://github.com/monoscope-tech/monoscope
- Extracted from upstream docs: https://raw.githubusercontent.com/monoscope-tech/monoscope/HEAD/README.md

## Documentation

- https://docs.monoscope.tech

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/investigate-telemetry-incidents-with-monoscope-mcp-and-agent-mode-cli/)
