---
title: "Blender Geometry Nodes Script Generator"
description: "The Blender Geometry Nodes Script Generator creates Python scripts using Blender&#8217;s bpy.data.node_groups API to programmatically build Geometry Nodes modifier stacks. It translates natural language descriptions of parametric 3D operations into node tree configurations including Mesh Primitives, Curve operations, Instance on Points, Attribute nodes, and Math operations. The agent generates scripts compatible with Blender 4.x&#8217;s GeometryNodeTree interface, handling socket connections via node_tree.links.new(), group inputs/outputs through the new panel-based interface, and custom attribute domains (POINT, FACE, CORNER, CURVE, INSTANCE). Scripts can be run headless via blender &#8211;background &#8211;python for batch asset generation in CI/CD pipelines. Supports common procedural workflows: scatter systems, boolean operations, mesh deformation, curve-to-mesh pipes, and volume-based erosion. Output scripts include proper node positioning with node.location tuples for readable graph layouts."
source: "https://www.blender.org/"
verification: "security_reviewed"
category:
  - "Image &amp; Creative Automation"
framework:
  - "Custom Agents"
---

# Blender Geometry Nodes Script Generator

The Blender Geometry Nodes Script Generator creates Python scripts using Blender&#8217;s bpy.data.node_groups API to programmatically build Geometry Nodes modifier stacks. It translates natural language descriptions of parametric 3D operations into node tree configurations including Mesh Primitives, Curve operations, Instance on Points, Attribute nodes, and Math operations. The agent generates scripts compatible with Blender 4.x&#8217;s GeometryNodeTree interface, handling socket connections via node_tree.links.new(), group inputs/outputs through the new panel-based interface, and custom attribute domains (POINT, FACE, CORNER, CURVE, INSTANCE). Scripts can be run headless via blender &#8211;background &#8211;python for batch asset generation in CI/CD pipelines. Supports common procedural workflows: scatter systems, boolean operations, mesh deformation, curve-to-mesh pipes, and volume-based erosion. Output scripts include proper node positioning with node.location tuples for readable graph layouts.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/blender-geometry-nodes-script-generator/)
