---
name: "Maigret OSINT Username Profiler Across 3000+ Sites"
slug: "maigret-osint-username-profiler"
description: "Maigret collects a dossier on a person by username only, checking for accounts on over 3000 sites and gathering available information from web pages. A powerful Sherlock fork with recursive search, profile parsing, and structured report output."
github_stars: 19325
verification: "security_reviewed"
source: "https://github.com/soxoj/maigret"
category: "Research & Scraping"
framework: "Custom Agents"
tool_ecosystem:
  github_repo: "soxoj/maigret"
  github_stars: 19325
---

# Maigret OSINT Username Profiler Across 3000+ Sites

Maigret collects a dossier on a person by username only, checking for accounts on over 3000 sites and gathering available information from web pages. A powerful Sherlock fork with recursive search, profile parsing, and structured report output.

## Installation

Use the upstream install or setup path that matches your environment:
- pip install maigret
- git clone https://github.com/soxoj/maigret && cd maigret
- docker pull soxoj/maigret
- docker run -v /mydir:/app/reports soxoj/maigret:latest username --html

Requirements and caveats from upstream:
- <img alt="Minimum Python version required: 3.10+" src="https://img.shields.io/badge/Python-3.10%2B-brightgreen?style=flat-square" />
- Ensure you have Python 3.10 or higher.
- Embeddable in Python projects — import maigret and run searches programmatically (see [library usage](https://maigret.readthedocs.io/en/latest/library-usage.html)).

Basic usage or getting-started notes:
- [Usage](#usage)
- See also: [Quick start](https://maigret.readthedocs.io/en/latest/quick-start.html).
- Supports 3,000+ sites ([see full list](https://github.com/soxoj/maigret/blob/main/sites.md)). A default run checks the 500 highest-ranked sites by traffic; pass -a to scan everything, or --tags to narrow by category/c...

- Source: https://github.com/soxoj/maigret
- Extracted from upstream docs: https://raw.githubusercontent.com/soxoj/maigret/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/maigret-osint-username-profiler/)
