---
title: "Trace and evaluate agent runs with MLflow"
description: "Instrument LLM and agent applications with MLflow tracing, evaluation, prompt tracking, and monitoring so operators can debug behavior before and after deployment."
verification: "security_reviewed"
source: "https://github.com/mlflow/mlflow"
author: "MLflow"
publisher_type: "organization"
category:
  - "Monitoring & Alerts"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "mlflow/mlflow"
  github_stars: 26027
---

# Trace and evaluate agent runs with MLflow

Instrument LLM and agent applications with MLflow tracing, evaluation, prompt tracking, and monitoring so operators can debug behavior before and after deployment.

## Prerequisites

Python, uv or pip, MLflow tracking server, LLM or agent application

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Start a local tracking server with `uvx mlflow server`, point the application at it with `mlflow.set_tracking_uri("http://localhost:5000")`, then enable the relevant LLM or agent tracing integration such as `mlflow.openai.autolog()`.
```

## Documentation

- https://mlflow.org/docs/latest/genai/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/trace-and-evaluate-agent-runs-with-mlflow/)
