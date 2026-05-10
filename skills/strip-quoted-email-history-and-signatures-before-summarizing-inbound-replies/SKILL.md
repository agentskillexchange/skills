---
title: "Strip quoted email history and signatures before summarizing inbound replies"
slug: "strip-quoted-email-history-and-signatures-before-summarizing-inbound-replies"
description: "Uses mail-parser-reply to isolate the newest human reply from text email threads while removing quoted history, signatures, and common disclaimers. This is useful when an agent needs the actionable part of an inbound email before routing, summarizing, or creating follow-up tasks."
github_stars: 78
verification: "security_reviewed"
source: "https://github.com/alfonsrv/mail-parser-reply"
author: "alfonsrv"
publisher_type: "User"
category: "Calendar, Email & Productivity"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "alfonsrv/mail-parser-reply"
  github_stars: 78
---

# Strip quoted email history and signatures before summarizing inbound replies

Uses mail-parser-reply to isolate the newest human reply from text email threads while removing quoted history, signatures, and common disclaimers. This is useful when an agent needs the actionable part of an inbound email before routing, summarizing, or creating follow-up tasks.

## Prerequisites

Python and a mail ingestion source such as IMAP, Gmail API, Graph API, or a helpdesk webhook

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
pip install mail-parser-reply
```

## Documentation

- https://github.com/alfonsrv/mail-parser-reply#readme

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/strip-quoted-email-history-and-signatures-before-summarizing-inbound-replies/)
