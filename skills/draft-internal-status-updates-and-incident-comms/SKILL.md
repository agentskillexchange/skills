---
title: "Draft internal status updates and incident comms"
description: "internal-comms is an official skill directory inside the anthropics/skills repository. Its job-to-be-done is specific: help an agent produce internal communications such as 3P updates, newsletters, FAQ answers, status reports, leadership updates, project updates, and incident reports by selecting the right template path and following the corresponding guidance. That makes it skill-shaped in a way a generic repo listing is not. Use this when someone asks an agent to turn messy notes, operating context, or project progress into an internal communication artifact that needs the right structure and tone. It is the right invocation point when the user is not asking for free-form writing, but for a repeatable internal comms workflow with recognizable formats and an explicit decision step about which communication type applies. That is different from “using Anthropic or Claude normally,” because the value here is the reusable operating pattern and its examples. The scope boundary is tight. This entry is not for the entire anthropics/skills repository, and it is not a generic writing assistant card. It is limited to internal communications workflows, with example-driven instructions for choosing a format and producing the correct style of update. It does not claim to handle marketing copy, public relations, or arbitrary document creation outside that bounded lane. Integration points are straightforward and backed by the upstream source: the skill lives in the public Anthropic skills repo, ships with its own SKILL.md , and points agents to example files for 3P updates, company newsletters, FAQ replies, and general internal comms. That means the source itself defines when the agent should invoke it, what files it should load, and how the workflow stays constrained. Hidden product branding would not remove the value, because the operator task remains the same: draft clear internal updates from raw organizational context."
source: "https://github.com/anthropics/skills/tree/main/skills/internal-comms"
verification: "security_reviewed"
category:
  - "Templates &amp; Workflows"
framework:
  - "Claude Agents"
tool_ecosystem:
  github_repo: "anthropics/skills"
  github_stars: 116155
---

# Draft internal status updates and incident comms

internal-comms is an official skill directory inside the anthropics/skills repository. Its job-to-be-done is specific: help an agent produce internal communications such as 3P updates, newsletters, FAQ answers, status reports, leadership updates, project updates, and incident reports by selecting the right template path and following the corresponding guidance. That makes it skill-shaped in a way a generic repo listing is not. Use this when someone asks an agent to turn messy notes, operating context, or project progress into an internal communication artifact that needs the right structure and tone. It is the right invocation point when the user is not asking for free-form writing, but for a repeatable internal comms workflow with recognizable formats and an explicit decision step about which communication type applies. That is different from “using Anthropic or Claude normally,” because the value here is the reusable operating pattern and its examples. The scope boundary is tight. This entry is not for the entire anthropics/skills repository, and it is not a generic writing assistant card. It is limited to internal communications workflows, with example-driven instructions for choosing a format and producing the correct style of update. It does not claim to handle marketing copy, public relations, or arbitrary document creation outside that bounded lane. Integration points are straightforward and backed by the upstream source: the skill lives in the public Anthropic skills repo, ships with its own SKILL.md , and points agents to example files for 3P updates, company newsletters, FAQ replies, and general internal comms. That means the source itself defines when the agent should invoke it, what files it should load, and how the workflow stays constrained. Hidden product branding would not remove the value, because the operator task remains the same: draft clear internal updates from raw organizational context.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/draft-internal-status-updates-and-incident-comms/)
