---
title: "Generate and screen lookalike domains with dnstwist for brand abuse triage"
description: "Generate typosquat and homograph domain candidates, resolve them, and flag likely phishing or impersonation infrastructure before manual brand-abuse review."
verification: "listed"
source: "https://github.com/elceef/dnstwist"
category:
  - "Security & Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "elceef/dnstwist"
  github_stars: 5656
---

# Generate and screen lookalike domains with dnstwist for brand abuse triage

Use dnstwist when the immediate job is to generate lookalike domains for a known brand or domain, resolve them, and screen the results for likely phishing, typosquatting, or impersonation signals. The upstream project is explicitly focused on domain permutations and follow-up checks for brand abuse detection. Invoke this instead of normal DNS tooling when the goal is abuse triage around confusingly similar domains, not generic hostname lookup or broad attack-surface enumeration. The scope boundary is tight: dnstwist generates permutations and screens them for review. It is not a general DNS platform, registrar product, or full reconnaissance suite.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/generate-and-screen-lookalike-domains-with-dnstwist-for-brand-abuse-triage/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/generate-and-screen-lookalike-domains-with-dnstwist-for-brand-abuse-triage
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/generate-and-screen-lookalike-domains-with-dnstwist-for-brand-abuse-triage`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/generate-and-screen-lookalike-domains-with-dnstwist-for-brand-abuse-triage/)
