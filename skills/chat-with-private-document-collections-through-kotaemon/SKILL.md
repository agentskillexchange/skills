---
title: "Chat with private document collections through Kotaemon"
description: "Run a self-hosted Kotaemon document QA workflow so agents can index private files, ask grounded questions, and return cited answers."
verification: "security_reviewed"
source: "https://github.com/Cinnamon/kotaemon"
author: "Cinnamon"
publisher_type: "organization"
category:
  - "Data Extraction & Transformation"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "Cinnamon/kotaemon"
  github_stars: 25448
---

# Chat with private document collections through Kotaemon

Run a self-hosted Kotaemon document QA workflow so agents can index private files, ask grounded questions, and return cited answers.

## Prerequisites

Docker or Python environment, Kotaemon, document collection to index, configured LLM provider or local model such as Ollama

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Follow the Kotaemon user guide or run the documented Docker image from ghcr.io/cinnamon/kotaemon, configure the desired LLM and retrieval settings, then create collections and upload documents before running cited QA sessions.
```

## Documentation

- https://cinnamon.github.io/kotaemon/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/chat-with-private-document-collections-through-kotaemon/)
