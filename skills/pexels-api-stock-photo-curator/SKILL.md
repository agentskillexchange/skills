---
name: "Pexels API Stock Photo Curator"
description: "Searches and downloads royalty-free images from Pexels API with smart filtering by orientation, color, and size. Generates attribution HTML and maintains a local deduplication index via SQLite."
category: "Image &amp; Creative Automation"
framework: "Claude Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/pexels-api-stock-photo-curator/"
---
# Pexels API Stock Photo Curator

Searches and downloads royalty-free images from Pexels API with smart filtering by orientation, color, and size. Generates attribution HTML and maintains a local deduplication index via SQLite.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill pexels-api-stock-photo-curator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill pexels-api-stock-photo-curator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill pexels-api-stock-photo-curator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill pexels-api-stock-photo-curator -a codex
```

### OpenClaw

```bash
clawhub install pexels-api-stock-photo-curator
```

## Details

The Pexels API Stock Photo Curator automates sourcing royalty-free imagery for content pipelines, marketing teams, and blog publishers. It connects to the Pexels REST API v1 using API key authentication, supporting both photo search and curated collection endpoints. Smart filtering narrows results by orientation (landscape, portrait, square), dominant color hex codes, minimum resolution, and locale-specific queries. Downloaded images are stored with consistent naming conventions and tracked in a local SQLite database to prevent duplicate downloads across sessions. The skill generates proper attribution HTML snippets per Pexels licensing requirements, including photographer name, profile link, and Pexels source URL. Batch mode processes keyword lists from CSV files, downloading top-N results per keyword with configurable quality (original, large2x, large, medium). Image post-processing options include resizing via sharp.js, format conversion to WebP/AVIF, and EXIF metadata stripping for privacy. Rate limiting respects Pexels’ 200 requests/hour quota with automatic throttling. Integration hooks support direct upload to WordPress media library via REST API, S3 buckets, or Cloudinary.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pexels-api-stock-photo-curator/)
