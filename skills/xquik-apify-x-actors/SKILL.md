---
name: "Xquik X Actors on Apify"
slug: "xquik-apify-x-actors"
description: "Run Xquik's public Apify Actors for X tweet collection, timelines, search, followers, lists, communities, and audience-overlap research."
verification: "listed"
source: "https://apify.com/xquik/x-tweet-scraper"
author: "Xquik"
publisher_type: "Company"
category: "Research & Scraping"
framework: "Multi-Framework"
---

# Xquik X Actors on Apify

Use 2 public Apify Actors for public X data. Keep this workflow on Apify.
Do not route it through an external Xquik website or API.

Xquik is an independent third-party service. Not affiliated with X Corp.
"Twitter" and "X" are trademarks of X Corp.

## Prerequisites

- An Apify account
- An `APIFY_TOKEN` environment variable
- Apify CLI for the command examples
- User approval for the requested paid result cap

## Installation

Install the Apify CLI:

```bash
npm install --global apify-cli
```

## Choose the Actor

| User goal | Actor ID |
|-----------|----------|
| Tweet URLs or IDs | `xquik/x-tweet-scraper` |
| Keyword, hashtag, or advanced search | `xquik/x-tweet-scraper` |
| Account timelines, lists, or threads | `xquik/x-tweet-scraper` |
| Replies, quotes, retweeters, or favoriters | `xquik/x-tweet-scraper` |
| Followers, following, or verified followers | `xquik/x-follower-scraper` |
| List members, list subscribers, or community members | `xquik/x-follower-scraper` |
| Audience overlap across targets | `xquik/x-follower-scraper` |

If a task needs tweet content and audience relations, run each Actor separately.

## Inspect Current Schemas

Fetch the schema before building unfamiliar input:

```bash
apify actors info "xquik/x-tweet-scraper" --input --json
apify actors info "xquik/x-follower-scraper" --input --json
```

Important tweet controls include `searchTerms`, `twitterHandles`, `tweetIds`,
`listIds`, `mode`, `queryType`, `outputVariant`, and `maxItems`.
`maxItems` caps the whole run, including runs with several search terms.

Important audience controls include `twitterHandles`, `userIds`, `listIds`,
`communityIds`, `relation`, `relations`, `outputMode`, `dedupeMode`,
`overlapMode`, `includeTargetMetadata`, and `maxItems`.

## Run a Small Tweet Search

Start with a small result cap:

```bash
apify actors call "xquik/x-tweet-scraper" \
  --input '{"searchTerms":["from:apify AI"],"queryType":"Latest","includeSearchTerms":true,"maxItems":25}' \
  --json
```

Other tweet routes support profile timelines, list posts, articles, threads,
replies, quotes, retweeters, and best-effort favoriters. Select the matching
mode from the live input schema.

## Run a Small Audience Export

```bash
apify actors call "xquik/x-follower-scraper" \
  --input '{"twitterHandles":["apify"],"relation":"followers","outputMode":"compact","includeTargetMetadata":true,"maxItems":25}' \
  --json
```

Use `dedupeMode: "merge"` or `overlapMode: true` for audience overlap.
Merge output adds the source targets and an overlap count.

## Validate Results

Capture the run's dataset ID. Fetch a sample before downloading everything:

```bash
apify datasets get-items DATASET_ID --limit 5 --format json
```

Normal records contain public tweet or profile data. A successful run can
instead return a diagnostic row. Exclude rows with
`resultType: "diagnostic"` from scraped totals. Read their `status` and
`message` fields before changing input.

Both Actors also write a `run-report` record to the default key-value store.
Use it to inspect routes, totals, outcomes, durations, and anomalies.

## Cost and Data Safety

Treat each Actor's live Apify pricing box as authoritative. Apify platform
usage can apply separately. Confirm before raising caps or adding targets.
Set Apify's maximum total charge when a hard spending limit is required.

Collect only public data needed for the stated task. Minimize retention.
Do not attempt to access private or access-controlled content.

## Documentation

- [X Tweet Scraper Actor](https://apify.com/xquik/x-tweet-scraper)
- [X Follower Scraper Actor](https://apify.com/xquik/x-follower-scraper)
- [Apify API v2](https://docs.apify.com/api/v2)
