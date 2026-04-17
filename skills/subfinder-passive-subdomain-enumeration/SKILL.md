---
title: "Subfinder Fast Passive Subdomain Enumeration Tool"
description: "What is Subfinder?\nSubfinder is a subdomain enumeration tool built by ProjectDiscovery that discovers valid subdomains for target domains using passive online sources. Unlike active enumeration tools that send requests to the target, Subfinder queries third-party data sources, making it fast and stealthy. Written in Go, it is designed to do one thing well: passive subdomain discovery.\nHow It Works\nInstall Subfinder via Go (go install github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest), Homebrew, Docker, or download pre-built binaries from GitHub releases. Run subfinder -d example.com to enumerate subdomains for a domain. Results come from curated passive sources including certificate transparency logs, search engine caches, DNS datasets, and security intelligence APIs. Configure API keys for premium sources like Shodan, SecurityTrails, and Censys in the provider config file to expand coverage.\nKey Features\nSubfinder includes fast DNS resolution with wildcard elimination to filter out false positives. It supports multiple output formats including plaintext, JSONL with source attribution, and directory-based output for batch processing. The tool handles rate limiting per provider, recursive subdomain discovery through capable sources, and proxy support for network-restricted environments. STDIN/STDOUT support enables piping results directly into other tools like httpx, nuclei, or nmap.\nConfiguration\nProvider API keys are stored in a YAML config file at the standard config directory. Each source can be individually enabled or disabled, and rate limits can be tuned per provider. You can specify custom DNS resolvers, exclude specific sources, or run with only select sources for targeted enumeration.\nIntegration Points\nSubfinder fits into security reconnaissance pipelines alongside other ProjectDiscovery tools. Pipe discovered subdomains to httpx for HTTP probing, to nuclei for vulnerability scanning, or to naabu for port scanning. The JSONL output mode preserves source metadata, enabling analysis of which data sources produce the most results for a given target. The Go library API allows embedding Subfinder directly into custom security tooling."
verification: security_reviewed
source: "https://github.com/projectdiscovery/subfinder"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "projectdiscovery/subfinder"
  github_stars: 13332
---

# Subfinder Fast Passive Subdomain Enumeration Tool

What is Subfinder?
Subfinder is a subdomain enumeration tool built by ProjectDiscovery that discovers valid subdomains for target domains using passive online sources. Unlike active enumeration tools that send requests to the target, Subfinder queries third-party data sources, making it fast and stealthy. Written in Go, it is designed to do one thing well: passive subdomain discovery.
How It Works
Install Subfinder via Go (go install github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest), Homebrew, Docker, or download pre-built binaries from GitHub releases. Run subfinder -d example.com to enumerate subdomains for a domain. Results come from curated passive sources including certificate transparency logs, search engine caches, DNS datasets, and security intelligence APIs. Configure API keys for premium sources like Shodan, SecurityTrails, and Censys in the provider config file to expand coverage.
Key Features
Subfinder includes fast DNS resolution with wildcard elimination to filter out false positives. It supports multiple output formats including plaintext, JSONL with source attribution, and directory-based output for batch processing. The tool handles rate limiting per provider, recursive subdomain discovery through capable sources, and proxy support for network-restricted environments. STDIN/STDOUT support enables piping results directly into other tools like httpx, nuclei, or nmap.
Configuration
Provider API keys are stored in a YAML config file at the standard config directory. Each source can be individually enabled or disabled, and rate limits can be tuned per provider. You can specify custom DNS resolvers, exclude specific sources, or run with only select sources for targeted enumeration.
Integration Points
Subfinder fits into security reconnaissance pipelines alongside other ProjectDiscovery tools. Pipe discovered subdomains to httpx for HTTP probing, to nuclei for vulnerability scanning, or to naabu for port scanning. The JSONL output mode preserves source metadata, enabling analysis of which data sources produce the most results for a given target. The Go library API allows embedding Subfinder directly into custom security tooling.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/subfinder-passive-subdomain-enumeration
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/subfinder-passive-subdomain-enumeration` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/subfinder-passive-subdomain-enumeration/)
