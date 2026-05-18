---
name: "Gorse AI-Powered Open Source Recommender System Engine"
slug: "gorse-ai-recommender-system-engine"
description: "Gorse is an AI-powered open-source recommender system written in Go that generates personalized recommendations via collaborative filtering, item-to-item similarity, and LLM-based ranking. It provides RESTful APIs and a GUI dashboard for recommendation pipeline editing, system monitoring, and data management."
github_stars: 9600
verification: "listed"
source: "https://github.com/gorse-io/gorse"
author: "Gorse"
category: "Data Extraction & Transformation"
framework: "Custom Agents"
tool_ecosystem:
  github_repo: "gorse-io/gorse"
  github_stars: 9600
---

# Gorse AI-Powered Open Source Recommender System Engine

Gorse is an AI-powered open-source recommender system written in Go that generates personalized recommendations via collaborative filtering, item-to-item similarity, and LLM-based ranking. It provides RESTful APIs and a GUI dashboard for recommendation pipeline editing, system monitoring, and data management.

## Installation

Use the upstream install or setup path that matches your environment:
- docker run -p 8088:8088 zhenghaoz/gorse-in-one --playground

Requirements and caveats from upstream:
- Gorse is a single-node training and distributed prediction recommender system. Gorse stores data in MySQL (MariaDB), MongoDB, Postgres, or ClickHouse, with intermediate results cached in Redis, MySQL (MariaDB), MongoD...
- The cluster consists of a master node, multiple worker nodes, and server nodes.
- The master node is responsible for model training, non-personalized recommendation, configuration management, and membership management.

Basic usage or getting-started notes:
- The playground mode has been prepared for beginners. Just set up a recommender system for GitHub repositories by the following commands.
- bash
- The playground mode will download data from [GitRec](https://gitrec.gorse.io/) and import it into Gorse. The dashboard is available at http://localhost:8088.

- Source: https://github.com/gorse-io/gorse
- Extracted from upstream docs: https://raw.githubusercontent.com/gorse-io/gorse/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gorse-ai-recommender-system-engine/)
