---
name: "Healthchecks.io Cron Job Monitoring and Alerting Platform"
slug: "healthchecks-io-cron-job-monitoring-alerting-platform"
description: "Healthchecks.io is an open-source cron and background task monitoring platform that alerts when scheduled jobs fail to ping on time. It gives teams a dashboard, API, and notification integrations for tracking recurring jobs without building their own heartbeat system."
github_stars: 9967
verification: "security_reviewed"
source: "https://github.com/healthchecks/healthchecks"
author: "healthchecks"
publisher_type: "Open Source Project"
category: "Monitoring & Alerts"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "healthchecks/healthchecks"
  github_stars: 9967
---

# Healthchecks.io Cron Job Monitoring and Alerting Platform

Healthchecks.io is an open-source cron and background task monitoring platform that alerts when scheduled jobs fail to ping on time. It gives teams a dashboard, API, and notification integrations for tracking recurring jobs without building their own heartbeat system.

## Prerequisites

Python 3.12+, PostgreSQL/MySQL/MariaDB

## Installation

Use the upstream install or setup path that matches your environment:
- git clone https://github.com/healthchecks/healthchecks.git
- pip install -r healthchecks/requirements.txt -r healthchecks/requirements-dev.txt
- pip uninstall -y pycurl
- pip install pycurl==$PYCURL_VERSION --compile --no-cache-dir

Requirements and caveats from upstream:
- Python 3.12+
- A [Dockerfile](https://github.com/healthchecks/healthchecks/tree/master/docker)
- and [pre-built Docker images](https://hub.docker.com/r/healthchecks/healthchecks) are

Basic usage or getting-started notes:
- Run tests:
- Run development server:
- in this file. You can copy the provided hc/local_settings.py.example as

- Source: https://github.com/healthchecks/healthchecks
- Extracted from upstream docs: https://raw.githubusercontent.com/healthchecks/healthchecks/HEAD/README.md

## Documentation

- https://healthchecks.io/docs/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/healthchecks-io-cron-job-monitoring-alerting-platform/)
