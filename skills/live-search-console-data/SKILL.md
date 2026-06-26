---
name: "Live Search Console Data"
slug: "live-search-console-data"
description: "Give Claude Code, Codex, or OpenCode live access to Google Search Console and GA4 data through RefreshAgent. Provides authenticated GSC queries, keyword positions, sitemap status, cannibalization detection, and analytics without manual GCP OAuth setup."
verification: "listed"
source: "https://github.com/refreshagent/live-search-console-data"
category: "Data Extraction & Transformation"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "refreshagent/live-search-console-data"
---

# Live Search Console Data

Give coding agents authenticated access to Google Search Console and Google Analytics 4 data via RefreshAgent. No GCP OAuth setup, no service accounts, and no manual key copying.

RefreshAgent is a secure proxy between the agent and Google's official GSC/GA4 APIs. The bundled Python helper handles authentication via a browser-based login flow that saves the API key to `~/.config/refreshagent/.env`. All API calls go through Google's official APIs and cache ages are reported per-response for data freshness.

## Installation

### OpenClaw

```bash
clawhub install live-search-console-data
```

### Direct repo/manual install

Clone the Agent Skill Exchange repository and copy this skill directory into the skill folder used by your agent runtime:

```bash
git clone https://github.com/agentskillexchange/skills.git
cp -R skills/skills/live-search-console-data ~/.agent-skills/live-search-console-data
```

### Optional Third-Party Installer

```bash
npm exec --package=skills@1.5.7 -- skills add agentskillexchange/skills --skill live-search-console-data
```

### Direct from GitHub

```bash
npx skills add refreshagent/live-search-console-data
```

## Capabilities

- List GSC sites and GA4 properties
- Traffic summaries with period-over-period comparison
- Top queries and pages by clicks and impressions
- Exact keyword position tracking with historical comparison
- Cannibalization detection (query+page conflicts)
- Sitemap submission status and index counts
- GA4 organic sessions, landing pages, and top events
- Client site mapping and proposal building

## Usage

The skill includes a Python REST helper that handles authentication automatically. On first use it opens a browser-based Google sign-in to obtain an API key, saves it to `~/.config/refreshagent/.env`, then continues the request.

```bash
python3 {skill_dir}/scripts/refreshagent_api.py GET /api/v1/sc/sites
python3 {skill_dir}/scripts/refreshagent_api.py GET /api/v1/sc/query --param site_url=sc-domain:example.com --param date_range=30d
python3 {skill_dir}/scripts/refreshagent_api.py GET /api/v1/sc/keyword-position --param site_url=sc-domain:example.com --param keyword="seo tools"
```

## Source

- [GitHub: refreshagent/live-search-console-data](https://github.com/refreshagent/live-search-console-data)
- [Agent Skill Exchange](https://agentskillexchange.com/skills/live-search-console-data/)
