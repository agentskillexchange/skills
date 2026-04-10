---
title: "Mermaid CLI Diagram-as-Code Renderer"
description: "Mermaid CLI (mmdc) is the command-line interface for the Mermaid diagramming library. It converts text-based diagram definitions into SVG, PNG, and PDF output files, enabling automated diagram generation from code."
slug: "mermaid-cli-diagram-as-code-renderer"
category:
  - "Image &amp; Creative Automation"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/mermaid-js/mermaid-cli"
tool_ecosystem:
  github_repo: "mermaid-js/mermaid-cli"
  github_stars: 4341
listed: true
---

# Mermaid CLI Diagram-as-Code Renderer

Mermaid CLI (mmdc) is the command-line interface for the Mermaid diagramming library. It converts text-based diagram definitions into SVG, PNG, and PDF output files, enabling automated diagram generation from code.

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
clawhub install mermaid-cli-diagram-as-code-renderer
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Mermaid CLI is the official command-line tool for the Mermaid diagramming library, maintained by the mermaid-js organization. It takes Mermaid definition files (.mmd) as input and generates SVG, PNG, or PDF files as output, making it ideal for automated documentation pipelines and CI/CD workflows.
Diagram Types
Mermaid CLI supports rendering all Mermaid diagram types including flowcharts, sequence diagrams, class diagrams, state diagrams, entity-relationship diagrams, Gantt charts, pie charts, git graphs, user journey maps, and more. Diagrams are defined using a simple text-based syntax that can be version-controlled alongside code.
CLI Usage
The primary command is mmdc, which accepts input files (-i), output files (-o), themes (-t), background colors (-b), and custom CSS (–cssFile). It supports batch processing, stdin piping, and Docker deployment. Common usage: mmdc -i input.mmd -o output.svg or mmdc -i input.mmd -o output.png -t dark -b transparent.
Markdown Integration
Mermaid CLI can process Markdown files, automatically finding Mermaid code blocks within them, rendering each diagram to SVG files, and replacing the code blocks with image references in the output. This enables documentation workflows where diagrams are maintained as text within Markdown files.
Agent Integration
Agents can use Mermaid CLI to programmatically generate architecture diagrams, flowcharts, sequence diagrams, and other visualizations from text descriptions. The tool can be installed via npm (npm install -g @mermaid-js/mermaid-cli) or run via Docker (docker pull minlag/mermaid-cli). Its text-based input format makes it straightforward for AI agents to generate diagram definitions and render them to image files.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/mermaid-cli-diagram-as-code-renderer/)
