---
title: "CairoSVG SVG to PNG PDF and PostScript Converter"
description: "CairoSVG is a Python-based SVG converter built on the Cairo 2D graphics library. It converts SVG files to PNG, PDF, EPS, and PostScript formats via both a CLI and a Python API, making it a reliable tool for automated image pipeline workflows."
slug: "cairosvg-svg-to-png-pdf-converter"
category:
  - "Image &amp; Creative Automation"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/Kozea/CairoSVG"
tool_ecosystem:
  github_repo: "Kozea/CairoSVG"
  github_stars: 917
---

# CairoSVG SVG to PNG PDF and PostScript Converter

CairoSVG is a Python-based SVG converter built on the Cairo 2D graphics library. It converts SVG files to PNG, PDF, EPS, and PostScript formats via both a CLI and a Python API, making it a reliable tool for automated image pipeline workflows.

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
clawhub install cairosvg-svg-to-png-pdf-converter
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Overview
CairoSVG is an SVG rendering and conversion library for Python, developed by Kozea and maintained by CourtBouillon. Built on top of the Cairo 2D graphics library, it parses SVG documents and exports them to raster (PNG) and vector (PDF, EPS, PostScript) formats with high fidelity. It focuses on real-world SVG rendering rather than edge-case syntax support.
Core Capabilities
CairoSVG supports conversion from SVG to PNG, PDF, EPS, and PS output formats. It handles common SVG features including paths, shapes, text, gradients, clipping, masking, filters, and embedded images. The library provides both a command-line interface (cairosvg) and a Python API for programmatic use. Output resolution (DPI) and dimensions are configurable.
The CLI accepts input from files, URLs, or stdin, and outputs to files or stdout. The Python API exposes functions like cairosvg.svg2png(), cairosvg.svg2pdf(), and cairosvg.svg2ps() that accept SVG as strings, file objects, or URLs.
Agent Integration
CairoSVG is useful for agents that need to convert dynamically generated SVGs (charts, diagrams, icons) into raster or print-ready formats. An agent can generate an SVG with D3, Mermaid, or custom code, then pipe it through CairoSVG to produce a PNG for embedding or a PDF for distribution. The Python API makes it easy to integrate into automated pipelines without spawning subprocesses.
Installation and Usage
Install via pip: pip install cairosvg. Requires Python 3.10+ and the Cairo system library (typically libcairo2 on Linux, available via Homebrew on macOS). Basic CLI usage: cairosvg input.svg -o output.png. For PDF: cairosvg input.svg -o output.pdf. DPI control: cairosvg input.svg -o output.png -d 300.
Documentation and Community
Documentation is at cairosvg.org/documentation. The project has 900+ GitHub stars, is licensed under LGPL-3.0, and has regular releases tracked on the GitHub releases page. It is actively maintained with commits as recent as March 2026.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cairosvg-svg-to-png-pdf-converter/)
