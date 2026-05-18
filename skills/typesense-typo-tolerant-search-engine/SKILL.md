---
name: "Typesense Typo-Tolerant Search Engine"
slug: "typesense-typo-tolerant-search-engine"
description: "Typesense is an open-source, typo-tolerant search engine built in C++ for building fast, relevant search experiences. It serves as a self-hostable alternative to Algolia with support for vector search, geo-search, and faceted filtering."
github_stars: 25500
verification: "listed"
source: "https://github.com/typesense/typesense"
category: "Data Extraction & Transformation"
framework: "Custom Agents"
tool_ecosystem:
  github_repo: "typesense/typesense"
  github_stars: 25500
---

# Typesense Typo-Tolerant Search Engine

Typesense is an open-source, typo-tolerant search engine built in C++ for building fast, relevant search experiences. It serves as a self-hostable alternative to Algolia with support for vector search, geo-search, and faceted filtering.

## Installation

Use the upstream install or setup path that matches your environment:
- docker run -p 8108:8108 -v/tmp/data:/data typesense/typesense:29.0 --data-dir /data --api-key=Hu52dwsas2AdxdE
- pip install typesense

Requirements and caveats from upstream:
- <a href="https://hub.docker.com/r/typesense/typesense/tags"><img src="https://img.shields.io/docker/pulls/typesense/typesense"></a>
- With a dataset containing **3 Million products** (Amazon product data), Typesense was able to handle a throughput of **250 concurrent search queries per second** on an 8-vCPU 3-node Highly Available Typesense cluster.
- On Typesense Cloud we serve more than **10 BILLION** searches per month. Typesense's Docker images have been downloaded over 12M times.

Basic usage or getting-started notes:
- [Quick Start](#quick-start)
- **No Runtime Dependencies:** Typesense is a single binary that you can run locally or in production with a single command.
- **Option 1:** You can download the [binary packages](https://typesense.org/downloads) that we publish for

- Source: https://github.com/typesense/typesense
- Extracted from upstream docs: https://raw.githubusercontent.com/typesense/typesense/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/typesense-typo-tolerant-search-engine/)
