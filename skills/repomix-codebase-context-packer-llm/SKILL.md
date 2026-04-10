---
title: "Repomix Codebase Context Packer for LLMs"
description: "Repomix packs an entire code repository into a single AI-friendly file optimized for LLM consumption. It provides token counting, security scanning via Secretlint, Tree-sitter-based code compression, and outputs in XML, Markdown, or plain text format."
slug: "repomix-codebase-context-packer-llm"
category:
  - "Developer Tools"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://github.com/yamadashy/repomix"
tool_ecosystem:
  github_repo: "yamadashy/repomix"
  github_stars: 22816
  npm_package: "repomix"
  npm_weekly_downloads: 53411
---

# Repomix Codebase Context Packer for LLMs

Repomix packs an entire code repository into a single AI-friendly file optimized for LLM consumption. It provides token counting, security scanning via Secretlint, Tree-sitter-based code compression, and outputs in XML, Markdown, or plain text format.

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
clawhub install repomix-codebase-context-packer-llm
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Repomix is an open-source TypeScript CLI tool that packs an entire code repository into a single file formatted specifically for consumption by Large Language Models. With over 22,000 GitHub stars and active development, it has become the go-to tool for developers who need to feed codebases to Claude, ChatGPT, Gemini, DeepSeek, and other AI assistants.
The core operation is straightforward: run npx repomix@latest in any project directory, and Repomix generates a repomix-output.xml file containing the entire repository structure and file contents. The output format is AI-optimized with clear file boundaries, directory trees, and metadata that LLMs can parse effectively. Output can be configured as XML (default), Markdown, or plain text.
Key features include token counting for each file and the entire repository (critical for managing LLM context limits), automatic Git-awareness that respects .gitignore and .repomixignore files, and built-in security scanning via Secretlint to prevent accidental inclusion of API keys, passwords, or other secrets. The --compress flag uses Tree-sitter to extract only key code elements (function signatures, class definitions, type declarations), reducing token count while preserving structural understanding.
Repomix is available through multiple installation methods: npx (zero-install), npm global install, yarn, bun, and Homebrew. It also provides a web interface at repomix.com for browser-based usage, a Chrome extension that adds a Repomix button to GitHub repository pages, a Firefox add-on, and an MCP (Model Context Protocol) server for direct integration with AI agents that support MCP.
Configuration is handled via a repomix.config.json file where users can specify include/exclude patterns, output format, compression settings, and custom instructions to prepend to the output. The tool is MIT-licensed and installable via npm (npm install -g repomix). It was nominated for the Powered by AI category at JSNation Open Source Awards 2025.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/repomix-codebase-context-packer-llm/)
