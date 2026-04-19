---
title: "Lint YAML configs for syntax, duplicate keys, and style drift before CI or deploy"
description: "This entry is built around yamllint , the open source YAML linter maintained in the adrienverge/yamllint project. In an agent workflow, the job is not “use a YAML tool” in the abstract. The job is to take changed configuration files such as GitHub Actions workflows, Docker Compose files, Kubernetes manifests, Ansible vars, or app settings, run a focused lint pass, and return concrete fixes before those files move deeper into CI or deployment. The agent behavior is narrow and testable: inspect YAML, flag syntax problems, catch duplicate keys, surface indentation drift, point out trailing spaces or line-length issues, and summarize what is safe to auto-fix versus what needs a human decision. You should invoke this skill when an agent has edited YAML directly, generated YAML from another source, or is reviewing a config-heavy pull request and needs a quick confidence gate. It is especially useful before opening a PR, before running a deployment pipeline, or before handing a generated config bundle back to a human operator. The value is speed and precision: yamllint produces file and line scoped findings that make agent remediation loops straightforward. The scope boundary matters. This is not a generic configuration management platform, deployment engine, or schema validator. It does not apply infrastructure, evaluate runtime policy, or understand every domain-specific semantic rule in the target system. Its lane is YAML correctness and style hygiene. Integration points include pre-commit hooks, CI jobs, repo review bots, editor tasks, and agent repair loops that patch config files and re-run the linter until the output is clean."
source: "https://github.com/adrienverge/yamllint"
verification: "security_reviewed"
category:
  - "Code Quality &amp; Review"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "adrienverge/yamllint"
  github_stars: 3360
---

# Lint YAML configs for syntax, duplicate keys, and style drift before CI or deploy

This entry is built around yamllint , the open source YAML linter maintained in the adrienverge/yamllint project. In an agent workflow, the job is not “use a YAML tool” in the abstract. The job is to take changed configuration files such as GitHub Actions workflows, Docker Compose files, Kubernetes manifests, Ansible vars, or app settings, run a focused lint pass, and return concrete fixes before those files move deeper into CI or deployment. The agent behavior is narrow and testable: inspect YAML, flag syntax problems, catch duplicate keys, surface indentation drift, point out trailing spaces or line-length issues, and summarize what is safe to auto-fix versus what needs a human decision. You should invoke this skill when an agent has edited YAML directly, generated YAML from another source, or is reviewing a config-heavy pull request and needs a quick confidence gate. It is especially useful before opening a PR, before running a deployment pipeline, or before handing a generated config bundle back to a human operator. The value is speed and precision: yamllint produces file and line scoped findings that make agent remediation loops straightforward. The scope boundary matters. This is not a generic configuration management platform, deployment engine, or schema validator. It does not apply infrastructure, evaluate runtime policy, or understand every domain-specific semantic rule in the target system. Its lane is YAML correctness and style hygiene. Integration points include pre-commit hooks, CI jobs, repo review bots, editor tasks, and agent repair loops that patch config files and re-run the linter until the output is clean.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/lint-yaml-configs-for-syntax-duplicate-keys-and-style-drift-before-ci-or-deploy/)
