---
title: "Pexels API Stock Photo Curator"
description: "Searches and downloads royalty-free images from Pexels API with smart filtering by orientation, color, and size. Generates attribution HTML and maintains a local deduplication index via SQLite."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/pexels-api-stock-photo-curator/"
category:
  - "Image & Creative Automation"
framework:
  - "Claude Agents"
---

# Pexels API Stock Photo Curator

The Pexels API Stock Photo Curator automates sourcing royalty-free imagery for content pipelines, marketing teams, and blog publishers. It connects to the Pexels REST API v1 using API key authentication, supporting both photo search and curated collection endpoints. Smart filtering narrows results by orientation (landscape, portrait, square), dominant color hex codes, minimum resolution, and locale-specific queries. Downloaded images are stored with consistent naming conventions and tracked in a local SQLite database to prevent duplicate downloads across sessions. The skill generates proper attribution HTML snippets per Pexels licensing requirements, including photographer name, profile link, and Pexels source URL. Batch mode processes keyword lists from CSV files, downloading top-N results per keyword with configurable quality (original, large2x, large, medium). Image post-processing options include resizing via sharp.js, format conversion to WebP/AVIF, and EXIF metadata stripping for privacy. Rate limiting respects Pexels’ 200 requests/hour quota with automatic throttling. Integration hooks support direct upload to WordPress media library via REST API, S3 buckets, or Cloudinary.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/pexels-api-stock-photo-curator/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/pexels-api-stock-photo-curator
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/pexels-api-stock-photo-curator`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pexels-api-stock-photo-curator/)
