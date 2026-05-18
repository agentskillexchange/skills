---
name: "Kokoro FastAPI OpenAI-Compatible Text-to-Speech Server"
slug: "kokoro-fastapi-openai-compatible-text-to-speech-server"
description: "Kokoro-FastAPI is a Dockerized FastAPI wrapper around the Kokoro-82M text-to-speech model with OpenAI-compatible speech endpoints. It supports local TTS serving, multi-language synthesis, web UI access, and timestamped audio generation workflows."
github_stars: 4671
verification: "listed"
source: "https://github.com/remsky/Kokoro-FastAPI"
author: "remsky"
publisher_type: "Individual Developer"
category: "Media & Transcription"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "remsky/Kokoro-FastAPI"
  github_stars: 4671
---

# Kokoro FastAPI OpenAI-Compatible Text-to-Speech Server

Kokoro-FastAPI is a Dockerized FastAPI wrapper around the Kokoro-82M text-to-speech model with OpenAI-compatible speech endpoints. It supports local TTS serving, multi-language synthesis, web UI access, and timestamped audio generation workflows.

## Prerequisites

Docker

## Installation

Use the upstream install or setup path that matches your environment:
- docker run -p 8880:8880 ghcr.io/remsky/kokoro-fastapi-cpu:latest # CPU, or:
- docker run --gpus all -p 8880:8880 ghcr.io/remsky/kokoro-fastapi-gpu:latest # NVIDIA GPU, or:
- docker run --device=/dev/kfd --device=/dev/dri -p 8880:8880 ghcr.io/remsky/kokoro-fastapi-rocm:latest # AMD GPU (ROCm, experimental, amd64 only)
- git clone https://github.com/remsky/Kokoro-FastAPI.git

Requirements and caveats from upstream:
- <summary>Quickest Start (docker run)</summary>
- <summary>Quick Start (docker compose) </summary>
- Install prerequisites, and start the service using Docker Compose (Full setup including UI):

Basic usage or getting-started notes:
- Pre built images are available to run, with arm/multi-arch support, and baked in models
- ### Named versions should be pinned for your regular usage.

- Source: https://github.com/remsky/Kokoro-FastAPI
- Extracted from upstream docs: https://raw.githubusercontent.com/remsky/Kokoro-FastAPI/HEAD/README.md

## Documentation

- https://github.com/remsky/Kokoro-FastAPI/wiki

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kokoro-fastapi-openai-compatible-text-to-speech-server/)
