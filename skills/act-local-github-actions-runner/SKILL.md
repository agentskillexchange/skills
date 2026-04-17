---
title: "act Local GitHub Actions Runner"
description: "act is an open-source command-line tool that executes GitHub Actions workflows on your local machine, available at github.com/nektos/act with over 57,000 GitHub stars. Its tagline is “Think globally, act locally” — it reads your .github/workflows/ directory, resolves the dependency graph between jobs and steps, and runs each action in Docker containers that replicate the GitHub-hosted runner environment.\nThe primary use case is fast feedback during workflow development. Without act, testing a workflow change requires committing, pushing, waiting for GitHub to pick up the job, and watching the run complete — a cycle that can take minutes per iteration. With act, developers run the workflow locally in seconds and see the output immediately in their terminal. The environment variables, filesystem layout, and available tools are configured to match what GitHub provides on its hosted runners.\nact also serves as a local task runner. Developers who already define their build, test, and deploy steps as GitHub Actions can use act to execute those same workflows locally, eliminating the need to maintain a separate Makefile or task runner configuration. The same workflow file drives both CI and local development.\nThe tool uses the Docker API to pull or build the images specified in workflow files, then executes each step in order based on the dependency graph. It supports workflow features including matrix strategies, job dependencies with needs, environment variables and secrets (passed via .env files or command flags), conditional execution with if expressions, and composite actions. Docker container actions and JavaScript actions are both supported.\nInstallation is available through Homebrew, winget, scoop, chocolatey, pacman, nix, and Go install. A VS Code extension called GitHub Local Actions provides a graphical interface for running act from within the editor. The tool requires Docker to be installed and running on the host machine.\nFor agent skills focused on CI/CD development, workflow validation, or pipeline debugging, act enables local testing of GitHub Actions before pushing changes. An agent can modify a workflow file, run it locally with act to verify it passes, and only then commit and push the validated change. This dramatically reduces the iteration time for CI/CD development and catches configuration errors before they reach the remote repository."
verification: security_reviewed
source: "https://github.com/nektos/act"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "nektos/act"
  github_stars: 69661
---

# act Local GitHub Actions Runner

act is an open-source command-line tool that executes GitHub Actions workflows on your local machine, available at github.com/nektos/act with over 57,000 GitHub stars. Its tagline is “Think globally, act locally” — it reads your .github/workflows/ directory, resolves the dependency graph between jobs and steps, and runs each action in Docker containers that replicate the GitHub-hosted runner environment.
The primary use case is fast feedback during workflow development. Without act, testing a workflow change requires committing, pushing, waiting for GitHub to pick up the job, and watching the run complete — a cycle that can take minutes per iteration. With act, developers run the workflow locally in seconds and see the output immediately in their terminal. The environment variables, filesystem layout, and available tools are configured to match what GitHub provides on its hosted runners.
act also serves as a local task runner. Developers who already define their build, test, and deploy steps as GitHub Actions can use act to execute those same workflows locally, eliminating the need to maintain a separate Makefile or task runner configuration. The same workflow file drives both CI and local development.
The tool uses the Docker API to pull or build the images specified in workflow files, then executes each step in order based on the dependency graph. It supports workflow features including matrix strategies, job dependencies with needs, environment variables and secrets (passed via .env files or command flags), conditional execution with if expressions, and composite actions. Docker container actions and JavaScript actions are both supported.
Installation is available through Homebrew, winget, scoop, chocolatey, pacman, nix, and Go install. A VS Code extension called GitHub Local Actions provides a graphical interface for running act from within the editor. The tool requires Docker to be installed and running on the host machine.
For agent skills focused on CI/CD development, workflow validation, or pipeline debugging, act enables local testing of GitHub Actions before pushing changes. An agent can modify a workflow file, run it locally with act to verify it passes, and only then commit and push the validated change. This dramatically reduces the iteration time for CI/CD development and catches configuration errors before they reach the remote repository.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/act-local-github-actions-runner
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/act-local-github-actions-runner` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/act-local-github-actions-runner/)
