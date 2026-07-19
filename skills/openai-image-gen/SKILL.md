---
name: "OpenAI Image Gen"
slug: "openai-image-gen"
description: "Batch-generate images through the OpenAI Images API with a prompt sampler and gallery output."
github_stars: 10942
verification: "security_reviewed"
source: "https://github.com/openai/openai-node"
author: "OpenAI"
publisher_type: "open_source_collective"
category: "Image & Creative Automation"
framework: "OpenClaw"
tool_ecosystem:
  github_repo: "openai/openai-node"
  github_stars: 10942
  npm_package: "openai"
  npm_weekly_downloads: 26927983
---

# OpenAI Image Gen

Batch-generate images through the OpenAI Images API with a prompt sampler and gallery output.

## Prerequisites

Node.js, npm

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

## Documentation

- https://platform.openai.com/docs/api-reference

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/openai-image-gen/)
