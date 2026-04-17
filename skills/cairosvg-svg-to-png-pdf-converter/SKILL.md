---
title: "CairoSVG SVG to PNG PDF and PostScript Converter"
description: "Overview\nCairoSVG is an SVG rendering and conversion library for Python, developed by Kozea and maintained by CourtBouillon. Built on top of the Cairo 2D graphics library, it parses SVG documents and exports them to raster (PNG) and vector (PDF, EPS, PostScript) formats with high fidelity. It focuses on real-world SVG rendering rather than edge-case syntax support.\nCore Capabilities\nCairoSVG supports conversion from SVG to PNG, PDF, EPS, and PS output formats. It handles common SVG features including paths, shapes, text, gradients, clipping, masking, filters, and embedded images. The library provides both a command-line interface (cairosvg) and a Python API for programmatic use. Output resolution (DPI) and dimensions are configurable.\nThe CLI accepts input from files, URLs, or stdin, and outputs to files or stdout. The Python API exposes functions like cairosvg.svg2png(), cairosvg.svg2pdf(), and cairosvg.svg2ps() that accept SVG as strings, file objects, or URLs.\nAgent Integration\nCairoSVG is useful for agents that need to convert dynamically generated SVGs (charts, diagrams, icons) into raster or print-ready formats. An agent can generate an SVG with D3, Mermaid, or custom code, then pipe it through CairoSVG to produce a PNG for embedding or a PDF for distribution. The Python API makes it easy to integrate into automated pipelines without spawning subprocesses.\nInstallation and Usage\nInstall via pip: pip install cairosvg. Requires Python 3.10+ and the Cairo system library (typically libcairo2 on Linux, available via Homebrew on macOS). Basic CLI usage: cairosvg input.svg -o output.png. For PDF: cairosvg input.svg -o output.pdf. DPI control: cairosvg input.svg -o output.png -d 300.\nDocumentation and Community\nDocumentation is at cairosvg.org/documentation. The project has 900+ GitHub stars, is licensed under LGPL-3.0, and has regular releases tracked on the GitHub releases page. It is actively maintained with commits as recent as March 2026."
verification: security_reviewed
source: "https://github.com/Kozea/CairoSVG"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "Kozea/CairoSVG"
  github_stars: 917
---

# CairoSVG SVG to PNG PDF and PostScript Converter

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

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/cairosvg-svg-to-png-pdf-converter
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/cairosvg-svg-to-png-pdf-converter` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cairosvg-svg-to-png-pdf-converter/)
