---
title: "Test agent-written web changes in a real browser and hand failures back for repair with Expect"
description: "Use Expect when the job is post-codegen browser QA for a changed web app, not when a user just needs a generic browser automation or test framework. The invoke moment is specific: after an agent edits a web product, Expect reads the git diff, generates a test plan, runs it in a real browser with Playwright, and reports failures back so the agent can repair and re-verify. That scope boundary, agent-native browser validation and fix feedback for recent code changes, keeps this skill-shaped instead of collapsing into a plain testing product card."
source: "https://github.com/millionco/expect"
verification: "listed"
category:
  - "Browser Automation"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "millionco/expect"
  github_stars: 3362
  npm_package: "expect-cli"
  npm_weekly_downloads: 24457
---

# Test agent-written web changes in a real browser and hand failures back for repair with Expect

Use Expect when the job is post-codegen browser QA for a changed web app, not when a user just needs a generic browser automation or test framework. The invoke moment is specific: after an agent edits a web product, Expect reads the git diff, generates a test plan, runs it in a real browser with Playwright, and reports failures back so the agent can repair and re-verify. That scope boundary, agent-native browser validation and fix feedback for recent code changes, keeps this skill-shaped instead of collapsing into a plain testing product card.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/test-agent-written-web-changes-in-a-real-browser-and-hand-failures-back-for-repair-with-expect/)
