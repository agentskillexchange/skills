---
name: "BeachFinder Swim Spot Finder"
slug: "beachfinder-swim-spot-finder"
description: "Finds and compares 184,900 swimming spots worldwide (beaches, lakes, bathing places) with live water temperature, wind, UV and wave signals, local guides and source-backed activity providers, via the public BeachFinder MCP server."
verification: "listed"
source: "https://getbeachfinder.com"
category: "Integrations & Connectors"
framework: "Multi-Framework"
---

# BeachFinder Swim Spot Finder

Routes beach, swimming, surf, dive, snorkel, whitewater, vanlife and coastal-provider
requests to the public [BeachFinder](https://getbeachfinder.com) MCP server: search
and compare 184,900 swimming spots worldwide, pull live weather, water temperature,
wind, UV and wave planning signals for the top results, read localized guides, and
find source-backed local activity providers.

The skill picks the narrowest useful tool (nearby/family search, surf, dive/snorkel,
river/whitewater, vanlife, providers, guides, live conditions, or a 2-5 spot
comparison), passes the right language code out of 14 supported languages, respects
BeachFinder's provider verification tiers (`owner_verified`, `source_backed`,
`mapped`), and never declares a spot safe to swim — it defers to official closures,
flags, lifeguards and local authorities. Every result links back to
[getbeachfinder.com](https://getbeachfinder.com).

## Installation

### OpenClaw

```bash
clawhub install beachfinder-swim-spot-finder
```

### Direct repo/manual install

Clone the Agent Skill Exchange repository and copy this skill directory into the
skill folder used by your agent runtime:

```bash
git clone https://github.com/agentskillexchange/skills.git
cp -R skills/skills/beachfinder-swim-spot-finder ~/.agent-skills/beachfinder-swim-spot-finder
```

### Requirements

Requires the public BeachFinder MCP server (no API key, no account):

```json
{
  "mcpServers": {
    "beachfinder": { "type": "http", "url": "https://getbeachfinder.com/mcp" }
  }
}
```

Full skill source, references and the OpenAI-runtime manifest:
https://github.com/troulin-a11y/beachfinder-skills
