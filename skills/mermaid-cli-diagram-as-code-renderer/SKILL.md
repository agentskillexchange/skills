---
title: "Mermaid CLI Diagram-as-Code Renderer"
description: "Mermaid CLI (mmdc) is the command-line interface for the Mermaid diagramming library. It converts text-based diagram definitions into SVG, PNG, and PDF output files, enabling automated diagram generation from code."
verification: security_reviewed
source: "https://github.com/mermaid-js/mermaid-cli"
category:
  - "Image & Creative Automation"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "mermaid-js/mermaid-cli"
  github_stars: 4341
  license: "MIT"
---

# Mermaid CLI Diagram-as-Code Renderer

Mermaid CLI is the official command-line tool for the Mermaid diagramming library, maintained by the mermaid-js organization. It takes Mermaid definition files (.mmd) as input and generates SVG, PNG, or PDF files as output, making it ideal for automated documentation pipelines and CI/CD workflows.

Diagram Types Mermaid CLI supports rendering all Mermaid diagram types including flowcharts, sequence diagrams, class diagrams, state diagrams, entity-relationship diagrams, Gantt charts, pie charts, git graphs, user journey maps, and more. Diagrams are defined using a simple text-based syntax that can be version-controlled alongside code.

CLI Usage The primary command is mmdc, which accepts input files (-i), output files (-o), themes (-t), background colors (-b), and custom CSS (–cssFile). It supports batch processing, stdin piping, and Docker deployment. Common usage: mmdc -i input.mmd -o output.svg or mmdc -i input.mmd -o output.png -t dark -b transparent.

Markdown Integration Mermaid CLI can process Markdown files, automatically finding Mermaid code blocks within them, rendering each diagram to SVG files, and replacing the code blocks with image references in the output. This enables documentation workflows where diagrams are maintained as text within Markdown files.

Agent Integration Agents can use Mermaid CLI to programmatically generate architecture diagrams, flowcharts, sequence diagrams, and other visualizations from text descriptions. The tool can be installed via npm (npm install -g @mermaid-js/mermaid-cli) or run via Docker (docker pull minlag/mermaid-cli). Its text-based input format makes it straightforward for AI agents to generate diagram definitions and render them to image files.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/mermaid-cli-diagram-as-code-renderer
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/mermaid-cli-diagram-as-code-renderer` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/mermaid-cli-diagram-as-code-renderer/)
