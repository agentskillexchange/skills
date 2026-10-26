---
name: "Audit performance claims with Pstack benchmark-checklist"
slug: "audit-performance-claims-with-pstack-benchmark-checklist"
description: "Check tuning, bottlenecks, correctness, repeatability, and end-to-end relevance before an agent reports a measured speedup or regression."
github_stars: 2792
verification: "security_reviewed"
source: "https://github.com/backnotprop/pstack"
author: "Lauren Tan (Pstack upstream); backnotprop (standalone mirror)"
publisher_type: "community"
category: "Code Quality & Review"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "backnotprop/pstack"
  github_stars: 2792
---

# Audit performance claims with Pstack benchmark-checklist

Check tuning, bottlenecks, correctness, repeatability, and end-to-end relevance before an agent reports a measured speedup or regression.

## Prerequisites

Agent Skills-compatible coding agent; Node.js/npm for the documented skills installer; project benchmark harness; relevant runtime profiler and host diagnostics

## Installation

Install or set up from the source-backed instructions:

Run npx skills add backnotprop/pstack, select benchmark-checklist in the interactive skill list, then choose your supported agent. Explicitly invoke benchmark-checklist with the performance claim, measurement script, revisions, data and run evidence. The skill is documented as standalone. Inspected source commit: fad8d01588a1b1ae803f87c8a1e0de79e28cffec. Installer/runtime behavior was not exercised.

- Source: https://github.com/backnotprop/pstack

## Documentation

- https://github.com/backnotprop/pstack/blob/fad8d01588a1b1ae803f87c8a1e0de79e28cffec/skills/benchmark-checklist/SKILL.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/audit-performance-claims-with-pstack-benchmark-checklist/)
