---
title: "Scaffold and bundle rich single-file web artifacts with React, Tailwind, and shadcn/ui"
description: "Use Anthropic’s web-artifacts-builder skill to scaffold a React artifact project, build a richer interface with state or routing, and bundle everything into one shareable HTML file. It is for artifact-delivery workflows, not for listing React or Tailwind as standalone products."
verification: "security_reviewed"
source: "https://github.com/anthropics/skills/tree/main/skills/web-artifacts-builder"
author: "Anthropic"
publisher_type: "Public repository"
category:
  - "Templates & Workflows"
framework:
  - "Claude Agents"
---

# Scaffold and bundle rich single-file web artifacts with React, Tailwind, and shadcn/ui

Use Anthropic’s web-artifacts-builder skill to scaffold a React artifact project, build a richer interface with state or routing, and bundle everything into one shareable HTML file. It is for artifact-delivery workflows, not for listing React or Tailwind as standalone products.

## Prerequisites

Node.js 18+, React, TypeScript, Vite, Parcel, Tailwind CSS, and shadcn/ui

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Clone or install anthropics/skills, run bash skills/web-artifacts-builder/scripts/init-artifact.sh <project-name>, build the artifact in the generated React project, then run bash skills/web-artifacts-builder/scripts/bundle-artifact.sh to produce a single self-contained HTML file.
```

## Documentation

- https://raw.githubusercontent.com/anthropics/skills/main/skills/web-artifacts-builder/SKILL.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/scaffold-and-bundle-rich-single-file-web-artifacts-with-react-tailwind-and-shadcn-ui/)
