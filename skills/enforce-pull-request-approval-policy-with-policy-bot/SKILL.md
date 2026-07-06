---
name: "Enforce pull-request approval policy with Policy Bot"
slug: "enforce-pull-request-approval-policy-with-policy-bot"
description: "Codify complex GitHub review rules, evaluate pull requests, and expose approval status as a required check."
github_stars: 1032
verification: "security_reviewed"
source: "https://github.com/palantir/policy-bot"
author: "Palantir"
publisher_type: "organization"
category: "Code Quality & Review"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "palantir/policy-bot"
  github_stars: 1032
---

# Enforce pull-request approval policy with Policy Bot

Codify complex GitHub review rules, evaluate pull requests, and expose approval status as a required check.

## Prerequisites

Policy Bot GitHub App, GitHub repository, policy.yml

## Installation

Use the upstream install or setup path that matches your environment:
- make it easier for developers to figure out who they should ask for approval.
- yarn install
- yarn run build
- docker run --rm -v "$(pwd)/config:/secrets/" -p 8080:8080 palantirtechnologies/policy-bot:latest

Requirements and caveats from upstream:
- [![Docker Pulls](https://img.shields.io/docker/pulls/palantirtechnologies/policy-bot.svg)](https://hub.docker.com/r/palantirtechnologies/policy-bot/)
- Require reviews from specific users, organizations, or teams
- policy requires that all of its rules are approved to approve the pull request.

Basic usage or getting-started notes:
- After evaluation, a rule can be in one of four states:
- approved - all of the predicates and requirements are true
- pending - all of the predicates are true but one or more requirements are not true

- Source: https://github.com/palantir/policy-bot
- Extracted from upstream docs: https://raw.githubusercontent.com/palantir/policy-bot/HEAD/README.md

## Documentation

- https://github.com/palantir/policy-bot

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/enforce-pull-request-approval-policy-with-policy-bot/)
