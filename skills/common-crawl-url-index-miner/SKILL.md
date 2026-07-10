---
name: "Common Crawl URL Index Miner"
slug: "common-crawl-url-index-miner"
description: "Queries the Common Crawl Index API and CC-MAIN collections to surface historical URL coverage, MIME types, and crawl snapshots at scale. Handy for research workflows that need broad web recall without building a full crawler from scratch."
github_stars: 127
verification: "security_reviewed"
source: "https://github.com/commoncrawl/cc-index-table"
author: "commoncrawl"
category: "Research & Scraping"
framework: "MCP"
tool_ecosystem:
  github_repo: "commoncrawl/cc-index-table"
  github_stars: 127
---

# Common Crawl URL Index Miner

Queries the Common Crawl Index API and CC-MAIN collections to surface historical URL coverage, MIME types, and crawl snapshots at scale. Handy for research workflows that need broad web recall without building a full crawler from scratch.

## Installation

Use the upstream install or setup path that matches your environment:
- docker build . -t cc-index-table
- docker run --rm -ti cc-index-table --help
- docker run --rm --entrypoint=/opt/spark/bin/spark-submit cc-index-table
- docker run --mount=type=bind,source=/tmp/data,destination=/data --rm cc-index-table /data/in /data/out

Requirements and caveats from upstream:
- ## Building and running using Docker
- A [Dockerfile](./Dockerfile) is provided to compile the project and run the Spark job in a Docker container.
- build the Docker image:

Basic usage or getting-started notes:
- This projects provides a comprehensive set of example queries (SQL) and also Java code to fetch and process the WARC records matched by a SQL query.
- Run mvn spotless:check and mvn spotless:apply, see the [Spotless Maven guide](https://github.com/diffplug/spotless/blob/main/plugin-maven/README.md). Java formatting rules are defined in [eclipse-formatter.xml](eclips...
- run the table converter tool, here showing the command-line help (--help):

- Source: https://github.com/commoncrawl/cc-index-table
- Extracted from upstream docs: https://raw.githubusercontent.com/commoncrawl/cc-index-table/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/common-crawl-url-index-miner/)
