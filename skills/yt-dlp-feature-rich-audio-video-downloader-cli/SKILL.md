---
title: "yt-dlp Feature-Rich Audio and Video Downloader CLI"
description: "yt-dlp is a feature-rich command-line audio and video downloader forked from youtube-dl, with over 153,000 GitHub stars making it one of the most popular open-source media tools. Written in Python, it supports downloading from thousands of websites through an extensible extractor architecture.\nCore Capabilities\nThe tool downloads video and audio streams with precise format selection using a powerful filter syntax. Users can specify resolution, codec, bitrate, and container preferences. yt-dlp handles playlist downloads, channel archives, live stream recording, and geo-restricted content via proxy and cookie support. It extracts subtitles in multiple formats (SRT, VTT, ASS) and embeds metadata, thumbnails, and chapter markers into downloaded files.\nPost-Processing Pipeline\nyt-dlp integrates with FFmpeg for transcoding, audio extraction, format conversion, and thumbnail embedding. The SponsorBlock integration automatically removes sponsor segments, intros, and outros from downloaded videos. Output templates provide fine-grained control over filename patterns using video metadata fields like title, upload date, channel name, and resolution.\nAdvanced Features\nThe tool supports authentication via cookies, netrc files, and browser cookie extraction. Rate limiting, retry logic, and fragment downloading handle unreliable connections. The plugin system allows community-developed extractors for additional sites. Archive files prevent re-downloading previously fetched content, making it ideal for automated media archival workflows.\nIntegration Points\nyt-dlp works as a Python library for programmatic embedding in automation scripts. JSON output mode provides structured metadata for media cataloging systems. It integrates with media servers like Plex and Jellyfin for automated content ingestion. The CLI interface works in shell scripts, cron jobs, and CI/CD pipelines for media processing workflows."
verification: security_reviewed
source: "https://github.com/yt-dlp/yt-dlp"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "yt-dlp/yt-dlp"
  github_stars: 154307
---

# yt-dlp Feature-Rich Audio and Video Downloader CLI

yt-dlp is a feature-rich command-line audio and video downloader forked from youtube-dl, with over 153,000 GitHub stars making it one of the most popular open-source media tools. Written in Python, it supports downloading from thousands of websites through an extensible extractor architecture.
Core Capabilities
The tool downloads video and audio streams with precise format selection using a powerful filter syntax. Users can specify resolution, codec, bitrate, and container preferences. yt-dlp handles playlist downloads, channel archives, live stream recording, and geo-restricted content via proxy and cookie support. It extracts subtitles in multiple formats (SRT, VTT, ASS) and embeds metadata, thumbnails, and chapter markers into downloaded files.
Post-Processing Pipeline
yt-dlp integrates with FFmpeg for transcoding, audio extraction, format conversion, and thumbnail embedding. The SponsorBlock integration automatically removes sponsor segments, intros, and outros from downloaded videos. Output templates provide fine-grained control over filename patterns using video metadata fields like title, upload date, channel name, and resolution.
Advanced Features
The tool supports authentication via cookies, netrc files, and browser cookie extraction. Rate limiting, retry logic, and fragment downloading handle unreliable connections. The plugin system allows community-developed extractors for additional sites. Archive files prevent re-downloading previously fetched content, making it ideal for automated media archival workflows.
Integration Points
yt-dlp works as a Python library for programmatic embedding in automation scripts. JSON output mode provides structured metadata for media cataloging systems. It integrates with media servers like Plex and Jellyfin for automated content ingestion. The CLI interface works in shell scripts, cron jobs, and CI/CD pipelines for media processing workflows.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/yt-dlp-feature-rich-audio-video-downloader-cli
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/yt-dlp-feature-rich-audio-video-downloader-cli` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/yt-dlp-feature-rich-audio-video-downloader-cli/)
