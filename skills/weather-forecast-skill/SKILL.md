---
name: "Weather Forecast Skill"
description: "Check current weather and forecasts inside OpenClaw workflows without needing a paid weather API."
category: "Calendar, Email & Productivity"
framework: "OpenClaw"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/weather-forecast-skill/"
---

# Weather Forecast Skill

Check current weather and forecasts inside OpenClaw workflows without needing a paid weather API.

## Overview

Weather Forecast Skill provides quick current-weather and forecast checks through public weather sources such as wttr.in. It is intentionally simple: the goal is to give OpenClaw a fast, low-friction weather lookup path for everyday planning rather than severe-weather analysis or historical data work.

Best for

checking current weather for a city or airport code

getting short forecasts for travel and daily planning

answering common weather questions without extra API setup

Install notes

Requires `curl` and basic web access. Install the skill, then query supported weather endpoints with the target location in your request.

**Source:** OpenClaw official weather skill.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill weather-forecast-skill
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill weather-forecast-skill -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill weather-forecast-skill -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill weather-forecast-skill -a codex
```

### OpenClaw

```bash
clawhub install weather-forecast-skill
```

## Source

- Marketplace: https://agentskillexchange.com/skills/weather-forecast-skill/
