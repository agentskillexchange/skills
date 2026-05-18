---
name: "Datadog Synthetics Failure Triage Skill"
slug: "datadog-synthetics-failure-triage-skill"
description: "Investigates broken checks with the Datadog Synthetics API, Monitors API, and Logs Search API to connect failed browser or API tests with the signals that explain them. Handy for turning a red synthetic check into an actionable diagnosis instead of a vague outage alarm."
github_stars: 158
verification: "listed"
source: "https://github.com/DataDog/datadog-api-client-python"
category: "Runbooks & Diagnostics"
framework: "Claude Code"
tool_ecosystem:
  github_repo: "DataDog/datadog-api-client-python"
  github_stars: 158
---

# Datadog Synthetics Failure Triage Skill

Investigates broken checks with the Datadog Synthetics API, Monitors API, and Logs Search API to connect failed browser or API tests with the signals that explain them. Handy for turning a red synthetic check into an actionable diagnosis instead of a vague outage alarm.

## Installation

Use the upstream install or setup path that matches your environment:
- pip install datadog-api-client

Requirements and caveats from upstream:
- # datadog-api-client-python
- This repository contains a Python API client for the [Datadog API](https://docs.datadoghq.com/api/).
- Building and using the API client library requires [Python 3.8+](https://www.python.org/downloads/).

Basic usage or getting-started notes:
- To install the API client library, simply execute:
- shell
- from datadog_api_client import ApiClient, Configuration

- Source: https://github.com/DataDog/datadog-api-client-python
- Extracted from upstream docs: https://raw.githubusercontent.com/DataDog/datadog-api-client-python/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-synthetics-failure-triage-skill/)
