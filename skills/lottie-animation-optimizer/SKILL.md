---
title: Lottie Animation Optimizer
description: 'The Lottie Animation Optimizer parses After Effects-exported Lottie
  JSON files and applies size and performance optimizations for web and mobile delivery.
  It uses the lottie-web renderer’s internal data model to identify redundant keyframes,
  unused layers, oversized embedded images (replacing them with external asset references),
  and unnecessarily complex Bezier paths. The agent applies path simplification using
  Ramer-Douglas-Peucker algorithm on shape layers, deduplicates identical transform
  keyframes across layers, and strips editor metadata. For Telegram sticker compliance,
  it validates against the TGS spec: max 64KB gzipped, 512×512 canvas, 60fps max,
  no embedded raster images, no expressions. Output includes optimized JSON, gzipped
  .tgs for Telegram, and dotlottie (.lottie) container format with embedded assets.
  Performance benchmarks compare render time on lottie-web, lottie-ios (Airbnb), and
  rlottie (Samsung) renderers.'
verification: security_reviewed
source: https://github.com/airbnb/lottie-web
category:
- Image &amp; Creative Automation
framework:
- ChatGPT Agents
tool_ecosystem:
  github_repo: airbnb/lottie-web
  github_stars: 31786
---

# Lottie Animation Optimizer

The Lottie Animation Optimizer parses After Effects-exported Lottie JSON files and applies size and performance optimizations for web and mobile delivery. It uses the lottie-web renderer’s internal data model to identify redundant keyframes, unused layers, oversized embedded images (replacing them with external asset references), and unnecessarily complex Bezier paths. The agent applies path simplification using Ramer-Douglas-Peucker algorithm on shape layers, deduplicates identical transform keyframes across layers, and strips editor metadata. For Telegram sticker compliance, it validates against the TGS spec: max 64KB gzipped, 512×512 canvas, 60fps max, no embedded raster images, no expressions. Output includes optimized JSON, gzipped .tgs for Telegram, and dotlottie (.lottie) container format with embedded assets. Performance benchmarks compare render time on lottie-web, lottie-ios (Airbnb), and rlottie (Samsung) renderers.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/lottie-animation-optimizer/)
