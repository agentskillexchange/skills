---
name: "ImagineVid AI Generation"
slug: "imaginevid-ai-generation"
description: "Use ImagineVid's OAuth-protected MCP and CLI tools to discover and safely run current image, video, and music generation capabilities."
verification: "listed"
source: "https://github.com/imagineVid/agent-skills/tree/main/skills/imaginevid-ai-generation"
category: "Image & Creative Automation"
framework: "MCP"
---

# ImagineVid AI Generation

Use this Skill when a user wants to create an AI image, video, or music track
through the [ImagineVid AI generation platform](https://imaginevid.io/). It
connects an agent to ImagineVid's OAuth-protected, provider-neutral capability
catalog instead of hard-coding individual model providers. The public source
and complete workflow are available at
https://github.com/imagineVid/agent-skills/tree/main/skills/imaginevid-ai-generation.

## Installation

Clone the public Skill package and copy the skill folder into the host's local
skills directory:

```bash
git clone https://github.com/imagineVid/agent-skills.git
cp -R agent-skills/skills/imaginevid-ai-generation ~/.agent-skills/imaginevid-ai-generation
```

Then connect the host to the ImagineVid remote MCP endpoint through its OAuth
flow:

```text
https://imaginevid.io/api/mcp
```

Do not ask users to paste access tokens, cookies, or provider credentials.

## Workflow

1. Call `models_list` and select a capability ID returned by the live catalog.
2. Upload local media through a trusted host surface and pass only the owned
   `assetId` values returned by that surface.
3. Call `generation_quote` with the selected capability, prompt, values, and
   assets. Treat the server quote and normalized request as authoritative.
4. Show the capability, important inputs, and exact credit quote. Ask the
   human for explicit approval before any credit-consuming operation.
5. Call `generation_create` once with the approved quote and a stable,
   idempotent request ID. Never retry an ambiguous submission automatically.
6. Poll the owned result with `generation_get` and report only safe status,
   errors, and result metadata returned by the server.

## Safety

Generation can consume user credits. A vague request to generate is not enough
to authorize spending. Stop on `insufficient_credits`, `forbidden_scope`, or
invalid input. Treat `submission_unknown` as non-retryable and continue polling
the durable generation when one is available. Never expose provider endpoints,
callback URLs, local filesystem paths, raw tokens, or private account data.
