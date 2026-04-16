---
title: "Co-author structured docs with staged context gathering and reader testing"
description: "Use Anthropic’s doc-coauthoring skill to run a disciplined writing workflow instead of freeform drafting. The agent gathers missing context, iterates section by section, and pressure-tests the final document with reader-style review before teammates see it."
verification: "security_reviewed"
source: "https://github.com/anthropics/skills/tree/main/skills/doc-coauthoring"
category:
  - "Templates &amp; Workflows"
framework:
  - "Claude Agents"
tool_ecosystem:
  github_repo: "anthropics/skills"
  github_stars: 116918
---

# Co-author structured docs with staged context gathering and reader testing

Anthropic’s doc-coauthoring skill is a real, source-backed workflow for drafting substantial documents with an agent instead of treating the model like a generic text box. The agent does three specific jobs in sequence: it gathers the missing context behind the document, shapes that context into a clear structure section by section, and then performs reader-style testing to catch gaps before the document is shared. That is the concrete job-to-be-done here. The agent is not just “a writing tool.” It behaves like a co-author that closes context gaps, proposes structure, asks targeted clarifying questions, and checks whether the draft will still make sense to someone who was not in the room.

This should be invoked when a user is writing an RFC, proposal, design doc, decision memo, PRD, or other structured document where hidden assumptions are the real failure mode. It is more useful than using a product normally when the challenge is not raw typing, but transferring team context into a document that other people can actually understand and critique. The skill specifically supports information dumps, linked source material, iterative section refinement, and final reader testing. That makes it a better fit for serious documentation work than a generic editor or a plain prompt asking for “a draft.”

The scope boundary is what keeps this from being a product card. The entry is not listing Claude, a word processor, or a generic documentation platform. It is documenting a narrow operator workflow from Anthropic’s skill repository: staged context gathering, guided co-authoring, and reader validation for structured docs. Integration points include shared docs, pasted notes, uploaded files, and connected sources such as team chats or document stores when those are available. Hide the upstream name and the workflow still stands on its own, which is exactly the bar this catalog should enforce.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/co-author-structured-docs-with-staged-context-gathering-and-reader-testing/)
