---
name: "Capture simulate and diff HTTP dependencies before flaky integration tests hit real external services with Hoverfly"
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

Use the upstream install or setup path that matches your environment:
- git clone https://github.com/SpectoLabs/hoverfly.git
- make build
- make test
- brew install ruby

Requirements and caveats from upstream:
- Hoverfly is a lightweight, open source API simulation tool. Using Hoverfly, you can create realistic simulations of the APIs your application depends on.
- Some middleware tests may fail if you don't have ruby and python setup in your environment. If you are using Mac, you can install them with [Homebrew](https://brew.sh/):

Basic usage or getting-started notes:
- Lightweight, high-performance, run anywhere
- [Download and installation](https://hoverfly.readthedocs.io/en/latest/pages/introduction/downloadinstallation.html)
- [Read the docs](https://hoverfly.readthedocs.io)

- Source: https://github.com/SpectoLabs/hoverfly
- Extracted from upstream docs: https://raw.githubusercontent.com/SpectoLabs/hoverfly/HEAD/README.md

## Documentation

- https://docs.hoverfly.io/en/latest/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/capture-simulate-and-diff-http-dependencies-before-flaky-integration-tests-hit-real-external-services-with-hoverfly/)
