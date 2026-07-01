---
name: "Serve local model endpoints for agent tests with OpenLLM"
slug: "serve-local-model-endpoints-for-agent-tests-with-openllm"
description: "Launch an OpenAI-compatible OpenLLM server for a chosen open model, point an agent runtime at it, and compare behavior before production use."
github_stars: 12346
verification: "security_reviewed"
source: "https://github.com/bentoml/OpenLLM"
author: "BentoML"
publisher_type: "open-source organization"
category: "Developer Tools"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "bentoml/OpenLLM"
  github_stars: 12346
  npm_package: "openllm"
  npm_weekly_downloads: 0
---

# Serve local model endpoints for agent tests with OpenLLM

Launch an OpenAI-compatible OpenLLM server for a chosen open model, point an agent runtime at it, and compare behavior before production use.

## Prerequisites

OpenLLM, Python environment, supported open model, required GPU/CPU resources, Hugging Face token for gated models, agent runtime or SDK that can call an OpenAI-compatible endpoint.

## Installation

Use the upstream install or setup path that matches your environment:
- pip install openllm # or pip3 install openllm

Requirements and caveats from upstream:
- <summary>OpenAI Python client</summary>
- python

Basic usage or getting-started notes:
- OpenLLM allows developers to run **any open-source LLMs** (Llama 3.3, Qwen2.5, Phi3 and [more](#supported-models)) or **custom models** as **OpenAI-compatible APIs** with a single command. It features a [built-in chat...
- Run the following commands to install OpenLLM and explore it interactively.
- OpenLLM supports a wide range of state-of-the-art open-source LLMs. You can also add a [model repository to run custom models](#set-up-a-custom-repository) with OpenLLM.

- Source: https://github.com/bentoml/OpenLLM
- Extracted from upstream docs: https://raw.githubusercontent.com/bentoml/OpenLLM/HEAD/README.md

## Documentation

- https://github.com/bentoml/OpenLLM

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/serve-local-model-endpoints-for-agent-tests-with-openllm/)
