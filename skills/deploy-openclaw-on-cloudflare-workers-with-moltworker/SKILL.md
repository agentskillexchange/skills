---
title: "Deploy OpenClaw on Cloudflare Workers with Moltworker"
description: "Use Moltworker to deploy a supervised OpenClaw personal agent stack on Cloudflare Workers, Sandbox containers, Access, R2, and optional AI Gateway."
verification: "security_reviewed"
source: "https://github.com/cloudflare/moltworker"
author: "Cloudflare"
publisher_type: "organization"
category:
  - "Templates & Workflows"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "cloudflare/moltworker"
  github_stars: 9898
---

# Deploy OpenClaw on Cloudflare Workers with Moltworker

Use Moltworker to deploy a supervised OpenClaw personal agent stack on Cloudflare Workers, Sandbox containers, Access, R2, and optional AI Gateway.

## Prerequisites

Cloudflare Workers Paid plan, Wrangler, Cloudflare Sandbox containers, Cloudflare Access, model provider or Cloudflare AI Gateway credentials, optional R2 Storage

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Clone the Moltworker repository, run npm install, set the required Wrangler secrets for the model provider and gateway token, deploy with npm run deploy, then configure Cloudflare Access, device pairing, and optional R2 persistence.
```

## Documentation

- https://blog.cloudflare.com/moltworker-self-hosted-ai-agent/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/deploy-openclaw-on-cloudflare-workers-with-moltworker/)
