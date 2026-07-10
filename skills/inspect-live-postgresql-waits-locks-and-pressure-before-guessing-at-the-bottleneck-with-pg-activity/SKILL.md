---
name: "Inspect live PostgreSQL waits locks and pressure before guessing at the bottleneck with pg_activity"
slug: "inspect-live-postgresql-waits-locks-and-pressure-before-guessing-at-the-bottleneck-with-pg-activity"
description: "Open a live PostgreSQL activity view during incidents so you can see sessions, waits, locks, and pressure before making a bad call."
github_stars: 3010
verification: "security_reviewed"
source: "https://github.com/dalibo/pg_activity"
author: "DALIBO"
publisher_type: "organization"
category: "Runbooks & Diagnostics"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "dalibo/pg_activity"
  github_stars: 3010
  npm_package: "pg_activity"
  npm_weekly_downloads: 20770
---

# Inspect live PostgreSQL waits locks and pressure before guessing at the bottleneck with pg_activity

Open a live PostgreSQL activity view during incidents so you can see sessions, waits, locks, and pressure before making a bad call.

## Prerequisites

PostgreSQL connection access, pg_activity installation, terminal access to the target environment

## Installation

Use the upstream install or setup path that matches your environment:
- $ pipx install "pg_activity[psycopg]"
- $ git clone https://github.com/dalibo/pg_activity.git
- $ git clone https://github.com/dalibo/pg_activity

Requirements and caveats from upstream:
- [![Latest PyPI version](https://img.shields.io/pypi/v/pg_activity.svg)](https://pypi.python.org/pypi/pg_activity)
- pg\_activity can be installed using pip on Python 3.8 or later along with
- pg_activity must be the same user running postgresql server (postgres by

Basic usage or getting-started notes:
- ## From distribution packages
- The simplest way to install pg\_activity is through the package manager of your
- Linux distribution, if it ships with a package. E.g., on Debian-based

- Source: https://github.com/dalibo/pg_activity
- Extracted from upstream docs: https://raw.githubusercontent.com/dalibo/pg_activity/HEAD/README.md

## Documentation

- https://github.com/dalibo/pg_activity

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/inspect-live-postgresql-waits-locks-and-pressure-before-guessing-at-the-bottleneck-with-pg-activity/)
