---
title: "Podcast RSS Feed Builder"
description: "The Podcast RSS Feed Builder skill creates specification-compliant podcast RSS 2.0 feeds with all required iTunes/Apple Podcasts namespace extensions. It handles feed generation, episode management, and cross-platform distribution setup for podcast publishers.\nFeed generation produces valid XML with proper itunes:category taxonomy mapping, itunes:type (episodic/serial) configuration, and podcast:locked/podcast:funding tags from the Podcasting 2.0 namespace. Episode entries include enclosure URLs with accurate byte-length and MIME type declarations, itunes:duration formatting, and chapter markers using the podcast:chapters JSON format. The skill validates feeds against the Apple Podcasts specification and Spotify podcast delivery requirements.\nAudio file metadata management uses the mutagen library to read and write ID3v2 tags, ensuring episode titles, artwork, and chapter information are embedded directly in MP3/M4A files. Integration with the Podcast Index API enables submission to the open podcast directory and retrieval of cross-platform listening statistics. The skill generates OPML files for feed collections, creates podcast:transcript references linking to SRT/VTT caption files, and manages artwork requirements (minimum 1400×1400, maximum 3000×3000 JPEG/PNG) with automatic resizing via Pillow. Distribution automation submits feeds to Apple Podcasts Connect, Spotify for Podcasters, and Google Podcasts simultaneously."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/podcast-rss-feed-builder/"
framework:
  - "Claude Agents"
---

# Podcast RSS Feed Builder

The Podcast RSS Feed Builder skill creates specification-compliant podcast RSS 2.0 feeds with all required iTunes/Apple Podcasts namespace extensions. It handles feed generation, episode management, and cross-platform distribution setup for podcast publishers.
Feed generation produces valid XML with proper itunes:category taxonomy mapping, itunes:type (episodic/serial) configuration, and podcast:locked/podcast:funding tags from the Podcasting 2.0 namespace. Episode entries include enclosure URLs with accurate byte-length and MIME type declarations, itunes:duration formatting, and chapter markers using the podcast:chapters JSON format. The skill validates feeds against the Apple Podcasts specification and Spotify podcast delivery requirements.
Audio file metadata management uses the mutagen library to read and write ID3v2 tags, ensuring episode titles, artwork, and chapter information are embedded directly in MP3/M4A files. Integration with the Podcast Index API enables submission to the open podcast directory and retrieval of cross-platform listening statistics. The skill generates OPML files for feed collections, creates podcast:transcript references linking to SRT/VTT caption files, and manages artwork requirements (minimum 1400×1400, maximum 3000×3000 JPEG/PNG) with automatic resizing via Pillow. Distribution automation submits feeds to Apple Podcasts Connect, Spotify for Podcasters, and Google Podcasts simultaneously.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/podcast-rss-feed-builder
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/podcast-rss-feed-builder` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/podcast-rss-feed-builder/)
