---
title: "SVG Animation Builder"
description: "The SVG Animation Builder skill creates complex animated SVG graphics using the GreenSock Animation Platform (GSAP) library. It generates GSAP timeline sequences with gsap.timeline() for orchestrating multi-element animations including transforms, opacity, stroke-dasharray draws, and filter effects. Path morphing between complex shapes uses the flubber library for smooth interpolation between SVG path d-attributes with different point counts. The skill constructs SVG elements programmatically using the SVG DOM API with document.createElementNS for elements like path, circle, rect, and g containers. Animation easing leverages GSAP built-in eases including power4.inOut, elastic.out, and custom cubic-bezier curves. ScrollTrigger plugin integration enables scroll-position-linked animations with configurable trigger points, scrub values, and pin settings. The skill outputs self-contained HTML files with embedded SVG and minimal GSAP runtime from the CDN. Export options include animated GIF conversion via puppeteer screenshot sequences and Lottie JSON format via bodymovin for cross-platform mobile playback."
source: "https://agentskillexchange.com/skills/svg-animation-builder/"
verification: "security_reviewed"
category:
  - "Image &amp; Creative Automation"
framework:
  - "Custom Agents"
---

# SVG Animation Builder

The SVG Animation Builder skill creates complex animated SVG graphics using the GreenSock Animation Platform (GSAP) library. It generates GSAP timeline sequences with gsap.timeline() for orchestrating multi-element animations including transforms, opacity, stroke-dasharray draws, and filter effects. Path morphing between complex shapes uses the flubber library for smooth interpolation between SVG path d-attributes with different point counts. The skill constructs SVG elements programmatically using the SVG DOM API with document.createElementNS for elements like path, circle, rect, and g containers. Animation easing leverages GSAP built-in eases including power4.inOut, elastic.out, and custom cubic-bezier curves. ScrollTrigger plugin integration enables scroll-position-linked animations with configurable trigger points, scrub values, and pin settings. The skill outputs self-contained HTML files with embedded SVG and minimal GSAP runtime from the CDN. Export options include animated GIF conversion via puppeteer screenshot sequences and Lottie JSON format via bodymovin for cross-platform mobile playback.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/svg-animation-builder/)
