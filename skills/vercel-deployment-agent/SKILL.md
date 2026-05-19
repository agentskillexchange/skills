---
name: "Vercel Deployment Agent"
slug: "vercel-deployment-agent"
description: ""
github_stars: 15296
verification: "security_reviewed"
source: "https://github.com/vercel/vercel"
category: "Templates & Workflows"
framework: "Custom Agents"
tool_ecosystem:
  github_repo: "vercel/vercel"
  github_stars: 15296
  npm_package: "vercel"
  npm_weekly_downloads: 2351487
---

# Vercel Deployment Agent



## Installation

Use the upstream install or setup path that matches your environment:
- npm i -g vercel
- npm i -g @vercel/vc-native --force
- npm i -g @vercel/vc-native-darwin-x64 --force
- git clone https://github.com/vercel/vercel

Requirements and caveats from upstream:
- The --force flag allows npm to replace existing global vercel and vc bin links. Users who do not install @vercel/vc-native continue using the regular Node.js-based CLI from npm i -g vercel.
- const { nodeFileTrace } = require('@vercel/nft');

Basic usage or getting-started notes:
- This project uses [pnpm](https://pnpm.io/) to install dependencies and run scripts.
- You can use the vercel script to run local changes as if you were invoking Vercel CLI. For example, vercel deploy --cwd=/path/to/project could be run with local changes with pnpm vercel deploy --cwd=/path/to/project.
- Unit tests are run locally with jest and execute quickly because they are testing the smallest units of code.

- Source: https://github.com/vercel/vercel
- Extracted from upstream docs: https://raw.githubusercontent.com/vercel/vercel/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/vercel-deployment-agent/)
