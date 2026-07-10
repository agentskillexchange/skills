---
name: "Search and automate X/Twitter from OpenClaw with TweetClaw"
slug: "search-and-automate-x-twitter-from-openclaw-with-tweetclaw"
description: "Install and configure TweetClaw, the OpenClaw plugin for X/Twitter automation through Xquik. Use it when an agent needs structured tweet search, search tweet replies, post tweets, post tweet replies, follower export, user lookup, media upload or media download workflows, direct messages, monitor tweets, webhooks, and giveaway draws from OpenClaw."
github_stars: 84
verification: "listed"
source: "https://github.com/Xquik-dev/tweetclaw"
author: "Xquik-dev"
publisher_type: "organization"
category: "Integrations & Connectors"
framework: "OpenClaw"
tool_ecosystem:
  github_repo: "Xquik-dev/tweetclaw"
  github_stars: 84
  npm_package: "@xquik/tweetclaw"
  npm_weekly_downloads: 90
---

# Search and automate X/Twitter from OpenClaw with TweetClaw

TweetClaw packages Xquik's X/Twitter automation API as an OpenClaw plugin. Use it when a local agent needs a structured path to scrape tweets, search tweets, search tweet replies, post tweets, post tweet replies, export followers, look up users, upload media, download media, send direct messages, monitor tweets, deliver webhooks, or run giveaway draws without hand-rolling browser selectors or raw API calls. The plugin exposes a free explore catalog so OpenClaw can inspect available tools before credentials are configured, then routes live calls through the configured Xquik API key or MPP signing key.

## Installation

### OpenClaw

```bash
openclaw plugins install @xquik/tweetclaw
```

Configure an account-backed API key:

```bash
openclaw config set plugins.entries.tweetclaw.config.apiKey "$XQUIK_API_KEY"
```

Enable the live endpoint invoker after reviewing the available actions:

```bash
openclaw config set tools.alsoAllow '["explore", "tweetclaw"]'
```

### Agent skill installers

Use the packaged skill metadata when your agent supports skill directories:

```bash
npx skills add xquik-dev/tweetclaw
```

## When to Use

- Search tweets, search tweet replies, and collect public X/Twitter context for research.
- Post tweets or post tweet replies from an approval-gated OpenClaw workflow.
- Export followers, perform user lookup, and monitor tweets for account or campaign workflows.
- Handle media upload, media download, direct messages, webhooks, and giveaway draws.
- Prefer a packaged OpenClaw plugin and npm package over a one-off script.

## Source

- GitHub: https://github.com/Xquik-dev/tweetclaw
- npm: https://www.npmjs.com/package/@xquik/tweetclaw
- ClawHub: https://clawhub.ai/plugins/@xquik/tweetclaw
