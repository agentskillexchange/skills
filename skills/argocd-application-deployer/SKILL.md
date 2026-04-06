---
name: ArgoCD Application Deployer
description: Manages ArgoCD application deployments via the ArgoCD REST API and argocd
  CLI. Configures GitOps sync policies, automated rollbacks, and multi-cluster application
  sets with generator templates.
category: CI/CD Integrations
framework: Claude Code
verification: security_reviewed
source: "https://agentskillexchange.com/skills/argocd-application-deployer/"
---
# ArgoCD Application Deployer

Manages ArgoCD application deployments via the ArgoCD REST API and argocd CLI. Configures GitOps sync policies, automated rollbacks, and multi-cluster application sets with generator templates.

The ArgoCD Application Deployer skill automates Kubernetes GitOps deployments through the ArgoCD REST API and argocd CLI tooling. It manages Application and ApplicationSet custom resources for declarative, Git-driven continuous deployment across single and multi-cluster environments.

Application management creates ArgoCD Application manifests with proper source repository configuration, target cluster/namespace settings, and sync policy definitions. Automated sync policies include self-heal for drift correction, auto-prune for resource cleanup, and configurable sync windows that restrict deployments to approved maintenance periods. The skill configures health checks using custom Lua scripts for CRDs and manages resource hooks (PreSync, Sync, PostSync) for database migrations and smoke tests.

ApplicationSet support enables multi-cluster and multi-tenant deployment patterns using generators: Git directory generators for monorepo structures, cluster generators for fleet-wide rollouts, matrix generators for combinatorial deployments, and pull request generators for preview environments. The skill interfaces with the ArgoCD API to monitor sync status, retrieve application health, trigger manual syncs, and initiate rollbacks to previous Git revisions. Notification configuration integrates ArgoCD Notifications with Slack, Teams, and webhook triggers for deployment status updates. It generates Kustomize overlays and Helm value files organized by environment (dev/staging/production) with proper ArgoCD source directory or Helm chart references.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill argocd-application-deployer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill argocd-application-deployer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill argocd-application-deployer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill argocd-application-deployer -a codex
```

### OpenClaw

```bash
clawhub install argocd-application-deployer
```


## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/argocd-application-deployer/)
