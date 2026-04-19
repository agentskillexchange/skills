---
title: "Podcast RSS Feed Builder"
description: "The Podcast RSS Feed Builder skill creates specification-compliant podcast RSS 2.0 feeds with all required iTunes/Apple Podcasts namespace extensions. It handles feed generation, episode management, and cross-platform distribution setup for podcast publishers. Feed generation produces valid XML with proper itunes:category taxonomy mapping, itunes:type (episodic/serial) configuration, and podcast:locked/podcast:funding tags from the Podcasting 2.0 namespace. Episode entries include enclosure URLs with accurate byte-length and MIME type declarations, itunes:duration formatting, and chapter markers using the podcast:chapters JSON format. The skill validates feeds against the Apple Podcasts specification and Spotify podcast delivery requirements. Audio file metadata management uses the mutagen library to read and write ID3v2 tags, ensuring episode titles, artwork, and chapter information are embedded directly in MP3/M4A files. Integration with the Podcast Index API enables submission to the open podcast directory and retrieval of cross-platform listening statistics. The skill generates OPML files for feed collections, creates podcast:transcript references linking to SRT/VTT caption files, and manages artwork requirements (minimum 1400&#215;1400, maximum 3000&#215;3000 JPEG/PNG) with automatic resizing via Pillow. Distribution automation submits feeds to Apple Podcasts Connect, Spotify for Podcasters, and Google Podcasts simultaneously."
source: "https://agentskillexchange.com/skills/podcast-rss-feed-builder/"
verification: "security_reviewed"
category:
  - "Media &amp; Transcription"
framework:
  - "Claude Agents"
---

# Podcast RSS Feed Builder

The Podcast RSS Feed Builder skill creates specification-compliant podcast RSS 2.0 feeds with all required iTunes/Apple Podcasts namespace extensions. It handles feed generation, episode management, and cross-platform distribution setup for podcast publishers. Feed generation produces valid XML with proper itunes:category taxonomy mapping, itunes:type (episodic/serial) configuration, and podcast:locked/podcast:funding tags from the Podcasting 2.0 namespace. Episode entries include enclosure URLs with accurate byte-length and MIME type declarations, itunes:duration formatting, and chapter markers using the podcast:chapters JSON format. The skill validates feeds against the Apple Podcasts specification and Spotify podcast delivery requirements. Audio file metadata management uses the mutagen library to read and write ID3v2 tags, ensuring episode titles, artwork, and chapter information are embedded directly in MP3/M4A files. Integration with the Podcast Index API enables submission to the open podcast directory and retrieval of cross-platform listening statistics. The skill generates OPML files for feed collections, creates podcast:transcript references linking to SRT/VTT caption files, and manages artwork requirements (minimum 1400&#215;1400, maximum 3000&#215;3000 JPEG/PNG) with automatic resizing via Pillow. Distribution automation submits feeds to Apple Podcasts Connect, Spotify for Podcasters, and Google Podcasts simultaneously.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/podcast-rss-feed-builder/)
