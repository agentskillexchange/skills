---
title: "Slidev Markdown Presentation Slides for Developers"
description: "Slidev is a web-based presentation tool built for developers that turns Markdown files into interactive slide decks with code highlighting, live coding via Monaco Editor, LaTeX math, Mermaid diagrams, and export to PDF or PPTX."
verification: security_reviewed
source: "https://github.com/slidevjs/slidev"
category:
  - "Developer Tools"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "slidevjs/slidev"
  github_stars: 45362
---

# Slidev Markdown Presentation Slides for Developers

Slidev is an open-source presentation framework built specifically for developers who want to create slide decks using Markdown and Vue components. Created by Anthony Fu and available as the @slidev/cli npm package, it has earned over 35,000 GitHub stars and become the go-to tool for technical presentations at conferences and meetups worldwide.

The tool transforms Markdown files into fully interactive HTML presentations powered by Vite for instant hot-reload during editing. Each slide is separated by a simple --- delimiter in the Markdown source, and developers can embed Vue components directly alongside their content. Code blocks get first-class treatment with Shiki syntax highlighting, and the integrated Monaco Editor enables live coding demonstrations right inside the presentation. This means speakers can write and execute code on stage without switching to a separate editor.

Beyond text and code, Slidev supports LaTeX math equations via KaTeX, diagram generation through Mermaid integration, drawing and annotations with Drauu, and access to any icon set through Iconify. The theming system uses npm packages, so sharing and reusing presentation themes across teams is straightforward. UnoCSS provides on-demand utility-first styling, giving presenters fine-grained control over slide appearance.

For delivery, Slidev includes a presenter mode with speaker notes (usable from a phone), built-in recording with camera overlay, and export capabilities to PDF, PNG, or PPTX formats. A VS Code extension provides IDE-level editing support with preview.

An agent skill wrapping Slidev enables automated presentation generation from technical content, conference talk scaffolding, and batch export of documentation into slide format. The skill handles Markdown composition, theme selection, component embedding, and export orchestration. Slidev is MIT-licensed and requires Node.js 18 or later.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/slidev-markdown-presentation-slides-developers
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/slidev-markdown-presentation-slides-developers` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/slidev-markdown-presentation-slides-developers/)
