---
title: "Convert browser HAR captures into reusable k6 load tests with har-to-k6"
description: "Use har-to-k6 when an agent has recorded browser traffic and needs to turn it into a repeatable k6 script instead of hand-writing one from scratch. The skill is about transforming captured sessions into a starter load-test artifact with validation and export, not about listing k6 or Grafana as products."
verification: "security_reviewed"
source: "https://github.com/grafana/har-to-k6"
category:
  - "Templates & Workflows"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "grafana/har-to-k6"
  github_stars: 159
---

# Convert browser HAR captures into reusable k6 load tests with har-to-k6

This ASE entry is built around har-to-k6, the open source converter maintained by Grafana for turning HAR or LI-HAR archives into executable k6 scripts. The agent behavior is concrete: validate a recorded archive, convert it into a starter k6 scenario, write the generated script, and hand the result back for editing, parameterization, or CI execution. That is a bounded operator task. It is not a listing for Grafana k6, not a generic performance-testing platform card, and not a catch-all HTTP tooling entry. Invoke this skill when a user already has browser-recorded traffic from DevTools, a proxy, or another capture tool and wants an agent to bootstrap a realistic load-test script quickly. It is a strong fit for debugging high-traffic endpoints, recreating checkout or login flows under load, seeding a performance test suite from a manually verified session, or turning one-off exploratory browsing into a repeatable benchmark artifact. An agent can also validate that the archive is structurally sound before conversion, which reduces wasted cycles on malformed exports. The scope boundary is what keeps this skill honest. The agent is not acting as a full observability stack, a generic JavaScript CLI wrapper, or a broad “performance engineering platform.” The job is archive-to-script transformation for k6. Integration points include Chrome or browser HAR exports, the k6 CLI, npm-based test repositories, Docker-based performance jobs, and CI pipelines that want generated scripts checked into version control before further tuning. Upstream evidence is solid: the official GitHub repo exists, the npm package exists, Apache-2.0 licensing is published, releases and tags are present, the README documents validation and conversion flows, npm download counts are available, and recent commits show current maintenance.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/convert-browser-har-captures-into-reusable-k6-load-tests-with-har-to-k6/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/convert-browser-har-captures-into-reusable-k6-load-tests-with-har-to-k6
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/convert-browser-har-captures-into-reusable-k6-load-tests-with-har-to-k6`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/convert-browser-har-captures-into-reusable-k6-load-tests-with-har-to-k6/)
