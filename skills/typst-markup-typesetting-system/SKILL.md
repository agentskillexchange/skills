---
title: "Typst Markup-Based Document Typesetting System"
description: "Typst is a modern markup-based typesetting system designed to replace LaTeX with a faster, easier-to-learn alternative. It features built-in markup, a scripting system, math typesetting, bibliography management, and incremental compilation for near-instant builds."
slug: "typst-markup-typesetting-system"
category:
  - "Content Writing &amp; SEO"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/typst/typst"
tool_ecosystem:
  github_repo: "typst/typst"
  github_stars: 52359
listed: true
---

# Typst Markup-Based Document Typesetting System

Typst is a modern markup-based typesetting system designed to replace LaTeX with a faster, easier-to-learn alternative. It features built-in markup, a scripting system, math typesetting, bibliography management, and incremental compilation for near-instant builds.

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
clawhub install typst-markup-typesetting-system
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Typst is an open-source, markup-based typesetting system built in Rust that compiles documents to PDF. Created as a modern alternative to LaTeX, Typst dramatically reduces the complexity of document preparation while retaining full control over layout and formatting.
Core Capabilities
The Typst CLI (typst compile and typst watch) takes .typ source files and produces PDF output. The system includes built-in markup for headings, emphasis, lists, and other common formatting tasks, eliminating the need for preambles or package imports that LaTeX requires. For advanced formatting, Typst provides set rules and show rules that let you configure or completely redefine how elements appear.
Scripting and Math
Typst embeds a tightly integrated scripting language directly in documents. Variables, functions, loops, and conditionals work inline using hash-prefixed expressions. Math typesetting uses dollar-sign delimiters with a clean syntax — no backslashes needed for common symbols like sqrt, floor, or Greek letters. Bibliography management is built in, supporting BibTeX and other citation formats.
Agent Integration
AI coding agents can use the Typst CLI to programmatically generate reports, papers, invoices, and formatted documents from structured data. The typst compile command converts markup to PDF in a single step, and typst watch enables live recompilation during iterative editing. Agents can template documents using Typst scripting, passing data through variables and functions to produce consistently formatted output. The Typst package ecosystem on Typst Universe provides community templates for academic papers, resumes, slides, and more.
Installation and Usage
Install via your package manager: brew install typst (macOS), winget install Typst.Typst (Windows), cargo install --locked typst-cli (Rust), or download pre-built binaries from the releases page. Docker images are also available at ghcr.io/typst/typst. Full documentation is at typst.app/docs.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/typst-markup-typesetting-system/)
