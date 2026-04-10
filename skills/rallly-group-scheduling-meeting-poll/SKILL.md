---
title: "Rallly Open-Source Group Scheduling and Meeting Poll Platform"
description: "Rallly is an open-source scheduling and collaboration tool that makes organizing group meetings effortless. Create meeting polls to find the best date and time based on participant availability, replacing back-and-forth email chains with a simple voting interface."
slug: "rallly-group-scheduling-meeting-poll"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/lukevella/rallly"
tool_ecosystem:
  github_repo: "lukevella/rallly"
  github_stars: 5027
---

# Rallly Open-Source Group Scheduling and Meeting Poll Platform

Rallly is an open-source scheduling and collaboration tool that makes organizing group meetings effortless. Create meeting polls to find the best date and time based on participant availability, replacing back-and-forth email chains with a simple voting interface.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install rallly-group-scheduling-meeting-poll
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Rallly is an open-source scheduling and collaboration platform built with Next.js, Prisma, tRPC, and TailwindCSS. It serves as a self-hostable alternative to Doodle, allowing teams and groups to find the best time to meet through a simple polling interface.
How It Works
Users create a poll with proposed dates and times for a meeting or event. Participants then vote on their availability without needing to create an account. The platform aggregates votes and highlights the optimal time slot that works for the most participants.
Key Features
- Create date-based polls for group scheduling without sign-up requirements for participants
- Self-hostable with Docker for complete data ownership and privacy
- Built on a modern TypeScript stack: Next.js frontend, Prisma ORM, tRPC for type-safe APIs, PostgreSQL database
- Internationalized with community translations via Crowdin
- Email notifications for poll updates and new responses
- Clean, responsive UI with TailwindCSS
Integration Points
Rallly exposes a REST API that agents can use to programmatically create polls, add participants, check poll status, and retrieve results. Agents can automate the entire scheduling workflow: create a poll when a meeting is requested, distribute the link to participants, monitor responses, and announce the winning time slot.
Agent Use Cases
An AI agent can use Rallly to automate group scheduling. When someone asks to schedule a team meeting, the agent creates a Rallly poll with proposed times, shares the link via Slack or email, monitors for when enough participants have voted, and then creates a calendar event for the winning time. This eliminates the manual coordination overhead that plagues most scheduling workflows.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/rallly-group-scheduling-meeting-poll/)
