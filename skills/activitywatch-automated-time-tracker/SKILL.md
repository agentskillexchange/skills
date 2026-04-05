---
name: "ActivityWatch Cross-Platform Automated Time Tracker and Productivity Analyzer"
description: "ActivityWatch is a privacy-first, open-source automated time tracker that records application usage, browser activity, and AFK status across Windows, macOS, and Linux. With 16k+ GitHub stars, it provides detailed productivity analytics without sending data to external servers."
category: "Calendar, Email &amp; Productivity"
framework: "Multi-Framework"
verification: security_reviewed
source: "https://github.com/ActivityWatch/activitywatch"
---
# ActivityWatch Cross-Platform Automated Time Tracker and Productivity Analyzer

ActivityWatch is a privacy-first, open-source automated time tracker that records application usage, browser activity, and AFK status across Windows, macOS, and Linux. With 16k+ GitHub stars, it provides detailed productivity analytics without sending data to external servers.

ActivityWatch is a cross-platform automated time tracking application designed to collect valuable lifedata while keeping user privacy at the forefront. With over 16,000 GitHub stars and an active development community, it has become the leading open-source alternative to services like RescueTime and Toggl Track.

How It Works ActivityWatch runs a local server (aw-server or aw-server-rust) that collects events from watchers — lightweight background processes that monitor specific activity sources. The two core watchers included are aw-watcher-window (tracks the currently active application and window title) and aw-watcher-afk (detects keyboard and mouse idle states). A browser extension (aw-watcher-web) tracks active tabs and URLs in Chrome and Firefox.

Key Features All data stays on your local machine. The web-based dashboard provides timeline views, activity summaries, and category breakdowns. A built-in query language lets you write custom reports and filter events by application, window title, URL, or time range. The REST API on localhost:5600 enables programmatic access to all collected data for custom integrations and exports.

Integration Points for AI Agents The localhost REST API makes ActivityWatch particularly useful for AI agent workflows. Agents can query productivity data to generate daily summaries, detect focus patterns, identify time sinks, or trigger alerts when certain thresholds are reached. The JSON export format is straightforward to parse and transform. Community watchers extend tracking to VS Code editor activity, Spotify playback, and custom data sources.

Technical Stack The server is available in Python (aw-server) or Rust (aw-server-rust) implementations. The web UI uses Vue.js. Desktop builds are distributed as standalone bundles for Windows, macOS, and Linux. An Android app provides mobile tracking. The project uses the Mozilla Public License 2.0, allowing both open-source and proprietary integrations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill activitywatch-automated-time-tracker
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill activitywatch-automated-time-tracker -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill activitywatch-automated-time-tracker -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill activitywatch-automated-time-tracker -a codex
```

### OpenClaw

```bash
clawhub install activitywatch-automated-time-tracker
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/activitywatch-automated-time-tracker/)
