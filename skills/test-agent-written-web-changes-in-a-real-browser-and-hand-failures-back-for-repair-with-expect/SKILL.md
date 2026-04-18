---
title: "Test agent-written web changes in a real browser and hand failures back for repair with Expect"
description: "Run an agent-native browser QA loop that reads recent code changes, generates a test plan, and returns concrete failures for the coding agent to fix."
verification: listed
source: "https://github.com/millionco/expect"
category:
  - "Browser Automation"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "millionco/expect"
  github_stars: 3362
  ase_npm_package: "expect-cli"
  npm_weekly_downloads: 24457
---

# Test agent-written web changes in a real browser and hand failures back for repair with Expect

Use Expect when the job is post-codegen browser QA for a changed web app, not when a user just needs a generic browser automation or test framework. The invoke moment is specific: after an agent edits a web product, Expect reads the git diff, generates a test plan, runs it in a real browser with Playwright, and reports failures back so the agent can repair and re-verify. That scope boundary, agent-native browser validation and fix feedback for recent code changes, keeps this skill-shaped instead of collapsing into a plain testing product card.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/test-agent-written-web-changes-in-a-real-browser-and-hand-failures-back-for-repair-with-expect
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/test-agent-written-web-changes-in-a-real-browser-and-hand-failures-back-for-repair-with-expect` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/test-agent-written-web-changes-in-a-real-browser-and-hand-failures-back-for-repair-with-expect/)
