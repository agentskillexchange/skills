---
name: "ACF Custom Fields REST Exposer"
description: "Exposes Advanced Custom Fields data through the WordPress REST API using register_rest_field and acf_format_value. Handles repeater fields, flexible content layouts, and gallery fields with proper serialization."
category: "WordPress & CMS"
framework: "Cursor"
verification: "community"
rating: "0"
reviews: "0"
creator: "Community"
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skill/acf-custom-fields-rest-exposer/"
---

# ACF Custom Fields REST Exposer

Exposes Advanced Custom Fields data through the WordPress REST API using register_rest_field and acf_format_value. Handles repeater fields, flexible content layouts, and gallery fields with proper serialization.

## Installation

Install this skill in your agent framework of choice:

### npx (Any Agent)
```bash
npx agentskills install acf-custom-fields-rest-exposer
```

### Claude Code
```bash
claude mcp add skill-acf-custom-fields-rest-exposer -- npx agentskills run acf-custom-fields-rest-exposer
```

### Cursor
Add to your `.cursor/mcp.json`:
```json
{
  "mcpServers": {
    "skill-acf-custom-fields-rest-exposer": {
      "command": "npx",
      "args": ["agentskills", "run", "acf-custom-fields-rest-exposer"]
    }
  }
}
```

### OpenClaw
```bash
clawhub install acf-custom-fields-rest-exposer
```

### Codex
```bash
codex install acf-custom-fields-rest-exposer
```

## Details

| | |
|---|---|
| **Category** | WordPress & CMS |
| **Framework** | Cursor |
| **Verification** | community |
| **Rating** | 0 ⭐ (0 reviews) |

## Creator

**Community**


## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skill/acf-custom-fields-rest-exposer/)
- [Browse All Skills](https://agentskillexchange.com/)
