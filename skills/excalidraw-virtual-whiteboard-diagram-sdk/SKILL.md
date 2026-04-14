---
title: "Excalidraw Virtual Whiteboard and Diagram SDK"
description: "Excalidraw is an open-source virtual whiteboard for creating hand-drawn style diagrams, wireframes, and sketches. With 103k+ GitHub stars, it provides an infinite canvas, real-time collaboration, end-to-end encryption, and a React component library for embedding in custom applications."
verification: security_reviewed
source: "https://github.com/excalidraw/excalidraw"
category:
  - "Image &amp; Creative Automation"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "excalidraw/excalidraw"
  github_stars: 119886
---

# Excalidraw Virtual Whiteboard and Diagram SDK

Excalidraw is a free and open-source diagramming tool that produces drawings with a distinctive hand-drawn aesthetic. Unlike pixel-perfect diagramming tools, Excalidraw intentionally renders shapes with a sketchy, organic feel that makes diagrams feel approachable and easy to iterate on. The project has become one of the most popular open-source drawing tools with over 103,000 GitHub stars and adoption by companies including Google Cloud, Meta, Notion, and Replit.

Core Capabilities
The Excalidraw editor provides an infinite canvas with tools for rectangles, circles, diamonds, arrows, lines, free-draw, and text. Arrows automatically bind to shapes and support labels. The editor includes undo/redo, zoom, panning, dark mode, and export to PNG, SVG, and clipboard. Drawings are saved in an open JSON-based .excalidraw format that is human-readable and easy to diff in version control.

React Component Library
The @excalidraw/excalidraw npm package provides a fully customizable React component that can be embedded in any web application. Developers can control the initial scene, handle change events, customize the toolbar, add custom shape libraries, and integrate with their application state. The component supports localization with i18n and can be styled to match any design system.

Collaboration and PWA
The hosted version at excalidraw.com demonstrates real-time collaboration with end-to-end encryption, meaning the server never sees the contents of your drawings. It works as a Progressive Web App with full offline support and local-first storage. Shareable read-only links let you distribute diagrams without requiring recipients to have an account.

Shape Libraries
Excalidraw supports reusable shape libraries that can be shared and imported. The community has created libraries for UML diagrams, network architecture, UI components, icons, and more. Libraries are simple JSON files that can be hosted anywhere and loaded into any Excalidraw instance.

Agent Integration
AI agents can programmatically generate Excalidraw diagrams by constructing the JSON scene format, which specifies elements with positions, dimensions, and styling. Agents can create architecture diagrams, flowcharts, wireframes, or explanatory sketches and output them as .excalidraw files or rendered PNG/SVG images for documentation and communication.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/excalidraw-virtual-whiteboard-diagram-sdk/)
