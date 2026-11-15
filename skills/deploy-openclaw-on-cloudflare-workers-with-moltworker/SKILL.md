---
name: "Deploy OpenClaw on Cloudflare Workers with Moltworker"
slug: "deploy-openclaw-on-cloudflare-workers-with-moltworker"
description: "Use Moltworker to deploy a supervised OpenClaw personal agent stack on Cloudflare Workers, Sandbox containers, Access, R2, and optional AI Gateway."
github_stars: 9898
verification: "security_reviewed"
source: "https://github.com/cloudflare/moltworker"
author: "Cloudflare"
publisher_type: "organization"
category: "Templates & Workflows"
framework: "OpenClaw"
tool_ecosystem:
  github_repo: "cloudflare/moltworker"
  github_stars: 9898
---

# Deploy OpenClaw on Cloudflare Workers with Moltworker

Use Moltworker to deploy a supervised OpenClaw personal agent stack on Cloudflare Workers, Sandbox containers, Access, R2, and optional AI Gateway.

## Prerequisites

Cloudflare Workers Paid plan, Wrangler, Cloudflare Sandbox containers, Cloudflare Access, model provider or Cloudflare AI Gateway credentials, optional R2 Storage

## Installation

Use the upstream install or setup path that matches your environment:
- npm install
- npx wrangler secret put ANTHROPIC_API_KEY
- npm run deploy
- npx wrangler secret put CF_ACCESS_TEAM_DOMAIN

Requirements and caveats from upstream:
- **Important:** You will not be able to use the Control UI until you complete the following steps. You MUST:
- This is the most secure option as it requires explicit approval for each device.

Basic usage or getting-started notes:
- Run [OpenClaw](https://github.com/openclaw/openclaw) (formerly Moltbot, formerly Clawdbot) personal AI assistant in a [Cloudflare Sandbox](https://developers.cloudflare.com/sandbox/).
- **Experimental:** This is a proof of concept demonstrating that OpenClaw can run in Cloudflare Sandbox. It is not officially supported and may break without notice. Use at your own risk.
- [Workers Paid plan](https://www.cloudflare.com/plans/developer-platform/) ($5 USD/month) — required for Cloudflare Sandbox containers. Running the container incurs additional compute costs; see [Container Cost Estimat...

- Source: https://github.com/cloudflare/moltworker
- Extracted from upstream docs: https://raw.githubusercontent.com/cloudflare/moltworker/HEAD/README.md

## Documentation

- https://blog.cloudflare.com/moltworker-self-hosted-ai-agent/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/deploy-openclaw-on-cloudflare-workers-with-moltworker/)
