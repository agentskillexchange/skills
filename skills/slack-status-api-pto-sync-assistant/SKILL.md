---
title: "Slack Status API PTO Sync Assistant"
description: "Syncs away-state updates through Slack users.profile APIs, status fields, and directory lookups so agents can keep status text aligned with calendar-based time off. Useful for teams that want cleaner presence signals without manually editing every Slack profile."
verification: "security_reviewed"
source: "https://api.slack.com/"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "Custom Agents"
---

# Slack Status API PTO Sync Assistant

Slack Status API PTO Sync Assistant is for organizations that rely on Slack presence as a lightweight operating signal and want agents to keep it accurate during vacations, holidays, and planned absences. It uses Slack profile and users endpoints, including status text and expiration fields, to update presence information in a way that matches team availability. That is especially useful when calendar systems already know who is out but Slack status remains stale and teammates end up pinging the wrong people.

The workflow can compare current status values against planned absences, suggest a status update, and standardize phrasing across a team or department. It also helps avoid inconsistent or forgotten manual edits that make PTO harder to respect. Because it works with Slack’s own profile model rather than an external overlay, the status remains visible where people already look first.

Use this skill when you want cleaner away-state hygiene, more reliable availability signals, and a simple bridge between time-off data and Slack presence.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/slack-status-api-pto-sync-assistant/)
