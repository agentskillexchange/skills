---
name: "Inbox Zero AI Email Assistant"
description: "Inbox Zero is an open-source AI email assistant with over 10,000 GitHub stars that auto-triages your inbox, pre-drafts replies in your tone, bulk unsubscribes from unwanted senders, and blocks cold emails. Includes MCP server integration and Slack/Telegram chat interface."
category: "Calendar, Email & Productivity"
framework: "Custom Agents"
verification: security_reviewed
source: "https://github.com/elie222/inbox-zero"
tool_ecosystem:
  tool: inbox-zero
  github_repo: elie222/inbox-zero
  github_stars: 10370
---
# Inbox Zero AI Email Assistant

Inbox Zero is an open-source AI email assistant with over 10,000 GitHub stars that auto-triages your inbox, pre-drafts replies in your tone, bulk unsubscribes from unwanted senders, and blocks cold emails. Includes MCP server integration and Slack/Telegram chat interface.

## Overview

What is Inbox Zero?

Inbox Zero is an open-source AI-powered email management platform with over 10,000 GitHub stars, designed to help users reach inbox zero efficiently. Built as a Next.js application with Gmail and Microsoft Outlook support, it provides AI-driven email triage, reply drafting, bulk unsubscribing, cold email blocking, and email analytics. The project is actively maintained with frequent releases and includes an MCP server for AI agent integration.

How the Skill Works

The Inbox Zero skill connects AI agents to email management workflows through its REST API and MCP server. The AI personal assistant component uses natural language rules (similar to Cursor rules) to define how incoming email should be handled: categorizing messages, drafting replies that match the user’s writing style, labeling conversations, and archiving low-priority mail automatically.

The Reply Zero feature tracks emails that need responses and those awaiting replies from others, creating a prioritized action queue. The bulk unsubscriber analyzes email patterns to identify newsletters and marketing emails the user never reads, enabling one-click unsubscribe and archive operations. The cold email blocker uses AI classification to identify and auto-archive unsolicited outreach.

Integration Points

Inbox Zero integrates with Gmail via Google Pub/Sub for real-time email processing and Microsoft Outlook through the Graph API. The MCP server exposes email management tools to any MCP-compatible AI client. Slack and Telegram integrations allow users to manage their inbox through chat interfaces. The platform uses Upstash Redis for caching and supports deployment on Vercel with one-click setup.

What It Outputs

The skill outputs email triage decisions, drafted replies, unsubscribe actions, analytics reports with activity trends, and meeting briefs that pull context from email and calendar data. Smart filing automatically saves email attachments to Google Drive or OneDrive based on configurable rules.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill inbox-zero-ai-email-assistant
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill inbox-zero-ai-email-assistant -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill inbox-zero-ai-email-assistant -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill inbox-zero-ai-email-assistant -a codex
```

### OpenClaw

```bash
clawhub install inbox-zero-ai-email-assistant
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/inbox-zero-ai-email-assistant/)
