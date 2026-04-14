---
title: "Repomix Codebase Context Packer for LLMs"
description: "Repomix packs an entire code repository into a single AI-friendly file optimized for LLM consumption. It provides token counting, security scanning via Secretlint, Tree-sitter-based code compression, and outputs in XML, Markdown, or plain text format."
verification: security_reviewed
source: "https://github.com/yamadashy/repomix"
category:
  - "Developer Tools"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "yamadashy/repomix"
  github_stars: 22816
  npm_package: "repomix"
  npm_weekly_downloads: 54823
---

# Repomix Codebase Context Packer for LLMs

Repomix is an open-source TypeScript CLI tool that packs an entire code repository into a single file formatted specifically for consumption by Large Language Models. With over 22,000 GitHub stars and active development, it has become the go-to tool for developers who need to feed codebases to Claude, ChatGPT, Gemini, DeepSeek, and other AI assistants.

The core operation is straightforward: run npx repomix@latest in any project directory, and Repomix generates a repomix-output.xml file containing the entire repository structure and file contents. The output format is AI-optimized with clear file boundaries, directory trees, and metadata that LLMs can parse effectively. Output can be configured as XML (default), Markdown, or plain text.

Key features include token counting for each file and the entire repository (critical for managing LLM context limits), automatic Git-awareness that respects .gitignore and .repomixignore files, and built-in security scanning via Secretlint to prevent accidental inclusion of API keys, passwords, or other secrets. The --compress flag uses Tree-sitter to extract only key code elements (function signatures, class definitions, type declarations), reducing token count while preserving structural understanding.

Repomix is available through multiple installation methods: npx (zero-install), npm global install, yarn, bun, and Homebrew. It also provides a web interface at repomix.com for browser-based usage, a Chrome extension that adds a Repomix button to GitHub repository pages, a Firefox add-on, and an MCP (Model Context Protocol) server for direct integration with AI agents that support MCP.

Configuration is handled via a repomix.config.json file where users can specify include/exclude patterns, output format, compression settings, and custom instructions to prepend to the output. The tool is MIT-licensed and installable via npm (npm install -g repomix). It was nominated for the Powered by AI category at JSNation Open Source Awards 2025.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/repomix-codebase-context-packer-llm/)
