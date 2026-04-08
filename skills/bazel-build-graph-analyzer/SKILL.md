---
title: Bazel Build Graph Analyzer
description: The Bazel Build Graph Analyzer provides deep inspection of Bazel build
  dependency structures using the Bazel Query Language and Action Graph API. It parses
  the Build Event Protocol (BEP) output stream to identify critical path bottlenecks
  and suggest parallelization improvements. The agent executes bazel query expressions
  including deps(), rdeps(), allpaths(), and somepath() to map dependency chains and
  detect unnecessary transitive dependencies. It analyzes action execution logs from
  the Build Event Protocol JSON profile to compute critical path duration and identify
  slow actions that dominate build times. Key capabilities include Starlark rule analysis
  for custom build rule optimization, repository rule caching evaluation via the repository
  cache API, and remote execution performance analysis using the Remote Execution
  API v2 metrics. The agent generates build optimization reports with concrete recommendations
  for target splitting, visibility restriction, and build configuration tuning using
  .bazelrc flag combinations. It also detects test sharding opportunities using bazel
  test –test_sharding_strategy analysis.
verification: security_reviewed
source: https://agentskillexchange.com/skills/bazel-build-graph-analyzer/
category:
- Developer Tools
framework:
- MCP
---

# Bazel Build Graph Analyzer

The Bazel Build Graph Analyzer provides deep inspection of Bazel build dependency structures using the Bazel Query Language and Action Graph API. It parses the Build Event Protocol (BEP) output stream to identify critical path bottlenecks and suggest parallelization improvements. The agent executes bazel query expressions including deps(), rdeps(), allpaths(), and somepath() to map dependency chains and detect unnecessary transitive dependencies. It analyzes action execution logs from the Build Event Protocol JSON profile to compute critical path duration and identify slow actions that dominate build times. Key capabilities include Starlark rule analysis for custom build rule optimization, repository rule caching evaluation via the repository cache API, and remote execution performance analysis using the Remote Execution API v2 metrics. The agent generates build optimization reports with concrete recommendations for target splitting, visibility restriction, and build configuration tuning using .bazelrc flag combinations. It also detects test sharding opportunities using bazel test –test_sharding_strategy analysis.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/bazel-build-graph-analyzer/)
