---
title: "Improve Qdrant vector search relevance and retrieval quality"
description: "Use Qdrant’s official qdrant-search-quality skill when an agent needs to diagnose weak recall, irrelevant matches, or embedding and chunking mistakes in a live retrieval pipeline. It is a bounded search-quality tuning workflow, not a generic database listing."
verification: "security_reviewed"
source: "https://github.com/qdrant/skills/tree/main/skills/qdrant-search-quality"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Multi-Framework"
---

# Improve Qdrant vector search relevance and retrieval quality

Use Qdrant’s official qdrant-search-quality skill when an agent needs to diagnose weak recall, irrelevant matches, or embedding and chunking mistakes in a live retrieval pipeline. It is a bounded search-quality tuning workflow, not a generic database listing.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/improve-qdrant-vector-search-relevance-and-retrieval-quality/)
