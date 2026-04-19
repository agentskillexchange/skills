---
title: "Mermaid CLI Diagram-as-Code Renderer"
description: "Mermaid CLI is the official command-line tool for the Mermaid diagramming library, maintained by the mermaid-js organization. It takes Mermaid definition files (.mmd) as input and generates SVG, PNG, or PDF files as output, making it ideal for automated documentation pipelines and CI/CD workflows. Diagram Types Mermaid CLI supports rendering all Mermaid diagram types including flowcharts, sequence diagrams, class diagrams, state diagrams, entity-relationship diagrams, Gantt charts, pie charts, git graphs, user journey maps, and more. Diagrams are defined using a simple text-based syntax that can be version-controlled alongside code. CLI Usage The primary command is mmdc, which accepts input files (-i), output files (-o), themes (-t), background colors (-b), and custom CSS (&#8211;cssFile). It supports batch processing, stdin piping, and Docker deployment. Common usage: mmdc -i input.mmd -o output.svg or mmdc -i input.mmd -o output.png -t dark -b transparent . Markdown Integration Mermaid CLI can process Markdown files, automatically finding Mermaid code blocks within them, rendering each diagram to SVG files, and replacing the code blocks with image references in the output. This enables documentation workflows where diagrams are maintained as text within Markdown files. Agent Integration Agents can use Mermaid CLI to programmatically generate architecture diagrams, flowcharts, sequence diagrams, and other visualizations from text descriptions. The tool can be installed via npm (npm install -g @mermaid-js/mermaid-cli) or run via Docker (docker pull minlag/mermaid-cli). Its text-based input format makes it straightforward for AI agents to generate diagram definitions and render them to image files."
source: "https://github.com/mermaid-js/mermaid-cli"
verification: "security_reviewed"
category:
  - "Image &amp; Creative Automation"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "mermaid-js/mermaid-cli"
  github_stars: 4341
---

# Mermaid CLI Diagram-as-Code Renderer

Mermaid CLI is the official command-line tool for the Mermaid diagramming library, maintained by the mermaid-js organization. It takes Mermaid definition files (.mmd) as input and generates SVG, PNG, or PDF files as output, making it ideal for automated documentation pipelines and CI/CD workflows. Diagram Types Mermaid CLI supports rendering all Mermaid diagram types including flowcharts, sequence diagrams, class diagrams, state diagrams, entity-relationship diagrams, Gantt charts, pie charts, git graphs, user journey maps, and more. Diagrams are defined using a simple text-based syntax that can be version-controlled alongside code. CLI Usage The primary command is mmdc, which accepts input files (-i), output files (-o), themes (-t), background colors (-b), and custom CSS (&#8211;cssFile). It supports batch processing, stdin piping, and Docker deployment. Common usage: mmdc -i input.mmd -o output.svg or mmdc -i input.mmd -o output.png -t dark -b transparent . Markdown Integration Mermaid CLI can process Markdown files, automatically finding Mermaid code blocks within them, rendering each diagram to SVG files, and replacing the code blocks with image references in the output. This enables documentation workflows where diagrams are maintained as text within Markdown files. Agent Integration Agents can use Mermaid CLI to programmatically generate architecture diagrams, flowcharts, sequence diagrams, and other visualizations from text descriptions. The tool can be installed via npm (npm install -g @mermaid-js/mermaid-cli) or run via Docker (docker pull minlag/mermaid-cli). Its text-based input format makes it straightforward for AI agents to generate diagram definitions and render them to image files.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/mermaid-cli-diagram-as-code-renderer/)
