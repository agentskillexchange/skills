---
title: "Browser Session Replay Analyzer"
description: "Records and replays browser sessions using rrweb recording library with DOM mutation serialization. Integrates with LogRocket API and FullStory Data Export API for session analytics."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/browser-session-replay-analyzer/"
category:
  - "Browser Automation"
framework:
  - "Custom Agents"
---

# Browser Session Replay Analyzer

The Browser Session Replay Analyzer captures and analyzes user browser sessions for UX research and debugging. It uses the rrweb library to record DOM mutations, mouse movements, scroll positions, and network requests as a serialized event stream with minimal performance overhead. Recorded sessions are compressed using lz-string and stored with metadata tags for filtering. The skill integrates with LogRocket’s REST API to pull session recordings filtered by user segments, error occurrences, and conversion funnels. FullStory Data Export API integration enables bulk session analysis with custom event tracking. Replay analysis uses automated heuristic detection for rage clicks (3+ clicks within 500ms on same element), dead clicks on non-interactive elements, and excessive scrolling patterns indicating content findability issues. The skill generates UX insight reports with heatmap overlays using canvas-based rendering. Session segments can be exported as MP4 video files using puppeteer-screen-recorder for stakeholder presentations. Integration with Jira API automatically creates UX bug tickets from detected interaction anomalies.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/browser-session-replay-analyzer/)
