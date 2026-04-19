---
title: "Slack Status API PTO Sync Assistant"
description: "Slack Status API PTO Sync Assistant is for organizations that rely on Slack presence as a lightweight operating signal and want agents to keep it accurate during vacations, holidays, and planned absences. It uses Slack profile and users endpoints, including status text and expiration fields, to update presence information in a way that matches team availability. That is especially useful when calendar systems already know who is out but Slack status remains stale and teammates end up pinging the wrong people. The workflow can compare current status values against planned absences, suggest a status update, and standardize phrasing across a team or department. It also helps avoid inconsistent or forgotten manual edits that make PTO harder to respect. Because it works with Slack’s own profile model rather than an external overlay, the status remains visible where people already look first. Use this skill when you want cleaner away-state hygiene, more reliable availability signals, and a simple bridge between time-off data and Slack presence."
source: "https://api.slack.com/"
verification: "security_reviewed"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "Custom Agents"
---

# Slack Status API PTO Sync Assistant

Slack Status API PTO Sync Assistant is for organizations that rely on Slack presence as a lightweight operating signal and want agents to keep it accurate during vacations, holidays, and planned absences. It uses Slack profile and users endpoints, including status text and expiration fields, to update presence information in a way that matches team availability. That is especially useful when calendar systems already know who is out but Slack status remains stale and teammates end up pinging the wrong people. The workflow can compare current status values against planned absences, suggest a status update, and standardize phrasing across a team or department. It also helps avoid inconsistent or forgotten manual edits that make PTO harder to respect. Because it works with Slack’s own profile model rather than an external overlay, the status remains visible where people already look first. Use this skill when you want cleaner away-state hygiene, more reliable availability signals, and a simple bridge between time-off data and Slack presence.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/slack-status-api-pto-sync-assistant/)
