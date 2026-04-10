---
title: "Cariddi Domain Crawler and Endpoint Secret Scanner"
description: "Cariddi is a Go-based security tool that takes a list of domains, crawls their URLs, and scans for endpoints, secrets, API keys, file extensions, tokens, and errors. It supports configurable concurrency, depth limits, proxy routing, and multiple output formats."
slug: "cariddi-domain-crawler-endpoint-secret-scanner"
category:
  - "Security &amp; Verification"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/edoardottt/cariddi"
---

# Cariddi Domain Crawler and Endpoint Secret Scanner

Cariddi is a Go-based security tool that takes a list of domains, crawls their URLs, and scans for endpoints, secrets, API keys, file extensions, tokens, and errors. It supports configurable concurrency, depth limits, proxy routing, and multiple output formats.

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
clawhub install cariddi-domain-crawler-endpoint-secret-scanner
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Cariddi is an open-source web crawler and security scanner written in Go that takes a list of target domains via stdin, crawls discovered URLs, and scans for sensitive information including API keys, secrets, tokens, error messages, and interesting file extensions. It is designed for bug bounty hunters, penetration testers, and security researchers who need automated reconnaissance across multiple domains.
Core Capabilities
Cariddi performs several types of scans simultaneously. Endpoint hunting (-e) identifies potentially sensitive API endpoints and URL patterns. Secret scanning (-s) uses pattern matching to detect exposed API keys, tokens, and credentials in page source code. Error detection (-err) finds verbose error messages that leak implementation details. File extension scanning (-ext) discovers downloadable files ranked by sensitivity level from 1 (most sensitive) to 7. Information gathering (-info) extracts useful metadata from crawled pages.
Crawling Configuration
The crawler supports configurable concurrency levels (-c, default 20), maximum depth limits (-md), request delays (-d), custom headers (-headers), random user agent rotation (-rua), and proxy routing through HTTP or SOCKS5 proxies. URL filtering (-i) lets you ignore paths containing specific keywords like forum, blog, or community. The -intensive flag extends crawling to subdomains of each target.
Output and Integration
Results can be output as plain text to stdout (-plain), JSON (-json), text files (-ot), or HTML reports (-oh). HTTP responses can be stored for later analysis with -sr. The caching system (-cache) avoids re-crawling previously visited URLs across runs. Custom endpoint patterns (-ef) and secret patterns (-sf) can be loaded from external files for domain-specific scanning rules.
Installation
Cariddi is available through multiple package managers: Homebrew (brew install cariddi), Snap (snap install cariddi), Go install (go install github.com/edoardottt/cariddi/cmd/cariddi@latest), Arch Linux (pacman -Syu cariddi), and Nix. It can also be built from source with standard Go tooling.
Agent Integration Points
Security-focused agents can pipe domain lists into Cariddi for automated reconnaissance during penetration testing workflows. The JSON output mode integrates cleanly with downstream analysis pipelines. Agents can combine Cariddi with subdomain enumeration tools like Subfinder to build comprehensive attack surface maps, or use it in CI/CD pipelines to scan staging environments for accidentally exposed secrets before production deployment.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cariddi-domain-crawler-endpoint-secret-scanner/)
