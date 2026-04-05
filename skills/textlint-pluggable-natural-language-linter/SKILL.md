---
name: "textlint Pluggable Natural Language Linter"
description: "Lint natural language text with textlint, the pluggable linting framework inspired by ESLint. Install community rules from npm to enforce writing standards, catch grammar issues, and maintain consistent documentation style across your project."
category: "Content Writing & SEO"
framework: "Multi-Framework"
verification: security_reviewed
source: "https://github.com/textlint/textlint"
tool_ecosystem:
  github_repo: "textlint/textlint"
  github_stars: 3099
  npm_package: "textlint"
  npm_weekly_downloads: 98739
  license: "MIT"
---
# textlint Pluggable Natural Language Linter

Lint natural language text with textlint, the pluggable linting framework inspired by ESLint. Install community rules from npm to enforce writing standards, catch grammar issues, and maintain consistent documentation style across your project.

textlint is an open-source, pluggable linting tool designed specifically for natural language text. Built with Node.js and available via npm, it applies the same modular rule-based approach that ESLint uses for JavaScript code — but targets prose, documentation, and technical writing instead.



The core architecture ships with zero bundled rules by design. Instead, you install individual rule packages from npm (e.g. textlint-rule-no-dead-link, textlint-rule-terminology, textlint-rule-write-good) that target specific writing concerns. This composable approach means teams can build custom linting profiles tuned to their documentation standards without carrying unnecessary overhead.



textlint parses input files into an AST (Abstract Syntax Tree) for Markdown, plain text, HTML, and other formats via processor plugins. Rules traverse this AST to detect issues and optionally provide auto-fix suggestions. The --fix flag applies corrections automatically, while the standard output mode reports violations with file, line, and column references.



Integration points include CI/CD pipelines (GitHub Actions, CircleCI), editor plugins (VS Code, Atom, Vim), and pre-commit hooks. Configuration lives in .textlintrc (JSON or YAML), making it version-controllable alongside your codebase. For AI agents, textlint can run as a CLI subprocess that scans generated content, blog posts, or README files before publishing, catching terminology inconsistencies, broken links, and style violations that LLMs commonly introduce.



The textlint ecosystem includes over 100 community-contributed rules on npm covering technical writing conventions, sentence length limits, heading consistency, Oxford comma enforcement, and language-specific grammar checks for English, Japanese, Korean, and more. The official documentation at textlint.org provides rule authoring guides, plugin development references, and configuration examples.



Source: github.com/textlint/textlint — MIT licensed, 3,000+ GitHub stars, actively maintained with regular releases.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill textlint-pluggable-natural-language-linter
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill textlint-pluggable-natural-language-linter -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill textlint-pluggable-natural-language-linter -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill textlint-pluggable-natural-language-linter -a codex
```

### OpenClaw

```bash
clawhub install textlint-pluggable-natural-language-linter
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/textlint-pluggable-natural-language-linter/)
