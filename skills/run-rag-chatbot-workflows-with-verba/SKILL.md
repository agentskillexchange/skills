---
title: "Run RAG chatbot workflows with Verba"
description: "Ingest a bounded document set into Verba, configure retrieval and model providers, then review grounded chatbot answers before handing context to an agent workflow."
verification: "security_reviewed"
source: "https://github.com/weaviate/Verba"
author: "Weaviate"
publisher_type: "open-source organization"
category:
  - "Data Extraction & Transformation"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "weaviate/Verba"
  github_stars: 7716
---

# Run RAG chatbot workflows with Verba

Ingest a bounded document set into Verba, configure retrieval and model providers, then review grounded chatbot answers before handing context to an agent workflow.

## Prerequisites

Verba, Python 3.10 through 3.12 or Docker, Weaviate embedded/cloud/Docker deployment, configured model and embedding provider keys as needed.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install with `pip install goldenverba`, optionally create a `.env` file with only the provider keys you intend to use, then run `verba start`. For Docker, clone https://github.com/weaviate/Verba and run `docker compose --env-file <your-env-file> up -d --build`.
```

## Documentation

- https://github.com/weaviate/Verba

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-rag-chatbot-workflows-with-verba/)
