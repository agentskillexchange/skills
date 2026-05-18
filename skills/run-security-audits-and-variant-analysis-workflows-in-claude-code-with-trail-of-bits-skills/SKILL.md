---
name: "Run security audits and variant analysis workflows in Claude Code with Trail of Bits Skills"
slug: "run-security-audits-and-variant-analysis-workflows-in-claude-code-with-trail-of-bits-skills"
description: "Use curated Trail of Bits security skills inside Claude Code when the job is auditing, variant hunting, or fix verification rather than generic coding assistance."
github_stars: 4663
verification: "security_reviewed"
source: "https://github.com/trailofbits/skills"
author: "Trail of Bits"
publisher_type: "company"
category: "Security & Verification"
framework: "Claude Code"
tool_ecosystem:
  github_repo: "trailofbits/skills"
  github_stars: 4663
---

# Run security audits and variant analysis workflows in Claude Code with Trail of Bits Skills

Use curated Trail of Bits security skills inside Claude Code when the job is auditing, variant hunting, or fix verification rather than generic coding assistance.

## Prerequisites

Claude Code with plugin marketplace support, the Trail of Bits skills repository or marketplace install, and whatever upstream tools a selected security skill requires such as Semgrep, CodeQL, SARIF tooling, Burp exports, or language-specific analyzers.

## Installation

Use the upstream install or setup path that matches your environment:
- git clone https://github.com/trailofbits/skills.git ~/.codex/trailofbits-skills

Requirements and caveats from upstream:
- | [modern-python](plugins/modern-python/) | Modern Python tooling and best practices with uv, ruff, and pytest |

Basic usage or getting-started notes:
- ### Claude Code Marketplace
- /plugin marketplace add trailofbits/skills
- ### Browse and Install Plugins

- Source: https://github.com/trailofbits/skills
- Extracted from upstream docs: https://raw.githubusercontent.com/trailofbits/skills/HEAD/README.md

## Documentation

- https://github.com/trailofbits/skills#readme

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-security-audits-and-variant-analysis-workflows-in-claude-code-with-trail-of-bits-skills/)
