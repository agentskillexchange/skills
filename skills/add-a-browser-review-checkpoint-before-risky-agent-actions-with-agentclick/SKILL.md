---
name: "Add a browser review checkpoint before risky agent actions with AgentClick"
slug: "add-a-browser-review-checkpoint-before-risky-agent-actions-with-agentclick"
description: "Use AgentClick when an agent should pause before risky commands, plans, drafts, or code changes so a human can inspect, edit, approve, or reject them in a purpose-built browser UI."
github_stars: 22
verification: "security_reviewed"
source: "https://github.com/agentlayer-io/AgentClick"
author: "agentlayer-io"
publisher_type: "organization"
category: "Code Quality & Review"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "agentlayer-io/agentclick"
  github_stars: 22
  npm_package: "@harvenstar/agentclick"
  npm_weekly_downloads: 9
---

# Add a browser review checkpoint before risky agent actions with AgentClick

Use AgentClick when an agent should pause before risky commands, plans, drafts, or code changes so a human can inspect, edit, approve, or reject them in a purpose-built browser UI.

## Prerequisites

AgentClick, browser access, npm, compatible local agent that can invoke tools and follow skill instructions

## Installation

Use the upstream install or setup path that matches your environment:
- git clone https://github.com/agentlayer-io/AgentClick.git
- npm install
- npm run dev
- npm run build

Requirements and caveats from upstream:
- For OpenClaw in particular, use a stronger model with solid instruction-following, since the workflow is skill-based and depends on the agent following routing instructions reliably.

Basic usage or getting-started notes:
- AgentClick works as a **skill / plugin** for modern AI agents. Any agent that can run local tools, send HTTP requests, and follow skill instructions can integrate with it.

- Source: https://github.com/agentlayer-io/AgentClick
- Extracted from upstream docs: https://raw.githubusercontent.com/agentlayer-io/AgentClick/HEAD/README.md

## Documentation

- https://github.com/agentlayer-io/AgentClick

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/add-a-browser-review-checkpoint-before-risky-agent-actions-with-agentclick/)
