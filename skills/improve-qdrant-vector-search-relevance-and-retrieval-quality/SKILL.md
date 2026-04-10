---
name: Improve Qdrant vector search relevance and retrieval quality
description: Use Qdrant&#8217;s official qdrant-search-quality skill when an agent
  needs to diagnose weak recall, irrelevant matches, or embedding and chunking mistakes
  in a live retrieval pipeline. It is a bounded search-quality tuning workflow, not
  a generic database listing.
verification: listed
source: https://github.com/qdrant/skills/tree/main/skills/qdrant-search-quality
category:
- Runbooks &amp; Diagnostics
framework:
- Multi-Framework
tool_ecosystem:
  github_repo: qdrant/skills
  github_stars: 60
---
# Improve Qdrant vector search relevance and retrieval quality

Tool name: Qdrant Search Quality, from Qdrant's official skills repository.
This is a real job-to-be-done entry, not a product card. The agent's task is to diagnose why a Qdrant-backed retrieval system is returning poor results and improve it using a structured workflow. The upstream skill explicitly tells the agent to separate embedding-model issues from Qdrant configuration issues and from query-strategy issues before changing parameters. It also calls out a concrete failure mode, poor chunking, as a common cause of degraded search quality.
Use this when a user reports bad semantic search results, low precision, low recall, irrelevant matches, missing expected documents, quality regressions after a model swap, or confusion about when to use exact search, hybrid search, reranking, or relevance feedback. This is the right invocation when the user wants an agent to investigate and tune retrieval quality, not when they simply need to install Qdrant, browse the API, or compare vector databases.
The scope boundary is tight. This entry is about search quality diagnosis and remediation only. It is not a general Qdrant deployment guide, SDK overview, cluster administration reference, or product introduction. The agent should stay within retrieval relevance work: evaluating chunks, testing exact search, checking embedding choices, and selecting better query strategies. If the need is scaling, monitoring, or version upgrades, those are separate jobs.
Integration points include RAG systems, semantic search applications, support bots, internal knowledge search, and any pipeline that sends embeddings into Qdrant. Source-backed evidence is solid: official repo, license, active commits, and explicit skill documentation. Adoption also clears the bar through repo stars and recent maintenance.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/improve-qdrant-vector-search-relevance-and-retrieval-quality/)
