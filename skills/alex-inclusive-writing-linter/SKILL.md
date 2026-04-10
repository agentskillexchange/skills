---
name: "alex Inclusive Writing Linter"
description: "Catch insensitive, inconsiderate writing with alex. This CLI tool and Node.js library scans Markdown and plain text for gender-biased, polarizing, or exclusionary language and suggests inclusive alternatives."
verification: security_reviewed
source: "https://github.com/get-alex/alex"
category:
  - "Content Writing &amp; SEO"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "get-alex/alex"
  github_stars: 5096
  ase_npm_package: "alex"
  npm_weekly_downloads: 30585
---

# alex Inclusive Writing Linter

alex is a command-line tool and Node.js library that helps you find and fix insensitive, inconsiderate writing. Whether you are reviewing your own documentation or auditing contributed content, alex flags language that could be gender-biased, polarizing, race-related, or otherwise exclusionary, and suggests inclusive replacements.
Built on the retext natural language processing ecosystem, alex parses Markdown and plain text into a syntax tree and applies two core rule sets: retext-equality (which detects potentially insensitive phrasing) and retext-profanities (which catches inappropriate language). The output includes file location, the problematic term, and suggested alternatives with clear reasoning.
Installation is straightforward via npm: npm install alex --save-dev. The CLI accepts file paths or globs (alex *.md) and exits with a non-zero code when issues are found, making it suitable for CI gating. Configuration uses .alexrc files or package.json entries to whitelist known terms, set severity levels, and toggle specific rules.
For AI agent workflows, alex serves as a post-generation quality gate. Content produced by language models can inadvertently include biased or exclusionary terms. Running alex as a subprocess against generated blog posts, documentation, README files, or marketing copy catches these issues before they reach publication. The structured JSON output (alex --reporter json) is easy to parse programmatically for automated correction pipelines.
alex integrates with popular development tools: VS Code extensions, GitHub Actions workflows, pre-commit hooks, and text editor plugins. It supports both CommonMark Markdown and plain text input, with the Markdown parser correctly ignoring code blocks and HTML tags to reduce false positives.
The project has been widely adopted in open-source communities for enforcing inclusive language standards in documentation. It is MIT licensed with over 5,000 GitHub stars and an active community of contributors.
Source: github.com/get-alex/alex | Website: alexjs.com

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/alex-inclusive-writing-linter/)
