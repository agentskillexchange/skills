---
title: "PeerTube Video Publishing and Moderation API"
description: "Uses PeerTube’s REST API and federation-aware platform features to automate video uploads, channel management, moderation queues, and instance operations. A strong fit for creators or communities running their own open video infrastructure."
slug: "peertube-video-publishing-moderation-api"
category:
  - "Media &amp; Transcription"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/Chocobozzz/PeerTube"
---

# PeerTube Video Publishing and Moderation API

Uses PeerTube’s REST API and federation-aware platform features to automate video uploads, channel management, moderation queues, and instance operations. A strong fit for creators or communities running their own open video infrastructure.

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
clawhub install peertube-video-publishing-moderation-api
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

PeerTube Video Publishing and Moderation API is a skill centered on PeerTube, the federated video platform originally developed by Framasoft and published as an open-source project on GitHub. The skill gives agents a real platform to automate: uploading and importing videos, managing channels, editing metadata, handling moderation decisions, checking processing status, and working with instance-level administration through documented APIs and operational tooling. That makes it more than a generic “video workflow” idea — it is tied to a concrete upstream product with active releases, public documentation, and an established user base.
This is especially useful for organizations that host their own video instance and want agents to help with publishing or trust-and-safety workflows. An agent can watch a queue for newly uploaded assets, create titles and descriptions, schedule publishing, apply channel defaults, review reports, or trigger follow-up actions when transcoding finishes. PeerTube also supports ActivityPub federation, so the skill fits communities that want open distribution instead of relying entirely on centralized video hosts. Upstream documentation covers production installation, admin operations, and the REST API reference, while the main repository shows recent maintenance and a large star count. Integration points include the REST API, instance administration, upload and import tooling, PostgreSQL-backed deployments, and Node.js-based server maintenance commands.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/peertube-video-publishing-moderation-api/)
