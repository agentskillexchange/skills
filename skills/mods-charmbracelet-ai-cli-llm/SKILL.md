---
name: "Mods AI-Powered Command-Line LLM Interface by Charmbracelet"
description: "Mods is a CLI tool by Charmbracelet that pipes stdin directly to large language models. It enables AI-powered text processing, code review, commit message generation, and data transformation from the terminal with support for OpenAI, Anthropic, and local models."
category: "Developer Tools"
framework: "Custom Agents"
verification: security_reviewed
source: "https://github.com/charmbracelet/mods"
tool_ecosystem:
  github_repo: "https://github.com/charmbracelet/mods"
  github_stars: 4515
---
# Mods AI-Powered Command-Line LLM Interface by Charmbracelet

Mods is a CLI tool by Charmbracelet that pipes stdin directly to large language models. It enables AI-powered text processing, code review, commit message generation, and data transformation from the terminal with support for OpenAI, Anthropic, and local models.

Mods by Charmbracelet brings AI-powered text processing directly to the command line. It acts as a Unix-style pipe that sends standard input to large language models and returns the result to standard output, making it composable with existing shell workflows.

Core Capabilities

Mods accepts any text via stdin and sends it to a configured LLM provider along with an optional prompt. This enables a wide range of automation scenarios: pipe git diffs for AI-powered code review, send log files for anomaly detection, transform CSV data with natural language instructions, or generate documentation from code. The tool supports multiple LLM backends including OpenAI GPT-4, Anthropic Claude, Google Gemini, Groq, and local models via Ollama and LocalAI.

Integration with Shell Workflows

Because mods follows Unix pipe conventions, it integrates seamlessly with existing CLI tools. Common patterns include git diff | mods "write a commit message", cat error.log | mods "explain these errors", and curl api.example.com | mods "summarize this JSON". The output goes to stdout by default, so it can be piped further or redirected to files.

Configuration and Model Management

Mods uses a YAML configuration file to manage API keys, model preferences, and custom aliases. Users can define named configurations for different use cases — for example, a review config that uses GPT-4 with a specific system prompt, or a quick config that uses a fast local model. The mods --settings command opens the config in your default editor.

Conversation History

Mods supports multi-turn conversations via the --continue and --continue-last flags. Previous conversations are stored locally and can be listed with mods --list or shown with mods --show. This enables iterative refinement of outputs without losing context.

Installation

Install via Homebrew with brew install charmbracelet/tap/mods, via Go with go install github.com/charmbracelet/mods@latest, or download pre-built binaries from the GitHub releases page. Packages are also available for Arch Linux, Nix, and Docker.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill mods-charmbracelet-ai-cli-llm
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill mods-charmbracelet-ai-cli-llm -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill mods-charmbracelet-ai-cli-llm -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill mods-charmbracelet-ai-cli-llm -a codex
```

### OpenClaw

```bash
clawhub install mods-charmbracelet-ai-cli-llm
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/mods-charmbracelet-ai-cli-llm/)
