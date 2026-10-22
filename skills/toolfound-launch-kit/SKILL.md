---
name: "Toolfound Launch Kit"
slug: "toolfound-launch-kit"
description: "Research, prepare, submit, and track a maker product launch through the Toolfound MCP. Use when asked to list a product, compare directory alternatives, choose a launch date, verify ownership, check launch status, or get a listing badge."
category: "Templates & Workflows"
framework: "MCP"
verification: listed
source: "https://github.com/MelMayssonOwen/agent-skills/tree/main/skills/toolfound-launch-kit"
---

# Toolfound Launch Kit

This skill helps a maker move from a rough product idea to a complete directory submission. It uses Toolfound's public discovery tools to inspect categories, search similar products, review alternatives, and check the launch calendar. From that context, it drafts a factual tagline and description based on details supplied by the maker.

The workflow pauses before submission. It displays the destination URL, owner email, product name, tagline, and description and submits only after the user confirms the exact fields. After submission, the agent explains the available ownership checks, such as a site meta tag, DNS record, or emailed verification link. The owner completes that step. The skill can then check queue status and retrieve badge snippets for the verified listing.

The live calendar includes current capacity information. Whether a free slot is available can change, so the skill instructs the agent to check the live counter instead of promising a free launch. The workflow is suitable for makers preparing a first public listing or comparing how a product fits a category. It does not make claims about votes, placement, or launch performance.

Creator: Opsibyte. License: MIT. Product: https://toolfound.com/?utm_source=ase&utm_medium=skill&utm_campaign=agent-skills&utm_content=toolfound-launch-kit

## Installation

### Direct repo/manual install

```bash
git clone https://github.com/MelMayssonOwen/agent-skills.git
cp -R agent-skills/skills/toolfound-launch-kit ~/.agent-skills/toolfound-launch-kit
```

### Optional Third-Party Installer

```bash
npx skills add MelMayssonOwen/agent-skills --skill toolfound-launch-kit
```
