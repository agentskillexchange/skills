---
title: "Timewarrior Command-Line Time Tracking and Reporting"
description: "Timewarrior is a command-line time tracking tool from the Taskwarrior project. It records time intervals with tags, generates flexible reports, and integrates with Taskwarrior for automatic time tracking of tasks. Data is stored as plain text files with no database required."
slug: "timewarrior-command-line-time-tracking-reporting"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/GothenburgBitFactory/timewarrior"
---

# Timewarrior Command-Line Time Tracking and Reporting

Timewarrior is a command-line time tracking tool from the Taskwarrior project. It records time intervals with tags, generates flexible reports, and integrates with Taskwarrior for automatic time tracking of tasks. Data is stored as plain text files with no database required.

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
clawhub install timewarrior-command-line-time-tracking-reporting
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Timewarrior is an open-source command-line time tracking and reporting tool developed by the GothenburgBitFactory team, the same organization behind Taskwarrior. Written in C++, it provides precise time tracking with a simple CLI interface, storing all data as local plain-text files that are easy to back up, sync, and version-control.
Core Workflow
Starting and stopping time tracking is as simple as timew start ProjectA coding and timew stop. Intervals are tagged with arbitrary labels for categorization. The timew summary command shows tracked time grouped by day and tag, while timew report provides more detailed breakdowns. Retroactive tracking is supported with commands like timew track 9:00 - 12:00 meeting client-review for recording past work.
Reporting and Analysis
Built-in reports include daily, weekly, and monthly summaries with tag-based filtering. The timew export command outputs data as JSON for integration with external reporting tools, invoicing systems, or custom dashboards. Date range filtering with natural-language expressions like timew summary :week or timew summary 2024-01-01 - 2024-01-31 makes it easy to slice data by any period.
Taskwarrior Integration
Timewarrior integrates directly with Taskwarrior through hooks: when you start a task in Taskwarrior, Timewarrior automatically begins tracking time for it. This creates a seamless workflow where task management and time tracking are unified. The integration requires no configuration beyond installing the hook script.
Extension System
Timewarrior supports Python and other scripting languages through its extension API. Custom extensions can generate reports in any format, calculate billable hours, or push data to external services. Several community extensions provide CSV export, invoice generation, and calendar integration.
Agent Skill Applications
AI agents can use Timewarrior to track time spent on different tasks and projects automatically. Combined with Taskwarrior, agents get a complete task-plus-time-tracking system operated entirely from the command line. The JSON export enables agents to analyze time allocation, generate productivity reports, or feed time data into billing workflows.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/timewarrior-command-line-time-tracking-reporting/)
