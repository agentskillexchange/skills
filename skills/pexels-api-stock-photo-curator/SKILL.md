---
title: Pexels API Stock Photo Curator
description: The Pexels API Stock Photo Curator automates sourcing royalty-free imagery
  for content pipelines, marketing teams, and blog publishers. It connects to the
  Pexels REST API v1 using API key authentication, supporting both photo search and
  curated collection endpoints. Smart filtering narrows results by orientation (landscape,
  portrait, square), dominant color hex codes, minimum resolution, and locale-specific
  queries. Downloaded images are stored with consistent naming conventions and tracked
  in a local SQLite database to prevent duplicate downloads across sessions. The skill
  generates proper attribution HTML snippets per Pexels licensing requirements, including
  photographer name, profile link, and Pexels source URL. Batch mode processes keyword
  lists from CSV files, downloading top-N results per keyword with configurable quality
  (original, large2x, large, medium). Image post-processing options include resizing
  via sharp.js, format conversion to WebP/AVIF, and EXIF metadata stripping for privacy.
  Rate limiting respects Pexels’ 200 requests/hour quota with automatic throttling.
  Integration hooks support direct upload to WordPress media library via REST API,
  S3 buckets, or Cloudinary.
verification: security_reviewed
source: https://agentskillexchange.com/skills/pexels-api-stock-photo-curator/
category:
- Image &amp; Creative Automation
framework:
- Claude Agents
---

# Pexels API Stock Photo Curator

The Pexels API Stock Photo Curator automates sourcing royalty-free imagery for content pipelines, marketing teams, and blog publishers. It connects to the Pexels REST API v1 using API key authentication, supporting both photo search and curated collection endpoints. Smart filtering narrows results by orientation (landscape, portrait, square), dominant color hex codes, minimum resolution, and locale-specific queries. Downloaded images are stored with consistent naming conventions and tracked in a local SQLite database to prevent duplicate downloads across sessions. The skill generates proper attribution HTML snippets per Pexels licensing requirements, including photographer name, profile link, and Pexels source URL. Batch mode processes keyword lists from CSV files, downloading top-N results per keyword with configurable quality (original, large2x, large, medium). Image post-processing options include resizing via sharp.js, format conversion to WebP/AVIF, and EXIF metadata stripping for privacy. Rate limiting respects Pexels’ 200 requests/hour quota with automatic throttling. Integration hooks support direct upload to WordPress media library via REST API, S3 buckets, or Cloudinary.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pexels-api-stock-photo-curator/)
