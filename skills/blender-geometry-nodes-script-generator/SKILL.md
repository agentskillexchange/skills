---
name: "Blender Geometry Nodes Script Generator"
description: "Generates Blender Python (bpy) scripts that programmatically create Geometry Nodes modifier trees, using the node_groups API and GeometryNodeTree interface for parametric 3D asset generation."
category: "Image & Creative Automation"
framework: "Custom Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/blender-geometry-nodes-script-generator/"
---

# Blender Geometry Nodes Script Generator

Generates Blender Python (bpy) scripts that programmatically create Geometry Nodes modifier trees, using the node_groups API and GeometryNodeTree interface for parametric 3D asset generation.

## Overview

The Blender Geometry Nodes Script Generator creates Python scripts using Blender’s bpy.data.node_groups API to programmatically build Geometry Nodes modifier stacks. It translates natural language descriptions of parametric 3D operations into node tree configurations including Mesh Primitives, Curve operations, Instance on Points, Attribute nodes, and Math operations. The agent generates scripts compatible with Blender 4.x’s GeometryNodeTree interface, handling socket connections via node_tree.links.new(), group inputs/outputs through the new panel-based interface, and custom attribute domains (POINT, FACE, CORNER, CURVE, INSTANCE). Scripts can be run headless via blender –background –python for batch asset generation in CI/CD pipelines. Supports common procedural workflows: scatter systems, boolean operations, mesh deformation, curve-to-mesh pipes, and volume-based erosion. Output scripts include proper node positioning with node.location tuples for readable graph layouts.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill blender-geometry-nodes-script-generator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill blender-geometry-nodes-script-generator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill blender-geometry-nodes-script-generator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill blender-geometry-nodes-script-generator -a codex
```

### OpenClaw

```bash
clawhub install blender-geometry-nodes-script-generator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/blender-geometry-nodes-script-generator/
