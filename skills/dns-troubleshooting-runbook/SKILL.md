---
name: "DNS Troubleshooting Runbook"
description: "Use this skill to systematically diagnose DNS resolution failures, propagation delays, misconfigured records, and DNS-related connectivity issues. It guides through dig/nslookup commands and DNS record validation steps. Trigger when domains are not resolving, DNS propagation issues occur after changes, or specific DNS record types are failing."
category: "Monitoring & Alerts"
framework: "Custom Agents"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/dns-troubleshooting-runbook/"
---

# DNS Troubleshooting Runbook

Use this skill to systematically diagnose DNS resolution failures, propagation delays, misconfigured records, and DNS-related connectivity issues. It guides through dig/nslookup commands and DNS record validation steps. Trigger when domains are not resolving, DNS propagation issues occur after changes, or specific DNS record types are failing.

## Overview

Use this skill to systematically diagnose DNS resolution failures, propagation delays, misconfigured records, and DNS-related connectivity issues. It guides through dig/nslookup commands and DNS record validation steps. Trigger when domains are not resolving, DNS propagation issues occur after changes, or specific DNS record types are failing.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill dns-troubleshooting-runbook
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill dns-troubleshooting-runbook -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill dns-troubleshooting-runbook -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill dns-troubleshooting-runbook -a codex
```

### OpenClaw

```bash
clawhub install dns-troubleshooting-runbook
```

## Source

- Marketplace: https://agentskillexchange.com/skills/dns-troubleshooting-runbook/
