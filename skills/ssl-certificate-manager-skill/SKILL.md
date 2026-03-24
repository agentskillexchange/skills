---
name: "SSL Certificate Manager Skill"
description: "Use this skill to check SSL certificate expiry, renew certificates via Let’s Encrypt or other CAs, and validate the full certificate chain for domains. It automates certificate lifecycle management and alerts on expiring certificates. Trigger when certificates are expiring, HTTPS errors occur, or certificate chain validation fails."
category: "Security & Verification"
framework: "Custom Agents"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/ssl-certificate-manager-skill/"
---

# SSL Certificate Manager Skill

Use this skill to check SSL certificate expiry, renew certificates via Let’s Encrypt or other CAs, and validate the full certificate chain for domains. It automates certificate lifecycle management and alerts on expiring certificates. Trigger when certificates are expiring, HTTPS errors occur, or certificate chain validation fails.

## Overview

Use this skill to check SSL certificate expiry, renew certificates via Let’s Encrypt or other CAs, and validate the full certificate chain for domains. It automates certificate lifecycle management and alerts on expiring certificates. Trigger when certificates are expiring, HTTPS errors occur, or certificate chain validation fails.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill ssl-certificate-manager-skill
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill ssl-certificate-manager-skill -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill ssl-certificate-manager-skill -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill ssl-certificate-manager-skill -a codex
```

### OpenClaw

```bash
clawhub install ssl-certificate-manager-skill
```

## Source

- Marketplace: https://agentskillexchange.com/skills/ssl-certificate-manager-skill/
