---
name: "gptme — Terminal AI Agent with Local Tools"
slug: "gptme-terminal-ai-agent-with-local-tools"
description: "gptme is an open-source Python framework for running LLM-powered agents in your terminal with access to shell commands, file editing, browser control, Python execution, and persistent memory. It supports OpenAI, Anthropic, Google Gemini, local models via Ollama and llama.cpp, and OpenRouter, making it suitable for offline, privacy-focused, or multi-provider agentic workflows. Built for autonomous operation with session persistence and tool-native agent loops."
github_stars: 4355
verification: "listed"
source: "https://github.com/gptme/gptme"
category: "Developer Tools"
framework: "Custom Agents"
tool_ecosystem:
  github_repo: "gptme/gptme"
  github_stars: 4355
---

# gptme — Terminal AI Agent with Local Tools

gptme is an open-source framework for building and running LLM-powered agents directly in your terminal. It equips agents with real local tools — shell execution, file editing, browser control, Python REPL, and persistent context — and supports multiple model providers out of the box.

Unlike browser-based AI assistants, gptme agents run natively in your environment and can read your files, run commands, browse the web, and persist state across sessions. It is designed for autonomous operation: agents can be left running, pick up work from structured task files, and chain tool calls without per-step human confirmation.

## Key Features

- **Multi-provider**: OpenAI, Anthropic Claude, Google Gemini, OpenRouter, Ollama (local), llama.cpp, and any OpenAI-compatible endpoint
- **Rich tool set**: Shell (`bash`), file read/write/patch, Python REPL, browser automation (Playwright), `computer` (screenshot + click), RAG over local documents
- **Persistent sessions**: Conversations are stored locally; resume any session by name
- **Autonomous loops**: Built-in support for long-running unattended agents with structured task management and journaling
- **Local-first**: Works fully offline with local models; no cloud dependency required
- **Extensible**: MCP server support, custom tools, skill injection via `gptme.toml`

## Installation

```bash
# Install with pip (minimal)
pip install gptme

# Install with all optional extras (browser, computer, RAG)
pip install 'gptme[browser,computer,rag]'

# Install with uv (recommended for project isolation)
uv tool install gptme
```

Requires Python 3.10+.

## Basic Usage

Because gptme can run shell commands, edit files, control a browser, and persist sessions locally, run it with an explicit operating boundary. Prefer a project sandbox or worktree, review enabled tool permissions before unattended runs, and avoid pointing agents at sensitive directories unless you intend those files to be inspected or modified.

```bash
# Start an interactive session
gptme "Write a Python script to list all .md files in the current dir"

# Run non-interactively (for scripting and automation)
gptme --non-interactive "Fix the failing test in tests/test_api.py"

# Use a specific provider / model
gptme -m anthropic/claude-opus-4-5 "Review the PR diff and summarize findings"

# Use a local model via Ollama
OPENAI_API_BASE="http://localhost:11434/v1" gptme -m local/llama3.2 "Hello"

# Resume a named session
gptme --name my-project "Continue where we left off"
```

## Autonomous Agent Setup

gptme ships an agent template for building persistent autonomous agents with task queues, journals, and structured work loops. See [gptme-agent-template](https://github.com/gptme/gptme-agent-template) for the scaffold.

```bash
# Install gptme-agent-template to bootstrap a new agent workspace
git clone https://github.com/gptme/gptme-agent-template.git my-agent
cd my-agent
./scripts/fork.sh . MyAgent
gptme "Hello, I am MyAgent. What shall we build today?"
```

## Source

- [gptme on GitHub](https://github.com/gptme/gptme)
- [Documentation](https://gptme.org/docs/)
- [Agent Skill Exchange](https://agentskillexchange.com/skills/gptme-terminal-ai-agent-with-local-tools/)
