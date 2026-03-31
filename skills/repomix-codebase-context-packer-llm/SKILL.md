---
name: "Repomix Codebase Context Packer for LLMs"
description: "Repomix packs an entire code repository into a single AI-friendly file optimized for LLM consumption. It provides token counting, security scanning via Secretlint, Tree-sitter-based code compression, and outputs in XML, Markdown, or plain text format."
category: "Developer Tools"
framework: "Claude Code"
verification: security_reviewed
source: "https://github.com/yamadashy/repomix"
---
# Repomix Codebase Context Packer for LLMs

Repomix packs an entire code repository into a single AI-friendly file optimized for LLM consumption. It provides token counting, security scanning via Secretlint, Tree-sitter-based code compression, and outputs in XML, Markdown, or plain text format.

## Overview

Repomix is an open-source TypeScript CLI tool that packs an entire code repository into a single file formatted specifically for consumption by Large Language Models. With over 22,000 GitHub stars and active development, it has become the go-to tool for developers who need to feed codebases to Claude, ChatGPT, Gemini, DeepSeek, and other AI assistants.

The core operation is straightforward: run npx repomix@latest in any project directory, and Repomix generates a repomix-output.xml file containing the entire repository structure and file contents. The output format is AI-optimized with clear file boundaries, directory trees, and metadata that LLMs can parse effectively. Output can be configured as XML (default), Markdown, or plain text.

Key features include token counting for each file and the entire repository (critical for managing LLM context limits), automatic Git-awareness that respects .gitignore and .repomixignore files, and built-in security scanning via Secretlint to prevent accidental inclusion of API keys, passwords, or other secrets. The --compress flag uses Tree-sitter to extract only key code elements (function signatures, class definitions, type declarations), reducing token count while preserving structural understanding.

Repomix is available through multiple installation methods: npx (zero-install), npm global install, yarn, bun, and Homebrew. It also provides a web interface at repomix.com for browser-based usage, a Chrome extension that adds a Repomix button to GitHub repository pages, a Firefox add-on, and an MCP (Model Context Protocol) server for direct integration with AI agents that support MCP.

Configuration is handled via a repomix.config.json file where users can specify include/exclude patterns, output format, compression settings, and custom instructions to prepend to the output. The tool is MIT-licensed and installable via npm (npm install -g repomix). It was nominated for the Powered by AI category at JSNation Open Source Awards 2025.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill repomix-codebase-context-packer-llm
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill repomix-codebase-context-packer-llm -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill repomix-codebase-context-packer-llm -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill repomix-codebase-context-packer-llm -a codex
```

### OpenClaw

```bash
clawhub install repomix-codebase-context-packer-llm
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/repomix-codebase-context-packer-llm/)
