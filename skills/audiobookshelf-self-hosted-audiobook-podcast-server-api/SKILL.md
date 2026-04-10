---
title: "Audiobookshelf Self-Hosted Audiobook and Podcast Server API"
description: "Integrate Audiobookshelf’s self-hosted audiobook and podcast server into AI agent workflows. Agents can manage libraries, track listening progress, search metadata, and automate podcast episode downloads through the comprehensive REST API."
slug: "audiobookshelf-self-hosted-audiobook-podcast-server-api"
category:
  - "Media &amp; Transcription"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/advplyr/audiobookshelf"
tool_ecosystem:
  github_repo: "advplyr/audiobookshelf"
  github_stars: 12295
listed: true
---

# Audiobookshelf Self-Hosted Audiobook and Podcast Server API

Integrate Audiobookshelf’s self-hosted audiobook and podcast server into AI agent workflows. Agents can manage libraries, track listening progress, search metadata, and automate podcast episode downloads through the comprehensive REST API.

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
clawhub install audiobookshelf-self-hosted-audiobook-podcast-server-api
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Audiobookshelf is a fully open-source, self-hosted audiobook and podcast server with over 12,000 GitHub stars and an active community. It provides a complete media management platform with a well-documented REST API that AI agents can use to manage audio libraries, track user progress, and automate media workflows.
What This Skill Enables
An agent skill built around Audiobookshelf lets AI agents serve as intelligent audio library managers. Through the Audiobookshelf API (documented at api.audiobookshelf.org), agents can search across audiobook and podcast libraries, retrieve detailed metadata including chapters, narrators, and series information, track and sync listening progress across devices, and manage podcast subscriptions with automated episode downloads.
Core Capabilities
The Audiobookshelf API exposes endpoints for library management (create, list, scan libraries), media item operations (get audiobooks, get podcasts, search), playback session tracking (start session, update progress, close session), user management with custom permissions, collection and playlist management, and podcast episode discovery and download. Agents can perform batch operations like bulk metadata updates, library reorganization, and automated tagging based on content analysis.
Integration Points
Audiobookshelf supports multiple audio formats with on-the-fly transcoding, meaning agents don’t need to worry about format compatibility. It integrates with metadata providers like Audible, Google Books, iTunes, and Audnexus for automatic cover art and metadata fetching. The server supports RSS feed generation for both audiobooks and podcasts, enabling agents to create custom feeds. Webhook support allows event-driven workflows when new media is added or playback milestones are reached. The platform includes Chromecast support and a Progressive Web App.
Technical Details
Audiobookshelf is built with Node.js and can be deployed via Docker (ghcr.io/advplyr/audiobookshelf). The REST API uses Bearer token authentication and returns JSON responses. The API supports filtering, sorting, and pagination across all list endpoints. WebSocket connections are available for real-time playback synchronization. The server auto-detects library changes without requiring manual rescans.
Use Cases
AI agents can use this skill to build voice-controlled audiobook players, automate podcast curation by searching and subscribing to shows based on topics, generate listening reports and recommendations, manage family audiobook libraries with per-user progress tracking, and create automated workflows that download new podcast episodes matching specific criteria.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/audiobookshelf-self-hosted-audiobook-podcast-server-api/)
