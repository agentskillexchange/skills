---
name: "Slidev Markdown Presentation Slides for Developers"
description: "Slidev is a web-based presentation tool built for developers that turns Markdown files into interactive slide decks with code highlighting, live coding via Monaco Editor, LaTeX math, Mermaid diagrams, and export to PDF or PPTX."
category: "Developer Tools"
framework: "Claude Code"
verification: security_reviewed
source: "https://github.com/slidevjs/slidev"
tool_ecosystem:
  github_repo: "slidevjs/slidev"
  github_stars: 45362
---
# Slidev Markdown Presentation Slides for Developers

Slidev is a web-based presentation tool built for developers that turns Markdown files into interactive slide decks with code highlighting, live coding via Monaco Editor, LaTeX math, Mermaid diagrams, and export to PDF or PPTX.

Slidev is an open-source presentation framework built specifically for developers who want to create slide decks using Markdown and Vue components. Created by Anthony Fu and available as the @slidev/cli npm package, it has earned over 35,000 GitHub stars and become the go-to tool for technical presentations at conferences and meetups worldwide.



The tool transforms Markdown files into fully interactive HTML presentations powered by Vite for instant hot-reload during editing. Each slide is separated by a simple --- delimiter in the Markdown source, and developers can embed Vue components directly alongside their content. Code blocks get first-class treatment with Shiki syntax highlighting, and the integrated Monaco Editor enables live coding demonstrations right inside the presentation. This means speakers can write and execute code on stage without switching to a separate editor.



Beyond text and code, Slidev supports LaTeX math equations via KaTeX, diagram generation through Mermaid integration, drawing and annotations with Drauu, and access to any icon set through Iconify. The theming system uses npm packages, so sharing and reusing presentation themes across teams is straightforward. UnoCSS provides on-demand utility-first styling, giving presenters fine-grained control over slide appearance.



For delivery, Slidev includes a presenter mode with speaker notes (usable from a phone), built-in recording with camera overlay, and export capabilities to PDF, PNG, or PPTX formats. A VS Code extension provides IDE-level editing support with preview.



An agent skill wrapping Slidev enables automated presentation generation from technical content, conference talk scaffolding, and batch export of documentation into slide format. The skill handles Markdown composition, theme selection, component embedding, and export orchestration. Slidev is MIT-licensed and requires Node.js 18 or later.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill slidev-markdown-presentation-slides-developers
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill slidev-markdown-presentation-slides-developers -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill slidev-markdown-presentation-slides-developers -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill slidev-markdown-presentation-slides-developers -a codex
```

### OpenClaw

```bash
clawhub install slidev-markdown-presentation-slides-developers
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/slidev-markdown-presentation-slides-developers/)
