---
name: "Ollama Local Large Language Model Runner and Serving Platform"
description: "Ollama makes it simple to run large language models locally on your machine. It provides a command-line interface and REST API to download, run, and manage models like DeepSeek, Llama, Gemma, Qwen, and Mistral with a single command."
category: "Developer Tools"
framework: "Multi-Framework"
verification: listed
source: "https://github.com/ollama/ollama"
---
# Ollama Local Large Language Model Runner and Serving Platform

Ollama makes it simple to run large language models locally on your machine. It provides a command-line interface and REST API to download, run, and manage models like DeepSeek, Llama, Gemma, Qwen, and Mistral with a single command.

## Overview

Ollama is an open-source platform for running large language models locally on macOS, Linux, and Windows. With over 166,000 GitHub stars, it has become the standard tool for local LLM inference, giving developers and AI practitioners a simple way to run powerful models without cloud dependencies or API costs.

How It Works

Ollama bundles model weights, configuration, and runtime into a single package managed through a simple CLI. Running `ollama run gemma3` downloads the model (if needed) and starts an interactive chat session. Under the hood, Ollama uses llama.cpp for inference, supporting NVIDIA GPU acceleration, Apple Metal, and CPU-only modes.

REST API

Ollama exposes an OpenAI-compatible REST API on localhost:11434, making it a drop-in replacement for OpenAI endpoints in existing applications. The `/api/chat`, `/api/generate`, and `/api/embeddings` endpoints support streaming, JSON mode, and tool calling. This means any application built for the OpenAI API can be pointed at Ollama with minimal changes.

Model Library

The Ollama model library at ollama.com/library hosts hundreds of pre-quantized models ready to run. Models range from small 1B parameter models that run on laptops to large 70B+ models for powerful workstations. Custom models can be created using Modelfiles that define system prompts, parameters, and adapter layers.

Client Libraries

Official Python (`pip install ollama`) and JavaScript (`npm i ollama`) client libraries provide typed interfaces for all API endpoints. The Python library supports both sync and async usage, while the JavaScript library works in Node.js and browser environments.

Agent Integration

Ollama integrates directly with coding agents like Claude Code, Codex, OpenCode, and OpenClaw. Running `ollama launch claude` or `ollama launch openclaw` connects local models to agent workflows. This makes Ollama the backbone for offline and private AI assistant deployments across messaging platforms.

Installation

Install with a single command: `curl -fsSL https://ollama.com/install.sh | sh` on Linux/macOS, or download the installer for Windows. Docker images are available as `ollama/ollama` on Docker Hub for containerized deployments.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill ollama-local-llm-runner-2
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill ollama-local-llm-runner-2 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill ollama-local-llm-runner-2 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill ollama-local-llm-runner-2 -a codex
```

### OpenClaw

```bash
clawhub install ollama-local-llm-runner-2
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ollama-local-llm-runner-2/)
