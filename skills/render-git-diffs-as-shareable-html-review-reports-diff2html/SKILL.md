---
title: "Render git diffs as shareable HTML review reports with Diff2Html"
description: "Use Diff2Html when an agent needs to turn raw unified diffs into readable HTML artifacts for reviews, audits, or status updates. This is a rendering and packaging workflow, not a generic Git hosting, code review, or SCM platform listing."
verification: security_reviewed
source: "https://github.com/rtfpessoa/diff2html"
category:
  - "Code Quality & Review"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "rtfpessoa/diff2html"
  github_stars: 3345
---

# Render git diffs as shareable HTML review reports with Diff2Html

Tool used: Diff2Html (rtfpessoa/diff2html).

This skill gives an agent a sharply bounded job: take a diff or patch and produce an HTML report that a human can review without opening a terminal or Git hosting UI. The output is useful in real workflows where raw patch text is too ugly for stakeholders, clients, auditors, or async reviewers. An agent can generate side-by-side or line-by-line views, bundle the report into release artifacts, and attach it to issue threads, docs, or internal approvals.

Invoke this when the input already exists as a git diff, patch file, or CI-generated change set and the user needs a portable review artifact. It is especially useful for compliance snapshots, vendor review packages, incident postmortems, and status updates where you want the actual code delta preserved in a readable form. Do not invoke it when the user simply wants a normal GitHub or GitLab code review, repository hosting, or automated code analysis. Diff2Html renders diffs. It does not replace source control, comment workflows, or review policy.

That scope boundary is the difference between a skill and a product card. The value here is the agent behavior: collect the diff, format it consistently, generate shareable HTML, and route the artifact where it belongs. Integration points include git hooks, CI pipelines, release packaging jobs, documentation systems, and chat or ticket workflows that need a self-contained review attachment rather than a repo link.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/render-git-diffs-as-shareable-html-review-reports-diff2html
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/render-git-diffs-as-shareable-html-review-reports-diff2html` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/render-git-diffs-as-shareable-html-review-reports-diff2html/)
