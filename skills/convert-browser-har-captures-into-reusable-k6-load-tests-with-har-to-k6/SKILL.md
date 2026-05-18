---
name: "Convert browser HAR captures into reusable k6 load tests with har-to-k6"
slug: "convert-browser-har-captures-into-reusable-k6-load-tests-with-har-to-k6"
description: "Use har-to-k6 when an agent has recorded browser traffic and needs to turn it into a repeatable k6 script instead of hand-writing one from scratch. The skill is about transforming captured sessions into a starter load-test artifact with validation and export, not about listing k6 or Grafana as products."
github_stars: 159
verification: "listed"
source: "https://github.com/grafana/har-to-k6"
author: "Grafana Labs"
publisher_type: "Company"
category: "Templates & Workflows"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "grafana/har-to-k6"
  github_stars: 159
---

# Convert browser HAR captures into reusable k6 load tests with har-to-k6

Use har-to-k6 when an agent has recorded browser traffic and needs to turn it into a repeatable k6 script instead of hand-writing one from scratch. The skill is about transforming captured sessions into a starter load-test artifact with validation and export, not about listing k6 or Grafana as products.

## Prerequisites

Node.js or Docker, a HAR or LI-HAR capture, and k6 for running the generated script

## Installation

Use the upstream install or setup path that matches your environment:
- $ npm install --save har-to-k6
- $ npm install --global har-to-k6
- $ docker pull grafana/har-to-k6:latest
- $ npx har-to-k6 archive.har -o my-k6-script.js

Requirements and caveats from upstream:
- ![DockerHub](https://img.shields.io/docker/pulls/grafana/har-to-k6.svg)
- [Docker](#docker)
- Note that this will require you to run the converter with npx har-to-k6 your-har-file or,

Basic usage or getting-started notes:
- [Usage](#usage)
- [CLI Usage](#cli-usage)
- [Programmatic Usage](#programmatic-usage)

- Source: https://github.com/grafana/har-to-k6
- Extracted from upstream docs: https://raw.githubusercontent.com/grafana/har-to-k6/HEAD/README.md

## Documentation

- https://github.com/grafana/har-to-k6#readme

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/convert-browser-har-captures-into-reusable-k6-load-tests-with-har-to-k6/)
