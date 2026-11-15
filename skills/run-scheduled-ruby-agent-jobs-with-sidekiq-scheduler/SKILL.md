---
name: "Run scheduled Ruby agent jobs with Sidekiq Scheduler"
slug: "run-scheduled-ruby-agent-jobs-with-sidekiq-scheduler"
description: "Use Sidekiq Scheduler to run recurring Ruby/Sidekiq agent jobs for refreshes, evaluations, reports, maintenance, and queue-driven automations with cron-style schedules."
github_stars: 1754
verification: "security_reviewed"
source: "https://github.com/sidekiq-scheduler/sidekiq-scheduler"
author: "Sidekiq Scheduler contributors"
publisher_type: "open_source"
category: "Templates & Workflows"
framework: "Custom Agents"
tool_ecosystem:
  github_repo: "sidekiq-scheduler/sidekiq-scheduler"
  github_stars: 1754
---

# Run scheduled Ruby agent jobs with Sidekiq Scheduler

Use Sidekiq Scheduler to run recurring Ruby/Sidekiq agent jobs for refreshes, evaluations, reports, maintenance, and queue-driven automations with cron-style schedules.

## Prerequisites

Ruby application using Sidekiq, Redis, sidekiq-scheduler gem, Sidekiq worker classes, sidekiq.yml scheduler configuration

## Installation

Use the upstream install or setup path that matches your environment:
- gem install sidekiq-scheduler

Basic usage or getting-started notes:
- ruby
- require 'sidekiq-scheduler'
- include Sidekiq::Job

- Source: https://github.com/sidekiq-scheduler/sidekiq-scheduler
- Extracted from upstream docs: https://raw.githubusercontent.com/sidekiq-scheduler/sidekiq-scheduler/HEAD/README.md

## Documentation

- https://sidekiq-scheduler.github.io/sidekiq-scheduler/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-scheduled-ruby-agent-jobs-with-sidekiq-scheduler/)
