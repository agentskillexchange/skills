---
title: "Sherlock Social Media Username Hunter Across 400+ Networks"
description: "Sherlock hunts down social media accounts by username across more than 400 social networks. It is the go-to OSINT CLI tool for verifying online identities, finding connected accounts, and building digital footprints from a single username string."
slug: "sherlock-social-media-username-hunter"
category:
  - "Research &amp; Scraping"
framework:
  - "Custom Agents"
verification: "security_reviewed"
source: "https://github.com/sherlock-project/sherlock"
tool_ecosystem:
  github_repo: "sherlock-project/sherlock"
  github_stars: 76214
---

# Sherlock Social Media Username Hunter Across 400+ Networks

Sherlock hunts down social media accounts by username across more than 400 social networks. It is the go-to OSINT CLI tool for verifying online identities, finding connected accounts, and building digital footprints from a single username string.

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
clawhub install sherlock-social-media-username-hunter
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Sherlock is an open-source OSINT (Open Source Intelligence) command-line tool that searches for a given username across more than 400 social networks and websites simultaneously. Developed and maintained by the Sherlock Project community, it has become one of the most widely used username enumeration tools in the security research and digital investigation space.
The tool works by taking one or more usernames as input and querying hundreds of platforms — including GitHub, Twitter/X, Instagram, Reddit, TikTok, LinkedIn, Medium, Steam, and many more — to determine whether an account with that username exists. Results are output to the terminal and optionally saved as text, CSV, or XLSX files for further analysis.
How It Works
Sherlock sends HTTP requests to each supported site using known URL patterns for user profile pages. It analyzes the HTTP response status codes, page content, and redirect behavior to determine whether an account exists, does not exist, or returned an ambiguous result. The tool supports Tor routing for anonymous lookups, custom proxy configuration, and timeout controls for slow networks.
Key Features and Capabilities
The tool supports searching multiple usernames in a single run, similar username fuzzing using the {?} wildcard (replacing with underscore, dash, and period variants), and NSFW site filtering. Output can be directed to custom folders or files, and the –browse flag will automatically open found profile URLs in the default browser.
Integration with AI Agents
As an agent skill, Sherlock enables automated OSINT workflows where an AI agent can verify claimed identities, cross-reference usernames across platforms, detect sock puppet accounts, or build comprehensive digital footprints. The structured CSV/XLSX output makes it straightforward to parse results programmatically. The tool is available via pip (sherlock-project) and Docker, making it easy to integrate into any automated pipeline or agent environment.
Technical Details
Sherlock is written in Python and distributed via PyPI as the sherlock-project package. It requires Python 3.x and has minimal dependencies. The project is MIT-licensed and has an active contributor community with regular site list updates. It is packaged for major Linux distributions including Debian, Kali, BlackArch, and Homebrew on macOS.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sherlock-social-media-username-hunter/)
