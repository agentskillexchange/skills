---
title: "Triage pull request security risks with staged threat modeling and investigation using VulnVibes"
description: "Analyze a GitHub pull request for security impact, run targeted vulnerability-investigation skills when Stage 1 finds credible threats, and return a structured verdict instead of doing an ad hoc manual review."
verification: "security_reviewed"
source: "https://github.com/anshumanbh/vulnvibes"
category:
  - "Security & Verification"
framework:
  - "Claude Agents"
tool_ecosystem:
  github_repo: "anshumanbh/vulnvibes"
  github_stars: 17
---

# Triage pull request security risks with staged threat modeling and investigation using VulnVibes

Use VulnVibes when the job is to perform bounded security triage on a GitHub pull request rather than browse a repository or run a generic code scanner. The workflow is explicit in the upstream project: invoke `vulnvibes pr analyze `, let the PR analyzer summarize the diff and threat-model the change set, then escalate only the identified risks into skill-based investigation passes mapped to specific CWE classes. The output is a structured verdict with confidence, reasoning, and the list of investigation skills used. Invoke this instead of using GitHub, the Claude API, or a generic security tool normally when you need an agent to review a PR for security implications across one repository or related repositories with a reproducible two-stage process. This is not a listing for the Claude Agent SDK, the GitHub API, or a general-purpose vulnerability product. The scope boundary is the PR-security-triage loop: fetch a PR, threat-model it, investigate suspicious paths with bundled security skills, and emit a review-ready result.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/triage-pull-request-security-risks-with-staged-threat-modeling-and-investigation-using-vulnvibes/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/triage-pull-request-security-risks-with-staged-threat-modeling-and-investigation-using-vulnvibes
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/triage-pull-request-security-risks-with-staged-threat-modeling-and-investigation-using-vulnvibes`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/triage-pull-request-security-risks-with-staged-threat-modeling-and-investigation-using-vulnvibes/)
