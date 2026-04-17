---
title: "Bazel Build Graph Analyzer"
description: "Analyzes Bazel build dependency graphs to identify bottlenecks and optimize build times. Uses the Bazel Query Language (BQL), Action Graph API, and Build Event Protocol (BEP) for deep build analysis."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/bazel-build-graph-analyzer/"
category:
  - "Developer Tools"
framework:
  - "MCP"
---

# Bazel Build Graph Analyzer

The Bazel Build Graph Analyzer provides deep inspection of Bazel build dependency structures using the Bazel Query Language and Action Graph API. It parses the Build Event Protocol (BEP) output stream to identify critical path bottlenecks and suggest parallelization improvements.

The agent executes bazel query expressions including deps(), rdeps(), allpaths(), and somepath() to map dependency chains and detect unnecessary transitive dependencies. It analyzes action execution logs from the Build Event Protocol JSON profile to compute critical path duration and identify slow actions that dominate build times.

Key capabilities include Starlark rule analysis for custom build rule optimization, repository rule caching evaluation via the repository cache API, and remote execution performance analysis using the Remote Execution API v2 metrics. The agent generates build optimization reports with concrete recommendations for target splitting, visibility restriction, and build configuration tuning using .bazelrc flag combinations. It also detects test sharding opportunities using bazel test –test_sharding_strategy analysis.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/bazel-build-graph-analyzer
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/bazel-build-graph-analyzer` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/bazel-build-graph-analyzer/)
