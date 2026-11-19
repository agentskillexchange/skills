---
name: "Diagnose Skales Browser Tool Readiness with DevKit"
slug: "diagnose-skales-browser-tool-readiness-with-devkit"
description: "Inspect Skales local DevKit status, model configuration and browser-tool enabled flags, then return a diagnostic handoff before a supervised browser run."
github_stars: 2242
verification: "security_reviewed"
source: "https://github.com/skalesapp/skales"
author: "Mario Simic / Skales"
publisher_type: "independent"
category: "Runbooks & Diagnostics"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "skalesapp/skales"
  github_stars: 2242
---

# Diagnose Skales Browser Tool Readiness with DevKit

Inspect Skales local DevKit status, model configuration and browser-tool enabled flags, then return a diagnostic handoff before a supervised browser run.

## Prerequisites

Running Skales Desktop; enabled DevKit; local HTTP client; DevKit Bearer token. Node.js 18+ only if using the optional bundled CLI.

## Installation

Install or set up from the source-backed instructions:

Install Skales Desktop from https://skales.app using the official platform installer. On v12.9.10 or later enable Settings → Add-Ons → DevKit, then Developer → DevKit → Set up DevKit. Use the bundled documentation and config under ~/.skales-data/devkit/. Keep api.token private. Locate the actual local app port (3000–3009); use an HTTP client for the read-only GET procedure. The optional bundled Node.js CLI supports status, model and tools. No npm package is required for this skill.

- Source: https://github.com/skalesapp/skales

## Documentation

- https://github.com/skalesapp/devkit/blob/main/docs/api-reference.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/diagnose-skales-browser-tool-readiness-with-devkit/)
