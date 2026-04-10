---
name: "sqlite-vec Vector Search Extension for SQLite"
description: "sqlite-vec is a lightweight SQLite extension for vector similarity search. Written in pure C with zero dependencies, it runs anywhere SQLite runs—Linux, macOS, Windows, WASM in browsers, and Raspberry Pis—and supports float, int8, and binary vector storage."
verification: security_reviewed
source: "https://github.com/asg017/sqlite-vec"
category:
  - "Developer Tools"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "asg017/sqlite-vec"
  github_stars: 7331
  ase_npm_package: "sqlite-vec"
  npm_weekly_downloads: 1425917
---

# sqlite-vec Vector Search Extension for SQLite

What is sqlite-vec?
sqlite-vec is an extremely small, dependency-free SQLite extension that adds vector similarity search capabilities to any SQLite database. Created by Alex Garcia and sponsored by Mozilla Builders, Fly.io, and Turso, it is the successor to sqlite-vss. Written in pure C, sqlite-vec compiles and runs anywhere SQLite runs: Linux, macOS, Windows, in the browser via WASM, on Raspberry Pis, and on mobile devices.
The extension uses vec0 virtual tables to store and query float, int8, and binary vectors. It supports KNN (k-nearest-neighbor) queries using the MATCH operator with distance ordering, and allows storing non-vector metadata in auxiliary columns alongside embeddings.
How It Works
After loading the extension with .load ./vec0, create a virtual table specifying the vector dimensions: CREATE VIRTUAL TABLE embeddings USING vec0(sample_embedding float[384]). Insert vectors as JSON arrays or in a compact binary format. Query with standard SQL using the MATCH clause to find nearest neighbors, ordering by distance and limiting results. The extension handles all the indexing internally.
sqlite-vec integrates with popular data tools. Datasette users install via datasette install datasette-sqlite-vec. sqlite-utils users add it with sqlite-utils install sqlite-utils-sqlite-vec. The extension also supports rqlite for distributed deployments. Partition key columns enable sharding vectors across logical groups for more efficient filtered queries.
Language Bindings and Adoption
Install in Python (pip install sqlite-vec), Node.js (npm install sqlite-vec), Ruby (gem install sqlite-vec), Go, or Rust (cargo add sqlite-vec). Documentation is available at alexgarcia.xyz/sqlite-vec. The project has over 7,200 GitHub stars, is Apache-2.0 licensed, and is used in production by projects like ScreenPipe for local AI search. It enables building fully local, privacy-preserving semantic search without external vector database dependencies.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sqlite-vec-vector-search-extension-sqlite/)
