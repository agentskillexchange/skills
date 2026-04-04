---
name: "Argo Workflows DAG Pipeline Builder"
category: "Templates & Workflows"
verification: "security_reviewed"
source: "https://github.com/argoproj/argo-workflows"
tool_ecosystem:
  github_repo: "argoproj/argo-workflows"
  github_stars: 16596
---

# Argo Workflows DAG Pipeline Builder

Constructs Kubernetes-native workflow DAGs using Argo Workflows CRDs with configurable retry strategies, artifact passing via S3/MinIO, and template composition through WorkflowTemplates and ClusterWorkflowTemplates.

## Installation

Install this skill using one of the following methods:

```bash
# ClawHub CLI
clawhub install argo-workflows-dag-pipeline-builder

# OpenClaw CLI
openclaw skills install argo-workflows-dag-pipeline-builder

# Chat command
/skill install argo-workflows-dag-pipeline-builder

# Direct download
curl -L https://agentskillexchange.com/skills/argo-workflows-dag-pipeline-builder/download -o argo-workflows-dag-pipeline-builder.zip

# Git clone this repo and copy the skill folder
cp -r skills/argo-workflows-dag-pipeline-builder ~/.openclaw/workspace/skills/
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/argo-workflows-dag-pipeline-builder/)
