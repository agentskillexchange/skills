---
title: "textlint Pluggable Natural Language Linter"
description: "textlint is an open-source, pluggable linting tool designed specifically for natural language text. Built with Node.js and available via npm, it applies the same modular rule-based approach that ESLint uses for JavaScript code — but targets prose, documentation, and technical writing instead. The core architecture ships with zero bundled rules by design. Instead, you install individual rule packages from npm (e.g. textlint-rule-no-dead-link , textlint-rule-terminology , textlint-rule-write-good ) that target specific writing concerns. This composable approach means teams can build custom linting profiles tuned to their documentation standards without carrying unnecessary overhead. textlint parses input files into an AST (Abstract Syntax Tree) for Markdown, plain text, HTML, and other formats via processor plugins. Rules traverse this AST to detect issues and optionally provide auto-fix suggestions. The --fix flag applies corrections automatically, while the standard output mode reports violations with file, line, and column references. Integration points include CI/CD pipelines (GitHub Actions, CircleCI), editor plugins (VS Code, Atom, Vim), and pre-commit hooks. Configuration lives in .textlintrc (JSON or YAML), making it version-controllable alongside your codebase. For AI agents, textlint can run as a CLI subprocess that scans generated content, blog posts, or README files before publishing, catching terminology inconsistencies, broken links, and style violations that LLMs commonly introduce. The textlint ecosystem includes over 100 community-contributed rules on npm covering technical writing conventions, sentence length limits, heading consistency, Oxford comma enforcement, and language-specific grammar checks for English, Japanese, Korean, and more. The official documentation at textlint.org provides rule authoring guides, plugin development references, and configuration examples. Source: github.com/textlint/textlint — MIT licensed, 3,000+ GitHub stars, actively maintained with regular releases."
source: "https://github.com/textlint/textlint"
verification: "security_reviewed"
category:
  - "Content Writing &amp; SEO"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "textlint/textlint"
  github_stars: 3099
  npm_package: "textlint"
  npm_weekly_downloads: 102876
---

# textlint Pluggable Natural Language Linter

textlint is an open-source, pluggable linting tool designed specifically for natural language text. Built with Node.js and available via npm, it applies the same modular rule-based approach that ESLint uses for JavaScript code — but targets prose, documentation, and technical writing instead. The core architecture ships with zero bundled rules by design. Instead, you install individual rule packages from npm (e.g. textlint-rule-no-dead-link , textlint-rule-terminology , textlint-rule-write-good ) that target specific writing concerns. This composable approach means teams can build custom linting profiles tuned to their documentation standards without carrying unnecessary overhead. textlint parses input files into an AST (Abstract Syntax Tree) for Markdown, plain text, HTML, and other formats via processor plugins. Rules traverse this AST to detect issues and optionally provide auto-fix suggestions. The --fix flag applies corrections automatically, while the standard output mode reports violations with file, line, and column references. Integration points include CI/CD pipelines (GitHub Actions, CircleCI), editor plugins (VS Code, Atom, Vim), and pre-commit hooks. Configuration lives in .textlintrc (JSON or YAML), making it version-controllable alongside your codebase. For AI agents, textlint can run as a CLI subprocess that scans generated content, blog posts, or README files before publishing, catching terminology inconsistencies, broken links, and style violations that LLMs commonly introduce. The textlint ecosystem includes over 100 community-contributed rules on npm covering technical writing conventions, sentence length limits, heading consistency, Oxford comma enforcement, and language-specific grammar checks for English, Japanese, Korean, and more. The official documentation at textlint.org provides rule authoring guides, plugin development references, and configuration examples. Source: github.com/textlint/textlint — MIT licensed, 3,000+ GitHub stars, actively maintained with regular releases.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/textlint-pluggable-natural-language-linter/)
