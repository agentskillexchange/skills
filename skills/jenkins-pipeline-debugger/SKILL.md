---
name: "Jenkins Pipeline Debugger"
description: "Connects to Jenkins via the Jenkins REST API and Blue Ocean API to debug Declarative and Scripted pipelines. Retrieves stage logs, replays failed builds, and traces Groovy CPS execution state."
category: "CI/CD Integrations"
framework: "Claude Agents"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/jenkins-pipeline-debugger/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "jenkins"  # from ase_tool_match
  github_stars: 25122  # from ase_github_stars (integer, not string)
  github_repo: "jenkinsci/jenkins"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Jenkins Pipeline Debugger

Connects to Jenkins via the Jenkins REST API and Blue Ocean API to debug Declarative and Scripted pipelines. Retrieves stage logs, replays failed builds, and traces Groovy CPS execution state.

## Overview

The Jenkins Pipeline Debugger skill provides deep inspection of Jenkins CI pipelines through the Jenkins REST API and Blue Ocean REST endpoints. It fetches pipeline run details from /blue/rest/organizations/{org}/pipelines/{name}/runs/{id}/nodes/ to map stage execution graphs. Failed stage logs are retrieved via the consoleText API and parsed for common error patterns including dependency resolution failures, Docker image pull errors, and credential binding issues. The skill can replay failed builds using the POST /job/{name}/{id}/replay endpoint with modified Groovy scripts. It inspects the CPS (Continuation Passing Style) execution state through the Pipeline Steps API to identify where Groovy closures stalled. Shared library resolution is traced using the Global Library configuration API. Build queue analysis via /queue/api/json identifies executor starvation and label mismatch bottlenecks.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill jenkins-pipeline-debugger
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill jenkins-pipeline-debugger -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill jenkins-pipeline-debugger -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill jenkins-pipeline-debugger -a codex
```

### OpenClaw

```bash
clawhub install jenkins-pipeline-debugger
```

## Source

- Marketplace: https://agentskillexchange.com/skills/jenkins-pipeline-debugger/
