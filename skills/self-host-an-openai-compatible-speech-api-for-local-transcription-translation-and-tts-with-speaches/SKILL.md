---
title: "Self-host an OpenAI-compatible speech API for local transcription, translation, and TTS with Speaches"
slug: "self-host-an-openai-compatible-speech-api-for-local-transcription-translation-and-tts-with-speaches"
description: "Use Speaches when an agent stack expects OpenAI-style audio endpoints but you want a self-hosted speech backend for transcription, translation, and text-to-speech instead of a hosted API."
verification: "security_reviewed"
source: "https://github.com/speaches-ai/speaches"
author: "speaches-ai"
publisher_type: "company"
category: "Media & Transcription"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "speaches-ai/speaches"
  github_stars: 3170
---

# Self-host an OpenAI-compatible speech API for local transcription, translation, and TTS with Speaches

Use Speaches when an agent stack expects OpenAI-style audio endpoints but you want a self-hosted speech backend for transcription, translation, and text-to-speech instead of a hosted API.

## Prerequisites

Docker or Python-based deployment environment, CPU or GPU runtime, supported speech models, and any client or agent stack that can call OpenAI-compatible audio endpoints.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Deploy Speaches with Docker or the supported local setup from the project docs, download or configure the speech models you plan to serve, start the API, then point your agent or application at the Speaches base URL using the same OpenAI-style audio calls it already expects.
```

## Documentation

- https://speaches.ai

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/self-host-an-openai-compatible-speech-api-for-local-transcription-translation-and-tts-with-speaches/)
