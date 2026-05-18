---
name: "Bearer CLI SAST Code Security and Privacy Scanner"
slug: "bearer-cli-sast-code-security-privacy-scanner"
description: "Bearer CLI is an open-source static application security testing (SAST) tool that scans source code to identify, filter, and prioritize security vulnerabilities and privacy risks. Covers OWASP Top 10 and CWE Top 25 with data flow analysis across multiple languages."
github_stars: 2610
verification: "listed"
source: "https://github.com/Bearer/bearer"
category: "Security & Verification"
framework: "Claude Code"
tool_ecosystem:
  github_repo: "Bearer/bearer"
  github_stars: 2610
---

# Bearer CLI SAST Code Security and Privacy Scanner

Bearer CLI is an open-source static application security testing (SAST) tool that scans source code to identify, filter, and prioritize security vulnerabilities and privacy risks. Covers OWASP Top 10 and CWE Top 25 with data flow analysis across multiple languages.

## Installation

Use the upstream install or setup path that matches your environment:
- brew install bearer/tap/bearer
- brew update && brew upgrade bearer/tap/bearer
- docker run --rm -v /path/to/repo:/tmp/scan bearer/bearer:latest-amd64 scan /tmp/scan
- Additionally, you can use docker compose. Add the following to your docker-compose.yml file and replace the volumes with the appropriate paths for your project:

Requirements and caveats from upstream:
- **Bearer CLI (Open Source)**: Go • Java • JavaScript • TypeScript • PHP • Python • Ruby
- **Advanced Cross-file Analysis**: Java • Python • C# _(alpha)_
- <summary>Docker</summary>

Basic usage or getting-started notes:
- [Getting Started](#rocket-getting-started) - [FAQ](#question-faqs) - [Documentation](https://docs.bearer.com) - [Report a Bug](https://github.com/Bearer/bearer/issues/new/choose)
- ## :rocket: Getting started
- Discover your most critical security risks and vulnerabilities in only a few minutes. In this guide, you will install Bearer CLI, run a security scan on a local project, and view the results. Let's get started!

- Source: https://github.com/Bearer/bearer
- Extracted from upstream docs: https://raw.githubusercontent.com/Bearer/bearer/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/bearer-cli-sast-code-security-privacy-scanner/)
