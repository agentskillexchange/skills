---
title: "Co-author structured docs with staged context gathering and reader testing"
description: "Use Anthropic’s doc-coauthoring skill to run a disciplined writing workflow instead of freeform drafting. The agent gathers missing context, iterates section by section, and pressure-tests the final document with reader-style review before teammates see it."
verification: security_reviewed
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

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/co-author-structured-docs-with-staged-context-gathering-and-reader-testing/)
