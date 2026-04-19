---
title: "Lottie Animation Optimizer"
description: "The Lottie Animation Optimizer parses After Effects-exported Lottie JSON files and applies size and performance optimizations for web and mobile delivery. It uses the lottie-web renderer&#8217;s internal data model to identify redundant keyframes, unused layers, oversized embedded images (replacing them with external asset references), and unnecessarily complex Bezier paths. The agent applies path simplification using Ramer-Douglas-Peucker algorithm on shape layers, deduplicates identical transform keyframes across layers, and strips editor metadata. For Telegram sticker compliance, it validates against the TGS spec: max 64KB gzipped, 512&#215;512 canvas, 60fps max, no embedded raster images, no expressions. Output includes optimized JSON, gzipped .tgs for Telegram, and dotlottie (.lottie) container format with embedded assets. Performance benchmarks compare render time on lottie-web, lottie-ios (Airbnb), and rlottie (Samsung) renderers."
source: "https://github.com/airbnb/lottie-web"
verification: "security_reviewed"
category:
  - "Image &amp; Creative Automation"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  github_repo: "airbnb/lottie-web"
  github_stars: 31794
---

# Lottie Animation Optimizer

The Lottie Animation Optimizer parses After Effects-exported Lottie JSON files and applies size and performance optimizations for web and mobile delivery. It uses the lottie-web renderer&#8217;s internal data model to identify redundant keyframes, unused layers, oversized embedded images (replacing them with external asset references), and unnecessarily complex Bezier paths. The agent applies path simplification using Ramer-Douglas-Peucker algorithm on shape layers, deduplicates identical transform keyframes across layers, and strips editor metadata. For Telegram sticker compliance, it validates against the TGS spec: max 64KB gzipped, 512&#215;512 canvas, 60fps max, no embedded raster images, no expressions. Output includes optimized JSON, gzipped .tgs for Telegram, and dotlottie (.lottie) container format with embedded assets. Performance benchmarks compare render time on lottie-web, lottie-ios (Airbnb), and rlottie (Samsung) renderers.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/lottie-animation-optimizer/)
