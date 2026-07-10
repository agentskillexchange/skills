---
name: "Run natural-language BI analysis with OpenChatBI agents"
slug: "run-natural-language-bi-analysis-with-openchatbi-agents"
description: "Deploy OpenChatBI when an agent needs to turn business questions into SQL, charts, anomaly analysis, and explainable BI results."
github_stars: 595
verification: "security_reviewed"
source: "https://github.com/zhongyu09/openchatbi"
author: "OpenChatBI contributors"
publisher_type: "open_source"
category: "Data Extraction & Transformation"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "zhongyu09/openchatbi"
  github_stars: 595
---

# Run natural-language BI analysis with OpenChatBI agents

Deploy OpenChatBI when an agent needs to turn business questions into SQL, charts, anomaly analysis, and explainable BI results.

## Prerequisites

Python, pip, database connection, configured LLM provider, optional MCP tools, optional Gradio or Streamlit UI

## Installation

Use the upstream install or setup path that matches your environment:
- git clone git@github.com:zhongyu09/openchatbi
- uv sync
- pip install openchatbi
- uv sync --group dev

Requirements and caveats from upstream:
- **Code Execution**: Execute Python code for data analysis and visualization
- multi-dimensional drill-down (Adtributor) and Python execution to cover trend forecasting, anomaly detection,
- Python 3.11 or higher

Basic usage or getting-started notes:
- <img src="https://github.com/zhongyu09/openchatbi/raw/main/example/demo.gif" alt="Demo" width="800">
- Access to a supported LLM provider (OpenAI, Anthropic, etc.)
- Data Warehouse (Database) credentials (like Presto, PostgreSQL, MySQL, etc.)

- Source: https://github.com/zhongyu09/openchatbi
- Extracted from upstream docs: https://raw.githubusercontent.com/zhongyu09/openchatbi/HEAD/README.md

## Documentation

- https://zhongyu09.github.io/openchatbi/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-natural-language-bi-analysis-with-openchatbi-agents/)
