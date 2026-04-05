---
name: "act Local GitHub Actions Runner"
description: "act is an open-source CLI tool that runs GitHub Actions workflows locally using Docker, enabling fast feedback on workflow changes without pushing to GitHub. With 57,000+ stars on GitHub, it is the standard tool for local Actions development and testing."
category: "CI/CD Integrations"
framework: "Claude Code"
verification: security_reviewed
source: "https://github.com/nektos/act"
tool_ecosystem:
  github_repo: "nektos/act"
  github_stars: 69661
---
# act Local GitHub Actions Runner

act is an open-source CLI tool that runs GitHub Actions workflows locally using Docker, enabling fast feedback on workflow changes without pushing to GitHub. With 57,000+ stars on GitHub, it is the standard tool for local Actions development and testing.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill act-local-github-actions-runner
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill act-local-github-actions-runner -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill act-local-github-actions-runner -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill act-local-github-actions-runner -a codex
```

### OpenClaw

```bash
clawhub install act-local-github-actions-runner
```

## Details

act is an open-source command-line tool that executes GitHub Actions workflows on your local machine, available at github.com/nektos/act with over 57,000 GitHub stars. Its tagline is “Think globally, act locally” — it reads your .github/workflows/ directory, resolves the dependency graph between jobs and steps, and runs each action in Docker containers that replicate the GitHub-hosted runner environment.

The primary use case is fast feedback during workflow development. Without act, testing a workflow change requires committing, pushing, waiting for GitHub to pick up the job, and watching the run complete — a cycle that can take minutes per iteration. With act, developers run the workflow locally in seconds and see the output immediately in their terminal. The environment variables, filesystem layout, and available tools are configured to match what GitHub provides on its hosted runners.

act also serves as a local task runner. Developers who already define their build, test, and deploy steps as GitHub Actions can use act to execute those same workflows locally, eliminating the need to maintain a separate Makefile or task runner configuration. The same workflow file drives both CI and local development.

The tool uses the Docker API to pull or build the images specified in workflow files, then executes each step in order based on the dependency graph. It supports workflow features including matrix strategies, job dependencies with needs, environment variables and secrets (passed via .env files or command flags), conditional execution with if expressions, and composite actions. Docker container actions and JavaScript actions are both supported.

Installation is available through Homebrew, winget, scoop, chocolatey, pacman, nix, and Go install. A VS Code extension called GitHub Local Actions provides a graphical interface for running act from within the editor. The tool requires Docker to be installed and running on the host machine.

For agent skills focused on CI/CD development, workflow validation, or pipeline debugging, act enables local testing of GitHub Actions before pushing changes. An agent can modify a workflow file, run it locally with act to verify it passes, and only then commit and push the validated change. This dramatically reduces the iteration time for CI/CD development and catches configuration errors before they reach the remote repository.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/act-local-github-actions-runner/)
