---
name: "Deploy conversational voice agents with Bolna"
slug: "deploy-conversational-voice-agents-with-bolna"
description: "Build and run voice-first conversational agents by configuring telephony, ASR, LLM, and TTS providers behind a deployable orchestration service."
github_stars: 666
verification: "security_reviewed"
source: "https://github.com/bolna-ai/bolna"
author: "bolna-ai"
publisher_type: "organization"
category: "Media & Transcription"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "bolna-ai/bolna"
  github_stars: 666
---

# Deploy conversational voice agents with Bolna

Build and run voice-first conversational agents by configuring telephony, ASR, LLM, and TTS providers behind a deployable orchestration service.

## Prerequisites

Docker Compose, Redis, a telephony provider such as Twilio or Plivo, ASR/LLM/TTS provider credentials, optional ngrok for local telephony testing

## Installation

Use the upstream install or setup path that matches your environment:
- docker compose build
- docker compose up -d
- docker compose up -d bolna-app twilio-app
- docker compose up -d bolna-app plivo-app

Requirements and caveats from upstream:
- This script will check for Docker dependencies, build all services with BuildKit enabled, and start them in detached mode.
- Make sure you have Docker with Docker Compose V2 installed
- Once the docker containers are up, you can now start to create your agents and instruct them to initiate calls.

Basic usage or getting-started notes:
- A basic local setup includes usage of [Twilio](local_setup/telephony_server/twilio_api_server.py) or [Plivo](local_setup/telephony_server/plivo_api_server.py) for telephony. We have dockerized the setup in local_setup...
- Choosing Twilio: for initiating the calls one will need to set up a [Twilio account](https://www.twilio.com/docs/usage/tutorials/how-to-use-your-free-trial-account)
- The easiest way to get started is to use the provided script:

- Source: https://github.com/bolna-ai/bolna
- Extracted from upstream docs: https://raw.githubusercontent.com/bolna-ai/bolna/HEAD/README.md

## Documentation

- https://docs.bolna.ai

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/deploy-conversational-voice-agents-with-bolna/)
