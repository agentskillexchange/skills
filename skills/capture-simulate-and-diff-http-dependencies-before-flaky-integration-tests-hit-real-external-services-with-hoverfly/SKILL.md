---
title: "Capture simulate and diff HTTP dependencies before flaky integration tests hit real external services with Hoverfly"
description: "Record real HTTP traffic, replay it in simulation mode, and compare dependency behavior without hammering live third-party services."
verification: "listed"
source: "https://github.com/SpectoLabs/hoverfly"
category:
  - "CI/CD Integrations"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "SpectoLabs/hoverfly"
  github_stars: 2482
---

# Capture simulate and diff HTTP dependencies before flaky integration tests hit real external services with Hoverfly

Use Hoverfly when an agent needs to proxy, capture, replay, or compare HTTP dependency behavior for integration testing and debugging. A user should invoke this instead of calling the real service normally when the goal is deterministic test isolation, safe replay, or controlled simulation of external APIs. The scope boundary is narrow: proxy-based HTTP dependency capture and simulation, not a generic test framework, proxy product, or broad API platform listing.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/capture-simulate-and-diff-http-dependencies-before-flaky-integration-tests-hit-real-external-services-with-hoverfly/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/capture-simulate-and-diff-http-dependencies-before-flaky-integration-tests-hit-real-external-services-with-hoverfly
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/capture-simulate-and-diff-http-dependencies-before-flaky-integration-tests-hit-real-external-services-with-hoverfly`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/capture-simulate-and-diff-http-dependencies-before-flaky-integration-tests-hit-real-external-services-with-hoverfly/)
