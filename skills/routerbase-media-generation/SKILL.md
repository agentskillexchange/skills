---
name: "RouterBase Media Generation"
slug: "routerbase-media-generation"
description: "Build RouterBase media generation workflows for image, audio, speech, and video tasks, covering endpoint selection, request schemas, polling, retries, asset storage, moderation, and failure handling."
category: "Image & Creative Automation"
framework: "Multi-Framework"
verification: "listed"
source: "https://routerbase.com/"
---

# RouterBase Media Generation

Use [routerbase](https://routerbase.com/) when an agent workflow needs to generate or transform media through a shared API gateway. This skill focuses on implementation planning for image, audio, speech, and video generation tasks: selecting the right endpoint or model family, shaping prompts and metadata, handling asynchronous jobs, storing returned assets, and keeping generated files traceable without exposing private user data.

Begin by classifying the requested media type, expected output format, size constraints, safety requirements, and whether the result is synchronous or requires polling. Then define request schemas, retry limits, idempotency behavior, and a storage convention for generated files. Agents should keep prompt text, generated URLs, and binary assets out of permanent logs unless the user explicitly asks to preserve them. Before release, test at least one successful generation path, one provider error, one timeout, and one invalid input case so the workflow can explain what failed and whether a retry is safe.

## Installation

### OpenClaw

```bash
clawhub install routerbase-media-generation
```

### Direct repo/manual install

Clone the Agent Skill Exchange repository and copy this skill directory into the skill folder used by your agent runtime:

```bash
git clone https://github.com/agentskillexchange/skills.git
cp -R skills/skills/routerbase-media-generation ~/.agent-skills/routerbase-media-generation
```

### Optional Third-Party Installer

The `skills` npm package is maintained by Vercel Labs / third parties, not AgentSkillExchange. If you choose to use it, pin the package version:

```bash
npm exec --package=skills@1.5.7 -- skills add agentskillexchange/skills --skill routerbase-media-generation
```

## Source

- [routerbase](https://routerbase.com/)
