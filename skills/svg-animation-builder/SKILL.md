---
title: "SVG Animation Builder"
description: "Creates animated SVGs using GSAP (GreenSock Animation Platform) and the SVG DOM API. Generates timeline-based animations with morphing paths via flubber and scroll-triggered sequences using ScrollTrigger plugin."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/svg-animation-builder/"
category:
  - "Image & Creative Automation"
framework:
  - "Custom Agents"
---

# SVG Animation Builder

The SVG Animation Builder skill creates complex animated SVG graphics using the GreenSock Animation Platform (GSAP) library. It generates GSAP timeline sequences with gsap.timeline() for orchestrating multi-element animations including transforms, opacity, stroke-dasharray draws, and filter effects. Path morphing between complex shapes uses the flubber library for smooth interpolation between SVG path d-attributes with different point counts. The skill constructs SVG elements programmatically using the SVG DOM API with document.createElementNS for elements like path, circle, rect, and g containers. Animation easing leverages GSAP built-in eases including power4.inOut, elastic.out, and custom cubic-bezier curves. ScrollTrigger plugin integration enables scroll-position-linked animations with configurable trigger points, scrub values, and pin settings. The skill outputs self-contained HTML files with embedded SVG and minimal GSAP runtime from the CDN. Export options include animated GIF conversion via puppeteer screenshot sequences and Lottie JSON format via bodymovin for cross-platform mobile playback.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/svg-animation-builder/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/svg-animation-builder
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/svg-animation-builder`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/svg-animation-builder/)
