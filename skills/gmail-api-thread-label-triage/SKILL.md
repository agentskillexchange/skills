---
name: "Gmail API Thread Label Triage"
description: "Triage inbox backlog with the Gmail API’s `users.threads`, `users.messages`, and `users.labels` methods so agents can classify and prioritize whole conversations instead of isolated emails. Useful for support, recruiting, or founder inboxes where thread context matters more than single-message scanning."
category: "Calendar, Email & Productivity"
framework: "Gemini"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/gmail-api-thread-label-triage/"
---

# Gmail API Thread Label Triage

Triage inbox backlog with the Gmail API’s `users.threads`, `users.messages`, and `users.labels` methods so agents can classify and prioritize whole conversations instead of isolated emails. Useful for support, recruiting, or founder inboxes where thread context matters more than single-message scanning.

## Overview

Gmail API Thread Label Triage is meant for workflows where an agent needs to sort conversation-heavy inboxes without losing thread context. It uses Gmail API resources such as `users.threads`, `users.messages`, and `users.labels` to inspect multi-message conversations, apply consistent labels, and separate urgent threads from background noise. That matters when a single reply chain contains the real state of a request and looking only at the most recent message would misclassify it.

The skill can review sender patterns, recent replies, unread state, and label history before suggesting or applying a triage outcome. It is especially effective in shared inboxes, recruiting pipelines, founder correspondence, or support queues where agents need to identify follow-up debt quickly. Because the workflow stays grounded in thread-level Gmail objects, it also makes downstream summaries and handoffs more coherent.

Use this skill when email triage should reflect the full conversation, when inbox labels drive workflow decisions, and when agents need something more structured than search operators alone.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill gmail-api-thread-label-triage
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill gmail-api-thread-label-triage -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill gmail-api-thread-label-triage -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill gmail-api-thread-label-triage -a codex
```

### OpenClaw

```bash
clawhub install gmail-api-thread-label-triage
```

## Source

- Marketplace: https://agentskillexchange.com/skills/gmail-api-thread-label-triage/
