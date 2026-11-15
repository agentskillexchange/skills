---
name: "Run GitHub Issues as a Spec, Build, Review and Ship Pipeline with workkit"
slug: "run-github-issues-as-a-spec-build-review-ship-pipeline-with-workkit"
description: "Use workkit when Claude Code should work a repository's GitHub Issues as a labeled pipeline: capture, triage, spec interview, a subagent build with blind review, owner QA, and a ship step that writes the changelog and releases."
github_stars: 4
verification: "listed"
source: "https://github.com/ITW-Creative-Works/workkit"
author: "ITW-Creative-Works"
category: "Templates & Workflows"
framework: "Claude Code"
tool_ecosystem:
  github_repo: "itw-creative-works/workkit"
  github_stars: 4
---

# Run GitHub Issues as a Spec, Build, Review and Ship Pipeline with workkit

Use workkit when a Claude Code session should treat a repository's GitHub Issues as the single work queue instead of chat history or a local task file. Each issue moves through `status:` labels (inbox, specced, building, qa, complete), and the stage label decides what Claude may do next. An accepted `## Spec` section in the issue body is the go-ahead to build. During the build, the main chat acts as a manager: worker subagents write the code and the tests, and a verifier subagent reviews the diff blind, without seeing how it was made. The finished change waits uncommitted in the working tree until the owner tries it and passes it.

workkit is a Claude Code plugin with nine skills (`workkit:feature`, `workkit:interview`, `workkit:diagnose`, `workkit:review`, `workkit:triage`, `workkit:status`, `workkit:checkpoint`, `workkit:migrate`, `workkit:ship`), five agents and 27 hooks. The hooks guard each step: for example, no code commits until the full test suite has passed on exactly what is being committed. `workkit:ship` writes the CHANGELOG entry in keepachangelog format, commits with Conventional Commits, cuts the release and closes the issue. A repository that has not run `workkit enable` gets none of the hooks.

## Prerequisites

git, the GitHub CLI (`gh`) signed in with `gh auth login`, jq, Node.js with npm (a current LTS release), and the Claude Code CLI. It runs on macOS, Linux, and Windows under Git Bash.

## Installation

Install or set up from the source-backed instructions:

claude plugin marketplace add ITW-Creative-Works/workkit
claude plugin install workkit@workkit

- Source: https://github.com/ITW-Creative-Works/workkit

## Documentation

- https://github.com/ITW-Creative-Works/workkit#readme
- https://github.com/ITW-Creative-Works/workkit/blob/main/docs/project-state.md
- https://github.com/ITW-Creative-Works/workkit/blob/main/docs/setup.md

## Source

- https://github.com/ITW-Creative-Works/workkit
