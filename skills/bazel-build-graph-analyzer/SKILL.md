---
name: "Bazel Build Graph Analyzer"
description: "Analyzes Bazel build dependency graphs to identify bottlenecks and optimize build times. Uses the Bazel Query Language (BQL), Action Graph API, and Build Event Protocol (BEP) for deep build analysis."
category: "Developer Tools"
framework: "MCP-compatible"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/bazel-build-graph-analyzer/"
---

# Bazel Build Graph Analyzer

Analyzes Bazel build dependency graphs to identify bottlenecks and optimize build times. Uses the Bazel Query Language (BQL), Action Graph API, and Build Event Protocol (BEP) for deep build analysis.

## Overview

The Bazel Build Graph Analyzer provides deep inspection of Bazel build dependency structures using the Bazel Query Language and Action Graph API. It parses the Build Event Protocol (BEP) output stream to identify critical path bottlenecks and suggest parallelization improvements.

The agent executes bazel query expressions including deps(), rdeps(), allpaths(), and somepath() to map dependency chains and detect unnecessary transitive dependencies. It analyzes action execution logs from the Build Event Protocol JSON profile to compute critical path duration and identify slow actions that dominate build times.

Key capabilities include Starlark rule analysis for custom build rule optimization, repository rule caching evaluation via the repository cache API, and remote execution performance analysis using the Remote Execution API v2 metrics. The agent generates build optimization reports with concrete recommendations for target splitting, visibility restriction, and build configuration tuning using .bazelrc flag combinations. It also detects test sharding opportunities using bazel test –test_sharding_strategy analysis.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill bazel-build-graph-analyzer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill bazel-build-graph-analyzer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill bazel-build-graph-analyzer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill bazel-build-graph-analyzer -a codex
```

### OpenClaw

```bash
clawhub install bazel-build-graph-analyzer
```

## Source

- Marketplace: https://agentskillexchange.com/skills/bazel-build-graph-analyzer/
