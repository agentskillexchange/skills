---
name: Blender Geometry Nodes Script Generator
description: Generates Blender Python (bpy) scripts that programmatically create Geometry
  Nodes modifier trees, using the node_groups API and GeometryNodeTree interface for
  parametric 3D asset generation.
verification: security_reviewed
source: https://www.blender.org/
category:
- Image &amp; Creative Automation
framework:
- Custom Agents
---
# Blender Geometry Nodes Script Generator

The Blender Geometry Nodes Script Generator creates Python scripts using Blender's bpy.data.node_groups API to programmatically build Geometry Nodes modifier stacks. It translates natural language descriptions of parametric 3D operations into node tree configurations including Mesh Primitives, Curve operations, Instance on Points, Attribute nodes, and Math operations. The agent generates scripts compatible with Blender 4.x's GeometryNodeTree interface, handling socket connections via node_tree.links.new(), group inputs/outputs through the new panel-based interface, and custom attribute domains (POINT, FACE, CORNER, CURVE, INSTANCE). Scripts can be run headless via blender -background -python for batch asset generation in CI/CD pipelines. Supports common procedural workflows: scatter systems, boolean operations, mesh deformation, curve-to-mesh pipes, and volume-based erosion. Output scripts include proper node positioning with node.location tuples for readable graph layouts.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/blender-geometry-nodes-script-generator/)
