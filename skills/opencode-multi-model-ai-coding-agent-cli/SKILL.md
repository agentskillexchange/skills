---
title: OpenCode Multi-Model AI Coding Agent CLI
description: OpenCode is a free, open-source AI coding agent built for the terminal,
  written in Go. With support for over 75 language models from multiple providers,
  it gives developers a flexible alternative to proprietary coding assistants. The
  project has garnered over 11,000 GitHub stars and active community contribution.
  How It Works OpenCode runs as an interactive TUI application in your terminal. You
  describe what you want to build, fix, or understand in natural language, and the
  agent reads your codebase, plans changes, edits files, and can execute shell commands
  to verify its work. It maintains conversation context across turns, understanding
  your project structure and prior decisions. The agent connects to any supported
  LLM provider through a unified configuration. You can use Claude via Anthropic,
  GPT models via OpenAI, Gemini via Google, or run local models through Ollama. Switching
  between models mid-session is supported, and you can configure different models
  for different tasks like code generation versus code review. Key Features File operations
  include reading, creating, editing, and searching across your project. The agent
  understands project structure through automatic codebase indexing. Shell command
  execution lets it run tests, install dependencies, and verify changes. Built-in
  LSP integration provides type-aware code understanding. Session management preserves
  conversation history and project context. Integration Points OpenCode installs as
  a single binary via go install, Homebrew, or direct download. It reads standard
  environment variables for API keys (ANTHROPIC_API_KEY, OPENAI_API_KEY, etc.) and
  stores configuration in ~/.config/opencode. The tool works with any Git repository
  and respects .gitignore patterns. MCP server support enables extending its capabilities
  with additional tools and data sources. Output OpenCode produces file modifications
  directly in your working directory, terminal output from executed commands, and
  conversational explanations of what it did and why. All changes are made to real
  files that you can review with git diff before committing.
verification: security_reviewed
source: https://github.com/opencode-ai/opencode
category:
- Developer Tools
framework:
- Custom Agents
tool_ecosystem:
  github_repo: opencode-ai/opencode
  github_stars: 11729
---

# OpenCode Multi-Model AI Coding Agent CLI

OpenCode is a free, open-source AI coding agent built for the terminal, written in Go. With support for over 75 language models from multiple providers, it gives developers a flexible alternative to proprietary coding assistants. The project has garnered over 11,000 GitHub stars and active community contribution. How It Works OpenCode runs as an interactive TUI application in your terminal. You describe what you want to build, fix, or understand in natural language, and the agent reads your codebase, plans changes, edits files, and can execute shell commands to verify its work. It maintains conversation context across turns, understanding your project structure and prior decisions. The agent connects to any supported LLM provider through a unified configuration. You can use Claude via Anthropic, GPT models via OpenAI, Gemini via Google, or run local models through Ollama. Switching between models mid-session is supported, and you can configure different models for different tasks like code generation versus code review. Key Features File operations include reading, creating, editing, and searching across your project. The agent understands project structure through automatic codebase indexing. Shell command execution lets it run tests, install dependencies, and verify changes. Built-in LSP integration provides type-aware code understanding. Session management preserves conversation history and project context. Integration Points OpenCode installs as a single binary via go install, Homebrew, or direct download. It reads standard environment variables for API keys (ANTHROPIC_API_KEY, OPENAI_API_KEY, etc.) and stores configuration in ~/.config/opencode. The tool works with any Git repository and respects .gitignore patterns. MCP server support enables extending its capabilities with additional tools and data sources. Output OpenCode produces file modifications directly in your working directory, terminal output from executed commands, and conversational explanations of what it did and why. All changes are made to real files that you can review with git diff before committing.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/opencode-multi-model-ai-coding-agent-cli/)
