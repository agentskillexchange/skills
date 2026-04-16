---
title: "SVG Animation Builder"
description: "Creates animated SVGs using GSAP (GreenSock Animation Platform) and the SVG DOM API. Generates timeline-based animations with morphing paths via flubber and scroll-triggered sequences using ScrollTrigger plugin."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/svg-animation-builder/"
category:
  - "Image &amp; Creative Automation"
framework:
  - "Custom Agents"
---

# SVG Animation Builder

The SVG Animation Builder skill creates complex animated SVG graphics using the GreenSock Animation Platform (GSAP) library. It generates GSAP timeline sequences with gsap.timeline() for orchestrating multi-element animations including transforms, opacity, stroke-dasharray draws, and filter effects. Path morphing between complex shapes uses the flubber library for smooth interpolation between SVG path d-attributes with different point counts. The skill constructs SVG elements programmatically using the SVG DOM API with document.createElementNS for elements like path, circle, rect, and g containers. Animation easing leverages GSAP built-in eases including power4.inOut, elastic.out, and custom cubic-bezier curves. ScrollTrigger plugin integration enables scroll-position-linked animations with configurable trigger points, scrub values, and pin settings. The skill outputs self-contained HTML files with embedded SVG and minimal GSAP runtime from the CDN. Export options include animated GIF conversion via puppeteer screenshot sequences and Lottie JSON format via bodymovin for cross-platform mobile playback.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/svg-animation-builder/)
