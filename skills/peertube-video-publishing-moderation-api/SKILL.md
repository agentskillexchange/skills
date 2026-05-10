---
title: "PeerTube Video Publishing and Moderation API"
slug: "peertube-video-publishing-moderation-api"
description: "Uses PeerTube's REST API and federation-aware platform features to automate video uploads, channel management, moderation queues, and instance operations. A strong fit for creators or communities running their own open video infrastructure."
github_stars: 14638
verification: "security_reviewed"
source: "https://github.com/Chocobozzz/PeerTube"
author: "Framasoft"
publisher_type: "Community"
category: "Media & Transcription"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "chocobozzz/peertube"
  github_stars: 14638
---

# PeerTube Video Publishing and Moderation API

Uses PeerTube's REST API and federation-aware platform features to automate video uploads, channel management, moderation queues, and instance operations. A strong fit for creators or communities running their own open video infrastructure.

## Prerequisites

Node.js, PostgreSQL, PeerTube REST API

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
cd ./peertube-latest && sudo -H -u peertube npm run install-node-dependencies -- --production
```

## Documentation

- https://docs.joinpeertube.org/api-rest-reference.html

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/peertube-video-publishing-moderation-api/)
