---
title: "Lottie Animation Optimizer"
description: "Analyzes and optimizes Lottie JSON animation files using lottie-web parser internals, reduces file size via keyframe deduplication and path simplification, and validates against the Telegram Lottie sticker spec (TGS)."
verification: security_reviewed
source: "https://github.com/airbnb/lottie-web"
category:
  - "Image &amp; Creative Automation"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  github_repo: "airbnb/lottie-web"
  github_stars: 31794
---

# Lottie Animation Optimizer

The Lottie Animation Optimizer parses After Effects-exported Lottie JSON files and applies size and performance optimizations for web and mobile delivery. It uses the lottie-web renderer’s internal data model to identify redundant keyframes, unused layers, oversized embedded images (replacing them with external asset references), and unnecessarily complex Bezier paths. The agent applies path simplification using Ramer-Douglas-Peucker algorithm on shape layers, deduplicates identical transform keyframes across layers, and strips editor metadata. For Telegram sticker compliance, it validates against the TGS spec: max 64KB gzipped, 512×512 canvas, 60fps max, no embedded raster images, no expressions. Output includes optimized JSON, gzipped .tgs for Telegram, and dotlottie (.lottie) container format with embedded assets. Performance benchmarks compare render time on lottie-web, lottie-ios (Airbnb), and rlottie (Samsung) renderers.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/lottie-animation-optimizer/)
