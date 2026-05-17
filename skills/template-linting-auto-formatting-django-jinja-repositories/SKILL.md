---
name: "Template Linting and Auto-Formatting for Django and Jinja Repositories"
slug: "template-linting-auto-formatting-django-jinja-repositories"
description: "Uses djLint to scan Django, Jinja, Nunjucks, Twig, and HTML templates for indentation problems, malformed tags, and style drift, then optionally rewrites them into a consistent format. This is for agents that need to clean and validate template-heavy repos before review or release, not for general web framework setup."
github_stars: 911
verification: "security_reviewed"
source: "https://github.com/djlint/djLint"
author: "djLint maintainers"
publisher_type: "Open Source Project"
category: "Code Quality & Review"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "djlint/djLint"
  github_stars: 911
---

# Template Linting and Auto-Formatting for Django and Jinja Repositories

Uses djLint to scan Django, Jinja, Nunjucks, Twig, and HTML templates for indentation problems, malformed tags, and style drift, then optionally rewrites them into a consistent format. This is for agents that need to clean and validate template-heavy repos before review or release, not for general web framework setup.

## Prerequisites

Python 3.9 or higher and djLint

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
pip install djlint
```

## Documentation

- https://djlint.com/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/template-linting-auto-formatting-django-jinja-repositories/)
