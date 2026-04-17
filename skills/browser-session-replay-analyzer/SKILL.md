---
title: "Browser Session Replay Analyzer"
description: "The Browser Session Replay Analyzer captures and analyzes user browser sessions for UX research and debugging. It uses the rrweb library to record DOM mutations, mouse movements, scroll positions, and network requests as a serialized event stream with minimal performance overhead. Recorded sessions are compressed using lz-string and stored with metadata tags for filtering. The skill integrates with LogRocket’s REST API to pull session recordings filtered by user segments, error occurrences, and conversion funnels. FullStory Data Export API integration enables bulk session analysis with custom event tracking. Replay analysis uses automated heuristic detection for rage clicks (3+ clicks within 500ms on same element), dead clicks on non-interactive elements, and excessive scrolling patterns indicating content findability issues. The skill generates UX insight reports with heatmap overlays using canvas-based rendering. Session segments can be exported as MP4 video files using puppeteer-screen-recorder for stakeholder presentations. Integration with Jira API automatically creates UX bug tickets from detected interaction anomalies."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/browser-session-replay-analyzer/"
framework:
  - "Custom Agents"
---

# Browser Session Replay Analyzer

The Browser Session Replay Analyzer captures and analyzes user browser sessions for UX research and debugging. It uses the rrweb library to record DOM mutations, mouse movements, scroll positions, and network requests as a serialized event stream with minimal performance overhead. Recorded sessions are compressed using lz-string and stored with metadata tags for filtering. The skill integrates with LogRocket’s REST API to pull session recordings filtered by user segments, error occurrences, and conversion funnels. FullStory Data Export API integration enables bulk session analysis with custom event tracking. Replay analysis uses automated heuristic detection for rage clicks (3+ clicks within 500ms on same element), dead clicks on non-interactive elements, and excessive scrolling patterns indicating content findability issues. The skill generates UX insight reports with heatmap overlays using canvas-based rendering. Session segments can be exported as MP4 video files using puppeteer-screen-recorder for stakeholder presentations. Integration with Jira API automatically creates UX bug tickets from detected interaction anomalies.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/browser-session-replay-analyzer
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/browser-session-replay-analyzer` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/browser-session-replay-analyzer/)
