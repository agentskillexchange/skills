---
name: "Aider AI Pair Programming CLI Agent"
description: "Aider is an open-source AI pair programming tool that runs in your terminal, letting you collaborate with LLMs to edit code across your entire codebase. With 42k+ GitHub stars and 15 billion tokens processed weekly, it features deep git integration, repo-wide code mapping, and support for 100+ programming languages."
category: "Developer Tools"
framework: "Custom Agents"
verification: security_reviewed
source: "https://github.com/Aider-AI/aider"
tool_ecosystem:
  github_repo: "Aider-AI/aider"
  github_stars: 42670
---
# Aider AI Pair Programming CLI Agent

Aider is an open-source AI pair programming tool that runs in your terminal, letting you collaborate with LLMs to edit code across your entire codebase. With 42k+ GitHub stars and 15 billion tokens processed weekly, it features deep git integration, repo-wide code mapping, and support for 100+ programming languages.

## Overview

Aider is a terminal-based AI pair programming agent that lets developers collaborate with large language models to write, edit, and refactor code directly in their existing codebases. Maintained at github.com/Aider-AI/aider with 42,000+ GitHub stars and over 4.1 million installations, it is the most widely deployed open-source CLI coding agent.

What makes Aider distinct from simple code generation tools is its deep understanding of your project. It builds a repository map of your entire codebase using tree-sitter parsing, which gives the LLM awareness of function signatures, class definitions, and module relationships across files. This means you can ask Aider to make changes that span multiple files — adding a new API endpoint with its route handler, database model, tests, and documentation — and it understands how the pieces connect.

Git integration is core to Aider’s workflow. Every change the AI makes is automatically committed with a descriptive commit message. This means you can use standard git tools to review diffs, cherry-pick changes, or revert anything the AI did. The tool also integrates with your existing linters and test suites, automatically running them after changes and fixing any issues detected.

Aider supports virtually every major LLM provider. It works best with Claude 3.7 Sonnet, DeepSeek R1, and GPT-4o, but connects to any OpenAI-compatible API including local models via Ollama. It handles over 100 programming languages including Python, JavaScript, TypeScript, Rust, Go, Ruby, C++, PHP, and more.

A skill leveraging Aider would enable an agent to perform sophisticated multi-file code edits with full version control safety. The agent could implement features, fix bugs, refactor code, or add tests — all with automatic commits and rollback capability. Install via `pip install aider-chat`. Aider is Apache 2.0 licensed with active daily development.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill aider-ai-pair-programming-cli-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill aider-ai-pair-programming-cli-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill aider-ai-pair-programming-cli-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill aider-ai-pair-programming-cli-agent -a codex
```

### OpenClaw

```bash
clawhub install aider-ai-pair-programming-cli-agent
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aider-ai-pair-programming-cli-agent/)
