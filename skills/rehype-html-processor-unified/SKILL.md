---
name: "rehype Plugin-Based HTML Processor by the Unified Collective"
description: "rehype is a plugin-based HTML processing toolkit built on the unified ecosystem. It parses HTML into an abstract syntax tree, transforms it with composable plugins, and serializes it back — enabling programmatic HTML minification, sanitization, link rewriting, heading extraction, and content manipulation at scale."
category: "Data Extraction &amp; Transformation"
framework: "Multi-Framework"
verification: security_reviewed
source: "https://github.com/rehypejs/rehype"
---
# rehype Plugin-Based HTML Processor by the Unified Collective

rehype is a plugin-based HTML processing toolkit built on the unified ecosystem. It parses HTML into an abstract syntax tree, transforms it with composable plugins, and serializes it back — enabling programmatic HTML minification, sanitization, link rewriting, heading extraction, and content manipulation at scale.

rehype is an open-source HTML processor maintained by the unified collective, a family of over 300 projects with a combined 69,000+ GitHub stars. rehype itself has 2,200+ stars and serves as the HTML arm of the unified ecosystem, sitting alongside remark (Markdown) and retext (natural language).

What It Does

rehype parses HTML into a hast (Hypertext Abstract Syntax Tree), passes it through a pipeline of plugins that inspect and transform the tree, then serializes it back to HTML. This architecture lets you compose any combination of HTML transformations — minification, sanitization, link rewriting, heading ID injection, table of contents generation, syntax highlighting, accessibility improvements, and more — in a single predictable pipeline.

Core Packages

The monorepo contains three core packages: rehype-parse (HTML to hast), rehype-stringify (hast to HTML), and rehype (both combined with unified). Dozens of official and community plugins extend the pipeline: rehype-minify for HTML minification, rehype-sanitize for XSS-safe HTML filtering, rehype-autolink-headings for anchor link injection, rehype-slug for heading ID generation, rehype-highlight for code syntax highlighting, and rehype-format for pretty-printing.

How Agents Use It

AI agents working with web content benefit from rehype in several ways. When processing scraped HTML, an agent can use rehype-sanitize to strip dangerous elements before analysis. For content publishing pipelines, agents can use remark-rehype to convert Markdown to HTML, then apply rehype plugins for minification, link rewriting, and SEO enhancements. Agents building documentation sites can extract headings, generate tables of contents, and inject navigation links programmatically.

Integration Points

rehype bridges seamlessly with the rest of the unified ecosystem. Use remark-rehype to convert Markdown ASTs to HTML ASTs, or rehype-remark to go the other direction. The unified API is consistent across all processors, so learning rehype means you already know how to use remark for Markdown and retext for prose. The ecosystem works in Node.js, Deno, browsers, and any JavaScript runtime.

Installation

Install via npm: npm install rehype rehype-parse rehype-stringify unified. Add plugins as needed: npm install rehype-sanitize rehype-minify rehype-autolink-headings.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill rehype-html-processor-unified
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill rehype-html-processor-unified -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill rehype-html-processor-unified -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill rehype-html-processor-unified -a codex
```

### OpenClaw

```bash
clawhub install rehype-html-processor-unified
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/rehype-html-processor-unified/)
