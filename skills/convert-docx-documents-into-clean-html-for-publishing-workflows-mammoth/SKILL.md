---
name: Convert DOCX documents into clean HTML for publishing workflows with Mammoth
description: Use Mammoth when an agent needs to turn a .docx file into simple HTML
  that preserves semantic structure instead of Word-specific styling. This is for
  ingestion and publishing workflows, not for full document editing or perfect visual
  fidelity.
verification: listed
source: https://github.com/mwilliamson/mammoth.js
category:
- Data Extraction &amp; Transformation
framework:
- Multi-Framework
tool_ecosystem:
  github_repo: mwilliamson/mammoth.js
  github_stars: 6163
---
# Convert DOCX documents into clean HTML for publishing workflows with Mammoth

Tool used: Mammoth (mwilliamson/mammoth.js).

This skill is for an agent that receives Microsoft Word .docx files and needs to convert them into clean HTML for a publishing or content-ingestion pipeline. The agent uses Mammoth to extract headings, lists, links, images, and other semantic structure from the source document, then hands the resulting HTML to the next system in the workflow, such as a CMS importer, a markdown cleanup step, or a review queue. The job-to-be-done is not “use a document converter.” It is “take an authored Word document and turn it into web-ready markup with minimal presentation junk.”

Invoke this when the user already has content in .docx and wants an automation step that converts it into clean output for websites, knowledge bases, newsletters, or editorial review. Do not invoke it just because Mammoth exists as a package. Use it when the agent’s job is specifically to ingest .docx content, preserve semantic meaning where possible, and feed that output into a broader automation. If the user needs round-trip editing, pixel-perfect rendering, or broad format conversion beyond Word-to-HTML, this is out of scope.

The boundary matters. Mammoth is not being listed here as a generic library card. The skill is narrowly about document-ingestion behavior: accept a .docx, convert it to simple HTML, note that complex formatting may not survive perfectly, and pass the normalized result onward. Typical integration points include Node.js automation, CMS publishing flows, static site generators, editorial pipelines, and post-processing steps that sanitize or transform the produced HTML.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/convert-docx-documents-into-clean-html-for-publishing-workflows-mammoth/)
