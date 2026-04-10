---
title: "Vercel Agent Browser"
description: "Vercel Agent Browser is a browser automation CLI built specifically for AI agents. It gives agents a fast, scriptable way to open pages, inspect accessibility snapshots, click elements, fill forms, capture screenshots, and manage browser state from the command line."
slug: "vercel-agent-browser"
category:
  - "Browser Automation"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/vercel-labs/agent-browser"
listed: true
---

# Vercel Agent Browser

Vercel Agent Browser is a browser automation CLI built specifically for AI agents. It gives agents a fast, scriptable way to open pages, inspect accessibility snapshots, click elements, fill forms, capture screenshots, and manage browser state from the command line.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install vercel-agent-browser
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Vercel Agent Browser is a browser automation CLI from Vercel Labs designed for AI-agent workflows rather than traditional end-to-end testing alone. The project centers on a command-line interface called agent-browser that can open websites, generate accessibility-tree snapshots, locate interactive elements semantically, click or type into controls, capture screenshots and PDFs, inspect network activity, and manage cookies, tabs, storage, and dialogs. That makes it a strong fit for skills that need to drive real websites from an agent runtime without forcing the user to wire up a custom Playwright layer.
The upstream project publishes both an official GitHub repository and an npm package, and the README documents installation through npm, Homebrew, Cargo, or source builds. The recommended install flow is npm install -g agent-browser followed by agent-browser install to download Chrome for Testing or reuse an existing Chrome-compatible browser. The tool also documents Linux dependency bootstrap support through agent-browser install --with-deps.
From an integration point of view, Agent Browser works well anywhere a coding or automation agent needs deterministic browser control: website QA, form automation, authenticated workflows, extraction of page text and DOM state, screenshot capture, and debugging of browser-side behavior. Its command surface is broad enough to support simple one-shot tasks and longer agent loops, and the project remains actively maintained with recent upstream activity, a permissive Apache-2.0 license, and substantial adoption. For ASE, this clearly maps to browser automation work with a real, tool-anchored job-to-be-done.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/vercel-agent-browser/)
