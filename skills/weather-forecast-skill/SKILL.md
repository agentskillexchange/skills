---
name: Weather Forecast Skill
description: Check current weather and forecasts inside OpenClaw workflows without needing a paid weather API.
category: Calendar, Email & Productivity
framework: OpenClaw
verification: security_reviewed
rating: 4.8
reviews: 80
source: https://agentskillexchange.com/skill/weather-forecast-skill/
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
Requires curl and basic web access. Install the skill, then query supported weather endpoints with the target location in your request.
Source: OpenClaw official weather skill.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill weather-forecast-skill
```

### OpenClaw

```bash
openclaw install weather-forecast-skill
```

### Manual

Download this `SKILL.md` file and place it in your agent's skills directory.

## Metadata

| Field | Value |
|-------|-------|
| Category | Calendar, Email & Productivity |
| Framework | OpenClaw |
| Verification | Security Reviewed |
| Rating | ⭐⭐⭐⭐ 4.8/5.0 (80 reviews) |

---

*Published on [Agent Skill Exchange](https://agentskillexchange.com/skill/weather-forecast-skill/)*
