---
title: "Check current weather and short forecasts for planning"
description: "Tool name: OpenClaw weather skill.\nThis entry captures a narrow but real job-to-be-done: an agent checks current weather or a short forecast for a named place and returns a decision-friendly answer for planning. The upstream source is specific about when to use it, when not to use it, and how the workflow is executed with wttr.in or related forecast endpoints. That is the key boundary that keeps this from being just a weather-site listing. The agent behavior is simple and useful: take a city, region, or airport code, request current conditions or a short forecast, then summarize the answer in the context of the user’s question, such as whether to carry an umbrella, how warm it will feel, or what conditions to expect on a trip.\nA user should invoke this instead of using the product normally when weather is only one step inside a broader assistant task. Good examples include checking tomorrow’s conditions before travel, answering a quick planning question during a scheduling flow, or adding a fast weather check to a daily assistant routine. In those cases the value is not the weather service itself. The value is an agent doing the lookup, choosing the right format, and returning only the decision-relevant result.\nThe scope boundary is explicit. This skill is not for historical climate data, severe weather alerting, marine or aviation forecasting, or deep meteorological analysis. It is also not a generic weather API catalog entry. Integration points are lightweight HTTP fetches, travel and calendar planning flows, and any assistant workflow that benefits from a quick location-based weather check. Even with the upstream name hidden, the entry would still make sense as a bounded agent task: retrieve present conditions or a short forecast for a place and use it to help someone plan."
verification: security_reviewed
source: "https://github.com/openclaw/openclaw/tree/main/skills/weather"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "openclaw/openclaw"
  github_stars: 356821
---

# Check current weather and short forecasts for planning

Tool name: OpenClaw weather skill.
This entry captures a narrow but real job-to-be-done: an agent checks current weather or a short forecast for a named place and returns a decision-friendly answer for planning. The upstream source is specific about when to use it, when not to use it, and how the workflow is executed with wttr.in or related forecast endpoints. That is the key boundary that keeps this from being just a weather-site listing. The agent behavior is simple and useful: take a city, region, or airport code, request current conditions or a short forecast, then summarize the answer in the context of the user’s question, such as whether to carry an umbrella, how warm it will feel, or what conditions to expect on a trip.
A user should invoke this instead of using the product normally when weather is only one step inside a broader assistant task. Good examples include checking tomorrow’s conditions before travel, answering a quick planning question during a scheduling flow, or adding a fast weather check to a daily assistant routine. In those cases the value is not the weather service itself. The value is an agent doing the lookup, choosing the right format, and returning only the decision-relevant result.
The scope boundary is explicit. This skill is not for historical climate data, severe weather alerting, marine or aviation forecasting, or deep meteorological analysis. It is also not a generic weather API catalog entry. Integration points are lightweight HTTP fetches, travel and calendar planning flows, and any assistant workflow that benefits from a quick location-based weather check. Even with the upstream name hidden, the entry would still make sense as a bounded agent task: retrieve present conditions or a short forecast for a place and use it to help someone plan.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/check-current-weather-and-short-forecasts-for-planning
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/check-current-weather-and-short-forecasts-for-planning` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/check-current-weather-and-short-forecasts-for-planning/)
