---
name: "DALL-E Batch Image Generator"
slug: "dalle-batch-image-generator"
description: "Generates and manages batch image creation jobs using the OpenAI Images API /v1/images/generations endpoint. Supports DALL-E 3 with size, quality, and style parameters plus automatic prompt revision tracking."
github_stars: 10813
verification: "listed"
source: "https://github.com/openai/openai-node"
category: "Image & Creative Automation"
framework: "Claude Agents"
tool_ecosystem:
  github_repo: "openai/openai-node"
  github_stars: 10813
  npm_package: "openai"
  npm_weekly_downloads: 18107622
---

# DALL-E Batch Image Generator

Generates and manages batch image creation jobs using the OpenAI Images API /v1/images/generations endpoint. Supports DALL-E 3 with size, quality, and style parameters plus automatic prompt revision tracking.

## Installation

Use the upstream install or setup path that matches your environment:
- npm install openai
- npx jsr add @openai/openai

Requirements and caveats from upstream:
- The full API of this library can be found in [api.md file](api.md) along with many [code examples](https://github.com/openai/openai-node/tree/master/examples).
- // If you have access to Node fs we recommend using fs.createReadStream():
- await client.chat.completions.create({ messages: [{ role: 'user', content: 'How can I list all files in a directory using Python?' }], model: 'gpt-5.2' }, {

Basic usage or getting-started notes:
- sh
- deno add jsr:@openai/openai
- These commands will make the module importable from the @openai/openai scope. You can also [import directly from JSR](https://jsr.io/docs/using-packages#importing-with-jsr-specifiers) without an install step if you're...

- Source: https://github.com/openai/openai-node
- Extracted from upstream docs: https://raw.githubusercontent.com/openai/openai-node/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dalle-batch-image-generator/)
