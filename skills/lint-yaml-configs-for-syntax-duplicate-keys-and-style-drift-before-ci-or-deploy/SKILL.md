---
title: "Lint YAML configs for syntax, duplicate keys, and style drift before CI or deploy"
description: "Uses yamllint to inspect hand-written or generated YAML before it reaches CI or deploy. The agent returns line-level syntax, duplicate-key, indentation, and formatting findings so config changes can be fixed before they break pipelines or runtime environments."
verification: security_reviewed
source: "https://github.com/adrienverge/yamllint"
category:
  - "Code Quality &amp; Review"
framework:
  - "Multi-Framework"
---

# Lint YAML configs for syntax, duplicate keys, and style drift before CI or deploy

This entry is built around yamllint, the open source YAML linter maintained in the adrienverge/yamllint project. In an agent workflow, the job is not “use a YAML tool” in the abstract. The job is to take changed configuration files such as GitHub Actions workflows, Docker Compose files, Kubernetes manifests, Ansible vars, or app settings, run a focused lint pass, and return concrete fixes before those files move deeper into CI or deployment. The agent behavior is narrow and testable: inspect YAML, flag syntax problems, catch duplicate keys, surface indentation drift, point out trailing spaces or line-length issues, and summarize what is safe to auto-fix versus what needs a human decision.

You should invoke this skill when an agent has edited YAML directly, generated YAML from another source, or is reviewing a config-heavy pull request and needs a quick confidence gate. It is especially useful before opening a PR, before running a deployment pipeline, or before handing a generated config bundle back to a human operator. The value is speed and precision: yamllint produces file and line scoped findings that make agent remediation loops straightforward.

The scope boundary matters. This is not a generic configuration management platform, deployment engine, or schema validator. It does not apply infrastructure, evaluate runtime policy, or understand every domain-specific semantic rule in the target system. Its lane is YAML correctness and style hygiene. Integration points include pre-commit hooks, CI jobs, repo review bots, editor tasks, and agent repair loops that patch config files and re-run the linter until the output is clean.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/lint-yaml-configs-for-syntax-duplicate-keys-and-style-drift-before-ci-or-deploy/)
