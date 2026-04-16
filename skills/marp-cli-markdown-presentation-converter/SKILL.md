---
title: "Marp CLI Markdown Presentation Converter and Slide Deck Generator"
description: "Marp CLI converts Markdown files into professional slide deck presentations. It outputs static HTML, PDF, PowerPoint (PPTX), and image formats from a single Markdown source, enabling developers and content creators to build presentations as code."
verification: "security_reviewed"
source: "https://github.com/marp-team/marp-cli"
category:
  - "Content Writing &amp; SEO"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "marp-team/marp-cli"
  github_stars: 3359
---

# Marp CLI Markdown Presentation Converter and Slide Deck Generator

What is Marp CLI?

Marp CLI is a command-line interface for the Marp presentation ecosystem, built on the Marpit framework. It transforms Markdown documents into polished slide decks in multiple output formats including HTML, PDF, PowerPoint (PPTX), and PNG/JPEG images. The tool enables a “presentation as code” workflow where slides are authored in plain Markdown and converted to any target format via a single CLI command.

Core Capabilities

The @marp-team/marp-cli npm package provides a complete presentation pipeline. It accepts standard Markdown files with Marp directives for theming, pagination, and layout control. The CLI supports watch mode for live preview during authoring, making it easy to iterate on slide content. Output formats cover every common presentation need: static HTML with embedded CSS for web publishing, PDF for print and sharing, PPTX for Microsoft PowerPoint compatibility, and rasterized images for embedding in documents or social media.

How Agents Use Marp CLI

AI agents and automation pipelines use Marp CLI to programmatically generate presentations from structured data or content. A typical workflow involves generating Markdown slide content (with Marp-specific directives like --- for slide breaks and marp: true frontmatter), then invoking npx @marp-team/marp-cli slide-deck.md --pdf to produce the final output. The tool also supports custom themes via CSS, HTML templating, and configuration files (.marprc.yml) for project-level defaults.

Installation and Usage

Install globally via npm: npm install -g @marp-team/marp-cli, or use without installing via npx @marp-team/marp-cli@latest. Docker images are also available at marpteam/marp-cli on Docker Hub. The CLI requires Node.js v18 or later. For PDF and image output, it uses a headless Chromium instance internally.

Integration Points

Marp CLI integrates with CI/CD pipelines for automated presentation generation, VS Code via the Marp for VS Code extension for live preview, and any Markdown-based content workflow. It supports custom Marpit engine plugins for extending the rendering pipeline, making it suitable for teams that need standardized, branded presentation templates generated from data.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/marp-cli-markdown-presentation-converter/)
