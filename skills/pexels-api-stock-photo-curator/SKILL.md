---
title: "Pexels API Stock Photo Curator"
description: "Searches and downloads royalty-free images from Pexels API with smart filtering by orientation, color, and size. Generates attribution HTML and maintains a local deduplication index via SQLite."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/pexels-api-stock-photo-curator/"
category:
  - "Image &amp; Creative Automation"
framework:
  - "Claude Agents"
---

# Pexels API Stock Photo Curator

The Pexels API Stock Photo Curator automates sourcing royalty-free imagery for content pipelines, marketing teams, and blog publishers. It connects to the Pexels REST API v1 using API key authentication, supporting both photo search and curated collection endpoints. Smart filtering narrows results by orientation (landscape, portrait, square), dominant color hex codes, minimum resolution, and locale-specific queries. Downloaded images are stored with consistent naming conventions and tracked in a local SQLite database to prevent duplicate downloads across sessions. The skill generates proper attribution HTML snippets per Pexels licensing requirements, including photographer name, profile link, and Pexels source URL. Batch mode processes keyword lists from CSV files, downloading top-N results per keyword with configurable quality (original, large2x, large, medium). Image post-processing options include resizing via sharp.js, format conversion to WebP/AVIF, and EXIF metadata stripping for privacy. Rate limiting respects Pexels’ 200 requests/hour quota with automatic throttling. Integration hooks support direct upload to WordPress media library via REST API, S3 buckets, or Cloudinary.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pexels-api-stock-photo-curator/)
