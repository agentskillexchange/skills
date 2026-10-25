---
name: PopNow Video Generation
slug: popnow-video
description: Use the existing MIT-licensed PopNow video skill to quote and create AI videos from text or an image through the commercial PopNow API, confirm the credit cost before generation, poll asynchronous jobs, and download the result.
category: Image & Creative Automation
framework: Multi-Framework
verification: listed
source: https://github.com/popnow-ai/popnow-skills
license: MIT
---

# PopNow Video Generation

This catalog entry points to the existing [official PopNow video skill](https://github.com/popnow-ai/popnow-skills/tree/main/skills/popnow-video). The upstream bundle contains a `SKILL.md`, a Python standard-library helper, and model-reference documentation. Use it when a user wants a short video from a written brief, wants to animate a photo, or needs a supported video extension or upscaling operation. It is not a local video-generation model: the helper calls the commercial PopNow API at `https://api.popnow.ai/api/v1`.

The skill and helper source are MIT-licensed. An authenticated PopNow account, an API key, an internet connection, and sufficient PopNow credits are needed for generation. Finding and installing the skill does not purchase credits. Model availability and prices can change; query the current model schema and quote the exact request rather than promising a fixed price or unsupported option.

## Installation

Install the complete upstream `popnow-video` bundle so its helper and references stay together. Do not treat this catalog overview as a replacement for those files.

For an agent supported by the upstream installer, follow the [upstream setup instructions](https://github.com/popnow-ai/popnow-skills#quickstart). A manual installation for Codex is:

```bash
git clone https://github.com/popnow-ai/popnow-skills.git
mkdir -p ~/.agents/skills/popnow-video
cp -R popnow-skills/skills/popnow-video/. ~/.agents/skills/popnow-video/
```

Read the installed `SKILL.md` and inspect the helper before using it. The REST helper needs Python 3. The alternative connected PopNow MCP server uses the remote endpoint documented at [popnow.ai/mcp](https://popnow.ai/mcp). Keep the upstream MIT notice with the bundle.

## Workflow and boundaries

1. Ask for the intended subject, motion, duration and supplied image when relevant. Keep content suitable for a general audience.
2. Read the selected model's live fields. Use the text-to-video model for a text brief and its image-to-video variant for a supplied photo.
3. Quote the exact request with the upstream helper. Tell the user the credit cost and wait for a clear confirmation before creating a paid job. Pass the confirmed maximum to `create --confirm-credits`; if the price increases, quote again and ask again.
4. Poll the asynchronous job and report its actual state. Download successful output promptly because signed result links expire. Do not describe a queued or failed task as a finished video.
5. Keep `POPNOW_API_KEY` in the user's environment. Never publish or echo a key, request that the user paste one into chat, or send it to a storage download host.

Full current commands, error handling and examples are maintained in the [upstream skill](https://github.com/popnow-ai/popnow-skills/blob/main/skills/popnow-video/SKILL.md). Official product and API documentation: [PopNow](https://popnow.ai), [API docs](https://popnow.ai/docs). This submission is a catalog inclusion request, with `verification: listed`; it does not claim an ASE security review or endorsement.
