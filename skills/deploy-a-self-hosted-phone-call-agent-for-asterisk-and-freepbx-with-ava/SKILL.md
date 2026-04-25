---
title: "Deploy a self-hosted phone-call agent for Asterisk and FreePBX with AVA"
description: "Bring up a self-hosted voice agent that answers, routes, or transfers live calls through Asterisk or FreePBX with a PBX-native workflow."
verification: "security_reviewed"
source: "https://github.com/hkjarral/AVA-AI-Voice-Agent-for-Asterisk"
category:
  - "Integrations & Connectors"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "hkjarral/AVA-AI-Voice-Agent-for-Asterisk"
  github_stars: 991
---

# Deploy a self-hosted phone-call agent for Asterisk and FreePBX with AVA

Use AVA when the job is to stand up a self-hosted AI phone agent inside an Asterisk or FreePBX environment, then verify a real call path from dialplan to AI engine. The upstream project is concrete about the workflow: run the preflight script, launch the admin UI and AI engine with Docker Compose, configure providers, and test live call handling through the PBX.

Invoke this instead of a hosted voice API or generic telephony product listing when the requirement is PBX-native call automation in infrastructure you control. The scope boundary is clear: AVA handles Asterisk or FreePBX backed call answering, routing, transfer, and voice-agent setup. It is not a generic voice model SDK, broad telephony platform card, or abstract conversational AI framework listing.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/deploy-a-self-hosted-phone-call-agent-for-asterisk-and-freepbx-with-ava/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/deploy-a-self-hosted-phone-call-agent-for-asterisk-and-freepbx-with-ava
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/deploy-a-self-hosted-phone-call-agent-for-asterisk-and-freepbx-with-ava`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/deploy-a-self-hosted-phone-call-agent-for-asterisk-and-freepbx-with-ava/)
