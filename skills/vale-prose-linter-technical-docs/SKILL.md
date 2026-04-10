---
name: Vale Prose Linter for Technical Documentation
description: Vale is an open-source, markup-aware prose linter that enforces editorial
  style guides on technical documentation. This skill enables agents to run Vale against
  Markdown, AsciiDoc, reStructuredText, and HTML to catch style, grammar, and terminology
  issues.
verification: security_reviewed
source: https://github.com/vale-cli/vale
category:
- Code Quality &amp; Review
framework:
- Custom Agents
tool_ecosystem:
  github_repo: vale-cli/vale
  github_stars: 5316
  license: MIT
---
# Vale Prose Linter for Technical Documentation

Vale is a command-line prose linter written in Go that brings code-style linting to written content. Unlike generic grammar checkers, Vale understands markup formats like Markdown, AsciiDoc, reStructuredText, HTML, and XML, allowing it to intelligently skip code blocks, front matter, and syntax elements while checking only the prose sections of documents.
This skill equips agents with the ability to run Vale against documentation repositories and report style violations. Agents learn to configure Vale using its YAML-based rule system, apply pre-built style packages (Microsoft, Google, write-good, Readability, and more from the Vale Package Hub), and create custom rules for project-specific terminology and voice guidelines. The configuration uses a simple .vale.ini file that specifies which styles to apply and which file types to lint.
Vale's rule engine supports pattern-matching with regular expressions, conditional checks based on document scope (headings, lists, paragraphs), and severity levels (suggestion, warning, error). Agents can run Vale in CI pipelines to enforce documentation standards automatically, generate reports of style violations across entire repositories, and suggest fixes based on the configured style guide. The tool integrates with VS Code, Vim, Emacs, and Sublime Text, making it easy to adopt across teams.
Output from Vale includes the file path, line number, severity, rule name, and a human-readable message for each violation. Agents can parse this structured output to generate pull request comments, documentation quality reports, or batch-fix suggestions. Vale has over 4,500 GitHub stars, 3 million+ downloads, and is MIT-licensed. It ships as a single static binary with zero dependencies, making deployment trivial across Linux, macOS, and Windows.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/vale-prose-linter-technical-docs/)
