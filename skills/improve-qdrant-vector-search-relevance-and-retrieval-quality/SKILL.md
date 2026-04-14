---
title: "Improve Qdrant vector search relevance and retrieval quality"
description: "Use Qdrant&#8217;s official qdrant-search-quality skill when an agent needs to diagnose weak recall, irrelevant matches, or embedding and chunking mistakes in a live retrieval pipeline. It is a bounded search-quality tuning workflow, not a generic database listing."
verification: security_reviewed
source: "https://github.com/qdrant/skills/tree/main/skills/qdrant-search-quality"
category:
  - "Runbooks &amp; Diagnostics"
---

# Improve Qdrant vector search relevance and retrieval quality

Use Qdrant&#8217;s official qdrant-search-quality skill when an agent needs to diagnose weak recall, irrelevant matches, or embedding and chunking mistakes in a live retrieval pipeline. It is a bounded search-quality tuning workflow, not a generic database listing.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/improve-qdrant-vector-search-relevance-and-retrieval-quality/)
