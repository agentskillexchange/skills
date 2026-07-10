---
title: "Deploy conversational voice agents with Bolna"
description: "Build and run voice-first conversational agents by configuring telephony, ASR, LLM, and TTS providers behind a deployable orchestration service."
verification: "security_reviewed"
source: "https://github.com/bolna-ai/bolna"
author: "bolna-ai"
publisher_type: "organization"
category:
  - "Media & Transcription"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "bolna-ai/bolna"
  github_stars: 666
---

# Deploy conversational voice agents with Bolna

Build and run voice-first conversational agents by configuring telephony, ASR, LLM, and TTS providers behind a deployable orchestration service.

## Prerequisites

Docker Compose, Redis, a telephony provider such as Twilio or Plivo, ASR/LLM/TTS provider credentials, optional ngrok for local telephony testing

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Clone `https://github.com/bolna-ai/bolna`, create the required `.env` from the sample configuration, run the local setup with Docker Compose from `local_setup`, connect the chosen telephony and model-provider credentials, then create and test a voice agent before deployment.
```

## Documentation

- https://docs.bolna.ai

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/deploy-conversational-voice-agents-with-bolna/)
