---
name: "Gmail Smart Triage Agent"
description: "Connects to Gmail via Google Gmail API v1 using OAuth 2.0 to fetch unread threads and apply label-based routing rules. Uses messages.list and threads.modify to bulk-archive, star, or move emails matching regex patterns. Drafts reply templates via users.drafts.create and sends them on a configurable schedule."
category: "Calendar, Email & Productivity"
framework: "OpenClaw"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/gmail-smart-triage-2/"
---

# Gmail Smart Triage Agent

Connects to Gmail via Google Gmail API v1 using OAuth 2.0 to fetch unread threads and apply label-based routing rules. Uses messages.list and threads.modify to bulk-archive, star, or move emails matching regex patterns. Drafts reply templates via users.drafts.create and sends them on a configurable schedule.

## Overview

Connects to Gmail via Google Gmail API v1 using OAuth 2.0 to fetch unread threads and apply label-based routing rules. Uses messages.list and threads.modify to bulk-archive, star, or move emails matching regex patterns. Drafts reply templates via users.drafts.create and sends them on a configurable schedule.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill gmail-smart-triage-2
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill gmail-smart-triage-2 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill gmail-smart-triage-2 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill gmail-smart-triage-2 -a codex
```

### OpenClaw

```bash
clawhub install gmail-smart-triage-2
```

## Source

- Marketplace: https://agentskillexchange.com/skills/gmail-smart-triage-2/
