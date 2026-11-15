---
name: "Soft Serve Self-Hosted Git Server with SSH TUI"
slug: "soft-serve-self-hosted-git-server-ssh-tui"
description: "Soft Serve is a self-hostable Git server by Charmbracelet that provides a beautiful terminal UI accessible over SSH. It supports cloning over SSH, HTTP, and Git protocol, Git LFS, access control with SSH keys, and on-demand repository creation."
github_stars: 6756
verification: "security_reviewed"
source: "https://github.com/charmbracelet/soft-serve"
category: "Developer Tools"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "charmbracelet/soft-serve"
  github_stars: 6756
---

# Soft Serve Self-Hosted Git Server with SSH TUI

Soft Serve is a self-hostable Git server by Charmbracelet that provides a beautiful terminal UI accessible over SSH. It supports cloning over SSH, HTTP, and Git protocol, Git LFS, access control with SSH keys, and on-demand repository creation.

## Installation

Use the upstream install or setup path that matches your environment:
- brew install charmbracelet/tap/soft-serve
- go install github.com/charmbracelet/soft-serve/cmd/soft@latest
- Make sure git is installed, then run soft serve. That’s it.
- git clone ssh://soft/dotfiles

Requirements and caveats from upstream:
- A [Docker image][docker] is also available.
- [docker]: https://github.com/charmbracelet/soft-serve/blob/main/docker.md
- Now you can access to repos that require read-write access.

Basic usage or getting-started notes:
- Just run ssh git.charm.sh for an example. You can also try some of the following commands:
- Soft Serve is a single binary called soft. You can get it from a package
- manager:

- Source: https://github.com/charmbracelet/soft-serve
- Extracted from upstream docs: https://raw.githubusercontent.com/charmbracelet/soft-serve/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/soft-serve-self-hosted-git-server-ssh-tui/)
