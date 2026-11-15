---
name: "Make Rails Active Job workloads resumable with Job Iteration"
slug: "make-rails-active-job-workloads-resumable-with-job-iteration"
description: "Use Job Iteration to turn long-running Rails Active Job workloads into checkpointed, interruptible jobs that coding or operations agents can safely generate, review, and run."
github_stars: 1316
verification: "security_reviewed"
source: "https://github.com/Shopify/job-iteration"
author: "Shopify"
publisher_type: "open_source"
category: "Templates & Workflows"
framework: "Custom Agents"
tool_ecosystem:
  github_repo: "Shopify/job-iteration"
  github_stars: 1316
---

# Make Rails Active Job workloads resumable with Job Iteration

Use Job Iteration to turn long-running Rails Active Job workloads into checkpointed, interruptible jobs that coding or operations agents can safely generate, review, and run.

## Prerequisites

Ruby 3.1 or later, Rails 7.1 or later, Active Job, the job-iteration gem, and a supported queue adapter such as Sidekiq, Resque, GoodJob, Solid Queue, Amazon SQS, or Delayed::Job

## Installation

Install or set up from the source-backed instructions:

Add gem 'job-iteration' to the Rails application's Gemfile, run bundle install, include JobIteration::Iteration in the target Active Job class, replace perform loops with build_enumerator(cursor:) and each_iteration methods, then verify the chosen queue adapter handles graceful interruption as documented upstream.

- Source: https://github.com/Shopify/job-iteration

## Documentation

- https://www.rubydoc.info/gems/job-iteration

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/make-rails-active-job-workloads-resumable-with-job-iteration/)
