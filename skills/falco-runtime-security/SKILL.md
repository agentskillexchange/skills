---
name: "Falco Runtime Security"
slug: "falco-runtime-security"
description: ""
github_stars: 8847
verification: "security_reviewed"
source: "https://github.com/falcosecurity/falco"
author: "Falco"
category: "Security & Verification"
framework: "Custom Agents"
tool_ecosystem:
  github_repo: "falcosecurity/falco"
  github_stars: 8847
---

# Falco Runtime Security



## Installation

Use the upstream install or setup path that matches your environment:
- cmake \
- make -j$(($nproc-1)) falco_unit_tests;

Requirements and caveats from upstream:
- A demo environment is provided via a docker-compose file that can be started on a docker host which includes falco, falcosidekick, falcosidekick-ui and its required redis database. For more information see the [docker...
- As a security tool meant to consume a crazy high throughput of events per second, Falco needs to squeeze performance in all hot paths at runtime and requires deep control on memory allocation, which the Go runtime can...

Basic usage or getting-started notes:
- If you're new to Falco, begin your journey with our [Getting Started](https://falco.org/docs/getting-started/) guide. For production deployments, please refer to our comprehensive [Setup](https://falco.org/docs/setup/...
- As final recommendations before deploying Falco, verify environment compatibility, define your detection goals, optimize performance, choose the appropriate build, and plan for SIEM or data lake integration to ensure...
- ### Demo Environment

- Source: https://github.com/falcosecurity/falco
- Extracted from upstream docs: https://raw.githubusercontent.com/falcosecurity/falco/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/falco-runtime-security/)
