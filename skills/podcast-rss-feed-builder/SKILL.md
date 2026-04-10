---
name: Podcast RSS Feed Builder
description: Generates and validates podcast RSS feeds compliant with the Apple Podcasts
  and Spotify specification. Uses the podcast-index API for cross-platform distribution
  and ID3 tag management via mutagen.
verification: security_reviewed
source: https://agentskillexchange.com/skills/podcast-rss-feed-builder/
category:
- Media &amp; Transcription
framework:
- Claude Agents
---
# Podcast RSS Feed Builder

The Podcast RSS Feed Builder skill creates specification-compliant podcast RSS 2.0 feeds with all required iTunes/Apple Podcasts namespace extensions. It handles feed generation, episode management, and cross-platform distribution setup for podcast publishers.
Feed generation produces valid XML with proper itunes:category taxonomy mapping, itunes:type (episodic/serial) configuration, and podcast:locked/podcast:funding tags from the Podcasting 2.0 namespace. Episode entries include enclosure URLs with accurate byte-length and MIME type declarations, itunes:duration formatting, and chapter markers using the podcast:chapters JSON format. The skill validates feeds against the Apple Podcasts specification and Spotify podcast delivery requirements.
Audio file metadata management uses the mutagen library to read and write ID3v2 tags, ensuring episode titles, artwork, and chapter information are embedded directly in MP3/M4A files. Integration with the Podcast Index API enables submission to the open podcast directory and retrieval of cross-platform listening statistics. The skill generates OPML files for feed collections, creates podcast:transcript references linking to SRT/VTT caption files, and manages artwork requirements (minimum 1400&#215;1400, maximum 3000&#215;3000 JPEG/PNG) with automatic resizing via Pillow. Distribution automation submits feeds to Apple Podcasts Connect, Spotify for Podcasters, and Google Podcasts simultaneously.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/podcast-rss-feed-builder/)
