---
name: "API Client Generator Skill"
description: "Use this skill to generate typed SDK client code from OpenAPI/Swagger specifications, enabling strongly-typed API interactions without manual HTTP client coding. It creates clients with proper authentication, error handling, and type definitions in target languages. Trigger when integrating a third-party API that has an OpenAPI spec or when standardizing API client generation across a team."
category: "Developer Tools"
framework: "Custom Agents"
verification: listed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/api-client-generator-skill/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "swagger"  # from ase_tool_match
  github_stars: 28702  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 3219093  # from ase_npm_downloads
  github_repo: "swagger-api/swagger-ui"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# API Client Generator Skill

Use this skill to generate typed SDK client code from OpenAPI/Swagger specifications, enabling strongly-typed API interactions without manual HTTP client coding. It creates clients with proper authentication, error handling, and type definitions in target languages. Trigger when integrating a third-party API that has an OpenAPI spec or when standardizing API client generation across a team.

## Overview

Use this skill to generate typed SDK client code from OpenAPI/Swagger specifications, enabling strongly-typed API interactions without manual HTTP client coding. It creates clients with proper authentication, error handling, and type definitions in target languages. Trigger when integrating a third-party API that has an OpenAPI spec or when standardizing API client generation across a team.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill api-client-generator-skill
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill api-client-generator-skill -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill api-client-generator-skill -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill api-client-generator-skill -a codex
```

### OpenClaw

```bash
clawhub install api-client-generator-skill
```

## Source

- Marketplace: https://agentskillexchange.com/skills/api-client-generator-skill/
