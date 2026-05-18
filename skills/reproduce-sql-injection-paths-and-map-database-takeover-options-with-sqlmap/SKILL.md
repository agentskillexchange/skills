---
name: "Reproduce SQL injection paths and map database takeover options with sqlmap"
slug: "reproduce-sql-injection-paths-and-map-database-takeover-options-with-sqlmap"
description: "Take a suspected injectable request, replay it on an authorized target, confirm the finding, and enumerate reachable database actions before manual follow-up."
github_stars: 37104
verification: "listed"
source: "https://github.com/sqlmapproject/sqlmap"
author: "sqlmapproject"
publisher_type: "open_source_project"
category: "Security & Verification"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "sqlmapproject/sqlmap"
  github_stars: 37104
---

# Reproduce SQL injection paths and map database takeover options with sqlmap

Take a suspected injectable request, replay it on an authorized target, confirm the finding, and enumerate reachable database actions before manual follow-up.

## Prerequisites

Python, authorized target URL or captured HTTP request, operator approval for security testing

## Installation

Use the upstream install or setup path that matches your environment:
- git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev

Requirements and caveats from upstream:
- [![.github/workflows/tests.yml](https://github.com/sqlmapproject/sqlmap/actions/workflows/tests.yml/badge.svg)](https://github.com/sqlmapproject/sqlmap/actions/workflows/tests.yml) [![Python 2.7|3.x](https://img.shiel...
- sqlmap works out of the box with [Python](https://www.python.org/download/) version **2.7** and **3.x** on any platform.
- python sqlmap.py -h

Basic usage or getting-started notes:
- ----
- You can download the latest tarball by clicking [here](https://github.com/sqlmapproject/sqlmap/tarball/master) or latest zipball by clicking [here](https://github.com/sqlmapproject/sqlmap/zipball/master).
- Preferably, you can download sqlmap by cloning the [Git](https://github.com/sqlmapproject/sqlmap) repository:

- Source: https://github.com/sqlmapproject/sqlmap
- Extracted from upstream docs: https://raw.githubusercontent.com/sqlmapproject/sqlmap/HEAD/README.md

## Documentation

- http://sqlmap.org

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/reproduce-sql-injection-paths-and-map-database-takeover-options-with-sqlmap/)
