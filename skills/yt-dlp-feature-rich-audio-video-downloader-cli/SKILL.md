---
name: "yt-dlp Feature-Rich Audio and Video Downloader CLI"
description: "yt-dlp is a powerful command-line tool for downloading audio and video from thousands of websites including YouTube, Vimeo, and social media platforms. It supports format selection, subtitle extraction, metadata embedding, SponsorBlock integration, and batch processing with extensive post-processing options."
verification: security_reviewed
source: "https://github.com/yt-dlp/yt-dlp"
category:
  - "Media &amp; Transcription"
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

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/yt-dlp-feature-rich-audio-video-downloader-cli/)
