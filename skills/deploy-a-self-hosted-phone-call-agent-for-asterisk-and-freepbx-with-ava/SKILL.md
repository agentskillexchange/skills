---
name: "Deploy a self-hosted phone-call agent for Asterisk and FreePBX with AVA"
slug: "deploy-a-self-hosted-phone-call-agent-for-asterisk-and-freepbx-with-ava"
description: "Bring up a self-hosted voice agent that answers, routes, or transfers live calls through Asterisk or FreePBX with a PBX-native workflow."
github_stars: 991
verification: "listed"
source: "https://github.com/hkjarral/AVA-AI-Voice-Agent-for-Asterisk"
author: "hkjarral"
publisher_type: "open_source_project"
category: "Integrations & Connectors"
framework: "Custom Agents"
tool_ecosystem:
  github_repo: "hkjarral/AVA-AI-Voice-Agent-for-Asterisk"
  github_stars: 991
---

# Deploy a self-hosted phone-call agent for Asterisk and FreePBX with AVA

Bring up a self-hosted voice agent that answers, routes, or transfers live calls through Asterisk or FreePBX with a PBX-native workflow.

## Prerequisites

Docker Compose, Asterisk or FreePBX environment, telephony configuration, STT/LLM/TTS provider credentials

## Installation

Use the upstream install or setup path that matches your environment:
- git clone https://github.com/hkjarral/Asterisk-AI-Voice-Agent.git
- docker compose -p asterisk-ai-voice-agent up -d --build --force-recreate admin_ui
- docker compose -p asterisk-ai-voice-agent up -d --build ai_engine
- docker compose -p asterisk-ai-voice-agent logs ai_engine | tail -20

Requirements and caveats from upstream:
- ![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
- ![Docker](https://img.shields.io/badge/docker-compose-blue.svg)
- **GPU users:** If you have an NVIDIA GPU for local AI inference, see **[docs/LOCAL_ONLY_SETUP.md](docs/LOCAL_ONLY_SETUP.md)** for the GPU compose overlay (docker-compose.gpu.yml) before building.

Basic usage or getting-started notes:
- [Quick Start](#-quick-start) • [Features](#-features) • [Roadmap](docs/ROADMAP.md) • [Demo](#-demo) • [Docs](docs/README.md) • [Community](#-community)
- ## 🚀 Quick Start
- ### 1. Run Pre-flight Check (Required)

- Source: https://github.com/hkjarral/AVA-AI-Voice-Agent-for-Asterisk
- Extracted from upstream docs: https://raw.githubusercontent.com/hkjarral/AVA-AI-Voice-Agent-for-Asterisk/HEAD/README.md

## Documentation

- https://github.com/hkjarral/AVA-AI-Voice-Agent-for-Asterisk

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/deploy-a-self-hosted-phone-call-agent-for-asterisk-and-freepbx-with-ava/)
