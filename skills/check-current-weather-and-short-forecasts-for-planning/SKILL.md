---
title: "Check current weather and short forecasts for planning"
description: "Tool name: OpenClaw weather skill. This entry captures a narrow but real job-to-be-done: an agent checks current weather or a short forecast for a named place and returns a decision-friendly answer for planning. The upstream source is specific about when to use it, when not to use it, and how the workflow is executed with wttr.in or related forecast endpoints. That is the key boundary that keeps this from being just a weather-site listing. The agent behavior is simple and useful: take a city, region, or airport code, request current conditions or a short forecast, then summarize the answer in the context of the user&#8217;s question, such as whether to carry an umbrella, how warm it will feel, or what conditions to expect on a trip. A user should invoke this instead of using the product normally when weather is only one step inside a broader assistant task. Good examples include checking tomorrow&#8217;s conditions before travel, answering a quick planning question during a scheduling flow, or adding a fast weather check to a daily assistant routine. In those cases the value is not the weather service itself. The value is an agent doing the lookup, choosing the right format, and returning only the decision-relevant result. The scope boundary is explicit. This skill is not for historical climate data, severe weather alerting, marine or aviation forecasting, or deep meteorological analysis. It is also not a generic weather API catalog entry. Integration points are lightweight HTTP fetches, travel and calendar planning flows, and any assistant workflow that benefits from a quick location-based weather check. Even with the upstream name hidden, the entry would still make sense as a bounded agent task: retrieve present conditions or a short forecast for a place and use it to help someone plan."
source: "https://github.com/openclaw/openclaw/tree/main/skills/weather"
verification: "security_reviewed"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "openclaw/openclaw"
  github_stars: 356821
---

# Check current weather and short forecasts for planning

Tool name: OpenClaw weather skill. This entry captures a narrow but real job-to-be-done: an agent checks current weather or a short forecast for a named place and returns a decision-friendly answer for planning. The upstream source is specific about when to use it, when not to use it, and how the workflow is executed with wttr.in or related forecast endpoints. That is the key boundary that keeps this from being just a weather-site listing. The agent behavior is simple and useful: take a city, region, or airport code, request current conditions or a short forecast, then summarize the answer in the context of the user&#8217;s question, such as whether to carry an umbrella, how warm it will feel, or what conditions to expect on a trip. A user should invoke this instead of using the product normally when weather is only one step inside a broader assistant task. Good examples include checking tomorrow&#8217;s conditions before travel, answering a quick planning question during a scheduling flow, or adding a fast weather check to a daily assistant routine. In those cases the value is not the weather service itself. The value is an agent doing the lookup, choosing the right format, and returning only the decision-relevant result. The scope boundary is explicit. This skill is not for historical climate data, severe weather alerting, marine or aviation forecasting, or deep meteorological analysis. It is also not a generic weather API catalog entry. Integration points are lightweight HTTP fetches, travel and calendar planning flows, and any assistant workflow that benefits from a quick location-based weather check. Even with the upstream name hidden, the entry would still make sense as a bounded agent task: retrieve present conditions or a short forecast for a place and use it to help someone plan.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/check-current-weather-and-short-forecasts-for-planning/)
