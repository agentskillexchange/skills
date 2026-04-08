---
title: Blender Geometry Nodes Script Generator
description: 'The Blender Geometry Nodes Script Generator creates Python scripts using
  Blender’s bpy.data.node_groups API to programmatically build Geometry Nodes modifier
  stacks. It translates natural language descriptions of parametric 3D operations
  into node tree configurations including Mesh Primitives, Curve operations, Instance
  on Points, Attribute nodes, and Math operations. The agent generates scripts compatible
  with Blender 4.x’s GeometryNodeTree interface, handling socket connections via node_tree.links.new(),
  group inputs/outputs through the new panel-based interface, and custom attribute
  domains (POINT, FACE, CORNER, CURVE, INSTANCE). Scripts can be run headless via
  blender –background –python for batch asset generation in CI/CD pipelines. Supports
  common procedural workflows: scatter systems, boolean operations, mesh deformation,
  curve-to-mesh pipes, and volume-based erosion. Output scripts include proper node
  positioning with node.location tuples for readable graph layouts.'
verification: security_reviewed
source: https://www.blender.org/
category:
- Image &amp; Creative Automation
framework:
- Custom Agents
---

# Blender Geometry Nodes Script Generator

The Blender Geometry Nodes Script Generator creates Python scripts using Blender’s bpy.data.node_groups API to programmatically build Geometry Nodes modifier stacks. It translates natural language descriptions of parametric 3D operations into node tree configurations including Mesh Primitives, Curve operations, Instance on Points, Attribute nodes, and Math operations. The agent generates scripts compatible with Blender 4.x’s GeometryNodeTree interface, handling socket connections via node_tree.links.new(), group inputs/outputs through the new panel-based interface, and custom attribute domains (POINT, FACE, CORNER, CURVE, INSTANCE). Scripts can be run headless via blender –background –python for batch asset generation in CI/CD pipelines. Supports common procedural workflows: scatter systems, boolean operations, mesh deformation, curve-to-mesh pipes, and volume-based erosion. Output scripts include proper node positioning with node.location tuples for readable graph layouts.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/blender-geometry-nodes-script-generator/)
