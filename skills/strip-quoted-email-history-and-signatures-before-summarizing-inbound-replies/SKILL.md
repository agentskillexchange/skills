---
title: "Strip quoted email history and signatures before summarizing inbound replies"
description: "Uses mail-parser-reply to isolate the newest human reply from text email threads while removing quoted history, signatures, and common disclaimers. This is useful when an agent needs the actionable part of an inbound email before routing, summarizing, or creating follow-up tasks."
verification: "security_reviewed"
source: "https://github.com/alfonsrv/mail-parser-reply"
category: ["Calendar, Email &amp; Productivity"]
framework: ["Multi-Framework"]
tool_ecosystem:
  github_repo: "alfonsrv/mail-parser-reply"
  github_stars: 78
---

# Strip quoted email history and signatures before summarizing inbound replies

Uses mail-parser-reply to isolate the newest human reply from text email threads while removing quoted history, signatures, and common disclaimers. This is useful when an agent needs the actionable part of an inbound email before routing, summarizing, or creating follow-up tasks.

## Installation

Choose the install path that fits your setup:

1. Install from the Agent Skill Exchange catalog if your agent client supports it.
2. Copy the skill folder into your local skills directory.
3. Add it as a git submodule in your shared agent-skills repo.
4. Vendor the files directly into a project-specific `.agents/skills/` or equivalent folder.
5. Keep a fork or mirror if you need local modifications or pinned revisions.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/strip-quoted-email-history-and-signatures-before-summarizing-inbound-replies/)
