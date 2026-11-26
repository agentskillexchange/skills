---
name: "Google Flights Fare Search"
slug: "google-flights-fare-search"
description: "Search Google Flights by route and date through the Apify Google Flights Actor (johnvc/Google-Flights-Data-Scraper-Flight-and-Price-Search) and get one JSON row per flight with price, airlines, times, stops, layovers and duration, plus route price insights. Use when an agent needs airfare data for a route, a fare comparison, or flight results as JSON or CSV."
verification: "listed"
source: "https://github.com/johnisanerd/claude-skill-google-flights-api"
category: "Research & Scraping"
framework: "Claude Code"
tool_ecosystem:
  github_repo: "johnisanerd/claude-skill-google-flights-api"
---

# Google Flights Fare Search

Google has no public Flights API, so this skill gets fares through a hosted Apify Actor that searches Google Flights and returns structured results. Give it IATA airport codes and dates and it returns one dataset item per results page, with about 30 flights in an `all_flights` array. Each flight has `price`, `currency`, `airlines`, `departure_time`, `arrival_time`, `stops`, `layover_airports`, `duration_minutes`, `travel_class` and `flight_numbers`. Each page also carries `price_insights` (`lowest_price`, `price_level`, `typical_price_range`, and a `price_history` series when Google shows one).

Use it for one-way, round-trip or multi-city searches. Filters cover maximum price, maximum stops (0 for nonstop), airlines and basic-economy exclusion. `currency`, `hl` and `gl` localize fares across 29 languages and 39 countries. `max_pages` controls how many result pages are fetched, and it is the main cost driver.

It is not for live flight status or tracking, and it does not book tickets. It returns booking tokens and, optionally, booking links.

Requirements: an Apify account, authenticated with `apify login` or an `APIFY_TOKEN` environment variable. Runs are billed to that account: a small per-run fee plus a per-page fee.

## Example

Flight dates must be in the future. Replace the two dates below with your own outbound and return dates (YYYY-MM-DD).

```bash
apify actors call "johnvc/Google-Flights-Data-Scraper-Flight-and-Price-Search" \
  -i '{"departure_id":"SFO","arrival_id":"CDG","outbound_date":"2027-03-10","return_date":"2027-03-20","max_stops":0,"max_price":900,"currency":"USD","max_pages":1}' \
  --output-dataset --silent
```

`--output-dataset` prints the run's dataset items rather than the run details, and `max_pages: 1` keeps the run to one results page. Each item is one results page, so for one row per flight (or a flat CSV), flatten each item's `all_flights` array, for example by piping the output to `jq '[.[].all_flights[]]'`.

Agents can also call it over MCP with the hosted server `https://mcp.apify.com/?tools=actors,docs,johnvc/Google-Flights-Data-Scraper-Flight-and-Price-Search`.

## Installation

### Claude Code, Cursor and other skills-compatible agents

```bash
npx skills add johnisanerd/claude-skill-google-flights-api
```

### Direct repo/manual install

```bash
git clone https://github.com/johnisanerd/claude-skill-google-flights-api.git
mkdir -p ~/.claude/skills
cp -R claude-skill-google-flights-api/apify-google-flights-api ~/.claude/skills/apify-google-flights-api
```

## Source

- Skill repo: https://github.com/johnisanerd/claude-skill-google-flights-api
- Actor: https://apify.com/johnvc/Google-Flights-Data-Scraper-Flight-and-Price-Search
