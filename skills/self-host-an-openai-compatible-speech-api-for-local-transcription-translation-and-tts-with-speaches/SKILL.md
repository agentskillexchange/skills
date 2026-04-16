---
title: "Self-host an OpenAI-compatible speech API for local transcription, translation, and TTS with Speaches"
description: "Use Speaches when an agent stack expects OpenAI-style audio endpoints but you want a self-hosted speech backend for transcription, translation, and text-to-speech instead of a hosted API."
verification: "security_reviewed"
source: "https://github.com/speaches-ai/speaches"
category:
  - "Media &amp; Transcription"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "speaches-ai/speaches"
  github_stars: 3170
---

# Self-host an OpenAI-compatible speech API for local transcription, translation, and TTS with Speaches

Tool: Speaches. This skill gives an agent operator a narrow, practical job: stand up a local or self-hosted speech server that speaks the OpenAI audio API shape, then swap existing agent audio workflows onto that endpoint with minimal integration churn. Speaches supports streaming transcription, translation, and speech generation, with dynamic model loading and both CPU and GPU deployment paths.

When to use it: invoke this when your agents already know how to call OpenAI-compatible speech endpoints, but you want local control over models, lower vendor dependence, or a unified speech back end for multiple clients. It is useful for voice assistants, transcription pipelines, speech-enabled support tools, and multimodal agent setups where the integration surface matters more than training or model research. Using this skill is different from using the product normally because the operator workflow is explicit: deploy the server, choose speech models, expose compatible endpoints, and repoint downstream agent tools.

Scope boundary: this is not a generic speech-product listing, not a hosted API comparison page, and not a broad model zoo entry. Its boundary is specific: run a self-hosted OpenAI-compatible speech server so existing agent pipelines can keep working while you control the runtime and model selection.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/self-host-an-openai-compatible-speech-api-for-local-transcription-translation-and-tts-with-speaches/)
