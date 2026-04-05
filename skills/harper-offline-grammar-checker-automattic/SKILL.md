---
name: "Harper Offline Privacy-First Grammar Checker by Automattic"
description: "Harper is an offline, privacy-first grammar checker written in Rust by Automattic. It runs locally with sub-10ms response times, supports LSP for editor integration, compiles to WebAssembly for browser use, and provides grammar, spelling, and style checking without sending text to external servers."
category: "Content Writing & SEO"
framework: "Multi-Framework"
verification: security_reviewed
source: "https://github.com/Automattic/harper"
tool_ecosystem:
  github_repo: "Automattic/harper"
  github_stars: 10182
---
# Harper Offline Privacy-First Grammar Checker by Automattic

Harper is an offline, privacy-first grammar checker written in Rust by Automattic. It runs locally with sub-10ms response times, supports LSP for editor integration, compiles to WebAssembly for browser use, and provides grammar, spelling, and style checking without sending text to external servers.

Harper is an open-source grammar checker built in Rust by Automattic (the company behind WordPress.com). It runs entirely offline on the user’s device, providing grammar, spelling, and style suggestions in under 10 milliseconds — no network requests, no cloud processing, no privacy concerns about text leaving the machine.



The architecture is designed for integration across multiple surfaces. Harper compiles to WebAssembly for browser-based usage, runs as a Language Server Protocol (LSP) server for editor integration, and provides a Node.js binding for JavaScript applications. This means the same grammar engine can power checks in VS Code, Neovim, Obsidian, web browsers, and custom applications.



For AI agents working on content writing and SEO tasks, Harper provides a fast local grammar layer that can validate and clean text before publishing. Unlike cloud-based grammar services, Harper processes everything locally, making it suitable for environments where text contains sensitive information or where network latency is a concern.



The grammar rules cover common English writing issues: subject-verb agreement, article usage, commonly confused words, spelling errors, and stylistic patterns. Harper uses a custom dictionary system that supports user-defined words and domain-specific terminology, which is important for technical content where standard dictionaries flag legitimate terms as errors.



Editor integrations include official support for VS Code (via the Harper extension), Neovim (via the LSP server), Obsidian, and Zed. The LSP server means any editor with LSP support can connect to Harper for real-time grammar checking. The Chrome extension provides in-browser grammar checking on any text input field.



Installation is straightforward: cargo install for the Rust toolchain, npm packages for Node.js integration, or pre-built binaries and extensions for specific editors. The project maintains active development with regular releases, and the Automattic backing provides long-term sustainability that many open-source grammar tools lack.



The Rust implementation delivers performance that makes real-time checking practical even in resource-constrained environments. Where LanguageTool requires a JVM and server process, Harper runs as a lightweight binary with minimal memory footprint.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill harper-offline-grammar-checker-automattic
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill harper-offline-grammar-checker-automattic -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill harper-offline-grammar-checker-automattic -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill harper-offline-grammar-checker-automattic -a codex
```

### OpenClaw

```bash
clawhub install harper-offline-grammar-checker-automattic
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/harper-offline-grammar-checker-automattic/)
