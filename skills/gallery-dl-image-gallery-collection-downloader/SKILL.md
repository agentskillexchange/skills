---
title: "gallery-dl Image Gallery and Collection Downloader"
description: "gallery-dl is a command-line tool for downloading image galleries and collections from dozens of hosting sites including Pixiv, DeviantArt, Twitter, Reddit, Instagram, and Danbooru. It supports authentication, metadata extraction, filtering, and configurable output templates."
slug: "gallery-dl-image-gallery-collection-downloader"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/mikf/gallery-dl"
tool_ecosystem:
  github_repo: "mikf/gallery-dl"
  github_stars: 17470
---

# gallery-dl Image Gallery and Collection Downloader

gallery-dl is a command-line tool for downloading image galleries and collections from dozens of hosting sites including Pixiv, DeviantArt, Twitter, Reddit, Instagram, and Danbooru. It supports authentication, metadata extraction, filtering, and configurable output templates.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install gallery-dl-image-gallery-collection-downloader
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

gallery-dl is a popular open-source command-line program for batch downloading image galleries and collections from a wide range of image hosting sites and social media platforms. Written in Python with over 17,000 GitHub stars, it fills the same niche for images that yt-dlp fills for video — reliable, scriptable, and extensively configurable bulk downloading.
Supported Sites
gallery-dl supports dozens of platforms including Pixiv, DeviantArt, Twitter/X, Reddit, Instagram, Danbooru, Gelbooru, ArtStation, Flickr, Tumblr, Imgur, and many more. Each site has a dedicated extractor module that handles the platform-specific API or HTML scraping required to discover and download images at full resolution.
Core Capabilities
The tool downloads entire galleries, user profiles, tag searches, and individual posts. It extracts and preserves metadata such as artist names, tags, descriptions, upload dates, and image dimensions. Output directory structures and filenames are fully customizable using Python format strings with metadata placeholders. Archive databases track previously downloaded files to avoid re-downloading on subsequent runs.
Authentication and Filtering
gallery-dl supports login credentials and browser cookie extraction for accessing age-restricted or private content. Post-processors handle file conversion, metadata writing to JSON sidecar files, and execution of custom commands after each download. Filter expressions allow selecting images by date range, file type, minimum resolution, tag inclusion or exclusion, and rating.
Integration Points
Configuration files in JSON format define site-specific settings, credentials, and output templates. The tool can be used as a Python library for programmatic integration. It works in automation pipelines via shell scripts and cron jobs. gallery-dl pairs well with media management tools like Hydrus Network for organizing downloaded collections with their preserved metadata.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gallery-dl-image-gallery-collection-downloader/)
