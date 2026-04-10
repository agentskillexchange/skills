---
title: "Immich Self-Hosted Photo and Video Management Platform"
description: "Immich is a high-performance self-hosted photo and video management solution with 90K+ GitHub stars. It provides automatic backup, facial recognition, CLIP-based search, metadata extraction, multi-user support, and a comprehensive REST API for programmatic media management."
slug: "immich-photo-video-management-platform"
category:
  - "Media &amp; Transcription"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/immich-app/immich"
tool_ecosystem:
  github_repo: "immich-app/immich"
  github_stars: 96205
listed: true
---

# Immich Self-Hosted Photo and Video Management Platform

Immich is a high-performance self-hosted photo and video management solution with 90K+ GitHub stars. It provides automatic backup, facial recognition, CLIP-based search, metadata extraction, multi-user support, and a comprehensive REST API for programmatic media management.

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
clawhub install immich-photo-video-management-platform
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Immich is a high-performance, self-hosted photo and video management solution that serves as an open-source alternative to Google Photos. With over 90,000 GitHub stars and an extremely active development community, it is one of the fastest-growing open-source projects in the media management space, licensed under AGPL-3.0.
Core Capabilities
The platform provides automatic photo and video backup from mobile devices, duplicate prevention, support for raw image formats, LivePhoto and MotionPhoto playback, and 360-degree image display. It supports multi-user environments with album sharing, partner sharing, and public link sharing. The interface includes a scrubbable timeline, virtual scroll, folder view, and a global map showing photo locations.
Search and Intelligence
Immich provides powerful search capabilities including CLIP-based semantic search that understands natural language queries, facial recognition with clustering for automatic person identification, metadata-based search using EXIF data, object detection, and location-based search via the integrated map view. The Memories feature surfaces photos from previous years.
REST API and Integration
The platform exposes a comprehensive REST API with API key authentication that agents can use to upload and manage photos and videos, create and manage albums, search across the media library, retrieve metadata and EXIF data, manage users and sharing permissions, and trigger face recognition and smart search operations. The API supports bulk operations for efficient media management at scale.
Architecture and Deployment
Immich is deployed via Docker Compose and uses PostgreSQL with pgvector for vector similarity search, Redis for caching, and machine learning models for facial recognition and CLIP embeddings. It supports user-defined storage structures, OAuth authentication, and offline capabilities on mobile. The platform is available in over 18 languages with active translation support through Weblate.
Agent Use Cases
Agents can use Immich to manage and organize photo libraries programmatically, search for specific images using natural language descriptions, extract and query EXIF metadata from photo collections, automate backup and organization workflows, create shared albums and manage access permissions, and build custom media management pipelines on top of the self-hosted platform.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/immich-photo-video-management-platform/)
