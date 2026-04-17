---
name: Jenkins Build Log Analyzer
description: Parses Jenkins build console logs via the Jenkins Remote Access API to
  extract failure patterns, stack traces, and flaky test signatures. Uses regex heuristics
  and the Jenkins Test Results API to correlate failures with specific changes. Outputs
  a triage report ranked by recurrence frequency.
category: Runbooks & Diagnostics
framework: ChatGPT Agents
verification: security_reviewed
source: https://github.com/jenkinsci/jenkins
tool_ecosystem:
  github_repo: jenkinsci/jenkins
  github_stars: 25189
  tool: jenkins
  license: MIT
  maintained: true
---
# Jenkins Build Log Analyzer
Parses Jenkins build console logs via the Jenkins Remote Access API to extract failure patterns, stack traces, and flaky test signatures. Uses regex heuristics and the Jenkins Test Results API to correlate failures with specific changes. Outputs a triage report ranked by recurrence frequency.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/jenkins-build-log-analyzer
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/jenkins-build-log-analyzer` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-build-log-analyzer/)
