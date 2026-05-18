---
name: "Inline CSS into HTML emails before delivery across mail clients with Juice"
slug: "inline-css-into-html-emails-before-delivery-across-mail-clients-juice"
description: "Use Juice when an agent already has finished HTML and needs it transformed into email-safe output before sending, archiving, or handing off to another system. The skill inlines stylesheet rules into element style attributes so downstream mail clients and embedded contexts keep the intended presentation without manual cleanup."
github_stars: 3245
verification: "listed"
source: "https://github.com/Automattic/juice"
author: "Automattic"
publisher_type: "organization"
category: "Calendar, Email & Productivity"
framework: "Custom Agents"
tool_ecosystem:
  github_repo: "Automattic/juice"
  github_stars: 3245
---

# Inline CSS into HTML emails before delivery across mail clients with Juice

Use Juice when an agent already has finished HTML and needs it transformed into email-safe output before sending, archiving, or handing off to another system. The skill inlines stylesheet rules into element style attributes so downstream mail clients and embedded contexts keep the intended presentation without manual cleanup.

## Prerequisites

Node.js

## Installation

Requirements and caveats from upstream:
- Attempting to Browserify require('juice') fails because portions of Juice and its dependencies interact with the file system using the standard require('fs'). However, you can require('juice/client') via Browserify wh...

Basic usage or getting-started notes:
- For example, Handlebars (hbs) templates are juice.codeBlocks.HBS = {start: '{{', end: '}}'}. codeBlocks can fix problems where otherwise juice might interpret code like <= as HTML, when it is meant to be template lang...
- To use Juice from CLI, run juice [options] input.html output.html
- The CLI should have all the above [options](#options) with the names changed from camel case to hyphen-delimited, so for example extraCss becomes extra-css and webResources.scripts becomes web-resources-scripts.

- Source: https://github.com/Automattic/juice
- Extracted from upstream docs: https://raw.githubusercontent.com/Automattic/juice/HEAD/README.md

## Documentation

- https://github.com/Automattic/juice#readme

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/inline-css-into-html-emails-before-delivery-across-mail-clients-juice/)
