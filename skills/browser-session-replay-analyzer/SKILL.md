---
name: Browser Session Replay Analyzer
description: Records and replays browser sessions using rrweb recording library with
  DOM mutation serialization. Integrates with LogRocket API and FullStory Data Export
  API for session analytics.
category: Browser Automation
framework: Custom Agents
verification: security_reviewed
source: "https://agentskillexchange.com/skills/browser-session-replay-analyzer/"
---
# Browser Session Replay Analyzer

Records and replays browser sessions using rrweb recording library with DOM mutation serialization. Integrates with LogRocket API and FullStory Data Export API for session analytics.

The Browser Session Replay Analyzer captures and analyzes user browser sessions for UX research and debugging. It uses the rrweb library to record DOM mutations, mouse movements, scroll positions, and network requests as a serialized event stream with minimal performance overhead. Recorded sessions are compressed using lz-string and stored with metadata tags for filtering. The skill integrates with LogRocket’s REST API to pull session recordings filtered by user segments, error occurrences, and conversion funnels. FullStory Data Export API integration enables bulk session analysis with custom event tracking. Replay analysis uses automated heuristic detection for rage clicks (3+ clicks within 500ms on same element), dead clicks on non-interactive elements, and excessive scrolling patterns indicating content findability issues. The skill generates UX insight reports with heatmap overlays using canvas-based rendering. Session segments can be exported as MP4 video files using puppeteer-screen-recorder for stakeholder presentations. Integration with Jira API automatically creates UX bug tickets from detected interaction anomalies.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill browser-session-replay-analyzer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill browser-session-replay-analyzer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill browser-session-replay-analyzer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill browser-session-replay-analyzer -a codex
```

### OpenClaw

```bash
clawhub install browser-session-replay-analyzer
```


## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/browser-session-replay-analyzer/)
