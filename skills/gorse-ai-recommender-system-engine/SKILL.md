---
name: "Gorse AI-Powered Open Source Recommender System Engine"
description: "Gorse is an AI-powered open-source recommender system written in Go that generates personalized recommendations via collaborative filtering, item-to-item similarity, and LLM-based ranking. It provides RESTful APIs and a GUI dashboard for recommendation pipeline editing, system monitoring, and data management."
category: "Data Extraction & Transformation"
framework: "Custom Agents"
verification: security_reviewed
source: "https://github.com/gorse-io/gorse"
---
# Gorse AI-Powered Open Source Recommender System Engine

Gorse is an AI-powered open-source recommender system written in Go that generates personalized recommendations via collaborative filtering, item-to-item similarity, and LLM-based ranking. It provides RESTful APIs and a GUI dashboard for recommendation pipeline editing, system monitoring, and data management.

Gorse is an AI-powered open-source recommender system engine written in Go, designed to be quickly integrated into a wide variety of online services. By importing items, users, and interaction data into Gorse, the system automatically trains models to generate recommendations for each user through multiple recommendation strategies.



Core Capabilities

Gorse provides multi-source recommendations combining latest items, user-to-user collaborative filtering, item-to-item similarity, and popularity-based approaches. The engine supports multimodal content including text, images, and videos through embedding representations, and offers both classical recommender algorithms and LLM-based ranking for modern AI-powered recommendations.



Architecture and Deployment

Gorse operates as a distributed system with a master node responsible for model training, non-personalized recommendations, and configuration management. Server nodes expose RESTful APIs for real-time recommendation serving, while worker nodes handle offline recommendation generation for each user. The system stores data in MySQL, MongoDB, PostgreSQL, or ClickHouse, with intermediate results cached in Redis or the primary database.



Integration Points

The primary integration method is through Gorse’s comprehensive RESTful API, which supports CRUD operations for users, items, and feedback data, as well as recommendation retrieval endpoints. A Docker image (zhenghaoz/gorse-in-one) provides a quick-start playground mode. The system includes a built-in GUI dashboard for monitoring recommendation pipeline status, managing data imports and exports, and tuning model parameters.



Agent Integration Use Cases

AI agents can leverage Gorse to build personalized content feeds, product suggestion engines, or skill recommendation systems. The REST API makes it straightforward for agents to insert user interaction data (clicks, views, purchases, stars) and retrieve ranked recommendation lists. Agents can automate A/B testing of recommendation strategies, monitor model training progress through the dashboard API, and dynamically adjust recommendation parameters based on user engagement metrics.



Getting Started

The fastest way to try Gorse is via Docker: docker run -p 8088:8088 zhenghaoz/gorse-in-one --playground. This downloads sample data and starts the dashboard at http://localhost:8088. For production deployments, Gorse supports Kubernetes via Helm charts and can be configured for high availability with multiple server and worker nodes.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill gorse-ai-recommender-system-engine
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill gorse-ai-recommender-system-engine -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill gorse-ai-recommender-system-engine -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill gorse-ai-recommender-system-engine -a codex
```

### OpenClaw

```bash
clawhub install gorse-ai-recommender-system-engine
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gorse-ai-recommender-system-engine/)
