---
name: "Plandex AI Coding Agent for Large Projects"
description: "Plandex is an open-source terminal-based AI coding agent designed for large projects and complex tasks. It handles up to 2M tokens of context, uses a diff sandbox for safe changes, and supports multi-model workflows across Anthropic, OpenAI, and Google providers."
category: "Developer Tools"
framework: "Custom Agents"
verification: security_reviewed
source: "https://github.com/plandex-ai/plandex"
tool_ecosystem:
  github_repo: "plandex-ai/plandex"
  github_stars: 15183
---
# Plandex AI Coding Agent for Large Projects

Plandex is an open-source terminal-based AI coding agent designed for large projects and complex tasks. It handles up to 2M tokens of context, uses a diff sandbox for safe changes, and supports multi-model workflows across Anthropic, OpenAI, and Google providers.

Overview

Plandex is an open-source, terminal-based AI development tool that plans and executes large coding tasks spanning many steps and dozens of files. Built in Go, it differentiates itself from other AI coding agents by offering a cumulative diff review sandbox, automatic project indexing with tree-sitter, and configurable autonomy levels.



Key Features



- 2M Token Context Window: Plandex can handle up to 2M tokens of context directly (~100k per file) and index directories with 20M+ tokens using tree-sitter project maps, loading only what is needed for each step.



- Diff Review Sandbox: AI-generated changes are kept separate from your project files in a sandbox. You can review, revise, and selectively apply changes, preventing the mess that other tools can leave behind.



- Multi-Model Support: Combine models from Anthropic (Claude), OpenAI (GPT-4), Google (Gemini), and open-source providers. Context caching is used across the board to reduce costs and latency.



- Configurable Autonomy: From full auto mode where Plandex loads files, plans, implements, and debugs automatically, to fine-grained step-by-step control for sensitive tasks.



- Automated Debugging: Plandex can automatically debug terminal commands including builds, linters, tests, and deployments. Browser application debugging is also supported when Chrome is installed.



- Tree-Sitter Integration: Fast project map generation and syntax validation supporting 30+ languages for reliable code understanding.



How It Works

As a skill, Plandex enables agents to handle large-scale coding tasks that would overwhelm simpler tools. The agent runs plandex in a project directory, loads relevant files into context, and issues natural language instructions. Plandex plans the changes, implements them across multiple files, and places results in its sandbox for review. The REPL mode provides fuzzy auto-complete for commands and file loading.



Technical Details

Plandex is written in Go and distributed as a CLI binary. It can be installed via curl script or built from source. The tool uses a client-server architecture, with an optional self-hosted Plandex server for team collaboration. It is licensed under MIT with over 15,000 GitHub stars. The CLI supports version-controlled plan branches for experimenting with different approaches.



Integration Points



- CLI interface for scripting and piping data into context



- Git-aware diff generation and application



- Self-hosted server option for team workflows



- Model pack configuration for mixing and matching LLM providers

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill plandex-ai-coding-agent-large-projects
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill plandex-ai-coding-agent-large-projects -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill plandex-ai-coding-agent-large-projects -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill plandex-ai-coding-agent-large-projects -a codex
```

### OpenClaw

```bash
clawhub install plandex-ai-coding-agent-large-projects
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/plandex-ai-coding-agent-large-projects/)
