---
name: "Subfinder Fast Passive Subdomain Enumeration Tool"
description: "Subfinder is a passive subdomain discovery tool by ProjectDiscovery that finds valid subdomains for websites using curated online sources. Optimized for speed and stealth, it integrates cleanly into s"
category: "General"
framework: "General"
verification: listed
source: "https://github.com/projectdiscovery/subfinder"
---

# Subfinder Fast Passive Subdomain Enumeration Tool

Subfinder is a passive subdomain discovery tool by ProjectDiscovery that finds valid subdomains for websites using curated online sources. Optimized for speed and stealth, it integrates cleanly into security reconnaissance pipelines via stdin/stdout support.

## Installation

Install this skill using one of these methods:

```bash
# Using clawhub (recommended)
clawhub install subfinder-passive-subdomain-enumeration

# Using OpenClaw CLI
openclaw skills install subfinder-passive-subdomain-enumeration

# Manual: clone into your skills directory
cd ~/.openclaw/workspace/skills
git clone https://github.com/agentskillexchange/skills.git --depth 1 --filter=blob:none --sparse
cd skills && git sparse-checkout set skills/subfinder-passive-subdomain-enumeration
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/subfinder-passive-subdomain-enumeration/)
