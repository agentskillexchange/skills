---
title: "Revise PDF Slides with Natural-Language Edits"
description: "Tool: Nano-PDF This skill gives an agent a narrow, operator-friendly workflow for changing slide PDFs without rebuilding them by hand. Nano-PDF renders target pages, applies natural-language edit instructions through Gemini 3 Pro Image, restores searchable text with OCR, and stitches the edited pages back into a working PDF. In practice, the agent can update dates, fix typos, adjust charts, swap branding, restyle headers, or add a new slide that matches the visual language of the existing deck. Use this instead of the product’s normal CLI flow when the user’s real need is task execution, not tool operation. The agent can decide which pages to edit, when to add style reference pages, whether document context is needed, and how to trade off quality versus speed with the resolution setting. That makes it useful for pitch deck refreshes, board updates, sales collateral fixes, and quick presentation corrections that would otherwise require a manual round-trip through PowerPoint, Keynote, or a design tool. The scope boundary matters. This is not a generic PDF library, image model listing, or slide-design platform card. The skill is specifically about page-level PDF revision and deck-consistent slide insertion from natural-language requests. Integration points are explicit and source-backed: Python, the nano-pdf package, Poppler for page rendering, Tesseract for OCR rehydration, and a paid Gemini API key for image generation."
source: "https://github.com/gavrielc/Nano-PDF"
verification: "security_reviewed"
category:
  - "Image &amp; Creative Automation"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "gavrielc/Nano-PDF"
  github_stars: 1237
---

# Revise PDF Slides with Natural-Language Edits

Tool: Nano-PDF This skill gives an agent a narrow, operator-friendly workflow for changing slide PDFs without rebuilding them by hand. Nano-PDF renders target pages, applies natural-language edit instructions through Gemini 3 Pro Image, restores searchable text with OCR, and stitches the edited pages back into a working PDF. In practice, the agent can update dates, fix typos, adjust charts, swap branding, restyle headers, or add a new slide that matches the visual language of the existing deck. Use this instead of the product’s normal CLI flow when the user’s real need is task execution, not tool operation. The agent can decide which pages to edit, when to add style reference pages, whether document context is needed, and how to trade off quality versus speed with the resolution setting. That makes it useful for pitch deck refreshes, board updates, sales collateral fixes, and quick presentation corrections that would otherwise require a manual round-trip through PowerPoint, Keynote, or a design tool. The scope boundary matters. This is not a generic PDF library, image model listing, or slide-design platform card. The skill is specifically about page-level PDF revision and deck-consistent slide insertion from natural-language requests. Integration points are explicit and source-backed: Python, the nano-pdf package, Poppler for page rendering, Tesseract for OCR rehydration, and a paid Gemini API key for image generation.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/revise-pdf-slides-with-natural-language-edits/)
