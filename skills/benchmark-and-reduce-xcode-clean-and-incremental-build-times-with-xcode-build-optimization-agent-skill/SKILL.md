---
name: "Benchmark and reduce Xcode clean and incremental build times with Xcode Build Optimization Agent Skill"
slug: "benchmark-and-reduce-xcode-clean-and-incremental-build-times-with-xcode-build-optimization-agent-skill"
description: "Benchmark clean and incremental Xcode builds, surface compile and configuration hotspots, and produce an approval-first optimization plan before changing project files."
github_stars: 981
verification: "listed"
source: "https://github.com/AvdLee/Xcode-Build-Optimization-Agent-Skill"
author: "Antoine van der Lee"
publisher_type: "open_source_project"
category: "Code Quality & Review"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "AvdLee/Xcode-Build-Optimization-Agent-Skill"
  github_stars: 981
---

# Benchmark and reduce Xcode clean and incremental build times with Xcode Build Optimization Agent Skill

Benchmark clean and incremental Xcode builds, surface compile and configuration hotspots, and produce an approval-first optimization plan before changing project files.

## Prerequisites

Xcode project, AI coding tool with Agent Skills support, Xcode build tooling, optional Swift Package Manager context

## Installation

Use the upstream install or setup path that matches your environment:
- npx skills add https://github.com/avdlee/xcode-build-optimization-agent-skill
- npx skills add https://github.com/avdlee/xcode-build-optimization-agent-skill --skill xcode-project-analyzer

Requirements and caveats from upstream:
- Available individual skills: xcode-build-benchmark, xcode-compilation-analyzer, xcode-project-analyzer, spm-build-analysis, xcode-build-orchestrator, xcode-build-fixer. Note that the orchestrator requires all other sk...

Basic usage or getting-started notes:
- bash
- Then open your Xcode project in your AI coding tool and say:
- Use the /xcode-build-orchestrator skill to analyze build performance and come up with a plan for improvements.

- Source: https://github.com/AvdLee/Xcode-Build-Optimization-Agent-Skill
- Extracted from upstream docs: https://raw.githubusercontent.com/AvdLee/Xcode-Build-Optimization-Agent-Skill/HEAD/README.md

## Documentation

- https://github.com/AvdLee/Xcode-Build-Optimization-Agent-Skill

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/benchmark-and-reduce-xcode-clean-and-incremental-build-times-with-xcode-build-optimization-agent-skill/)
