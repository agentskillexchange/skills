---
title: "httpx Fast Multi-Purpose HTTP Probing Toolkit by ProjectDiscovery"
description: "httpx by ProjectDiscovery is a fast, multi-purpose HTTP toolkit for running probes against lists of hosts. It detects live web servers, extracts response metadata, fingerprints technologies, and outputs structured results for security reconnaissance and monitoring pipelines."
slug: "httpx-http-probing-toolkit-projectdiscovery"
category:
  - "Security &amp; Verification"
framework:
  - "Custom Agents"
verification: "security_reviewed"
source: "https://github.com/projectdiscovery/httpx"
tool_ecosystem:
  github_repo: "projectdiscovery/httpx"
  github_stars: 9759
---

# httpx Fast Multi-Purpose HTTP Probing Toolkit by ProjectDiscovery

httpx by ProjectDiscovery is a fast, multi-purpose HTTP toolkit for running probes against lists of hosts. It detects live web servers, extracts response metadata, fingerprints technologies, and outputs structured results for security reconnaissance and monitoring pipelines.

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
clawhub install httpx-http-probing-toolkit-projectdiscovery
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

httpx is a fast and multi-purpose HTTP toolkit developed by ProjectDiscovery that allows running multiple probes against lists of hosts using a retryable HTTP client library. With nearly 10,000 GitHub stars, it is a cornerstone tool in security reconnaissance workflows, used to quickly identify live web servers, extract response metadata, and fingerprint web technologies at scale.
The tool accepts target hosts from STDIN, files, or direct input and performs configurable HTTP requests against each target. It then collects and displays a wide range of response attributes including status codes, content length, content type, page titles, redirect locations, TLS certificate information, response headers, JARM fingerprints, favicon hashes, and technology detection via Wappalyzer signatures.
Probing Capabilities
httpx can probe for dozens of different data points in a single run. Beyond basic HTTP metadata, it supports hash computation of response bodies (MD5, SHA1, SHA256, SHA512, mmh3, simhash), IP extraction, CDN/WAF detection, HTTP/2 support checking, virtual host detection, and pipeline status. The tool automatically handles HTTP and HTTPS schemes, following redirects and collecting certificate chains.
Input and Output Flexibility
Input can be piped from other tools like subfinder or katana via STDIN, read from files containing host lists, or specified directly via command-line targets. Output supports STDOUT for terminal display and tool chaining, JSON for structured processing, and CSV for spreadsheet analysis. Custom output templates allow users to format results exactly as needed for downstream consumption.
Performance and Reliability
Built in Go with the retryablehttp library, httpx handles connection failures, timeouts, and rate limiting gracefully. It supports configurable concurrency, custom HTTP methods, request headers, and body content. Proxy support including SOCKS5 is available for routing through anonymization networks.
Agent Integration
As an agent skill, httpx enables automated infrastructure reconnaissance and monitoring. An AI agent can submit a list of domains or IPs and receive back structured data about which hosts are alive, what technologies they run, their TLS configuration, and their response characteristics. The JSON output format makes it straightforward to filter and analyze results programmatically. httpx is available as a Go binary, Docker image, and via package managers. It is MIT-licensed and actively maintained with regular releases from the ProjectDiscovery team.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/httpx-http-probing-toolkit-projectdiscovery/)
