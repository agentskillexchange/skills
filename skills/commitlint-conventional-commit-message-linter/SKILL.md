---
name: "commitlint Conventional Commit Message Linter"
description: "commitlint checks whether git commit messages meet the Conventional Commits specification, enforcing structured formats like type(scope): subject. Shareable configuration packages let teams standardize commit conventions, and integration with husky enables automatic linting on every commit via git hooks."
category: "Code Quality & Review"
framework: "Claude Code"
verification: security_reviewed
source: "https://github.com/conventional-changelog/commitlint"
tool_ecosystem:
  github_repo: "conventional-changelog/commitlint"
  github_stars: 18425
  npm_package: "commitlint"
  npm_weekly_downloads: 527623
---
# commitlint Conventional Commit Message Linter

commitlint checks whether git commit messages meet the Conventional Commits specification, enforcing structured formats like type(scope): subject. Shareable configuration packages let teams standardize commit conventions, and integration with husky enables automatic linting on every commit via git hooks.

commitlint is a linting tool for git commit messages that enforces the Conventional Commits specification. The conventional format structures each commit message with a type, optional scope, and subject line, following patterns like feat(auth): add OAuth2 login or fix(api): handle null response. This structured format enables automated changelog generation, semantic versioning, and clearer project history.



The tool operates through a CLI that reads commit messages from stdin, git log, or direct string input and validates them against configurable rules. Rules cover the message structure including type, scope, subject, body, and footer sections, with checks for allowed types, maximum line lengths, case conventions, and whether certain fields are required or forbidden. Each rule can be set to warning or error level, giving teams control over enforcement strictness.



Configuration is managed through commitlint config files supporting JavaScript, TypeScript, JSON, and YAML formats. The most common setup extends @commitlint/config-conventional, which enforces the Angular commit convention with types like feat, fix, docs, style, refactor, perf, test, build, ci, chore, and revert. Teams can override individual rules or create entirely custom configurations that match their specific workflow conventions.



commitlint integrates with husky to run automatically as a commit-msg git hook, providing immediate feedback when a developer writes a non-conforming message. This local validation catches format issues before code is pushed, reducing CI failures and keeping the git log consistent. For CI environments, commitlint can validate ranges of commits on pull requests, ensuring all commits in a branch follow the convention.



The shareable configuration system lets organizations publish their commit conventions as npm packages that any repository can install and extend. commitlint is part of the conventional-changelog ecosystem, which includes tools for generating changelogs and determining version bumps from commit history. The project has over 17,000 GitHub stars, is MIT-licensed, and is actively maintained with support for modern Node.js versions and ESM configurations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill commitlint-conventional-commit-message-linter
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill commitlint-conventional-commit-message-linter -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill commitlint-conventional-commit-message-linter -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill commitlint-conventional-commit-message-linter -a codex
```

### OpenClaw

```bash
clawhub install commitlint-conventional-commit-message-linter
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/commitlint-conventional-commit-message-linter/)
