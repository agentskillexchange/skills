---
name: "TimeToPost Social Scheduler"
slug: "timetopost-social-scheduler"
description: "Draft, review, and schedule distinct social posts with the TimeToPost MCP. Use when asked to plan a social calendar, draft a post or thread, check approval drafts, choose a posting time, or schedule content."
category: "Calendar, Email & Productivity"
framework: "MCP"
verification: listed
source: "https://github.com/MelMayssonOwen/agent-skills/tree/main/skills/timetopost-social-scheduler"
---

# TimeToPost Social Scheduler

This skill helps an agent turn a brief into usable social drafts across connected accounts. It begins by checking the TimeToPost workspace and connected platforms, then reviews recent posts to match the account's voice. The workflow creates separate versions for each platform, checks common text and media limits, and uses account history for timing suggestions when available. When history is missing, any timing guidance is clearly labeled as a generic heuristic.

Drafts remain pending until a person reviews the copy. The agent shows the text, account, and proposed time, then waits for approval before scheduling. That keeps accidental publication out of the drafting step. A bundled Python helper can add attribution parameters to campaign links without network access.

Use this for weekly content planning, a one-off post, or a platform-specific rewrite. It requires a TimeToPost MCP connection for account-aware actions. The skill does not promise engagement outcomes and does not reuse identical copy across accounts. Installation is free; the connected product may have its own current plans and limits.

Creator: Opsibyte. License: MIT. Product: https://timetopost.co/?utm_source=ase&utm_medium=skill&utm_campaign=agent-skills&utm_content=timetopost-social-scheduler

## Installation

### Direct repo/manual install

```bash
git clone https://github.com/MelMayssonOwen/agent-skills.git
cp -R agent-skills/skills/timetopost-social-scheduler ~/.agent-skills/timetopost-social-scheduler
```

### Optional Third-Party Installer

```bash
npx skills add MelMayssonOwen/agent-skills --skill timetopost-social-scheduler
```
