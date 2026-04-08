---
title: Rive Runtime Animation Controller
description: The Rive Runtime Animation Controller manages interactive vector animations
  using the @rive-app/canvas-advanced package and Rive’s WASM runtime. It loads .riv
  files exported from the Rive editor, instantiates artboards, and drives state machine
  transitions by programmatically setting boolean, number, and trigger inputs via
  StateMachineInput objects. The agent handles multiple artboards within a single
  .riv file, synchronizes animation playback with application state (scroll position,
  user input, data changes), and manages the requestAnimationFrame render loop with
  proper cleanup. It supports Rive’s text runs for dynamic text content, mesh deformations
  for character animation, and Rive events (RiveEvent) for bidirectional communication
  between animation and host application. For React integration, it generates components
  using @rive-app/react-canvas with useRive and useStateMachineInput hooks. Performance
  optimization includes offscreen canvas rendering with transferToImageBitmap and
  Web Worker-based animation updates. Handles fallback to Lottie export for browsers
  without WASM support.
verification: security_reviewed
source: https://github.com/rive-app/rive-react
category:
- Image &amp; Creative Automation
framework:
- ChatGPT Agents
tool_ecosystem:
  github_repo: rive-app/rive-react
  github_stars: 1111
---

# Rive Runtime Animation Controller

The Rive Runtime Animation Controller manages interactive vector animations using the @rive-app/canvas-advanced package and Rive’s WASM runtime. It loads .riv files exported from the Rive editor, instantiates artboards, and drives state machine transitions by programmatically setting boolean, number, and trigger inputs via StateMachineInput objects. The agent handles multiple artboards within a single .riv file, synchronizes animation playback with application state (scroll position, user input, data changes), and manages the requestAnimationFrame render loop with proper cleanup. It supports Rive’s text runs for dynamic text content, mesh deformations for character animation, and Rive events (RiveEvent) for bidirectional communication between animation and host application. For React integration, it generates components using @rive-app/react-canvas with useRive and useStateMachineInput hooks. Performance optimization includes offscreen canvas rendering with transferToImageBitmap and Web Worker-based animation updates. Handles fallback to Lottie export for browsers without WASM support.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/rive-runtime-animation-controller/)
