---
name: "Instaloader Instagram Content and Metadata Downloader"
description: "Instaloader is a Python CLI tool and library that downloads Instagram photos, videos, stories, reels, highlights, and IGTV content along with captions, comments, geotags, and metadata. It supports public and private profiles, hashtags, and feeds with automatic resume and profile rename detection."
category: "Research & Scraping"
framework: "Custom Agents"
verification: security_reviewed
source: "https://github.com/instaloader/instaloader"
tool_ecosystem:
  github_repo: "instaloader/instaloader"
  github_stars: 12047
---
# Instaloader Instagram Content and Metadata Downloader

Instaloader is a Python CLI tool and library that downloads Instagram photos, videos, stories, reels, highlights, and IGTV content along with captions, comments, geotags, and metadata. It supports public and private profiles, hashtags, and feeds with automatic resume and profile rename detection.

## Overview

Instaloader is a free, open-source command-line tool written in Python that downloads pictures, videos, and associated metadata from Instagram. With over 12,000 GitHub stars and widespread adoption, it is the most capable open-source Instagram scraping tool available, supporting everything from public profile downloads to authenticated private profile access, story retrieval, and hashtag-based discovery.

The tool downloads posts along with their captions, comments, geotags, and metadata in a structured format. Each post is saved with its media files and a corresponding JSON sidecar containing all available metadata, making Instaloader valuable both for content archival and data analysis workflows.

Supported Content Types

Instaloader handles all major Instagram content types: regular posts (photos and videos), stories, highlights, reels, IGTV content, tagged posts, and saved media. It downloads from profiles, hashtags, the authenticated user feed, and saved collections. Each content type can be individually enabled or disabled via command-line flags.

Smart Update and Resumption

The –fast-update flag enables incremental updates by stopping at the first already-downloaded post. The –latest-stamps option stores download timestamps per profile, allowing previously downloaded media to be moved or deleted while still maintaining an up-to-date archive. Interrupted downloads automatically resume from where they left off. The tool detects Instagram username changes and automatically renames the local download directory to match.

Filtering and Customization

Instaloader provides fine-grained control over what gets downloaded through Python filter expressions. Users can filter by post date, like count, media type, caption content, and other attributes. Custom filename templates control how downloaded files are named and organized. The –geotags flag adds location data to media files where available.

Python Library API

Beyond the CLI, Instaloader exposes a full Python API through the instaloader module. Developers can programmatically log in, iterate over profiles and posts, access metadata, and implement custom download logic. This makes it straightforward to build automated data collection pipelines, social media monitoring tools, or content analysis systems.

Agent Integration

As an agent skill, Instaloader enables automated Instagram data collection and monitoring. An AI agent can download and analyze content from specified profiles, track hashtags for trend monitoring, archive stories before they expire, and extract structured metadata for analysis. The JSON metadata output is ideal for programmatic consumption. Instaloader is available on PyPI via pip install instaloader and requires Python 3.8 or later. It is MIT-licensed.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill instaloader-instagram-content-metadata-downloader
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill instaloader-instagram-content-metadata-downloader -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill instaloader-instagram-content-metadata-downloader -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill instaloader-instagram-content-metadata-downloader -a codex
```

### OpenClaw

```bash
clawhub install instaloader-instagram-content-metadata-downloader
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/instaloader-instagram-content-metadata-downloader/)
