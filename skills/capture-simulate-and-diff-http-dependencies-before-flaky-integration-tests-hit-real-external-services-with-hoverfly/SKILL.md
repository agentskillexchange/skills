---
title: "Capture simulate and diff HTTP dependencies before flaky integration tests hit real external services with Hoverfly"
slug: "capture-simulate-and-diff-http-dependencies-before-flaky-integration-tests-hit-real-external-services-with-hoverfly"
description: "Record real HTTP traffic, replay it in simulation mode, and compare dependency behavior without hammering live third-party services."
github_stars: 2482
verification: "security_reviewed"
source: "https://github.com/SpectoLabs/hoverfly"
author: "SpectoLabs"
publisher_type: "organization"
category: "CI/CD Integrations"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "SpectoLabs/hoverfly"
  github_stars: 2482
---

# Capture simulate and diff HTTP dependencies before flaky integration tests hit real external services with Hoverfly

Record real HTTP traffic, replay it in simulation mode, and compare dependency behavior without hammering live third-party services.

## Prerequisites

Hoverfly binary or container image, HTTP client or application under test, proxy configuration, and target dependency endpoints or recorded traffic fixtures

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install Hoverfly from the upstream releases or run the published container image, configure the application or test client to route traffic through the proxy, then use the documented capture, simulate, and diff modes for the target dependencies.
```

## Documentation

- https://docs.hoverfly.io/en/latest/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/capture-simulate-and-diff-http-dependencies-before-flaky-integration-tests-hit-real-external-services-with-hoverfly/)
