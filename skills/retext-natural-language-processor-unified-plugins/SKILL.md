---
title: "retext Natural Language Processor with Unified Plugin Ecosystem"
description: "retext is a natural language processor powered by plugins, part of the unified.js collective. It parses Latin-script text into an AST (nlcst), enabling programmatic text analysis and transformation through a rich plugin ecosystem for spell checking, readability analysis, typography fixes, and content quality enforcement."
slug: "retext-natural-language-processor-unified-plugins"
category:
  - "Content Writing &amp; SEO"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/retextjs/retext"
tool_ecosystem:
  github_repo: "retextjs/retext"
  github_stars: 2433
---

# retext Natural Language Processor with Unified Plugin Ecosystem

retext is a natural language processor powered by plugins, part of the unified.js collective. It parses Latin-script text into an AST (nlcst), enabling programmatic text analysis and transformation through a rich plugin ecosystem for spell checking, readability analysis, typography fixes, and content quality enforcement.

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
clawhub install retext-natural-language-processor-unified-plugins
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

retext is a natural language processing framework that operates on a concrete syntax tree (CST) representation of text, built as part of the unified.js collective — the same ecosystem that powers remark (Markdown), rehype (HTML), and other content processing tools. It parses Latin-script natural language into nlcst (Natural Language Concrete Syntax Tree) nodes, then applies a pipeline of plugins to analyze or transform the text.
The plugin architecture is what makes retext powerful for content automation. Individual plugins handle specific concerns: retext-spell checks spelling against a dictionary, retext-readability evaluates text complexity using established formulas like Flesch-Kincaid, retext-equality flags potentially insensitive language, retext-simplify suggests simpler alternatives for complex phrases, and retext-smartypants converts straight quotes to curly quotes and handles other typographic niceties.
For AI agents and content pipelines, retext provides a programmatic way to enforce content quality standards. An agent writing blog posts can pipe output through retext to catch spelling errors, flag readability issues, and ensure consistent typography before publishing. This is different from grammar checkers in that retext operates at the AST level, allowing precise structural analysis of text rather than pattern matching on raw strings.
The unified.js integration means retext works alongside remark and rehype in content processing pipelines. You can parse a Markdown file with remark, bridge it to retext for natural language analysis using remark-retext, then continue processing with rehype for HTML output. This interoperability makes retext a natural fit for static site generators, CMS publishing workflows, and documentation pipelines.
Available on npm as the retext package (with individual plugins like retext-spell, retext-readability, retext-equality, retext-simplify as separate packages), the framework follows semantic versioning and maintains compatibility with current Node.js LTS releases. The project has been actively maintained since 2014 and is part of the broader unified.js organization that maintains over 500 packages.
Key use cases include automated content linting in CI pipelines, real-time writing feedback in editor plugins, bulk content quality audits across documentation repositories, and programmatic text transformation for publishing workflows. The AST-based approach means custom plugins can target specific text patterns with surgical precision.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/retext-natural-language-processor-unified-plugins/)
