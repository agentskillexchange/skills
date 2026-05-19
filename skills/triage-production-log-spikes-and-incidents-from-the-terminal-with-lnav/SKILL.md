---
name: "Triage production log spikes and incidents from the terminal with lnav"
slug: "triage-production-log-spikes-and-incidents-from-the-terminal-with-lnav"
description: "Open raw logs, jump to error clusters, query structured fields, and summarize incident clues without shipping data to a separate platform."
github_stars: 10159
verification: "security_reviewed"
source: "https://github.com/tstack/lnav"
author: "tstack"
publisher_type: "individual"
category: "Runbooks & Diagnostics"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "tstack/lnav"
  github_stars: 10159
---

# Triage production log spikes and incidents from the terminal with lnav

Open raw logs, jump to error clusters, query structured fields, and summarize incident clues without shipping data to a separate platform.

## Prerequisites

lnav, local or remote log files, terminal access

## Installation

Use the upstream install or setup path that matches your environment:
- $ brew install lnav
- $ make

Requirements and caveats from upstream:
- You can SSH into a demo node to play with lnav before installing.

Basic usage or getting-started notes:
- filter messages using [regular expressions](https://docs.lnav.org/en/latest/usage.html#regular-expression-match) or [SQLite expressions](https://docs.lnav.org/en/latest/usage.html#sqlite-expression);
- an example:
- [Download a statically-linked binary for Linux/MacOS/Windows from the release page](https://github.com/tstack/lnav/releases/latest#release-artifacts)

- Source: https://github.com/tstack/lnav
- Extracted from upstream docs: https://raw.githubusercontent.com/tstack/lnav/HEAD/README.md

## Documentation

- https://docs.lnav.org/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/triage-production-log-spikes-and-incidents-from-the-terminal-with-lnav/)
