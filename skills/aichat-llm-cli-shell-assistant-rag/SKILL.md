---
title: "AIChat All-in-One LLM CLI with Shell Assistant and RAG"
description: "AIChat is an all-in-one LLM CLI tool built in Rust by sigoden, with nearly 10,000 GitHub stars. It provides shell assistance, an interactive chat REPL, retrieval-augmented generation (RAG), AI tool calling, and agent capabilities through a fast, single-binary application that integrates with over 20 LLM providers.\nMulti-Provider Integration\nAIChat connects to OpenAI, Claude, Gemini (Google AI Studio), Ollama, Groq, Azure-OpenAI, VertexAI, Bedrock, GitHub Models, Mistral, DeepSeek, AI21, XAI Grok, Cohere, Perplexity, Cloudflare, OpenRouter, and any OpenAI-compatible API. Switch between providers and models with a single configuration change, keeping your workflows provider-agnostic.\nShell Assistant\nDescribe tasks in natural language and AIChat generates the corresponding shell command for your OS and shell environment. It detects whether you are on macOS with zsh, Linux with bash, or Windows with PowerShell and adjusts commands accordingly. This eliminates searching for command syntax and flags.\nChat REPL\nThe interactive REPL supports tab autocompletion, multi-line input, history search, configurable keybindings, and custom prompts. Sessions can be saved and resumed, and conversations can reference previous context. The REPL provides a rich terminal experience comparable to dedicated chat applications.\nRAG (Retrieval-Augmented Generation)\nAIChat includes built-in RAG that indexes local files, directories, and URLs for context-aware responses. It chunks documents, generates embeddings, and retrieves relevant passages automatically. This allows you to ask questions about your codebase, documentation, or any text corpus directly from the terminal.\nFlexible Input\nAccept input from stdin pipes, local files and directories, remote URLs, and direct arguments. Combine multiple sources in a single command: aichat -f image.png -f data.txt \"analyze these\". Vision models can process images alongside text for multimodal workflows.\nAI Tools and Agents\nAIChat supports function calling and tool use with compatible models. Define custom tools that the LLM can invoke, enabling automated workflows that combine AI reasoning with system operations. Agent mode chains multiple tool calls to complete complex tasks.\nInstallation\nInstall via cargo (cargo install aichat), Homebrew (brew install aichat), pacman, Scoop, Termux, or download pre-built binaries for macOS, Linux, and Windows from GitHub Releases. Configuration lives in a single YAML file."
verification: security_reviewed
source: "https://github.com/sigoden/aichat"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "sigoden/aichat"
  github_stars: 9754
---

# AIChat All-in-One LLM CLI with Shell Assistant and RAG

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

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/aichat-llm-cli-shell-assistant-rag
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/aichat-llm-cli-shell-assistant-rag` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aichat-llm-cli-shell-assistant-rag/)
