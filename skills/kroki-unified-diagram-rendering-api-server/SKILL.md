---
title: "Kroki Unified Diagram Rendering API and Server"
description: "Kroki provides a unified HTTP API that converts textual diagram descriptions into images. It supports over 25 diagram libraries including PlantUML, Mermaid, GraphViz, D2, Excalidraw, and more through a single self-hostable service."
slug: "kroki-unified-diagram-rendering-api-server"
category:
  - "Image &amp; Creative Automation"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/yuzutech/kroki"
listed: true
---

# Kroki Unified Diagram Rendering API and Server

Kroki provides a unified HTTP API that converts textual diagram descriptions into images. It supports over 25 diagram libraries including PlantUML, Mermaid, GraphViz, D2, Excalidraw, and more through a single self-hostable service.

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
clawhub install kroki-unified-diagram-rendering-api-server
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Kroki is an open-source diagram rendering service that provides a single unified API for converting text-based diagram descriptions into SVG, PNG, and PDF images. Instead of installing and configuring each diagramming tool individually, Kroki acts as a gateway that routes requests to the appropriate rendering engine behind a consistent HTTP interface.
Supported Diagram Libraries
Kroki supports over 25 diagramming formats through its unified API, including BlockDiag, BPMN, Bytefield, C4 (via PlantUML), D2, DBML, Ditaa, Erd, Excalidraw, GoAT, GraphViz, Mermaid, Nomnoml, Pikchr, PlantUML, SvgBob, Symbolator, UMLet, Vega, Vega-Lite, WaveDrom, and WireViz. Each library runs in its own container or process, and Kroki handles the routing and format negotiation.
How It Works
Diagrams can be submitted via GET requests with the source encoded in the URL (deflate + base64), or via POST requests with the diagram source as JSON or plain text. The output format is specified through the URL path or Accept header. This makes integration straightforward from documentation pipelines, CI/CD systems, wikis, and any HTTP client.
Deployment and Integration
Kroki is distributed as Docker images. The core server (yuzutech/kroki) handles most diagram types natively, while companion containers provide Mermaid, BPMN, Excalidraw, and diagrams.net support. A docker-compose configuration brings up the full stack with a single command. The public instance at kroki.io is available for evaluation, but self-hosting is recommended for production use.
Agent Integration Points
Agents can use Kroki to programmatically generate architecture diagrams, sequence diagrams, flowcharts, entity-relationship diagrams, and network topologies from code or structured data. The HTTP API makes it easy to embed diagram generation into documentation workflows, pull request previews, or monitoring dashboards. The text-based input format means diagrams can be version-controlled alongside code.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kroki-unified-diagram-rendering-api-server/)
