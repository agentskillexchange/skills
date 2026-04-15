---
title: "Outlook Email Automation"
description: "Authenticates to Microsoft Graph API using MSAL with Mail.ReadWrite and Calendars.ReadWrite permissions. Reads, classifies, and responds to emails via GET /me/messages and POST /me/sendMail. Moves processed messages into folders and tracks reply SLAs in a local SQLite store."
verification: listed
source: "https://agentskillexchange.com/skills/outlook-email-automation/"
category:
  - "Calendar, Email & Productivity"
framework:
  - "Claude Code"
---

# Outlook Email Automation

Authenticates to Microsoft Graph API using MSAL with Mail.ReadWrite and Calendars.ReadWrite permissions. Reads, classifies, and responds to emails via GET /me/messages and POST /me/sendMail. Moves processed messages into folders and tracks reply SLAs in a local SQLite store.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/outlook-email-automation/)
