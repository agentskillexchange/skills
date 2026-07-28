---
name: "Diagnose local setup failures with Env Doctor"
slug: "justhandledlabs-env-doctor"
description: "Diagnose why a local Node, Python, Go, or Docker project will not start by checking runtimes, dependencies, ports, environment-key presence, permissions, and required services before changing application code."
verification: "listed"
source: "https://github.com/justhandledlabs/skills/tree/main/skills/env-doctor-free"
category: "Runbooks & Diagnostics"
framework: "Codex"
---

# Diagnose local setup failures with Env Doctor

Use Env Doctor when an application fails to start, works on one machine but not another, or appears broken before the application code has been proven responsible. The skill detects project type from files such as `package.json`, `pyproject.toml`, `go.mod`, and `Dockerfile`; checks installed runtime versions and missing dependencies; inspects common development ports with operating-system-appropriate commands; compares `.env.example` keys with `.env` without exposing values; and checks likely Postgres, Redis, MySQL, or Docker service state.

The workflow is evidence-first and deliberately cautious. It reports the process that owns a port before suggesting a stop action, never terminates a process without explicit approval, never displays environment-variable values, and explains mutating commands such as `go mod tidy` before they run. Results are returned as a prioritized checklist with evidence, a proposed fix, the likely start command, and a record of what was checked. Review the upstream [Env Doctor documentation](https://justhandledlabs.com/skills/env-doctor/?utm_source=agentskillexchange&utm_medium=directory&utm_campaign=env_doctor) for the complete workflow and safety fixtures.

## Installation

No source-backed install or usage instructions could be extracted automatically. Review the upstream project before running this skill in a sensitive workflow.

- Source: https://github.com/justhandledlabs/skills/tree/main/skills/env-doctor-free

