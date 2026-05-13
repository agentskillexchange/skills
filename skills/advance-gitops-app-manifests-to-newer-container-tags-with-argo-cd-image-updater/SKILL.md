---
title: "Advance GitOps app manifests to newer container tags with Argo CD Image Updater"
slug: "advance-gitops-app-manifests-to-newer-container-tags-with-argo-cd-image-updater"
description: "Track approved container images and write back the matching GitOps manifest changes instead of hand-editing tags across Argo CD applications."
github_stars: 1661
verification: "security_reviewed"
source: "https://github.com/argoproj-labs/argocd-image-updater"
author: "Argo Project Labs"
publisher_type: "organization"
category: "CI/CD Integrations"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "argoproj-labs/argocd-image-updater"
  github_stars: 1661
---

# Advance GitOps app manifests to newer container tags with Argo CD Image Updater

Track approved container images and write back the matching GitOps manifest changes instead of hand-editing tags across Argo CD applications.

## Prerequisites

Argo CD-managed Kubernetes applications, Argo CD Image Updater, registry access, and Git or Argo CD API write-back permissions

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install Argo CD Image Updater from the upstream manifests, Helm chart, or release artifacts, configure registry credentials and the desired write-back method, then annotate supported Argo CD applications so approved image tags can be tracked and updated automatically.
```

## Documentation

- https://argocd-image-updater.readthedocs.io/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/advance-gitops-app-manifests-to-newer-container-tags-with-argo-cd-image-updater/)
