---
title: "AIChat All-in-One LLM CLI with Shell Assistant and RAG"
description: "AIChat is a comprehensive LLM command-line tool written in Rust that combines chat-REPL, shell command generation, RAG, AI tools, and multi-provider support into a single binary. It connects to 20+ LLM providers including OpenAI, Claude, Gemini, and Ollama."
slug: "aichat-llm-cli-shell-assistant-rag"
category:
  - "Developer Tools"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/sigoden/aichat"
tool_ecosystem:
  github_repo: "sigoden/aichat"
  github_stars: 9754
listed: true
---

# AIChat All-in-One LLM CLI with Shell Assistant and RAG

AIChat is a comprehensive LLM command-line tool written in Rust that combines chat-REPL, shell command generation, RAG, AI tools, and multi-provider support into a single binary. It connects to 20+ LLM providers including OpenAI, Claude, Gemini, and Ollama.

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
clawhub install aichat-llm-cli-shell-assistant-rag
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

AIChat is an all-in-one LLM CLI tool built in Rust by sigoden, with nearly 10,000 GitHub stars. It provides shell assistance, an interactive chat REPL, retrieval-augmented generation (RAG), AI tool calling, and agent capabilities through a fast, single-binary application that integrates with over 20 LLM providers.
Multi-Provider Integration
AIChat connects to OpenAI, Claude, Gemini (Google AI Studio), Ollama, Groq, Azure-OpenAI, VertexAI, Bedrock, GitHub Models, Mistral, DeepSeek, AI21, XAI Grok, Cohere, Perplexity, Cloudflare, OpenRouter, and any OpenAI-compatible API. Switch between providers and models with a single configuration change, keeping your workflows provider-agnostic.
Shell Assistant
Describe tasks in natural language and AIChat generates the corresponding shell command for your OS and shell environment. It detects whether you are on macOS with zsh, Linux with bash, or Windows with PowerShell and adjusts commands accordingly. This eliminates searching for command syntax and flags.
Chat REPL
The interactive REPL supports tab autocompletion, multi-line input, history search, configurable keybindings, and custom prompts. Sessions can be saved and resumed, and conversations can reference previous context. The REPL provides a rich terminal experience comparable to dedicated chat applications.
RAG (Retrieval-Augmented Generation)
AIChat includes built-in RAG that indexes local files, directories, and URLs for context-aware responses. It chunks documents, generates embeddings, and retrieves relevant passages automatically. This allows you to ask questions about your codebase, documentation, or any text corpus directly from the terminal.
Flexible Input
Accept input from stdin pipes, local files and directories, remote URLs, and direct arguments. Combine multiple sources in a single command: aichat -f image.png -f data.txt "analyze these". Vision models can process images alongside text for multimodal workflows.
AI Tools and Agents
AIChat supports function calling and tool use with compatible models. Define custom tools that the LLM can invoke, enabling automated workflows that combine AI reasoning with system operations. Agent mode chains multiple tool calls to complete complex tasks.
Installation
Install via cargo (cargo install aichat), Homebrew (brew install aichat), pacman, Scoop, Termux, or download pre-built binaries for macOS, Linux, and Windows from GitHub Releases. Configuration lives in a single YAML file.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aichat-llm-cli-shell-assistant-rag/)
