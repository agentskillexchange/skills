---
name: "Incident Postmortem Generator"
slug: "incident-postmortem-generator"
description: "Generates structured incident postmortems by aggregating data from PagerDuty incidents API, Slack channel history, and Grafana dashboard snapshots. Produces blameless postmortem documents following the Google SRE template format."
verification: "security_reviewed"
source: "https://developer.pagerduty.com/"
author: "PagerDuty"
category: "Runbooks & Diagnostics"
framework: "ChatGPT Agents"
---

# Incident Postmortem Generator

Generates structured incident postmortems by aggregating data from PagerDuty incidents API, Slack channel history, and Grafana dashboard snapshots. Produces blameless postmortem documents following the Google SRE template format.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Documentation

- https://developer.pagerduty.com/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/incident-postmortem-generator/)
