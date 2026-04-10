---
name: Kokoro FastAPI OpenAI-Compatible Text-to-Speech Server
description: Kokoro-FastAPI is a Dockerized FastAPI wrapper around the Kokoro-82M
  text-to-speech model with OpenAI-compatible speech endpoints. It supports local
  TTS serving, multi-language synthesis, web UI access, and timestamped audio generation
  workflows.
verification: security_reviewed
source: https://github.com/remsky/Kokoro-FastAPI
category:
- Media &amp; Transcription
framework:
- Multi-Framework
tool_ecosystem:
  github_repo: remsky/Kokoro-FastAPI
  github_stars: 4671
---
# Kokoro FastAPI OpenAI-Compatible Text-to-Speech Server

Kokoro-FastAPI is a self-hostable text-to-speech server built around the Kokoro-82M model and exposed through a FastAPI application. The upstream project packages the model behind an OpenAI-compatible speech endpoint, making it much easier to drop into existing agent and automation systems that already know how to call speech APIs. The project README highlights multi-language support, CPU and NVIDIA GPU inference modes, a local web UI, debug endpoints, phoneme-aware generation, voice mixing, and per-word timestamped caption output.
The upstream source is the remsky/Kokoro-FastAPI repository. It is distributed with Docker and Docker Compose workflows, plus wiki-based integration guides for environments such as Kubernetes, DigitalOcean, and OpenWebUI. That makes it a strong fit for teams that want local or self-hosted speech generation instead of routing every request through a managed SaaS voice provider.
An ASE skill built around Kokoro-FastAPI is useful when an agent needs to stand up a local TTS service, generate speech from prompts, produce aligned captions, or expose a speech endpoint to downstream apps that expect an OpenAI-like interface. Typical outputs include generated audio files, API-ready speech responses, caption timestamps, deployment guidance for CPU or GPU hosts, and integration steps for chat interfaces or voice-enabled assistants. It also pairs well with content narration, accessibility tooling, demo voiceovers, and internal prototyping where controllable, self-hosted TTS infrastructure is more important than a managed black-box API.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kokoro-fastapi-openai-compatible-text-to-speech-server/)
