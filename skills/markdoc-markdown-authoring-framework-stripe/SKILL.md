---
name: Markdoc Markdown-Based Authoring Framework by Stripe
description: Markdoc is a powerful Markdown-based authoring framework created by Stripe
  to power their public documentation. It extends Markdown with custom tags, functions,
  and variables for building structured documentation sites and content experiences.
verification: security_reviewed
source: https://github.com/markdoc/markdoc
category:
- Content Writing &amp; SEO
framework:
- Multi-Framework
tool_ecosystem:
  github_repo: markdoc/markdoc
  github_stars: 7949
  license: MIT
---
# Markdoc Markdown-Based Authoring Framework by Stripe

Markdoc is an open-source, Markdown-based document authoring framework built and maintained by Stripe. Originally created to power Stripe's public documentation, Markdoc extends standard Markdown with a tag syntax, variables, functions, and schema validation, turning Markdown into a full content authoring system.
Core Capabilities
Markdoc processes documents through a three-stage pipeline: parse (Markdown to AST), transform (apply tags, functions, and schema), and render (output to React, HTML, or any target). The tag syntax uses {% tag %} delimiters to embed custom components directly in Markdown content. Markdoc validates content against schemas at build time, catching errors like missing required attributes or invalid nesting before deployment.
Custom Tags and Functions
Tags map directly to renderable components. A tag like {% callout type="warning" %} can render as a styled alert component in React or a <div> in HTML. Functions provide computed values within documents — date formatting, conditional display, string manipulation. Variables inject external data (API versions, config values) into documents at build time. All of these are defined in a schema that validates and transforms the AST.
Agent Integration
AI agents can use Markdoc to generate structured documentation from code, API specs, or data sources. The @markdoc/markdoc npm package provides parse, transform, and render functions that agents can call programmatically in Node.js. Agents can define custom tag schemas, write Markdoc content with embedded components, and render to React or static HTML. The schema validation catches content errors automatically, making agent-generated docs reliable. Markdoc integrates with Next.js, React, and any JavaScript framework.
Installation
Install with npm: npm install @markdoc/markdoc. For Next.js integration, add @markdoc/next.js. Full documentation is at markdoc.dev/docs. The project is licensed under MIT.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/markdoc-markdown-authoring-framework-stripe/)
