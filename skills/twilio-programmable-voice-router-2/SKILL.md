---
name: "Twilio Programmable Voice Router"
description: "Builds intelligent voice routing flows using the Twilio Programmable Voice API. Generates TwiML responses with , , and verbs, and manages call recordings via the Recordings REST resource."
category: "Integrations & Connectors"
framework: "Claude Agents"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/twilio-programmable-voice-router-2/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "twilio"  # from ase_tool_match
  github_stars: 1523  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 3810383  # from ase_npm_downloads
  github_repo: "twilio/twilio-node"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Twilio Programmable Voice Router

Builds intelligent voice routing flows using the Twilio Programmable Voice API. Generates TwiML responses with , , and verbs, and manages call recordings via the Recordings REST resource.

## Overview

The Twilio Programmable Voice Router creates sophisticated call handling workflows using Twilio’s Programmable Voice API. It generates dynamic TwiML documents that chain for DTMF/speech input, for call forwarding with SIP and Client endpoints, and for queue-based routing.

The skill manages the full call lifecycle: incoming call webhook handling, real-time call modification via the Calls resource (`client.calls(sid).update()`), and post-call recording retrieval through the Recordings REST API. It supports conference bridges with verb including mute/hold controls.

Advanced features include StatusCallback URL configuration for call progress events, AMD (Answering Machine Detection) with `machineDetection: 'DetectMessageEnd'`, and fallback URL routing. The agent handles Twilio signature validation using `twilio.webhook()` middleware for request authentication. Integrates with Twilio Studio for visual IVR flow management.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill twilio-programmable-voice-router-2
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill twilio-programmable-voice-router-2 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill twilio-programmable-voice-router-2 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill twilio-programmable-voice-router-2 -a codex
```

### OpenClaw

```bash
clawhub install twilio-programmable-voice-router-2
```

## Source

- Marketplace: https://agentskillexchange.com/skills/twilio-programmable-voice-router-2/
