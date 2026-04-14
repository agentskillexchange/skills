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

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/bazel-build-graph-analyzer/)
