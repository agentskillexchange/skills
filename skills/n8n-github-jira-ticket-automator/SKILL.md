---
name: "n8n GitHub Issue-to-Jira Ticket Automator"
description: "Deploys an n8n workflow via the n8n REST API using the GitHub Trigger node to capture new issue events and transform them into Jira tickets via the Jira Cloud REST API. Labels, priority mappings, and assignee routing rules are configured using n8n’s Function node with custom JavaScript."
category: "Developer Tools"
framework: "Codex"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/n8n-github-jira-ticket-automator/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "jira"  # from ase_tool_match
---

# n8n GitHub Issue-to-Jira Ticket Automator

Deploys an n8n workflow via the n8n REST API using the GitHub Trigger node to capture new issue events and transform them into Jira tickets via the Jira Cloud REST API. Labels, priority mappings, and assignee routing rules are configured using n8n’s Function node with custom JavaScript.

## Overview

Deploys an n8n workflow via the n8n REST API using the GitHub Trigger node to capture new issue events and transform them into Jira tickets via the Jira Cloud REST API. Labels, priority mappings, and assignee routing rules are configured using n8n’s Function node with custom JavaScript.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill n8n-github-jira-ticket-automator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill n8n-github-jira-ticket-automator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill n8n-github-jira-ticket-automator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill n8n-github-jira-ticket-automator -a codex
```

### OpenClaw

```bash
clawhub install n8n-github-jira-ticket-automator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/n8n-github-jira-ticket-automator/
