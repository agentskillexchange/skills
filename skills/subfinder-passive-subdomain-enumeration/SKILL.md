---
title: "Subfinder Fast Passive Subdomain Enumeration Tool"
slug: "subfinder-passive-subdomain-enumeration"
description: "Subfinder is a passive subdomain discovery tool by ProjectDiscovery that finds valid subdomains for websites using curated online sources. Optimized for speed and stealth, it integrates cleanly into security reconnaissance pipelines via stdin/stdout support."
verification: "security_reviewed"
source: "https://github.com/projectdiscovery/subfinder"
author: "ProjectDiscovery"
publisher_type: "Open Source Project"
category: "Security & Verification"
framework: "Custom Agents"
tool_ecosystem:
  github_repo: "projectdiscovery/subfinder"
  github_stars: 13332
---

# Subfinder Fast Passive Subdomain Enumeration Tool

Subfinder is a passive subdomain discovery tool by ProjectDiscovery that finds valid subdomains for websites using curated online sources. Optimized for speed and stealth, it integrates cleanly into security reconnaissance pipelines via stdin/stdout support.

## Prerequisites

Go 1.21+

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
go install github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
```

## Documentation

- https://docs.projectdiscovery.io/tools/subfinder/overview

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/subfinder-passive-subdomain-enumeration/)
