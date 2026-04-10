---
name: Check current weather and short forecasts for planning
description: This skill lets an agent fetch current conditions and short forecasts
  with a lightweight weather workflow instead of sending a user to a weather site.
  It is narrowly scoped to quick planning questions, not historical analysis, severe-alert
  monitoring, or a generic weather product listing.
verification: listed
source: https://github.com/openclaw/openclaw/tree/main/skills/weather
category:
- Calendar, Email &amp; Productivity
framework:
- OpenClaw
---
# Check current weather and short forecasts for planning

Tool name: OpenClaw weather skill.
This entry captures a narrow but real job-to-be-done: an agent checks current weather or a short forecast for a named place and returns a decision-friendly answer for planning. The upstream source is specific about when to use it, when not to use it, and how the workflow is executed with wttr.in or related forecast endpoints. That is the key boundary that keeps this from being just a weather-site listing. The agent behavior is simple and useful: take a city, region, or airport code, request current conditions or a short forecast, then summarize the answer in the context of the user's question, such as whether to carry an umbrella, how warm it will feel, or what conditions to expect on a trip.
A user should invoke this instead of using the product normally when weather is only one step inside a broader assistant task. Good examples include checking tomorrow's conditions before travel, answering a quick planning question during a scheduling flow, or adding a fast weather check to a daily assistant routine. In those cases the value is not the weather service itself. The value is an agent doing the lookup, choosing the right format, and returning only the decision-relevant result.
The scope boundary is explicit. This skill is not for historical climate data, severe weather alerting, marine or aviation forecasting, or deep meteorological analysis. It is also not a generic weather API catalog entry. Integration points are lightweight HTTP fetches, travel and calendar planning flows, and any assistant workflow that benefits from a quick location-based weather check. Even with the upstream name hidden, the entry would still make sense as a bounded agent task: retrieve present conditions or a short forecast for a place and use it to help someone plan.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/check-current-weather-and-short-forecasts-for-planning/)
