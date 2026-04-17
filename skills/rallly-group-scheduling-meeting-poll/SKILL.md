---
title: "Rallly Open-Source Group Scheduling and Meeting Poll Platform"
description: "Rallly is an open-source scheduling and collaboration tool that makes organizing group meetings effortless. Create meeting polls to find the best date and time based on participant availability, replacing back-and-forth email chains with a simple voting interface."
verification: security_reviewed
source: "https://github.com/lukevella/rallly"
category:
  - "Calendar, Email & Productivity"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "lukevella/rallly"
  github_stars: 5027
  license: "AGPL-3.0"
---

# Rallly Open-Source Group Scheduling and Meeting Poll Platform

Rallly is an open-source scheduling and collaboration platform built with Next.js, Prisma, tRPC, and TailwindCSS. It serves as a self-hostable alternative to Doodle, allowing teams and groups to find the best time to meet through a simple polling interface.

How It Works Users create a poll with proposed dates and times for a meeting or event. Participants then vote on their availability without needing to create an account. The platform aggregates votes and highlights the optimal time slot that works for the most participants.

Key Features

- Create date-based polls for group scheduling without sign-up requirements for participants

- Self-hostable with Docker for complete data ownership and privacy

- Built on a modern TypeScript stack: Next.js frontend, Prisma ORM, tRPC for type-safe APIs, PostgreSQL database

- Internationalized with community translations via Crowdin

- Email notifications for poll updates and new responses

- Clean, responsive UI with TailwindCSS

Integration Points Rallly exposes a REST API that agents can use to programmatically create polls, add participants, check poll status, and retrieve results. Agents can automate the entire scheduling workflow: create a poll when a meeting is requested, distribute the link to participants, monitor responses, and announce the winning time slot.

Agent Use Cases An AI agent can use Rallly to automate group scheduling. When someone asks to schedule a team meeting, the agent creates a Rallly poll with proposed times, shares the link via Slack or email, monitors for when enough participants have voted, and then creates a calendar event for the winning time. This eliminates the manual coordination overhead that plagues most scheduling workflows.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/rallly-group-scheduling-meeting-poll
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/rallly-group-scheduling-meeting-poll` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/rallly-group-scheduling-meeting-poll/)
