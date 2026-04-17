---
title: "Redoc OpenAPI Documentation Renderer"
description: "Redoc is an open-source API documentation generator from Redocly that transforms OpenAPI 3.1, OpenAPI 3.0, and Swagger 2.0 specifications into responsive, three-panel reference documentation. With over 25,000 GitHub stars, an MIT license, and nearly one million weekly downloads on npm, Redoc is the most popular tool in its category — used by organizations like Docker, Zuora, Discourse, and Rebilly to power their public API documentation.\nThe tool produces a clean, responsive layout with three synchronized panels: a searchable navigation menu on the left, the main documentation content in the center, and request/response examples with code samples on the right. The panels stay synchronized as users scroll, providing a fluid reading experience. Redoc supports all OpenAPI features including nested schemas with expandable details, discriminators, oneOf/anyOf/allOf compositions, callback definitions, and webhook documentation. Code samples can be embedded using vendor extensions, and the x-tagGroups extension enables high-level grouping in the navigation menu.\nRedoc is distributed in three forms: a CLI tool for generating static HTML files, an HTML tag for embedding in any web page, and a React component for integration into React applications. The fastest way to generate documentation is with the Redocly CLI: npx @redocly/cli build-docs openapi.yaml produces a self-contained HTML file ready for deployment. For dynamic embedding, adding a single script tag and a  element to any HTML page renders the documentation inline. The React component accepts the spec as a prop and renders within your component tree.\nFor agent and developer tool workflows, Redoc enables automated documentation generation as part of CI/CD pipelines. Agents can generate or update OpenAPI specs programmatically, then run Redoc to produce up-to-date documentation without human intervention. The Redocly CLI extends beyond documentation generation to include OpenAPI linting, bundling, and spec validation, making it a comprehensive API lifecycle tool. The static HTML output requires no server-side rendering, making it trivial to deploy to any static hosting service, GitHub Pages, or CDN."
verification: security_reviewed
source: "https://github.com/Redocly/redoc"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "Redocly/redoc"
  github_stars: 25596
  ase_npm_package: "redoc"
  npm_weekly_downloads: 1482933
---

# Redoc OpenAPI Documentation Renderer

Redoc is an open-source API documentation generator from Redocly that transforms OpenAPI 3.1, OpenAPI 3.0, and Swagger 2.0 specifications into responsive, three-panel reference documentation. With over 25,000 GitHub stars, an MIT license, and nearly one million weekly downloads on npm, Redoc is the most popular tool in its category — used by organizations like Docker, Zuora, Discourse, and Rebilly to power their public API documentation.
The tool produces a clean, responsive layout with three synchronized panels: a searchable navigation menu on the left, the main documentation content in the center, and request/response examples with code samples on the right. The panels stay synchronized as users scroll, providing a fluid reading experience. Redoc supports all OpenAPI features including nested schemas with expandable details, discriminators, oneOf/anyOf/allOf compositions, callback definitions, and webhook documentation. Code samples can be embedded using vendor extensions, and the x-tagGroups extension enables high-level grouping in the navigation menu.
Redoc is distributed in three forms: a CLI tool for generating static HTML files, an HTML tag for embedding in any web page, and a React component for integration into React applications. The fastest way to generate documentation is with the Redocly CLI: npx @redocly/cli build-docs openapi.yaml produces a self-contained HTML file ready for deployment. For dynamic embedding, adding a single script tag and a  element to any HTML page renders the documentation inline. The React component accepts the spec as a prop and renders within your component tree.
For agent and developer tool workflows, Redoc enables automated documentation generation as part of CI/CD pipelines. Agents can generate or update OpenAPI specs programmatically, then run Redoc to produce up-to-date documentation without human intervention. The Redocly CLI extends beyond documentation generation to include OpenAPI linting, bundling, and spec validation, making it a comprehensive API lifecycle tool. The static HTML output requires no server-side rendering, making it trivial to deploy to any static hosting service, GitHub Pages, or CDN.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/redoc-openapi-documentation-renderer
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/redoc-openapi-documentation-renderer` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/redoc-openapi-documentation-renderer/)
