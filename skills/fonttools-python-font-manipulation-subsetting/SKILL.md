---
title: "fonttools Python Font Manipulation and Subsetting Library"
description: "fonttools is a comprehensive Python library for manipulating font files, including TrueType, OpenType, WOFF, and WOFF2 formats. It includes the TTX tool for converting fonts to and from XML, a font subsetting utility for reducing font file sizes, and APIs for inspecting, modifying, and generating font files programmatically."
verification: security_reviewed
source: "https://github.com/fonttools/fonttools"
category:
  - "Developer Tools"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "fonttools/fonttools"
  github_stars: 5067
---

# fonttools Python Font Manipulation and Subsetting Library

Overview fonttools is the standard Python library for working with font files. Originally created by Just van Rossum, it has become the foundational tool used across the font development ecosystem. The library supports TrueType, OpenType, AFM, Type 1, WOFF, and WOFF2 formats, and is licensed under the MIT license.

Core Tools The package includes several key utilities. TTX converts binary font files to a human-readable XML format (also called TTX) and back, enabling inspection and manual editing of font tables. pyftsubset creates font subsets by selecting specific glyphs, reducing file size for web deployment. It can output in TrueType, WOFF, or WOFF2 formats, making it essential for web font optimization. pyftmerge merges multiple font files into one.

Font Subsetting for Web The subsetting tool is particularly valuable for web development. Running fonttools subset font.ttf --text="Hello World" --flavor=woff2 produces a minimal WOFF2 file containing only the glyphs needed. This dramatically reduces font file sizes — a full font might be 200KB+ while a subset for a specific language or character set can be under 20KB. The tool handles complex font features like ligatures, kerning tables, and OpenType layout features during subsetting.

Python API The programmatic API via from fontTools.ttLib import TTFont provides full access to font internals. Developers can read and modify any font table, add or remove glyphs, adjust metrics, generate variations for variable fonts, and compile modified fonts back to binary. The library integrates with fontTools.varLib for variable font operations and fontTools.designspaceLib for design space documents.

Installation Install via pip install fonttools. Optional extras include fonttools[woff] for WOFF/WOFF2 support (adds brotli and zopfli), fonttools[lxml] for faster XML processing, fonttools[unicode] for latest Unicode data, and fonttools[ufo] for UFO font source support. Requires Python 3.10+.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/fonttools-python-font-manipulation-subsetting
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/fonttools-python-font-manipulation-subsetting` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/fonttools-python-font-manipulation-subsetting/)
