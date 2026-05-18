---
name: "Naabu Fast Port Scanner by ProjectDiscovery"
slug: "naabu-fast-port-scanner-projectdiscovery"
description: "Naabu is a fast and reliable port scanning tool written in Go by ProjectDiscovery. It supports SYN, CONNECT, and UDP scans, integrates with Nmap for service discovery, and handles IPv4/IPv6 targets with automatic deduplication for efficient attack surface enumeration."
github_stars: 5876
verification: "security_reviewed"
source: "https://github.com/projectdiscovery/naabu"
category: "Security & Verification"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "projectdiscovery/naabu"
  github_stars: 5876
---

# Naabu Fast Port Scanner by ProjectDiscovery

Naabu is a fast and reliable port scanning tool written in Go by ProjectDiscovery. It supports SYN, CONNECT, and UDP scans, integrates with Nmap for service discovery, and handles IPv4/IPv6 targets with automatic deduplication for efficient attack surface enumeration.

## Installation

Use the upstream install or setup path that matches your environment:
- go install -v github.com/projectdiscovery/naabu/v2/cmd/naabu@latest

Requirements and caveats from upstream:
- Download the ready to run [binary](https://github.com/projectdiscovery/naabu/releases/) / [docker](https://hub.docker.com/r/projectdiscovery/naabu) or install with GO
- ## Prerequisite
- The ports to scan for on the host can be specified via -p parameter (udp ports must be expressed as u:port). It takes nmap format ports and runs enumeration on them.

Basic usage or getting-started notes:
- <a href="#usage">Usage</a> •
- sh
- naabu -h

- Source: https://github.com/projectdiscovery/naabu
- Extracted from upstream docs: https://raw.githubusercontent.com/projectdiscovery/naabu/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/naabu-fast-port-scanner-projectdiscovery/)
