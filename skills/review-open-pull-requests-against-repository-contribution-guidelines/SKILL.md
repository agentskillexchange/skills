---
title: "Review open pull requests against repository contribution guidelines"
description: "This entry turns GitHub Next’s Contribution Check workflow into a maintainer-facing agent routine. The agent batches open pull requests, compares them to CONTRIBUTING.md, labels likely-ready submissions, comments on gaps, and produces a report issue so humans can spend review time where it matters."
verification: security_reviewed
source: "https://github.com/githubnext/agentics/blob/main/docs/contribution-check.md"
category:
  - "Templates &amp; Workflows"
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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/review-open-pull-requests-against-repository-contribution-guidelines/)
