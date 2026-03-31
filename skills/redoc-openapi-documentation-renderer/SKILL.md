---
name: "Redoc OpenAPI Documentation Renderer"
description: "Redoc is an open-source tool by Redocly for generating beautiful, three-panel API reference documentation from OpenAPI specifications. With 25,000+ GitHub stars and nearly 1 million weekly npm downloads, it is the most widely used API documentation renderer."
category: "Library & API Reference"
framework: "Claude Code"
verification: security_reviewed
source: "https://github.com/Redocly/redoc"
---
# Redoc OpenAPI Documentation Renderer

Redoc is an open-source tool by Redocly for generating beautiful, three-panel API reference documentation from OpenAPI specifications. With 25,000+ GitHub stars and nearly 1 million weekly npm downloads, it is the most widely used API documentation renderer.

## Overview

Redoc is an open-source API documentation generator from Redocly that transforms OpenAPI 3.1, OpenAPI 3.0, and Swagger 2.0 specifications into responsive, three-panel reference documentation. With over 25,000 GitHub stars, an MIT license, and nearly one million weekly downloads on npm, Redoc is the most popular tool in its category — used by organizations like Docker, Zuora, Discourse, and Rebilly to power their public API documentation.

The tool produces a clean, responsive layout with three synchronized panels: a searchable navigation menu on the left, the main documentation content in the center, and request/response examples with code samples on the right. The panels stay synchronized as users scroll, providing a fluid reading experience. Redoc supports all OpenAPI features including nested schemas with expandable details, discriminators, oneOf/anyOf/allOf compositions, callback definitions, and webhook documentation. Code samples can be embedded using vendor extensions, and the x-tagGroups extension enables high-level grouping in the navigation menu.

Redoc is distributed in three forms: a CLI tool for generating static HTML files, an HTML tag for embedding in any web page, and a React component for integration into React applications. The fastest way to generate documentation is with the Redocly CLI: `npx @redocly/cli build-docs openapi.yaml` produces a self-contained HTML file ready for deployment. For dynamic embedding, adding a single script tag and a `<redoc>` element to any HTML page renders the documentation inline. The React component accepts the spec as a prop and renders within your component tree.

For agent and developer tool workflows, Redoc enables automated documentation generation as part of CI/CD pipelines. Agents can generate or update OpenAPI specs programmatically, then run Redoc to produce up-to-date documentation without human intervention. The Redocly CLI extends beyond documentation generation to include OpenAPI linting, bundling, and spec validation, making it a comprehensive API lifecycle tool. The static HTML output requires no server-side rendering, making it trivial to deploy to any static hosting service, GitHub Pages, or CDN.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill redoc-openapi-documentation-renderer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill redoc-openapi-documentation-renderer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill redoc-openapi-documentation-renderer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill redoc-openapi-documentation-renderer -a codex
```

### OpenClaw

```bash
clawhub install redoc-openapi-documentation-renderer
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/redoc-openapi-documentation-renderer/)
