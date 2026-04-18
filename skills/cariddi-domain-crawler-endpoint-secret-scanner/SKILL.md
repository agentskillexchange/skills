---
title: "Cariddi Domain Crawler and Endpoint Secret Scanner"
description: "Cariddi is a Go-based security tool that takes a list of domains, crawls their URLs, and scans for endpoints, secrets, API keys, file extensions, tokens, and errors. It supports configurable concurrency, depth limits, proxy routing, and multiple output formats."
verification: security_reviewed
source: "https://github.com/edoardottt/cariddi"
category:
  - "Security & Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "edoardottt/cariddi"
  github_stars: 3338
---

# Cariddi Domain Crawler and Endpoint Secret Scanner

Cariddi is an open-source web crawler and security scanner written in Go that takes a list of target domains via stdin, crawls discovered URLs, and scans for sensitive information including API keys, secrets, tokens, error messages, and interesting file extensions. It is designed for bug bounty hunters, penetration testers, and security researchers who need automated reconnaissance across multiple domains.

Core Capabilities Cariddi performs several types of scans simultaneously. Endpoint hunting (-e) identifies potentially sensitive API endpoints and URL patterns. Secret scanning (-s) uses pattern matching to detect exposed API keys, tokens, and credentials in page source code. Error detection (-err) finds verbose error messages that leak implementation details. File extension scanning (-ext) discovers downloadable files ranked by sensitivity level from 1 (most sensitive) to 7. Information gathering (-info) extracts useful metadata from crawled pages.

Crawling Configuration The crawler supports configurable concurrency levels (-c, default 20), maximum depth limits (-md), request delays (-d), custom headers (-headers), random user agent rotation (-rua), and proxy routing through HTTP or SOCKS5 proxies. URL filtering (-i) lets you ignore paths containing specific keywords like forum, blog, or community. The -intensive flag extends crawling to subdomains of each target.

Output and Integration Results can be output as plain text to stdout (-plain), JSON (-json), text files (-ot), or HTML reports (-oh). HTTP responses can be stored for later analysis with -sr. The caching system (-cache) avoids re-crawling previously visited URLs across runs. Custom endpoint patterns (-ef) and secret patterns (-sf) can be loaded from external files for domain-specific scanning rules.

Installation Cariddi is available through multiple package managers: Homebrew (brew install cariddi), Snap (snap install cariddi), Go install (go install github.com/edoardottt/cariddi/cmd/cariddi@latest), Arch Linux (pacman -Syu cariddi), and Nix. It can also be built from source with standard Go tooling.

Agent Integration Points Security-focused agents can pipe domain lists into Cariddi for automated reconnaissance during penetration testing workflows. The JSON output mode integrates cleanly with downstream analysis pipelines. Agents can combine Cariddi with subdomain enumeration tools like Subfinder to build comprehensive attack surface maps, or use it in CI/CD pipelines to scan staging environments for accidentally exposed secrets before production deployment.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/cariddi-domain-crawler-endpoint-secret-scanner
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/cariddi-domain-crawler-endpoint-secret-scanner` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cariddi-domain-crawler-endpoint-secret-scanner/)
