---
title: "OpenCode Multi-Model AI Coding Agent CLI"
description: "An open-source terminal-native AI coding agent written in Go that supports 75+ LLMs including Claude, GPT, Gemini, and local models. Provides file editing, code generation, shell command execution, and project understanding without subscription fees."
slug: "opencode-multi-model-ai-coding-agent-cli"
category:
  - "Developer Tools"
framework:
  - "Custom Agents"
verification: "security_reviewed"
source: "https://github.com/opencode-ai/opencode"
tool_ecosystem:
  github_repo: "opencode-ai/opencode"
  github_stars: 11729
listed: true
---

# OpenCode Multi-Model AI Coding Agent CLI

An open-source terminal-native AI coding agent written in Go that supports 75+ LLMs including Claude, GPT, Gemini, and local models. Provides file editing, code generation, shell command execution, and project understanding without subscription fees.

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
clawhub install opencode-multi-model-ai-coding-agent-cli
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

OpenCode is a free, open-source AI coding agent built for the terminal, written in Go. With support for over 75 language models from multiple providers, it gives developers a flexible alternative to proprietary coding assistants. The project has garnered over 11,000 GitHub stars and active community contribution.
How It Works
OpenCode runs as an interactive TUI application in your terminal. You describe what you want to build, fix, or understand in natural language, and the agent reads your codebase, plans changes, edits files, and can execute shell commands to verify its work. It maintains conversation context across turns, understanding your project structure and prior decisions.
The agent connects to any supported LLM provider through a unified configuration. You can use Claude via Anthropic, GPT models via OpenAI, Gemini via Google, or run local models through Ollama. Switching between models mid-session is supported, and you can configure different models for different tasks like code generation versus code review.
Key Features
File operations include reading, creating, editing, and searching across your project. The agent understands project structure through automatic codebase indexing. Shell command execution lets it run tests, install dependencies, and verify changes. Built-in LSP integration provides type-aware code understanding. Session management preserves conversation history and project context.
Integration Points
OpenCode installs as a single binary via go install, Homebrew, or direct download. It reads standard environment variables for API keys (ANTHROPIC_API_KEY, OPENAI_API_KEY, etc.) and stores configuration in ~/.config/opencode. The tool works with any Git repository and respects .gitignore patterns. MCP server support enables extending its capabilities with additional tools and data sources.
Output
OpenCode produces file modifications directly in your working directory, terminal output from executed commands, and conversational explanations of what it did and why. All changes are made to real files that you can review with git diff before committing.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/opencode-multi-model-ai-coding-agent-cli/)
