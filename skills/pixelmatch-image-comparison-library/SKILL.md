---
name: "Pixelmatch Pixel-Level Image Comparison Library by Mapbox"
description: "Pixelmatch is the smallest, simplest, and fastest JavaScript pixel-level image comparison library by Mapbox. It features anti-aliased pixel detection and perceptual color difference metrics, making it ideal for visual regression testing in CI/CD pipelines."
category: "Image &amp; Creative Automation"
framework: "Multi-Framework"
verification: security_reviewed
source: "https://github.com/mapbox/pixelmatch"
---
# Pixelmatch Pixel-Level Image Comparison Library by Mapbox

Pixelmatch is the smallest, simplest, and fastest JavaScript pixel-level image comparison library by Mapbox. It features anti-aliased pixel detection and perceptual color difference metrics, making it ideal for visual regression testing in CI/CD pipelines.

Pixelmatch is a lightweight JavaScript library created by Mapbox for pixel-level image comparison. At around 150 lines of code with zero dependencies, it is the smallest and fastest image diff tool available for Node.js and browser environments. With over 6,700 GitHub stars, it has become the standard for visual regression testing across the JavaScript ecosystem.

How It Works Pixelmatch operates on raw typed arrays of image data (Uint8Array or Uint8ClampedArray), comparing two images pixel by pixel. It uses perceptual color difference metrics based on YIQ NTSC color space research, and includes an anti-aliased pixel detection algorithm to avoid false positives on font rendering and smooth edges. The function returns the count of mismatched pixels and optionally generates a visual diff image.

Key Features

Zero dependencies: Runs anywhere — Node.js, browsers, CI environments — with no external packages required. Anti-aliasing detection: Identifies and optionally excludes anti-aliased pixels to reduce false positives in screenshot comparisons. Perceptual color diff: Uses YIQ-based color distance for human-perceptual accuracy rather than simple RGB comparison. Configurable threshold: Adjust sensitivity from 0 (exact match) to 1 (loose match) with 0.1 as default. Visual diff output: Generates a diff image highlighting mismatched pixels in configurable colors. CLI tool included: Ship with a binary for command-line image comparison without writing code. Diff mask mode: Can output diffs on transparent backgrounds for overlay comparison.

Installation npm install pixelmatch Usage Example import pixelmatch from "pixelmatch"; const numDiffPixels = pixelmatch(img1, img2, diff, 800, 600, {threshold: 0.1}); Integration with AI Agents Pixelmatch is a natural fit for AI agent visual regression testing workflows. Agents can capture before/after screenshots using Playwright or Puppeteer, then use pixelmatch to quantify visual changes. This enables automated UI change detection, screenshot-based test assertions, and visual diff reporting — all from within an agent skill pipeline. The CLI mode makes it trivially scriptable in CI/CD environments.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill pixelmatch-image-comparison-library
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill pixelmatch-image-comparison-library -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill pixelmatch-image-comparison-library -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill pixelmatch-image-comparison-library -a codex
```

### OpenClaw

```bash
clawhub install pixelmatch-image-comparison-library
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pixelmatch-image-comparison-library/)
