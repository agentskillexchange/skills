---
title: "Kokoro FastAPI OpenAI-Compatible Text-to-Speech Server"
description: "Kokoro-FastAPI is a Dockerized FastAPI wrapper around the Kokoro-82M text-to-speech model with OpenAI-compatible speech endpoints. It supports local TTS serving, multi-language synthesis, web UI access, and timestamped audio generation workflows."
verification: "security_reviewed"
source: "https://github.com/remsky/Kokoro-FastAPI"
author: "remsky"
publisher_type: "Individual Developer"
category:
  - "errors"
  - "error_data"
framework:
  - "errors"
  - "error_data"
tool_ecosystem:
  github_repo: "remsky/Kokoro-FastAPI"
  github_stars: 4671
---

# Kokoro FastAPI OpenAI-Compatible Text-to-Speech Server

Kokoro-FastAPI is a Dockerized FastAPI wrapper around the Kokoro-82M text-to-speech model with OpenAI-compatible speech endpoints. It supports local TTS serving, multi-language synthesis, web UI access, and timestamped audio generation workflows.

## Prerequisites

Docker

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
docker run -p 8880:8880 ghcr.io/remsky/kokoro-fastapi-cpu:latest
```

## Documentation

- https://github.com/remsky/Kokoro-FastAPI/wiki

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kokoro-fastapi-openai-compatible-text-to-speech-server/)
