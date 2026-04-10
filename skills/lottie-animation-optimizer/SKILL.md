---
title: "Lottie Animation Optimizer"
description: "Analyzes and optimizes Lottie JSON animation files using lottie-web parser internals, reduces file size via keyframe deduplication and path simplification, and validates against the Telegram Lottie sticker spec (TGS)."
slug: "lottie-animation-optimizer"
category:
  - "Image &amp; Creative Automation"
framework:
  - "ChatGPT Agents"
verification: "security_reviewed"
source: "https://github.com/airbnb/lottie-web"
tool_ecosystem:
  github_repo: "airbnb/lottie-web"
  github_stars: 31794
listed: true
---

# Lottie Animation Optimizer

Analyzes and optimizes Lottie JSON animation files using lottie-web parser internals, reduces file size via keyframe deduplication and path simplification, and validates against the Telegram Lottie sticker spec (TGS).

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
clawhub install lottie-animation-optimizer
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Lottie Animation Optimizer parses After Effects-exported Lottie JSON files and applies size and performance optimizations for web and mobile delivery. It uses the lottie-web renderer’s internal data model to identify redundant keyframes, unused layers, oversized embedded images (replacing them with external asset references), and unnecessarily complex Bezier paths. The agent applies path simplification using Ramer-Douglas-Peucker algorithm on shape layers, deduplicates identical transform keyframes across layers, and strips editor metadata. For Telegram sticker compliance, it validates against the TGS spec: max 64KB gzipped, 512×512 canvas, 60fps max, no embedded raster images, no expressions. Output includes optimized JSON, gzipped .tgs for Telegram, and dotlottie (.lottie) container format with embedded assets. Performance benchmarks compare render time on lottie-web, lottie-ios (Airbnb), and rlottie (Samsung) renderers.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/lottie-animation-optimizer/)
