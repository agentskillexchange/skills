---
name: "Subfinder Fast Passive Subdomain Enumeration Tool"
description: "Subfinder is a passive subdomain discovery tool by ProjectDiscovery that finds valid subdomains for websites using curated online sources. Optimized for speed and stealth, it integrates cleanly into security reconnaissance pipelines via stdin/stdout support."
category: "Security &amp; Verification"
framework: "Custom Agents"
verification: security_reviewed
source: "https://github.com/projectdiscovery/subfinder"
tool_ecosystem:
  github_repo: "https://github.com/projectdiscovery/subfinder"
  github_stars: 13332
  license: "MIT"
---
# Subfinder Fast Passive Subdomain Enumeration Tool

Subfinder is a passive subdomain discovery tool by ProjectDiscovery that finds valid subdomains for websites using curated online sources. Optimized for speed and stealth, it integrates cleanly into security reconnaissance pipelines via stdin/stdout support.

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

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill subfinder-passive-subdomain-enumeration
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill subfinder-passive-subdomain-enumeration -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill subfinder-passive-subdomain-enumeration -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill subfinder-passive-subdomain-enumeration -a codex
```

### OpenClaw

```bash
clawhub install subfinder-passive-subdomain-enumeration
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/subfinder-passive-subdomain-enumeration/)
