---
name: "Triage failed Ruby automation jobs with Resque"
slug: "triage-failed-ruby-automation-jobs-with-resque"
description: "Inspect a bounded set of Resque failures, correlate exception evidence and failure IDs, and prepare a recovery plan without retrying or deleting jobs."
verification: "security_reviewed"
source: "https://github.com/resque/resque/blob/master/docs/FAILURE_IDS.md"
author: "Resque contributors"
publisher_type: "open_source_project"
category: "Runbooks & Diagnostics"
framework: "Multi-Framework"
---

# Triage failed Ruby automation jobs with Resque

Inspect a bounded set of Resque failures, correlate exception evidence and failure IDs, and prepare a recovery plan without retrying or deleting jobs.

## Prerequisites

Existing Ruby/Resque application and bundle; configured failure backend; authorized Redis access; application logs or exception-tracker evidence.

## Installation

Install or set up from the source-backed instructions:

Use the application's existing Resque bundle and configuration. For a new prepared environment, add gem 'resque' to the Gemfile and run bundle install. Run the bounded read-only diagnostic with bundle exec ruby after loading the application; do not start workers or upgrade dependencies as part of triage.

- Source: https://github.com/resque/resque/blob/master/docs/FAILURE_IDS.md

## Documentation

- https://github.com/resque/resque/blob/master/README.markdown

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/triage-failed-ruby-automation-jobs-with-resque/)
