---
title: "Implement, review, and optimize SwiftUI code with trace-backed diagnostics"
description: "Guide SwiftUI implementation and refactoring with current Apple patterns, then analyze Instruments traces to diagnose hangs, hitches, and expensive view updates."
verification: "security_reviewed"
source: "https://github.com/AvdLee/SwiftUI-Agent-Skill/tree/main/swiftui-expert-skill"
category:
  - "Library & API Reference"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "avdlee/swiftui-agent-skill"
  github_stars: 2661
---

# Implement, review, and optimize SwiftUI code with trace-backed diagnostics

This skill gives an agent a concrete SwiftUI operator workflow instead of a generic Apple or SwiftUI listing. The agent reviews existing SwiftUI code, routes issues through topic-specific references, flags deprecated APIs, suggests targeted refactors, and can move into trace-driven diagnosis when the user provides or records an Instruments .trace file. The upstream skill includes explicit guidance for state management, view composition, performance, accessibility, iOS 26+ gating, and trace analysis. Use this when the user wants help implementing or refactoring SwiftUI code, reviewing architecture and performance decisions, or diagnosing runtime issues from Instruments traces. This is the right invocation shape when the user wants agent-guided code review and evidence-backed performance diagnosis rather than simply consulting SwiftUI docs or using Xcode normally. The scope boundary is sharp: this is not a plain SwiftUI framework card. It is a workflow skill for code review, optimization, and trace-based diagnosis with explicit steps, references, and performance-analysis procedures.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/implement-review-and-optimize-swiftui-code-with-trace-backed-diagnostics/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/implement-review-and-optimize-swiftui-code-with-trace-backed-diagnostics
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/implement-review-and-optimize-swiftui-code-with-trace-backed-diagnostics`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/implement-review-and-optimize-swiftui-code-with-trace-backed-diagnostics/)
