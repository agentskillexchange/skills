---
name: "PeerTube Video Publishing and Moderation API"
description: "Uses PeerTube's REST API and federation-aware platform features to automate video uploads, channel management, moderation queues, and instance operations. A strong fit for creators or communities running their own open video infrastructure."
verification: security_reviewed
source: "https://github.com/Chocobozzz/PeerTube"
category:
  - "Media &amp; Transcription"
framework:
  - "Multi-Framework"
---

# PeerTube Video Publishing and Moderation API

PeerTube Video Publishing and Moderation API is a skill centered on PeerTube, the federated video platform originally developed by Framasoft and published as an open-source project on GitHub. The skill gives agents a real platform to automate: uploading and importing videos, managing channels, editing metadata, handling moderation decisions, checking processing status, and working with instance-level administration through documented APIs and operational tooling. That makes it more than a generic “video workflow” idea — it is tied to a concrete upstream product with active releases, public documentation, and an established user base.
This is especially useful for organizations that host their own video instance and want agents to help with publishing or trust-and-safety workflows. An agent can watch a queue for newly uploaded assets, create titles and descriptions, schedule publishing, apply channel defaults, review reports, or trigger follow-up actions when transcoding finishes. PeerTube also supports ActivityPub federation, so the skill fits communities that want open distribution instead of relying entirely on centralized video hosts. Upstream documentation covers production installation, admin operations, and the REST API reference, while the main repository shows recent maintenance and a large star count. Integration points include the REST API, instance administration, upload and import tooling, PostgreSQL-backed deployments, and Node.js-based server maintenance commands.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/peertube-video-publishing-moderation-api/)
