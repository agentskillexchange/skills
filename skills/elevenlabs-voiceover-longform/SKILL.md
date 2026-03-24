---
name: "ElevenLabs Voiceover Generator for Long-Form Content"
description: "Splits blog posts or scripts into optimal chunks under ElevenLabs character limits, synthesizes each chunk using the v2 Multilingual model, and stitches MP3 segments together with pydub. Supports custom voice cloning via stored Voice IDs with per-segment stability and similarity tuning. Final audio is uploaded to Cloudflare R2 and a signed URL is returned."
category: "Media & Transcription"
framework: "Claude Code"
verification: listed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/elevenlabs-voiceover-longform/"
tool_ecosystem:
  tool: "cloudflare"
  github_stars: 1946
  npm_weekly_downloads: 1035304
  github_repo: "cloudflare/cloudflare-go"
  license: "Apache-2.0"
  maintained: true
---

# ElevenLabs Voiceover Generator for Long-Form Content

Splits blog posts or scripts into optimal chunks under ElevenLabs character limits, synthesizes each chunk using the v2 Multilingual model, and stitches MP3 segments together with pydub. Supports custom voice cloning via stored Voice IDs with per-segment stability and similarity tuning. Final audio is uploaded to Cloudflare R2 and a signed URL is returned.

## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill elevenlabs-voiceover-longform
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill elevenlabs-voiceover-longform -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill elevenlabs-voiceover-longform -a cursor
```

### OpenClaw
```bash
clawhub install elevenlabs-voiceover-longform
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill elevenlabs-voiceover-longform -a codex
```

## Details

| | |
|---|---|
| **Category** | Media & Transcription |
| **Framework** | Claude Code |
| **Verification** | 📋 Listed |
| **Tool** | [cloudflare](https://github.com/cloudflare/cloudflare-go) — ⭐ 1.9k · Apache-2.0 |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/elevenlabs-voiceover-longform/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
