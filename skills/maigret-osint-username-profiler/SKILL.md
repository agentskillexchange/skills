---
name: "Maigret OSINT Username Profiler Across 3000+ Sites"
description: "Maigret collects a dossier on a person by username only, checking for accounts on over 3000 sites and gathering available information from web pages. A powerful Sherlock fork with recursive search, profile parsing, and structured report output."
category: "Research &amp; Scraping"
framework: "Custom Agents"
verification: security_reviewed
source: "https://github.com/soxoj/maigret"
tool_ecosystem:
  github_repo: "https://github.com/soxoj/maigret"
  github_stars: 19325
---
# Maigret OSINT Username Profiler Across 3000+ Sites

Maigret collects a dossier on a person by username only, checking for accounts on over 3000 sites and gathering available information from web pages. A powerful Sherlock fork with recursive search, profile parsing, and structured report output.

Maigret is an advanced open-source OSINT tool that builds a comprehensive dossier on a person by searching for their username across more than 3000 websites and social networks. Created by soxoj and named after the fictional French detective Jules Maigret, it is a feature-rich fork of the Sherlock project that goes well beyond simple username enumeration.

While Sherlock checks whether a username exists on a given site, Maigret takes the investigation further by parsing found profile pages to extract personal information, links to other profiles, and additional identifiers. It then performs recursive searches using any newly discovered usernames and IDs, building an expanding web of connected accounts.

Core Features

Maigret supports over 3000 sites with a default search against the 500 most popular ones ranked by traffic. It handles Tor hidden services, I2P sites, and regular domains via DNS resolution. The tool detects censorship and CAPTCHA blocks, implements request retries with configurable timeouts, and can filter searches by site category or country using tags.

Profile Extraction Engine

The socid_extractor module parses profile pages to pull out structured data: display names, bios, join dates, follower counts, linked accounts, and other metadata. This extracted information feeds back into the search process, enabling Maigret to discover accounts that use different usernames but belong to the same person.

Output and Reporting

Results can be output as plain text, JSON, CSV, HTML reports, or PDF documents. The HTML report provides a visual overview of all found accounts with extracted metadata, making it suitable for investigation documentation. The tool also has a Telegram bot interface for online searches without local installation.

Agent Integration

As an agent skill, Maigret enables deep OSINT automation. An AI agent can submit a username and receive back a structured dossier including all found accounts, extracted profile data, and cross-references between identities. The JSON output format is ideal for programmatic consumption. Maigret is installable via pip (maigret package on PyPI) and Docker, with standalone Windows binaries also available. The project is MIT-licensed and actively maintained with regular site database updates.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill maigret-osint-username-profiler
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill maigret-osint-username-profiler -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill maigret-osint-username-profiler -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill maigret-osint-username-profiler -a codex
```

### OpenClaw

```bash
clawhub install maigret-osint-username-profiler
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/maigret-osint-username-profiler/)
