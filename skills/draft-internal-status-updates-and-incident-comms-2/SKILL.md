---
title: "Draft internal status updates and incident comms"
description: "Use Anthropic’s internal-comms skill to turn raw project notes into company-ready status reports, 3P updates, FAQs, leadership notes, and incident writeups. The skill is valuable because it gives the agent a bounded communication workflow and format guidance, not because it exposes a generic skills repo."
verification: "security_reviewed"
source: "https://github.com/anthropics/skills/tree/main/skills/internal-comms"
category:
  - "Templates & Workflows"
framework:
  - "Claude Agents"
tool_ecosystem:
  github_repo: "anthropics/skills"
  github_stars: 116155
---

# Draft internal status updates and incident comms

internal-comms is an official skill directory inside the anthropics/skills repository. Its job-to-be-done is specific: help an agent produce internal communications such as 3P updates, newsletters, FAQ answers, status reports, leadership updates, project updates, and incident reports by selecting the right template path and following the corresponding guidance. That makes it skill-shaped in a way a generic repo listing is not.

Use this when someone asks an agent to turn messy notes, operating context, or project progress into an internal communication artifact that needs the right structure and tone. It is the right invocation point when the user is not asking for free-form writing, but for a repeatable internal comms workflow with recognizable formats and an explicit decision step about which communication type applies. That is different from “using Anthropic or Claude normally,” because the value here is the reusable operating pattern and its examples.

The scope boundary is tight. This entry is not for the entire anthropics/skills repository, and it is not a generic writing assistant card. It is limited to internal communications workflows, with example-driven instructions for choosing a format and producing the correct style of update. It does not claim to handle marketing copy, public relations, or arbitrary document creation outside that bounded lane.

Integration points are straightforward and backed by the upstream source: the skill lives in the public Anthropic skills repo, ships with its own SKILL.md, and points agents to example files for 3P updates, company newsletters, FAQ replies, and general internal comms. That means the source itself defines when the agent should invoke it, what files it should load, and how the workflow stays constrained. Hidden product branding would not remove the value, because the operator task remains the same: draft clear internal updates from raw organizational context.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/draft-internal-status-updates-and-incident-comms-2/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/draft-internal-status-updates-and-incident-comms-2
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/draft-internal-status-updates-and-incident-comms-2`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/draft-internal-status-updates-and-incident-comms-2/)
