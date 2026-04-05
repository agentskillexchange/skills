---
name: "Lip Gloss CSS-Like Terminal Styling Library for Go"
description: "Lip Gloss by Charmbracelet is a Go library that brings CSS-like declarative styling to terminal UIs. With 11,000+ GitHub stars, it provides expressive color handling, borders, padding, tables, and layout primitives for building polished terminal applications."
category: "Developer Tools"
framework: "Multi-Framework"
verification: security_reviewed
source: "https://github.com/charmbracelet/lipgloss"
---
# Lip Gloss CSS-Like Terminal Styling Library for Go

Lip Gloss by Charmbracelet is a Go library that brings CSS-like declarative styling to terminal UIs. With 11,000+ GitHub stars, it provides expressive color handling, borders, padding, tables, and layout primitives for building polished terminal applications.

Lip Gloss is an open-source Go library by Charmbracelet that brings CSS-like declarative styling to terminal user interfaces. With over 11,000 stars on GitHub, it has become the de facto standard for styled terminal rendering in the Go ecosystem.



What It Does

Lip Gloss provides a fluent, chainable API for defining terminal styles. Developers familiar with CSS will find the approach intuitive — styles are defined with properties like Bold, Foreground, Background, Padding, Margin, and Width, then applied to text via a Render method. The library handles color profile detection automatically, downsampling Truecolor to 256-color or ANSI as needed.



Key Features

Declarative Styling: Define styles with a chainable API that mirrors CSS properties. Set colors, borders, padding, margins, alignment, and dimensions in a readable, composable way.



Adaptive Color Support: Lip Gloss supports Truecolor (16 million colors), ANSI 256-color, ANSI 16-color, and 1-bit ASCII profiles. It automatically detects the terminal capabilities and downgrades colors gracefully.



Color Utilities: Built-in functions for color manipulation — darken, lighten, complementary colors, alpha blending, and automatic light/dark variant selection at runtime.



Layout Primitives: Includes table rendering, tree structures, list formatting, and a JoinHorizontal/JoinVertical system for composing complex multi-panel layouts.



Bubble Tea Integration: Designed to work seamlessly with Bubble Tea (the Go TUI framework) while also functioning perfectly as a standalone library.



How Agents Use It

AI coding agents building Go CLI tools or TUI applications can use Lip Gloss to style output consistently. When generating terminal UIs, an agent can use the declarative API to create professional-looking output with proper alignment, coloring, and borders. The library is also essential for agents working with the broader Charmbracelet ecosystem (Bubble Tea, Huh, Gum) since Lip Gloss is the styling foundation they all share.



Installation

go get charm.land/lipgloss/v2

Integration Points

Lip Gloss integrates with Bubble Tea for interactive TUI apps, Glamour for markdown rendering, and the broader Go terminal ecosystem. It works with any Go program that writes to stdout or any io.Writer.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill lipgloss-terminal-styling-library
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill lipgloss-terminal-styling-library -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill lipgloss-terminal-styling-library -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill lipgloss-terminal-styling-library -a codex
```

### OpenClaw

```bash
clawhub install lipgloss-terminal-styling-library
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/lipgloss-terminal-styling-library/)
