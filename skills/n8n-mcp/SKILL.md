---
name: "n8n MCP"
description: "Connect agent actions to n8n workflow automation."
category: "Templates & Workflows"
framework: "Claude Code"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/n8n-mcp/"
---

# n8n MCP

Connect agent actions to n8n workflow automation.

## Overview

n8n MCP adds an MCP bridge for n8n so agents can trigger and coordinate workflow automation without forcing users into custom glue code.
Best for

- workflow orchestration

- automation handoffs

- connecting agent tasks to n8n flows

Install notes

Install from the GitHub repository, connect it to an accessible n8n instance, then register it in the host MCP configuration.

Source: czlonkowski/n8n-mcp.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill n8n-mcp
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill n8n-mcp -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill n8n-mcp -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill n8n-mcp -a codex
```

### OpenClaw

```bash
clawhub install n8n-mcp
```

## Source

- Marketplace: https://agentskillexchange.com/skills/n8n-mcp/
