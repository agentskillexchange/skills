---
name: Bubble Tea Go TUI Framework by Charmbracelet
description: Bubble Tea is a powerful Go framework for building terminal user interfaces
  based on The Elm Architecture. Developed by Charmbracelet, it supports inline, full-window,
  and mixed TUI applications with a high-performance cell-based renderer and declarative
  views.
verification: security_reviewed
source: https://github.com/charmbracelet/bubbletea
category:
- Library &amp; API Reference
framework:
- Multi-Framework
tool_ecosystem:
  github_repo: charmbracelet/bubbletea
  github_stars: 41168
  license: MIT
---
# Bubble Tea Go TUI Framework by Charmbracelet

Bubble Tea is a Go framework for building terminal user interfaces (TUIs) based on The Elm Architecture. Developed and maintained by Charmbracelet, the same team behind Glow, Freeze, VHS, and other popular terminal tools, Bubble Tea provides a functional and stateful approach to building both simple and complex terminal applications.
Architecture and Model
Bubble Tea follows The Elm Architecture pattern with three core concepts: a Model that holds application state, an Update function that handles messages and updates state, and a View function that renders the UI from the current state. This functional approach makes TUI development predictable and testable. The framework handles the event loop, input processing, and rendering lifecycle automatically.
Rendering and Performance
Bubble Tea includes a high-performance cell-based renderer that efficiently updates only changed portions of the terminal screen. It features built-in color downsampling for terminal compatibility, native clipboard support, and high-fidelity keyboard and mouse handling. The renderer supports both inline rendering (within existing terminal output) and full-window alternate screen mode.
Component Ecosystem
The companion library Bubbles provides pre-built UI components including text inputs, text areas, spinners, lists, tables, file pickers, progress bars, timers, stopwatches, paginated views, viewports, and help displays. Lip Gloss, another Charmbracelet library, handles styling with CSS-like syntax for colors, borders, padding, and layout.
Agent Integration
AI agents building CLI tools can use Bubble Tea to create interactive terminal interfaces for their applications. The framework is particularly useful for building dashboards, configuration wizards, interactive selectors, and real-time monitoring displays. Agents can programmatically compose Bubble Tea components to generate rich terminal UIs that go beyond simple text output.
Installation
Install via Go modules: go get charm.land/bubbletea/v2. Bubble Tea requires Go 1.18+ and works on Linux, macOS, and Windows. The framework is MIT licensed with over 41,000 GitHub stars and active daily development.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/bubble-tea-go-tui-framework/)
