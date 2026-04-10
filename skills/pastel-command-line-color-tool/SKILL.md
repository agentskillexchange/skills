---
title: "pastel Command-Line Color Generation Analysis and Manipulation Tool"
description: "pastel is a command-line tool for generating, analyzing, converting, and manipulating colors. Built in Rust by the creator of bat, fd, and hyperfine, it supports color spaces including RGB, HSL, Lab, and LCH, with features for palette generation, contrast checking, and color blending."
slug: "pastel-command-line-color-tool"
category:
  - "Developer Tools"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/sharkdp/pastel"
tool_ecosystem:
  github_repo: "sharkdp/pastel"
  github_stars: 6301
listed: true
---

# pastel Command-Line Color Generation Analysis and Manipulation Tool

pastel is a command-line tool for generating, analyzing, converting, and manipulating colors. Built in Rust by the creator of bat, fd, and hyperfine, it supports color spaces including RGB, HSL, Lab, and LCH, with features for palette generation, contrast checking, and color blending.

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
clawhub install pastel-command-line-color-tool
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

pastel is a command-line color utility written in Rust by David Peter (sharkdp), the developer behind popular CLI tools bat, fd, and hyperfine. It provides comprehensive color manipulation capabilities directly from the terminal, making it useful for designers, frontend developers, and anyone working with color in automated workflows.
Color Operations
pastel supports conversion between multiple color spaces: RGB, HSL, HSV, Lab, LCH, and CSS color names. The pastel color command displays detailed information about any color including its hex value, RGB components, HSL values, and WCAG luminance. Colors can be specified as hex codes, CSS names, RGB triplets, or HSL values.
Palette and Scheme Generation
The pastel distinct command generates a set of visually distinct colors, useful for data visualization and charting. Complementary, analogous, triadic, and tetradic color schemes can be generated from any base color. The pastel gradient command creates smooth color gradients between two endpoints with configurable step counts. The pastel mix command blends colors in perceptually uniform color spaces like Lab and LCH.
Accessibility and Contrast
pastel includes WCAG contrast ratio checking between foreground and background colors, helping ensure text readability meets accessibility standards. The pastel textcolor command automatically selects black or white text for optimal readability against any background color.
Terminal Integration
Colors are displayed with actual terminal color preview swatches alongside their numeric values. The pastel paint command outputs colored text to the terminal. All output formats are designed to be pipeable and scriptable for integration into larger workflows.
Agent Skill Applications
AI agents working on frontend design, theming, or data visualization can use pastel to generate accessible color palettes, check contrast ratios, convert between color formats, and create harmonious color schemes. The CLI interface makes it easy to integrate into automated design systems, style guide generators, or accessibility audit pipelines. Agents can pipe colors through pastel to ensure all generated UI meets WCAG contrast requirements.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pastel-command-line-color-tool/)
