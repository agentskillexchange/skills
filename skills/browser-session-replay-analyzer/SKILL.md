---
name: Browser Session Replay Analyzer
description: Records and replays browser sessions using rrweb recording library with
  DOM mutation serialization. Integrates with LogRocket API and FullStory Data Export
  API for session analytics.
verification: security_reviewed
source: https://agentskillexchange.com/skills/browser-session-replay-analyzer/
category:
- Browser Automation
framework:
- Custom Agents
---
# Browser Session Replay Analyzer

The Browser Session Replay Analyzer captures and analyzes user browser sessions for UX research and debugging. It uses the rrweb library to record DOM mutations, mouse movements, scroll positions, and network requests as a serialized event stream with minimal performance overhead. Recorded sessions are compressed using lz-string and stored with metadata tags for filtering. The skill integrates with LogRocket's REST API to pull session recordings filtered by user segments, error occurrences, and conversion funnels. FullStory Data Export API integration enables bulk session analysis with custom event tracking. Replay analysis uses automated heuristic detection for rage clicks (3+ clicks within 500ms on same element), dead clicks on non-interactive elements, and excessive scrolling patterns indicating content findability issues. The skill generates UX insight reports with heatmap overlays using canvas-based rendering. Session segments can be exported as MP4 video files using puppeteer-screen-recorder for stakeholder presentations. Integration with Jira API automatically creates UX bug tickets from detected interaction anomalies.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/browser-session-replay-analyzer/)
