---
title: "Blender Geometry Nodes Script Generator"
description: "Generates Blender Python (bpy) scripts that programmatically create Geometry Nodes modifier trees, using the node_groups API and GeometryNodeTree interface for parametric 3D asset generation."
verification: security_reviewed
source: "https://www.blender.org/"
category:
  - "Image & Creative Automation"
framework:
  - "Custom Agents"
---

# Blender Geometry Nodes Script Generator

The Blender Geometry Nodes Script Generator creates Python scripts using Blender’s bpy.data.node_groups API to programmatically build Geometry Nodes modifier stacks. It translates natural language descriptions of parametric 3D operations into node tree configurations including Mesh Primitives, Curve operations, Instance on Points, Attribute nodes, and Math operations. The agent generates scripts compatible with Blender 4.x’s GeometryNodeTree interface, handling socket connections via node_tree.links.new(), group inputs/outputs through the new panel-based interface, and custom attribute domains (POINT, FACE, CORNER, CURVE, INSTANCE). Scripts can be run headless via blender –background –python for batch asset generation in CI/CD pipelines. Supports common procedural workflows: scatter systems, boolean operations, mesh deformation, curve-to-mesh pipes, and volume-based erosion. Output scripts include proper node positioning with node.location tuples for readable graph layouts.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/blender-geometry-nodes-script-generator
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/blender-geometry-nodes-script-generator` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/blender-geometry-nodes-script-generator/)
