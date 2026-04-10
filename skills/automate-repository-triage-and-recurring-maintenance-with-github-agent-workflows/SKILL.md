---
name: "Automate repository triage and recurring repo maintenance with guarded GitHub agent workflows"
description: "Use GitHub Agentic Workflows to let an agent triage issues, inspect CI failures, or deliver scheduled repository upkeep inside GitHub Actions with explicit workflow definitions and reviewable runs. This is for bounded, repeatable repository operations, not for listing GitHub as a general coding platform."
verification: listed
source: "https://github.com/github/gh-aw"
category:
  - "Templates &amp; Workflows"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "github/gh-aw"
  github_stars: 4279
---

# Automate repository triage and recurring repo maintenance with guarded GitHub agent workflows

Tool: GitHub Agentic Workflows (github/gh-aw).
This entry is about a very specific agent job: running repeatable repository operations inside GitHub Actions with workflow files that define when the agent should act, what context it receives, and what guardrails apply. The agent behavior is not &#8220;use GitHub normally&#8221;. It is &#8220;take a repository maintenance task that would otherwise be done over and over by a human or an ad hoc coding agent session, and turn it into a reviewed workflow run.&#8221; Examples include scheduled issue triage, summarizing recent default-branch changes, investigating CI failures, and generating repository health reports.
Invoke this when the work is recurring, repository-scoped, and benefits from automation plus auditability. If a maintainer just wants to browse GitHub, open a PR manually, or chat with a coding agent interactively, they should use the product normally. This skill exists for the narrower case where an operator wants a repository job to run on a schedule, on a trigger, or from a slash-command style workflow with logs, policies, and repeatable inputs.
The scope boundary matters. GitHub Agentic Workflows is not being listed here as a generic CLI, SDK, or platform card. The useful unit is the operational pattern: define guarded agent workflows for repository hygiene and triage. Integration points include GitHub Actions, repository markdown workflow definitions, audit logs, scheduled runs, CI events, and coding agents supported by the upstream project. If you hide the product name, the task still makes sense: automate recurring repo maintenance with explicit guardrails and reviewable execution.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/automate-repository-triage-and-recurring-maintenance-with-github-agent-workflows/)
