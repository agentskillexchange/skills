---
name: dprint Pluggable High-Performance Code Formatting Platform
description: dprint is a pluggable and configurable code formatting platform written
  in Rust. It unifies formatting for TypeScript, JavaScript, JSON, Markdown, TOML,
  CSS, HTML, Dockerfile, and more through a single CLI with a Wasm-based plugin architecture
  for maximum speed.
category: "Code Quality &amp; Review"
framework: Multi-Framework
verification: security_reviewed
source: "https://github.com/dprint/dprint"
tool_ecosystem:
  github_repo: "https://github.com/dprint/dprint"
  github_stars: 3857
  npm_package: dprint
  npm_weekly_downloads: 153574
  license: MIT
---
# dprint Pluggable High-Performance Code Formatting Platform

dprint is a pluggable and configurable code formatting platform written in Rust. It unifies formatting for TypeScript, JavaScript, JSON, Markdown, TOML, CSS, HTML, Dockerfile, and more through a single CLI with a Wasm-based plugin architecture for maximum speed.

dprint is a code formatting platform that takes a fundamentally different approach from tools like Prettier: instead of one monolithic formatter, it uses a plugin architecture where each language formatter runs as a WebAssembly module. This design delivers extreme performance (10-30x faster than Prettier) while supporting a wide range of languages through community plugins.

What It Does

dprint formats source code files according to configurable rules. It ships with official plugins for TypeScript/JavaScript, JSON/JSONC, Markdown, TOML, Dockerfile, and Jupyter notebooks. Community plugins extend support to CSS/SCSS (Malva), HTML/Vue/Svelte (markup_fmt), GraphQL, YAML, Go, Python (via Ruff), PHP (via Mago), and C#/VB (via Roslyn). Configuration lives in a dprint.json file, and plugins are downloaded and cached automatically.

How Agents Use It

Agents invoke dprint as a CLI tool to format code files before committing or presenting output. The dprint fmt command formats all files matching configured patterns, while dprint check verifies formatting without modifying files (useful in CI). The dprint fmt --stdin <extension> mode formats code from standard input, making it ideal for agent pipelines that generate code and need consistent formatting. dprint can also wrap other formatters like Prettier, Biome, and Ruff as plugins.

Key Features

- Wasm-based plugin architecture for language-agnostic formatting

- 10-30x faster than Prettier on typical codebases

- Official plugins for TypeScript, JavaScript, JSON, Markdown, TOML, Dockerfile

- Community plugins for CSS, HTML, Vue, Svelte, GraphQL, YAML, Go, Python, PHP

- Incremental formatting with file caching

- stdin/stdout mode for pipeline integration

- exec plugin to wrap any CLI formatter

- Editor integrations for VS Code, Neovim, and more

Integration Points

Install via Homebrew (brew install dprint), npm (npm install -g dprint), or cargo (cargo install dprint). Initialize a project with dprint init which creates a dprint.json config. Run dprint fmt to format and dprint check to verify. See the full plugin list at dprint.dev/plugins.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill dprint-pluggable-code-formatter
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill dprint-pluggable-code-formatter -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill dprint-pluggable-code-formatter -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill dprint-pluggable-code-formatter -a codex
```

### OpenClaw

```bash
clawhub install dprint-pluggable-code-formatter
```


## Source

- [GitHub](https://github.com/dprint/dprint)
