---
title: "Match resumes to job descriptions with Resume Matcher"
description: "Run a reviewable resume-to-job-description matching workflow that produces ATS-style gaps, keyword suggestions, and human-checkable resume improvements."
verification: "security_reviewed"
source: "https://github.com/srbhr/Resume-Matcher"
author: "Resume Matcher maintainers"
publisher_type: "open-source project"
category:
  - "Data Extraction & Transformation"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "srbhr/Resume-Matcher"
  github_stars: 27243
---

# Match resumes to job descriptions with Resume Matcher

Run a reviewable resume-to-job-description matching workflow that produces ATS-style gaps, keyword suggestions, and human-checkable resume improvements.

## Prerequisites

Resume Matcher, uv, Node.js/npm, configured AI provider such as Ollama, OpenAI, Anthropic, Gemini, OpenRouter, or DeepSeek; Docker is optional.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Clone https://github.com/srbhr/Resume-Matcher, run the backend from apps/backend with cp .env.example .env, uv sync, and uv run app, then run the frontend from apps/frontend with npm install and npm run dev. Open http://localhost:3000 and configure the AI provider in Settings. The README also documents Docker images at ghcr.io/srbhr/resume-matcher.
```

## Documentation

- https://resumematcher.fyi/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/match-resumes-to-job-descriptions-with-resume-matcher/)
