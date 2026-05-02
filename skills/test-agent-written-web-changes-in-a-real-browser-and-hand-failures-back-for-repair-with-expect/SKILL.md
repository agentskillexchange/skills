---
title: "Test agent-written web changes in a real browser and hand failures back for repair with Expect"
description: "Run an agent-native browser QA loop that reads recent code changes, generates a test plan, and returns concrete failures for the coding agent to fix."
verification: "listed"
source: "https://github.com/millionco/expect"
author: "Million"
publisher_type: "organization"
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

Run an agent-native browser QA loop that reads recent code changes, generates a test plan, and returns concrete failures for the coding agent to fix.

## Prerequisites

Node.js, Expect CLI, a supported coding agent such as Claude Code or Codex, local browser access, and a web app repository with recent changes to test

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Follow the upstream init flow from https://www.expect.dev/, ensure a supported coding agent is installed, then run /expect in the repo after the agent changes a web app so Expect can generate and execute the browser test plan.
```

## Documentation

- https://expect.dev

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/test-agent-written-web-changes-in-a-real-browser-and-hand-failures-back-for-repair-with-expect/)
