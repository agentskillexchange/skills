---
name: Chafa Terminal Image and Graphics Renderer
description: Chafa converts images, animated GIFs, and video frames into ANSI/Unicode
  character art or terminal graphics protocols (Sixel, Kitty, iTerm2) for display
  in any terminal. It supports a wide range of image formats and output modes, making
  it the go-to tool for rendering rich visual content in CLI environments.
verification: security_reviewed
source: https://github.com/hpjansson/chafa
category:
- Image &amp; Creative Automation
framework:
- Multi-Framework
tool_ecosystem:
  github_repo: hpjansson/chafa
  github_stars: 4542
---
# Chafa Terminal Image and Graphics Renderer

Chafa is a versatile command-line utility and C library that converts image data—including animated GIFs, SVGs, and video frames—into graphics formats suitable for terminal display. Created by Hans Petter Jansson, Chafa supports multiple terminal graphics protocols including Sixel, Kitty graphics protocol, and iTerm2 inline images, as well as classic ANSI/Unicode character art.
What Chafa Does
Chafa reads image files in virtually any format (PNG, JPEG, WebP, TIFF, GIF, SVG via librsvg, and more) and converts them into output optimized for your terminal. It automatically detects your terminal's capabilities and selects the best rendering mode available—from high-fidelity Sixel graphics on supported terminals down to ASCII art on the most basic text displays.
Core Capabilities
The tool provides fine-grained control over output through options for canvas size, color space, dithering algorithms, symbol selection, and animation frame rate. It can render to Unicode block characters, Braille patterns, ASCII characters, or pixel-perfect terminal graphics protocols. The &#8216;-animate' flag enables smooth playback of animated GIFs directly in the terminal.
Integration Points
Chafa is available as both a CLI tool (&#8216;chafa') and a shared C library (libchafa) with a documented public API. The library can be embedded into other applications for terminal graphics rendering. Python bindings are available via the &#8216;chafa.py' package on PyPI. Chafa is packaged for most Linux distributions (apt, dnf, pacman), macOS (Homebrew), and can be built from source using autotools.
Agent Use Cases
For AI agents operating in terminal environments, Chafa enables visual content rendering within CLI workflows—displaying image previews, showing visual diffs, rendering charts or diagrams, and presenting image analysis results directly in the terminal. Agents can pipe image data through Chafa to produce human-readable visual output without leaving the command line. The tool is particularly useful in SSH sessions, CI/CD pipelines, and headless server environments where a graphical display is unavailable.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/chafa-terminal-image-graphics-renderer/)
