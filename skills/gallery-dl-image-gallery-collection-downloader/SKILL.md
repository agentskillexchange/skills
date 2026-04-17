---
title: "gallery-dl Image Gallery and Collection Downloader"
description: "gallery-dl is a popular open-source command-line program for batch downloading image galleries and collections from a wide range of image hosting sites and social media platforms. Written in Python with over 17,000 GitHub stars, it fills the same niche for images that yt-dlp fills for video — reliable, scriptable, and extensively configurable bulk downloading.\nSupported Sites\ngallery-dl supports dozens of platforms including Pixiv, DeviantArt, Twitter/X, Reddit, Instagram, Danbooru, Gelbooru, ArtStation, Flickr, Tumblr, Imgur, and many more. Each site has a dedicated extractor module that handles the platform-specific API or HTML scraping required to discover and download images at full resolution.\nCore Capabilities\nThe tool downloads entire galleries, user profiles, tag searches, and individual posts. It extracts and preserves metadata such as artist names, tags, descriptions, upload dates, and image dimensions. Output directory structures and filenames are fully customizable using Python format strings with metadata placeholders. Archive databases track previously downloaded files to avoid re-downloading on subsequent runs.\nAuthentication and Filtering\ngallery-dl supports login credentials and browser cookie extraction for accessing age-restricted or private content. Post-processors handle file conversion, metadata writing to JSON sidecar files, and execution of custom commands after each download. Filter expressions allow selecting images by date range, file type, minimum resolution, tag inclusion or exclusion, and rating.\nIntegration Points\nConfiguration files in JSON format define site-specific settings, credentials, and output templates. The tool can be used as a Python library for programmatic integration. It works in automation pipelines via shell scripts and cron jobs. gallery-dl pairs well with media management tools like Hydrus Network for organizing downloaded collections with their preserved metadata."
verification: security_reviewed
source: "https://github.com/mikf/gallery-dl"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "mikf/gallery-dl"
  github_stars: 17470
---

# gallery-dl Image Gallery and Collection Downloader

gallery-dl is a popular open-source command-line program for batch downloading image galleries and collections from a wide range of image hosting sites and social media platforms. Written in Python with over 17,000 GitHub stars, it fills the same niche for images that yt-dlp fills for video — reliable, scriptable, and extensively configurable bulk downloading.
Supported Sites
gallery-dl supports dozens of platforms including Pixiv, DeviantArt, Twitter/X, Reddit, Instagram, Danbooru, Gelbooru, ArtStation, Flickr, Tumblr, Imgur, and many more. Each site has a dedicated extractor module that handles the platform-specific API or HTML scraping required to discover and download images at full resolution.
Core Capabilities
The tool downloads entire galleries, user profiles, tag searches, and individual posts. It extracts and preserves metadata such as artist names, tags, descriptions, upload dates, and image dimensions. Output directory structures and filenames are fully customizable using Python format strings with metadata placeholders. Archive databases track previously downloaded files to avoid re-downloading on subsequent runs.
Authentication and Filtering
gallery-dl supports login credentials and browser cookie extraction for accessing age-restricted or private content. Post-processors handle file conversion, metadata writing to JSON sidecar files, and execution of custom commands after each download. Filter expressions allow selecting images by date range, file type, minimum resolution, tag inclusion or exclusion, and rating.
Integration Points
Configuration files in JSON format define site-specific settings, credentials, and output templates. The tool can be used as a Python library for programmatic integration. It works in automation pipelines via shell scripts and cron jobs. gallery-dl pairs well with media management tools like Hydrus Network for organizing downloaded collections with their preserved metadata.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/gallery-dl-image-gallery-collection-downloader
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/gallery-dl-image-gallery-collection-downloader` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gallery-dl-image-gallery-collection-downloader/)
