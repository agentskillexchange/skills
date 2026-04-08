---
title: Taskwarrior Command-Line Task Management System
description: 'Taskwarrior is a command-line task management system developed by Gothenburg
  Bit Factory. Active since 2006, it provides a feature-rich interface for managing
  personal and team task lists entirely from the terminal. It is written in C++, licensed
  under the MIT license, and available on Linux, macOS, BSD, and Windows. Core Task
  Management Taskwarrior supports task creation, modification, completion, deletion,
  and querying through a concise command syntax. Each task can have a description,
  project assignment, priority level, tags, due date, scheduled date, wait date, and
  recurrence pattern. Tasks support dependencies so that blocking relationships can
  be modeled. Filtering and Reporting The tool includes a powerful filter language
  for querying tasks by any combination of attributes. Built-in reports like task
  list , task next , task calendar , and task burndown provide different views of
  your task data. Custom reports can be defined in the configuration file. Annotations
  and Context Tasks can have annotations — timestamped notes attached to a task —
  allowing you to record decisions, URLs, or progress updates. The context feature
  lets you define named filter presets (e.g., “work” or “personal”) that automatically
  narrow your view to relevant tasks. Hooks and Extensions Taskwarrior has a hook
  system that runs scripts on task events (add, modify, complete, delete). This enables
  integrations with time trackers, notification systems, Git, and other tools. The
  ecosystem includes taskwarrior-tui (a terminal UI), Timewarrior (time tracking companion),
  Forecastle, and numerous community plugins. Sync Protocol Taskwarrior implements
  a sync protocol via Taskserver (taskd) or third-party services, enabling task synchronization
  across multiple machines. Tasks are stored locally in a plain-text format that is
  easy to back up and version-control. Agent Integration For AI agents, Taskwarrior
  provides a JSON export/import interface ( task export and task import ) and a structured
  command-line interface that can be driven programmatically. Agents can create tasks,
  query for overdue items, manage projects, and automate task workflows. Installation
  Install via package managers: brew install task (macOS), apt install taskwarrior
  (Debian/Ubuntu), dnf install task (Fedora), or build from source. The project has
  over 5,600 GitHub stars and comprehensive documentation at taskwarrior.org.'
verification: security_reviewed
source: https://github.com/GothenburgBitFactory/taskwarrior
category:
- Calendar, Email &amp; Productivity
framework:
- Multi-Framework
tool_ecosystem:
  github_repo: gothenburgbitfactory/taskwarrior
  github_stars: 5685
---

# Taskwarrior Command-Line Task Management System

Taskwarrior is a command-line task management system developed by Gothenburg Bit Factory. Active since 2006, it provides a feature-rich interface for managing personal and team task lists entirely from the terminal. It is written in C++, licensed under the MIT license, and available on Linux, macOS, BSD, and Windows. Core Task Management Taskwarrior supports task creation, modification, completion, deletion, and querying through a concise command syntax. Each task can have a description, project assignment, priority level, tags, due date, scheduled date, wait date, and recurrence pattern. Tasks support dependencies so that blocking relationships can be modeled. Filtering and Reporting The tool includes a powerful filter language for querying tasks by any combination of attributes. Built-in reports like task list , task next , task calendar , and task burndown provide different views of your task data. Custom reports can be defined in the configuration file. Annotations and Context Tasks can have annotations — timestamped notes attached to a task — allowing you to record decisions, URLs, or progress updates. The context feature lets you define named filter presets (e.g., “work” or “personal”) that automatically narrow your view to relevant tasks. Hooks and Extensions Taskwarrior has a hook system that runs scripts on task events (add, modify, complete, delete). This enables integrations with time trackers, notification systems, Git, and other tools. The ecosystem includes taskwarrior-tui (a terminal UI), Timewarrior (time tracking companion), Forecastle, and numerous community plugins. Sync Protocol Taskwarrior implements a sync protocol via Taskserver (taskd) or third-party services, enabling task synchronization across multiple machines. Tasks are stored locally in a plain-text format that is easy to back up and version-control. Agent Integration For AI agents, Taskwarrior provides a JSON export/import interface ( task export and task import ) and a structured command-line interface that can be driven programmatically. Agents can create tasks, query for overdue items, manage projects, and automate task workflows. Installation Install via package managers: brew install task (macOS), apt install taskwarrior (Debian/Ubuntu), dnf install task (Fedora), or build from source. The project has over 5,600 GitHub stars and comprehensive documentation at taskwarrior.org.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/taskwarrior-command-line-task-management-system/)
