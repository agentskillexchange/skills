---
name: "Penrose Mathematical Diagram Generator from Plain Text Notation"
description: "Penrose is an open-source platform that creates beautiful mathematical and scientific diagrams from plain text notation. Define domain concepts, write substance programs, and apply style rules to generate publication-quality SVG visualizations automatically."
verification: security_reviewed
source: "https://github.com/penrose/penrose"
category:
  - "Image &amp; Creative Automation"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "penrose/penrose"
  github_stars: 7933
---

# Penrose Mathematical Diagram Generator from Plain Text Notation

Penrose is an open-source diagramming platform developed at Carnegie Mellon University that lets users create beautiful, mathematically precise diagrams by typing plain text notation. Instead of manually positioning shapes and lines in a visual editor, you describe what you want to visualize and Penrose figures out how to lay it out. The system uses optimization-based layout algorithms to produce publication-quality SVG output suitable for research papers, textbooks, and educational materials.
The Three-Program Architecture
Penrose uses a unique trio of programs to separate concerns: Domain (.domain) files declare the types and predicates in your mathematical domain (e.g., sets, functions, vectors). Substance (.substance) files describe the specific objects and relationships you want to visualize (e.g., &#8220;Set A is a subset of Set B&#8221;). Style (.style) files map domain concepts to visual representations (e.g., &#8220;render Sets as circles, Subset as containment&#8221;). This separation means one style can be applied to many different substance programs, or one substance program can be visualized in multiple styles.
Supported Domains
Penrose ships with built-in domain definitions for set theory (Euler/Venn diagrams), linear algebra (vectors, matrices, transformations), graph theory, geometry, mesh/simplicial complexes, and more. The domain language is extensible — researchers can define custom types, functions, predicates, and constructors for any mathematical or scientific domain they work in. Community-contributed domains cover category theory, topology, and combinatorics.
Optimization-Based Layout
Unlike template-based diagramming tools, Penrose uses numerical optimization to find layouts that satisfy both hard constraints (containment, disjointness, alignment) and soft objectives (aesthetics, label placement, spacing). This means diagrams adapt automatically to the complexity of the input — add more objects and the layout adjusts without manual intervention. The optimizer supports multiple random seeds, generating different valid layouts from which users can pick the most appealing.
Integration and Usage
Penrose is available as an npm package (@penrose/core) for programmatic use in JavaScript and TypeScript applications. The @penrose/editor package provides a web-based IDE with live preview. There is also an online playground at penrose.cs.cmu.edu/try where users can experiment without installation. For batch generation, the @penrose/roger CLI compiles Penrose programs to SVG files from the command line, making it suitable for CI/CD pipelines and automated documentation workflows.
Research and Community
Penrose has been published at top venues including SIGGRAPH and featured in multiple research papers on mathematical visualization. The project is actively maintained with regular releases and an active Discord community. It is licensed under MIT and welcomes contributions of new domains, styles, and core improvements.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/penrose-math-diagram-generator/)
