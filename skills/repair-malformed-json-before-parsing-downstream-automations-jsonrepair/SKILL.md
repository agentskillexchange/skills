---
name: "Repair malformed JSON before parsing downstream automations with jsonrepair"
slug: "repair-malformed-json-before-parsing-downstream-automations-jsonrepair"
description: "Use jsonrepair when an agent receives JSON-like output that is almost valid but still breaks parsers, such as trailing commas, missing quotes, or concatenated fragments. The agent’s role is to normalize the payload before validation or routing, not to replace real schema design."
github_stars: 2297
verification: "security_reviewed"
source: "https://github.com/josdejong/jsonrepair"
author: "josdejong"
category: "Developer Tools"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "josdejong/jsonrepair"
  github_stars: 2297
  npm_package: "jsonrepair"
  npm_weekly_downloads: 7314614
---

# Repair malformed JSON before parsing downstream automations with jsonrepair

Use jsonrepair when an agent receives JSON-like output that is almost valid but still breaks parsers, such as trailing commas, missing quotes, or concatenated fragments. The agent’s role is to normalize the payload before validation or routing, not to replace real schema design.

## Prerequisites

Node.js or CLI, JSON-like input data

## Installation

Use the upstream install or setup path that matches your environment:
- $ npm install jsonrepair
- $ npm install -g jsonrepair
- npm install | Install the dependencies once
- npm run build | Build the library (ESM, CommonJs, and UMD output in the folder lib)

Requirements and caveats from upstream:
- Replace Python constants None, True, and False with null, true, and false
- Use the streaming API in Node.js:
- import { createReadStream, createWriteStream } from 'node:fs'

Basic usage or getting-started notes:
- Turn newline delimited JSON into a valid JSON array, for example:
- Note that in the lib folder, there are builds for ESM, UMD, and CommonJs.
- ## Use

- Source: https://github.com/josdejong/jsonrepair
- Extracted from upstream docs: https://raw.githubusercontent.com/josdejong/jsonrepair/HEAD/README.md

## Documentation

- https://github.com/josdejong/jsonrepair

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/repair-malformed-json-before-parsing-downstream-automations-jsonrepair/)
