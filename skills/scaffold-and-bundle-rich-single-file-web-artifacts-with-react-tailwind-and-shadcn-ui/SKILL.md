---
title: "Scaffold and bundle rich single-file web artifacts with React, Tailwind, and shadcn/ui"
description: "Use Anthropic’s web-artifacts-builder skill to scaffold a React artifact project, build a richer interface with state or routing, and bundle everything into one shareable HTML file. It is for artifact-delivery workflows, not for listing React or Tailwind as standalone products."
verification: "security_reviewed"
source: "https://github.com/anthropics/skills/tree/main/skills/web-artifacts-builder"
category:
  - "Templates & Workflows"
framework:
  - "Claude Agents"
tool_ecosystem:
  github_repo: "anthropics/skills"
  github_stars: 116154
---

# Scaffold and bundle rich single-file web artifacts with React, Tailwind, and shadcn/ui

Tool name: Anthropic’s web-artifacts-builder skill in the public anthropics/skills repository. The upstream instructions are tightly scoped: initialize an artifact project with scripts/init-artifact.sh, build the interface in a React and TypeScript workspace that already includes Tailwind CSS and shadcn/ui, then run scripts/bundle-artifact.sh to inline everything into a single HTML file. That is a concrete artifact-building workflow, not a generic frontend stack listing. What the agent does: create the starter project, develop the needed components and stateful interactions, use the preconfigured UI stack and aliases, then bundle the result into a self-contained bundle.html artifact that can be shared directly. The upstream docs also give a boundary that matters: use this skill for elaborate, multi-component artifacts that need state management, routing, or richer UI composition, and do not reach for it when a trivial one-file HTML snippet would do. When to use it: invoke this skill when the user wants a polished interactive artifact, mini dashboard, explainer UI, or other shareable single-file web experience where richer frontend structure materially helps. It is better than using React, Tailwind, or shadcn/ui “normally” because the value here is the packaged operator workflow that starts from a ready template and ends with a bundled artifact, which is exactly what an agent needs to ship. Scope boundary: this entry is not a general React tutorial, not a Tailwind product page, and not broad frontend-design advice. Its boundary is building and packaging self-contained web artifacts through the upstream skill’s scripts and stack choices. Integration points: Node.js 18+, React, TypeScript, Vite, Parcel, Tailwind CSS, shadcn/ui, and optional follow-up testing with browser tools after the artifact is shared.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/scaffold-and-bundle-rich-single-file-web-artifacts-with-react-tailwind-and-shadcn-ui/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/scaffold-and-bundle-rich-single-file-web-artifacts-with-react-tailwind-and-shadcn-ui
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/scaffold-and-bundle-rich-single-file-web-artifacts-with-react-tailwind-and-shadcn-ui`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/scaffold-and-bundle-rich-single-file-web-artifacts-with-react-tailwind-and-shadcn-ui/)
