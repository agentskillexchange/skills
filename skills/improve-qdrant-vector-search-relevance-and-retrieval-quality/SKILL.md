---
title: "Improve Qdrant vector search relevance and retrieval quality"
description: "Use Qdrant’s official qdrant-search-quality skill when an agent needs to diagnose weak recall, irrelevant matches, or embedding and chunking mistakes in a live retrieval pipeline. It is a bounded search-quality tuning workflow, not a generic database listing."
verification: "security_reviewed"
source: "https://github.com/qdrant/skills/tree/main/skills/qdrant-search-quality"
category: ["Runbooks &amp; Diagnostics"]
framework: ["Multi-Framework"]
---

# Improve Qdrant vector search relevance and retrieval quality

Use Qdrant’s official qdrant-search-quality skill when an agent needs to diagnose weak recall, irrelevant matches, or embedding and chunking mistakes in a live retrieval pipeline. It is a bounded search-quality tuning workflow, not a generic database listing.

## Installation

Choose the install path that fits your setup:

1. Install from the Agent Skill Exchange catalog if your agent client supports it.
2. Copy the skill folder into your local skills directory.
3. Add it as a git submodule in your shared agent-skills repo.
4. Vendor the files directly into a project-specific `.agents/skills/` or equivalent folder.
5. Keep a fork or mirror if you need local modifications or pinned revisions.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/improve-qdrant-vector-search-relevance-and-retrieval-quality/)
