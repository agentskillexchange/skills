---
title: "Convert HTML emails and web fragments into clean plain text for downstream agents"
description: "Use html-to-text when an agent receives raw HTML from inboxes, support systems, or scraped pages and needs readable plain text before classification, summarization, or indexing. The skill is deliberately bounded to deterministic HTML-to-text conversion, not crawling or summarization."
verification: "security_reviewed"
source: "https://www.npmjs.com/package/html-to-text"
category:
  - "Data Extraction & Transformation"
framework:
  - "Multi-Framework"
tool_ecosystem:
  ase_npm_package: "html-to-text"
  npm_weekly_downloads: 8213869
---

# Convert HTML emails and web fragments into clean plain text for downstream agents

This skill uses html-to-text, the Node.js package for turning HTML into readable plain text with predictable formatting rules. In agent workflows, that matters when the input is an email body, CMS snippet, ticket payload, or scraped page fragment that is still wrapped in tags, tracking links, spacer tables, and layout markup. Instead of asking the model to “mentally ignore the HTML,” an agent can run html-to-text first and hand the next step a cleaner body of text.


The concrete job-to-be-done is preprocessing HTML into a stable, LLM-friendly text representation. A good invocation point is when an automation already has the HTML in hand and needs a normalized plain-text version for summarization, triage, classification, search indexing, or downstream storage. html-to-text supports links, lists, tables, word wrapping, unicode, and selector-based customization, so the agent can keep important structure while dropping presentational noise. That makes it useful for support inbox pipelines, customer-feedback digests, archived newsletter parsing, CRM note cleanup, and webpage-to-text transformations inside larger research jobs.


The scope boundary is important: this is not a crawler, browser renderer, metadata extractor, or summarizer. The skill starts once the HTML has already been collected and ends once clean text has been produced. Integration points are simple: Node.js scripts, npm-based automations, queue workers, webhook handlers, or any agent runtime that can call a JavaScript helper. If the agent needs deterministic cleanup before it reasons over messy HTML, html-to-text is the right tool and the right boundary.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/convert-html-emails-and-web-fragments-into-clean-plain-text-for-downstream-agents/)
