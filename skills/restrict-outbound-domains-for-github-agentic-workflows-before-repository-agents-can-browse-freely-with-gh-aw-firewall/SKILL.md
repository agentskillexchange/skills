---
name: "Restrict outbound domains for GitHub Agentic Workflows before repository agents can browse freely with gh-aw-firewall"
slug: "restrict-outbound-domains-for-github-agentic-workflows-before-repository-agents-can-browse-freely-with-gh-aw-firewall"
description: "Run GitHub Agentic Workflow jobs behind a domain allowlist and optional API-key sidecar instead of giving repository agents broad outbound access."
github_stars: 55
verification: "security_reviewed"
source: "https://github.com/github/gh-aw-firewall"
author: "GitHub"
publisher_type: "organization"
category: "Security & Verification"
framework: "Custom Agents"
tool_ecosystem:
  github_repo: "github/gh-aw-firewall"
  github_stars: 55
---

# Restrict outbound domains for GitHub Agentic Workflows before repository agents can browse freely with gh-aw-firewall

Run GitHub Agentic Workflow jobs behind a domain allowlist and optional API-key sidecar instead of giving repository agents broad outbound access.

## Prerequisites

Docker 20.10+, Docker Compose v2, Linux host or compatible runtime

## Installation

Requirements and caveats from upstream:
- awf runs your command inside a Docker sandbox with three containers:
- **Docker**: 20.10+ with Docker Compose v2
- **Node.js**: 20.19.0+ (for building from source)

Basic usage or getting-started notes:
- **OS**: Ubuntu 22.04+ or compatible Linux distribution (x86_64 and arm64)
- See [Compatibility](docs/compatibility.md) for full details on supported versions and tested configurations.
- ## Get started fast

- Source: https://github.com/github/gh-aw-firewall
- Extracted from upstream docs: https://raw.githubusercontent.com/github/gh-aw-firewall/HEAD/README.md

## Documentation

- https://github.github.com/gh-aw-firewall/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/restrict-outbound-domains-for-github-agentic-workflows-before-repository-agents-can-browse-freely-with-gh-aw-firewall/)
