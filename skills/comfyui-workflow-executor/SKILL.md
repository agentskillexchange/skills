---
name: "ComfyUI Workflow Executor"
description: "Executes ComfyUI image generation workflows via the /prompt REST API endpoint with WebSocket progress tracking. Manages node graph JSON payloads, KSampler scheduler configurations (euler_ancestral, dpmpp_2m_sde), and output image retrieval from the /view endpoint."
category: "Image & Creative Automation"
framework: "Codex"
verification: security_reviewed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/comfyui-workflow-executor/"
tool_ecosystem:
  tool: "vault"
  github_stars: 35266
  npm_weekly_downloads: 0
  github_repo: "hashicorp/vault"
  license: "NOASSERTION"
  maintained: true
---

# ComfyUI Workflow Executor

Executes ComfyUI image generation workflows via the /prompt REST API endpoint with WebSocket progress tracking. Manages node graph JSON payloads, KSampler scheduler configurations (euler_ancestral, dpmpp_2m_sde), and output image retrieval from the /view endpoint.

## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill comfyui-workflow-executor
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill comfyui-workflow-executor -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill comfyui-workflow-executor -a cursor
```

### OpenClaw
```bash
clawhub install comfyui-workflow-executor
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill comfyui-workflow-executor -a codex
```

## Details

| | |
|---|---|
| **Category** | Image & Creative Automation |
| **Framework** | Codex |
| **Verification** | 🛡️ Security Reviewed |
| **Tool** | [vault](https://github.com/hashicorp/vault) — ⭐ 35.3k · NOASSERTION |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/comfyui-workflow-executor/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
