---
name: "ProductHunt Launch Tracker"
description: "Monitors Product Hunt launches using the GraphQL API to track daily rankings, upvote velocity, and maker activity. Queries the posts connection with date filters and topic tags, enriching results with Twitter follower counts and domain WHOIS age."
category: "Research & Scraping"
framework: "Custom Agents"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/producthunt-launch-tracker/"
---

# ProductHunt Launch Tracker

Monitors Product Hunt launches using the GraphQL API to track daily rankings, upvote velocity, and maker activity. Queries the posts connection with date filters and topic tags, enriching results with Twitter follower counts and domain WHOIS age.

## Overview

Overview

The ProductHunt Launch Tracker skill enables agents to monitor and analyze product launches on Product Hunt using the official GraphQL API at `https://api.producthunt.com/v2/api/graphql`. It authenticates via OAuth2 bearer tokens and queries the `posts` connection with filters for `postedAfter`, `postedBefore`, `topic`, and `order` to retrieve launches sorted by votes, newest, or featured rank. Each post node returns the name, tagline, description, votesCount, commentsCount, website URL, thumbnail, maker profiles, and associated topics.

How It Works

The agent runs periodic GraphQL queries to fetch the latest launches, storing results in a local JSON database indexed by post slug. It calculates upvote velocity by comparing vote counts across polling intervals — products gaining more than 50 upvotes per hour are flagged as trending. For competitive intelligence, the skill enriches each launch with external signals: it fetches the domain’s WHOIS age via the `rdap.org` API, checks the maker’s Twitter follower count via the Twitter API v2 `users/by/username` endpoint, and looks up the product’s Crunchbase profile for funding data if available.

Output and Reporting

Produces a daily launch digest with three sections: Top 5 by Votes, Fastest Climbers (highest velocity), and Developer Tools (filtered by topic:developer-tools). Each entry includes the product name, one-line tagline, vote count with velocity indicator, maker name, website link, and enrichment signals. Supports delivery via webhook POST to Slack, Discord, email via SendGrid, or local Markdown file. The agent respects Product Hunt’s API rate limit of 450 requests per 15 minutes and uses cursor-based pagination for result sets exceeding 20 items. Ideal for venture capital scouts, competitive analysts, and indie makers tracking market trends.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill producthunt-launch-tracker
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill producthunt-launch-tracker -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill producthunt-launch-tracker -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill producthunt-launch-tracker -a codex
```

### OpenClaw

```bash
clawhub install producthunt-launch-tracker
```

## Source

- Marketplace: https://agentskillexchange.com/skills/producthunt-launch-tracker/
