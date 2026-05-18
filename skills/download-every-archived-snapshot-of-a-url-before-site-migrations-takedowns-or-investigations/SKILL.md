---
name: "Download every archived snapshot of a URL before site migrations, takedowns, or investigations"
slug: "download-every-archived-snapshot-of-a-url-before-site-migrations-takedowns-or-investigations"
description: "Use waybackpack when an agent needs the full historical record for a URL, not a few clicks through the Wayback Machine UI. The agent can list or download snapshots, constrain by date, deduplicate archives, and preserve evidence locally before a site changes or disappears."
github_stars: 3173
verification: "listed"
source: "https://github.com/jsvine/waybackpack"
author: "Jeremy Singer-Vine"
category: "Research & Scraping"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "jsvine/waybackpack"
  github_stars: 3173
---

# Download every archived snapshot of a URL before site migrations, takedowns, or investigations

Use waybackpack when an agent needs the full historical record for a URL, not a few clicks through the Wayback Machine UI. The agent can list or download snapshots, constrain by date, deduplicate archives, and preserve evidence locally before a site changes or disappears.

## Prerequisites

Python 3, pip, a target URL, local disk space for archived snapshots, and optional tqdm for progress output.

## Installation

Use the upstream install or setup path that matches your environment:
- pip install waybackpack

Requirements and caveats from upstream:
- [![Version](https://img.shields.io/pypi/v/waybackpack.svg)](https://pypi.python.org/pypi/waybackpack) [![Support Python versions](https://img.shields.io/pypi/pyversions/waybackpack.svg)](https://pypi.python.org/pypi/w...
- Requires tqdm to be installed.
- Waypackback is written in pure Python, depends only on [requests](docs.python-requests.org), and should work wherever Python works. Requires Python 3.3+.

Basic usage or getting-started notes:
- For instance, to download every copy of the Department of Labor's homepage through 1996 (which happens to be the first year the site was archived), you'd run:
- [--from-date FROM_DATE] [--to-date TO_DATE]
- [--user-agent USER_AGENT] [--follow-redirects]

- Source: https://github.com/jsvine/waybackpack
- Extracted from upstream docs: https://raw.githubusercontent.com/jsvine/waybackpack/HEAD/README.md

## Documentation

- https://github.com/jsvine/waybackpack

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/download-every-archived-snapshot-of-a-url-before-site-migrations-takedowns-or-investigations/)
