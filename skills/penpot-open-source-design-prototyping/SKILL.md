---
name: "Penpot Open Source Design and Prototyping Platform"
description: "Penpot is the first open-source design and prototyping platform built for cross-domain teams. Designers create visual layouts, interactive prototypes, and scalable design systems while developers get ready-to-use CSS, SVG, and HTML code — no handoff friction, no vendor lock-in."
verification: security_reviewed
source: "https://github.com/penpot/penpot"
category:
  - "Image &amp; Creative Automation"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "penpot/penpot"
  github_stars: 45224
---

# Penpot Open Source Design and Prototyping Platform

What Penpot Does
Penpot is a browser-based, self-hostable design tool that works entirely with open web standards. Unlike Figma or Sketch, every design you create in Penpot is stored as SVG, CSS, and HTML — formats that developers already understand and can consume directly. The platform supports real-time collaboration, interactive prototyping, component libraries, and as of version 2.0, native CSS Grid Layout.
Why It Matters for Agents
Penpot exposes a REST API and supports webhooks, making it possible to integrate design workflows into automated pipelines. An agent can trigger exports, read component metadata, or sync design tokens between Penpot and a codebase. The open-standards approach means extracted assets need no proprietary conversion step — SVG and CSS go straight into version control.
Key Features

Open standards: SVG, CSS, HTML, and JSON throughout — no proprietary file formats
Design tokens: Native design token support for maintaining consistency across design and code
CSS Grid Layout: The first design tool with native CSS Grid, introduced in Penpot 2.0
Components and variants: Reusable component system with variants for scalable design systems
Real-time collaboration: Multi-user editing with shared workspaces
Self-hostable: Deploy via Docker, Kubernetes, or use the hosted SaaS at design.penpot.app
Plugin ecosystem: Extensible via Penpot plugins for custom workflows
API and webhooks: REST API with access tokens for programmatic integration

Integration Points
Penpot fits into design-to-code pipelines, design system management, and collaborative prototyping workflows. The inspect tab provides developers with ready-to-use CSS and SVG output. Webhooks enable event-driven automation — for example, triggering a CI pipeline when a component library is updated. The API supports token-based authentication for headless access to project data and exports.
Install Notes
Use the hosted SaaS at design.penpot.app or self-host with Docker: docker compose -p penpot -f docker-compose.yaml up -d. Detailed self-hosting instructions for Docker, Kubernetes, and Elestio are available at penpot.app/self-host. Requires no external dependencies beyond a browser for the SaaS version.
Source: github.com/penpot/penpot

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/penpot-open-source-design-prototyping/)
