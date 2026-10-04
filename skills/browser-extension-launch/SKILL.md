---
name: "Browser Extension Launch"
slug: "browser-extension-launch"
description: "Turns a plain-language idea into a tested Chrome Manifest V3 extension, release bundle, store materials, and a resumable launch workflow using Codex skills and Playwright MCP acceptance checks."
verification: "listed"
source: "https://github.com/xiehuan123/browser-extension-launch"
category: "Templates & Workflows"
framework: "Codex"
tool_ecosystem:
  github_repo: "xiehuan123/browser-extension-launch"
  npm_package: "browser-extension-launch"
---

# Browser Extension Launch

Browser Extension Launch is a Codex skill for taking a browser-extension idea from a plain-language request to a locally usable or store-ready Chrome Manifest V3 package. Use it when the requester may not know extension architecture, permissions, testing, or Chrome Web Store requirements. The workflow coordinates product-flow decisions, extension scaffolding, implementation, debugging, code review, release packaging, permission and privacy explanations, and resumable project state. It requires real-browser acceptance through Playwright MCP before a build is described as usable: the current unpacked extension must be loaded, exercised through its native entry point, and checked across repeated use or restart when persistence matters. Helper scripts fingerprint the candidate, validate evidence, and inspect release bundles. The project includes three open-source extensions built with the workflow, plus documented limits that keep source completion, acceptance, review submission, and public store availability as separate states.

## Installation

### npm installer

```bash
npx browser-extension-launch install
```

### Codex manual install

```bash
git clone https://github.com/xiehuan123/browser-extension-launch.git ~/.codex/skills/browser-extension-launch
```

Restart Codex after installation so it reloads skill metadata. The complete workflow also expects the child skills and Playwright MCP capability documented by the upstream project.
