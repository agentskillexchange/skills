---
name: "Lottie Animation Optimizer"
description: "Analyzes and optimizes Lottie JSON animation files using lottie-web parser internals, reduces file size via keyframe deduplication and path simplification, and validates against the Telegram Lottie sticker spec (TGS)."
category: "Image &amp; Creative Automation"
framework: "ChatGPT Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/lottie-animation-optimizer/"
---
# Lottie Animation Optimizer

Analyzes and optimizes Lottie JSON animation files using lottie-web parser internals, reduces file size via keyframe deduplication and path simplification, and validates against the Telegram Lottie sticker spec (TGS).

## Overview

The Lottie Animation Optimizer parses After Effects-exported Lottie JSON files and applies size and performance optimizations for web and mobile delivery. It uses the lottie-web renderer's internal data model to identify redundant keyframes, unused layers, oversized embedded images (replacing them with external asset references), and unnecessarily complex Bezier paths. The agent applies path simplification using Ramer-Douglas-Peucker algorithm on shape layers, deduplicates identical transform keyframes across layers, and strips editor metadata. For Telegram sticker compliance, it validates against the TGS spec: max 64KB gzipped, 512&#215;512 canvas, 60fps max, no embedded raster images, no expressions. Output includes optimized JSON, gzipped .tgs for Telegram, and dotlottie (.lottie) container format with embedded assets. Performance benchmarks compare render time on lottie-web, lottie-ios (Airbnb), and rlottie (Samsung) renderers.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill lottie-animation-optimizer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill lottie-animation-optimizer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill lottie-animation-optimizer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill lottie-animation-optimizer -a codex
```

### OpenClaw

```bash
clawhub install lottie-animation-optimizer
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/lottie-animation-optimizer/)
