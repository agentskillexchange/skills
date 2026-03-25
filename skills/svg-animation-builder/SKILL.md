---
name: "SVG Animation Builder"
description: "Creates animated SVGs using GSAP (GreenSock Animation Platform) and the SVG DOM API. Generates timeline-based animations with morphing paths via flubber and scroll-triggered sequences using ScrollTrigger plugin."
category: "Image & Creative Automation"
framework: "Custom Agents"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/svg-animation-builder/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "puppeteer"  # from ase_tool_match
  github_stars: 93932  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 8696130  # from ase_npm_downloads
  github_repo: "puppeteer/puppeteer"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# SVG Animation Builder

Creates animated SVGs using GSAP (GreenSock Animation Platform) and the SVG DOM API. Generates timeline-based animations with morphing paths via flubber and scroll-triggered sequences using ScrollTrigger plugin.

## Overview

The SVG Animation Builder skill creates complex animated SVG graphics using the GreenSock Animation Platform (GSAP) library. It generates GSAP timeline sequences with gsap.timeline() for orchestrating multi-element animations including transforms, opacity, stroke-dasharray draws, and filter effects. Path morphing between complex shapes uses the flubber library for smooth interpolation between SVG path d-attributes with different point counts. The skill constructs SVG elements programmatically using the SVG DOM API with document.createElementNS for elements like path, circle, rect, and g containers. Animation easing leverages GSAP built-in eases including power4.inOut, elastic.out, and custom cubic-bezier curves. ScrollTrigger plugin integration enables scroll-position-linked animations with configurable trigger points, scrub values, and pin settings. The skill outputs self-contained HTML files with embedded SVG and minimal GSAP runtime from the CDN. Export options include animated GIF conversion via puppeteer screenshot sequences and Lottie JSON format via bodymovin for cross-platform mobile playback.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill svg-animation-builder
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill svg-animation-builder -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill svg-animation-builder -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill svg-animation-builder -a codex
```

### OpenClaw

```bash
clawhub install svg-animation-builder
```

## Source

- Marketplace: https://agentskillexchange.com/skills/svg-animation-builder/
