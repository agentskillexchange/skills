---
title: "Review open pull requests against repository contribution guidelines"
description: "This entry is built from GitHub Next&#8217;s Contribution Check workflow in the githubnext/agentics repository. The underlying tool is a reusable GitHub Agentic Workflow installed through the gh-aw extension, but the skill here is the bounded maintainer job-to-be-done: periodically review open pull requests against a repository&#8217;s contribution rules and sort them into actionable groups. The agent fetches candidate pull requests, reads the repository&#8217;s CONTRIBUTING.md , checks for obvious policy mismatches, and then applies lightweight workflow outputs such as comments, labels, and a report issue. You invoke this when a repository receives enough outside contributions that maintainers need help triaging backlog before deep code review starts. It is useful for deciding which PRs look ready, which need contributor follow-up, and which appear outside project rules. It should be used instead of manual inbox-style PR scanning when the problem is repeated guideline enforcement rather than one-off review. The scope boundary matters: this entry does not replace full code review, security review, or general GitHub automation. It is specifically about contribution-guideline triage for open pull requests. Integration points include GitHub Actions scheduling, the gh CLI plus the gh-aw extension, repository labels, report issues, and the optional TARGET_REPOSITORY variable documented upstream. After editing the workflow, maintainers compile it with gh aw compile . Because the workflow depends on an actual CONTRIBUTING.md and produces narrow, review-supporting outputs, this remains a skill-shaped operator workflow instead of a generic product listing for GitHub or automation tooling."
source: "https://github.com/githubnext/agentics/blob/main/docs/contribution-check.md"
verification: "security_reviewed"
category:
  - "Templates &amp; Workflows"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "githubnext/agentics"
  github_stars: 585
---

# Review open pull requests against repository contribution guidelines

This entry is built from GitHub Next&#8217;s Contribution Check workflow in the githubnext/agentics repository. The underlying tool is a reusable GitHub Agentic Workflow installed through the gh-aw extension, but the skill here is the bounded maintainer job-to-be-done: periodically review open pull requests against a repository&#8217;s contribution rules and sort them into actionable groups. The agent fetches candidate pull requests, reads the repository&#8217;s CONTRIBUTING.md , checks for obvious policy mismatches, and then applies lightweight workflow outputs such as comments, labels, and a report issue. You invoke this when a repository receives enough outside contributions that maintainers need help triaging backlog before deep code review starts. It is useful for deciding which PRs look ready, which need contributor follow-up, and which appear outside project rules. It should be used instead of manual inbox-style PR scanning when the problem is repeated guideline enforcement rather than one-off review. The scope boundary matters: this entry does not replace full code review, security review, or general GitHub automation. It is specifically about contribution-guideline triage for open pull requests. Integration points include GitHub Actions scheduling, the gh CLI plus the gh-aw extension, repository labels, report issues, and the optional TARGET_REPOSITORY variable documented upstream. After editing the workflow, maintainers compile it with gh aw compile . Because the workflow depends on an actual CONTRIBUTING.md and produces narrow, review-supporting outputs, this remains a skill-shaped operator workflow instead of a generic product listing for GitHub or automation tooling.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/review-open-pull-requests-against-repository-contribution-guidelines/)
