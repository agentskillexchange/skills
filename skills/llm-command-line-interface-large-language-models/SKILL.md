---
title: "LLM Command-Line Interface for Large Language Models"
description: "LLM is a Python CLI tool and library by Simon Willison for accessing OpenAI, Anthropic Claude, Google Gemini, Meta Llama, and dozens of other language models from the terminal. It supports API-based and local models via plugins, conversation logging to SQLite, templates, embeddings, and tool use."
slug: "llm-command-line-interface-large-language-models"
category:
  - "Developer Tools"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/simonw/llm"
tool_ecosystem:
  github_repo: "simonw/llm"
  github_stars: 11508
listed: true
---

# LLM Command-Line Interface for Large Language Models

LLM is a Python CLI tool and library by Simon Willison for accessing OpenAI, Anthropic Claude, Google Gemini, Meta Llama, and dozens of other language models from the terminal. It supports API-based and local models via plugins, conversation logging to SQLite, templates, embeddings, and tool use.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install llm-command-line-interface-large-language-models
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

LLM is a versatile command-line tool and Python library created by Simon Willison that provides a unified interface for interacting with large language models. It supports OpenAI (GPT-4, GPT-4o), Anthropic Claude, Google Gemini, Meta Llama, and dozens of other models through a plugin architecture that works with both remote APIs and locally-running models.
Core Features
Send prompts directly from the terminal with llm "explain this error", pipe command output through models with cat error.log | llm "what went wrong?", and maintain interactive chat sessions with llm chat. Every prompt and response is automatically logged to a local SQLite database for later review, search, and analysis.
Plugin Ecosystem
LLM features a rich plugin ecosystem. Install llm-ollama to use Ollama-hosted local models, llm-claude-3 for Anthropic models, llm-gemini for Google models, and many more. Plugins can add new model providers, embedding models, and custom functionality. Over 100 plugins are available in the directory.
Templates and Fragments
Define reusable prompt templates with llm templates to standardize common workflows. Fragments allow inserting pre-defined text blocks into prompts. Model aliases let you create shortcuts like llm -m fast "quick question" mapped to your preferred model.
Embeddings
LLM includes a full embedding subsystem for generating, storing, and searching vector embeddings. Use llm embed to embed text, llm similar to find semantically similar content, and build lightweight RAG pipelines entirely from the command line.
Tool Use and Schemas
Recent versions support tool use (function calling) and structured output via JSON schemas, enabling LLMs to interact with external systems and return validated, typed responses directly from CLI invocations.
Installation
Install via pip: pip install llm. Configure API keys with llm keys set openai. The tool requires Python 3.8+ and stores all data in ~/.llm/ by default.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/llm-command-line-interface-large-language-models/)
