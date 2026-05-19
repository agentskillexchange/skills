---
name: "Implement, review, and optimize SwiftUI code with trace-backed diagnostics"
slug: "implement-review-and-optimize-swiftui-code-with-trace-backed-diagnostics"
description: "Guide SwiftUI implementation and refactoring with current Apple patterns, then analyze Instruments traces to diagnose hangs, hitches, and expensive view updates."
verification: "security_reviewed"
source: "https://github.com/AvdLee/SwiftUI-Agent-Skill/tree/main/swiftui-expert-skill"
author: "Antoine van der Lee"
publisher_type: "individual"
category: "Library & API Reference"
framework: "Custom Agents"
---

# Implement, review, and optimize SwiftUI code with trace-backed diagnostics

Guide SwiftUI implementation and refactoring with current Apple patterns, then analyze Instruments traces to diagnose hangs, hitches, and expensive view updates.

## Prerequisites

Xcode Instruments traces; SwiftUI source files; custom skill-capable agent client

## Installation

Use the upstream install or setup path that matches your environment:
- npx skills add https://github.com/avdlee/swiftui-agent-skill --skill swiftui-expert-skill

Requirements and caveats from upstream:
- Unlike the other reference files — which are text guidance — this part of the skill ships an executable Python toolchain that wraps xctrace. It lets the agent **record** a new .trace and **analyse** an existing one en...
- scripts/instruments_parser/ — one module per lane (time_profiler, hangs, hitches, swiftui, causes), plus cross-lane correlate and a markdown summary renderer. Pure stdlib Python 3; only external dep is xctrace (ships...
- Use this skill after new iOS or Xcode releases to refresh the deprecated API reference. It requires the [Sosumi MCP](https://github.com/NSHipster/sosumi.ai) to be available. See AGENTS.md or CONTRIBUTING.md for details.

Basic usage or getting-started notes:
- bash
- For more information, [visit the skills.sh platform page](https://skills.sh/avdlee/swiftui-agent-skill/swiftui-expert-skill).
- Then use the skill in your AI agent, for example:

- Source: https://github.com/AvdLee/SwiftUI-Agent-Skill/tree/main/swiftui-expert-skill
- Extracted from upstream docs: https://raw.githubusercontent.com/AvdLee/SwiftUI-Agent-Skill/HEAD/README.md

## Documentation

- https://github.com/AvdLee/SwiftUI-Agent-Skill

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/implement-review-and-optimize-swiftui-code-with-trace-backed-diagnostics/)
