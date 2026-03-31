---
name: "SVG Animation Builder"
description: "Creates animated SVGs using GSAP (GreenSock Animation Platform) and the SVG DOM API. Generates timeline-based animations with morphing paths via flubber and scroll-triggered sequences using ScrollTrigger plugin."
category: "Image & Creative Automation"
framework: "Custom Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/svg-animation-builder/"
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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/svg-animation-builder/)
