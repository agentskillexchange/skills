---
name: "Operate Rails Active Job queues with Mission Control Jobs"
slug: "operate-rails-active-job-queues-with-mission-control-jobs"
description: "Use Mission Control Jobs when an operator needs a Rails-mounted dashboard to inspect Active Job queues, review failed jobs, and retry or discard jobs with supervision."
github_stars: 1057
verification: "security_reviewed"
source: "https://github.com/rails/mission_control-jobs"
author: "Rails"
publisher_type: "open_source_project"
category: "Runbooks & Diagnostics"
framework: "Custom Agents"
tool_ecosystem:
  github_repo: "rails/mission_control-jobs"
  github_stars: 1057
---

# Operate Rails Active Job queues with Mission Control Jobs

Use Mission Control Jobs when an operator needs a Rails-mounted dashboard to inspect Active Job queues, review failed jobs, and retry or discard jobs with supervision.

## Prerequisites

Ruby on Rails, Active Job, mission_control-jobs gem, Resque or Solid Queue

## Installation

Install or set up from the source-backed instructions:

Add gem "mission_control-jobs" to the Rails application's Gemfile, run bundle install, mount MissionControl::Jobs::Engine in routes.rb, and configure authentication before exposing the dashboard. For API-only Rails apps or custom asset pipelines, follow the upstream README's Propshaft and asset precompile guidance.

- Source: https://github.com/rails/mission_control-jobs

## Documentation

- https://github.com/rails/mission_control-jobs

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/operate-rails-active-job-queues-with-mission-control-jobs/)
