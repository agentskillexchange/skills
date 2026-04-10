---
name: "LLM Command-Line Interface for Large Language Models"
description: "LLM is a Python CLI tool and library by Simon Willison for accessing OpenAI, Anthropic Claude, Google Gemini, Meta Llama, and dozens of other language models from the terminal. It supports API-based and local models via plugins, conversation logging to SQLite, templates, embeddings, and tool use."
verification: security_reviewed
source: "https://github.com/simonw/llm"
category:
  - "Developer Tools"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "simonw/llm"
  github_stars: 11508
---

# LLM Command-Line Interface for Large Language Models

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

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/llm-command-line-interface-large-language-models/)
