---
name: SerpBear Self-Hosted Search Engine Rank Tracking App
description: SerpBear is an open-source, self-hosted search engine position tracking
  application. It lets you monitor unlimited keyword rankings in Google with email
  notifications, a built-in SERP API, Google Search Console integration, and keyword
  research via Google Ads.
category: "Content Writing &amp; SEO"
framework: Multi-Framework
verification: security_reviewed
source: "https://github.com/towfiqi/serpbear"
tool_ecosystem:
  github_repo: "https://github.com/towfiqi/serpbear"
  github_stars: 1890
---
# SerpBear Self-Hosted Search Engine Rank Tracking App

SerpBear is an open-source, self-hosted search engine position tracking application. It lets you monitor unlimited keyword rankings in Google with email notifications, a built-in SERP API, Google Search Console integration, and keyword research via Google Ads.

SerpBear is an open-source search engine position rank tracking application built with Next.js and SQLite. It provides a complete self-hosted alternative to expensive commercial SERP tracking services like Ahrefs, SEMrush, or SE Ranking, giving SEO professionals and website owners full control over their keyword monitoring data.

Core Capabilities

The application allows you to add unlimited domains and track unlimited keywords across Google search results. It monitors your keyword positions and detects ranking changes over time. You can configure email notifications on a daily, weekly, or monthly basis to stay informed about position movements without manually checking.

API and Integrations

SerpBear ships with a built-in REST API that you can use to integrate keyword ranking data into your marketing dashboards, reporting tools, or custom workflows. The tool integrates with Google Search Console to show actual search visits, impressions, CTR, and average position for each tracked keyword. You can also discover new keyword opportunities and identify top-performing pages and countries through the Search Console integration.

Keyword Research

By connecting a Google Ads test account, SerpBear can perform keyword research and auto-generate keyword ideas from your tracked website content. It also displays monthly search volume data for your tracked keywords, helping you prioritize which terms to focus your SEO efforts on.

Technical Architecture

SerpBear uses Next.js for both the frontend and backend, with SQLite as its database. For scraping Google search results, it supports multiple third-party providers including ScrapingAnt, ScrapingRobot, SearchApi, SerpApi, HasData, and custom proxy IPs. The application can be deployed via Docker or directly on platforms like Railway and Fly.io.

Agent Integration

AI agents can use SerpBear’s REST API to programmatically check keyword rankings, trigger rank refreshes, and pull historical position data for automated SEO reporting workflows. The API enables agents to monitor ranking trends and alert on significant position changes across multiple domains.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill serpbear-self-hosted-serp-rank-tracker
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill serpbear-self-hosted-serp-rank-tracker -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill serpbear-self-hosted-serp-rank-tracker -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill serpbear-self-hosted-serp-rank-tracker -a codex
```

### OpenClaw

```bash
clawhub install serpbear-self-hosted-serp-rank-tracker
```


## Source

- [GitHub](https://github.com/towfiqi/serpbear)
