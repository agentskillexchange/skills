---
name: "Timewarrior Command-Line Time Tracking and Reporting"
description: "Timewarrior is a command-line time tracking tool from the Taskwarrior project. It records time intervals with tags, generates flexible reports, and integrates with Taskwarrior for automatic time tracking of tasks. Data is stored as plain text files with no database required."
verification: security_reviewed
source: "https://github.com/GothenburgBitFactory/timewarrior"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "gothenburgbitfactory/timewarrior"
  github_stars: 1580
---

# Timewarrior Command-Line Time Tracking and Reporting

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

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/timewarrior-command-line-time-tracking-reporting/)
