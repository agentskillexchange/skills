---
title: "Review open pull requests against repository contribution guidelines"
description: "This entry turns GitHub Next’s Contribution Check workflow into a maintainer-facing agent routine. The agent batches open pull requests, compares them to CONTRIBUTING.md, labels likely-ready submissions, comments on gaps, and produces a report issue so humans can spend review time where it matters."
verification: security_reviewed
source: "https://github.com/githubnext/agentics/blob/main/docs/contribution-check.md"
category:
  - "Templates & Workflows"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "githubnext/agentics"
  github_stars: 585
---

# Review open pull requests against repository contribution guidelines

This entry is built from GitHub Next’s Contribution Check workflow in the githubnext/agentics repository. The underlying tool is a reusable GitHub Agentic Workflow installed through the gh-aw extension, but the skill here is the bounded maintainer job-to-be-done: periodically review open pull requests against a repository’s contribution rules and sort them into actionable groups. The agent fetches candidate pull requests, reads the repository’s CONTRIBUTING.md, checks for obvious policy mismatches, and then applies lightweight workflow outputs such as comments, labels, and a report issue.

You invoke this when a repository receives enough outside contributions that maintainers need help triaging backlog before deep code review starts. It is useful for deciding which PRs look ready, which need contributor follow-up, and which appear outside project rules. It should be used instead of manual inbox-style PR scanning when the problem is repeated guideline enforcement rather than one-off review. The scope boundary matters: this entry does not replace full code review, security review, or general GitHub automation. It is specifically about contribution-guideline triage for open pull requests.

Integration points include GitHub Actions scheduling, the gh CLI plus the gh-aw extension, repository labels, report issues, and the optional TARGET_REPOSITORY variable documented upstream. After editing the workflow, maintainers compile it with gh aw compile. Because the workflow depends on an actual CONTRIBUTING.md and produces narrow, review-supporting outputs, this remains a skill-shaped operator workflow instead of a generic product listing for GitHub or automation tooling.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/review-open-pull-requests-against-repository-contribution-guidelines
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/review-open-pull-requests-against-repository-contribution-guidelines` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/review-open-pull-requests-against-repository-contribution-guidelines/)
