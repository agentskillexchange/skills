---
name: "LazyDocker Terminal UI for Docker Management"
slug: "lazydocker-terminal-docker-management"
description: "LazyDocker is a terminal UI for Docker and Docker Compose that provides container management, log viewing, resource monitoring, and image inspection through a keyboard-driven interface. Created by Jesse Duffield with 50,000+ GitHub stars."
github_stars: 50476
verification: "security_reviewed"
source: "https://github.com/jesseduffield/lazydocker"
category: "Developer Tools"
framework: "Claude Code"
tool_ecosystem:
  github_repo: "jesseduffield/lazydocker"
  github_stars: 50476
---

# LazyDocker Terminal UI for Docker Management

LazyDocker is a terminal UI for Docker and Docker Compose that provides container management, log viewing, resource monitoring, and image inspection through a keyboard-driven interface. Created by Jesse Duffield with 50,000+ GitHub stars.

## Installation

Use the upstream install or setup path that matches your environment:
- Minor rant incoming: Something's not working? Maybe a service is down. docker-compose ps. Yep, it's that microservice that's still buggy. No issue, I'll just restart it: docker-compose restart. Okay now let's try agai...
- brew install jesseduffield/lazydocker/lazydocker
- brew install lazydocker
- go install github.com/jesseduffield/lazydocker@latest

Requirements and caveats from upstream:
- A simple terminal UI for both docker and docker-compose, written in Go with the [gocui](https://github.com/jroimartin/gocui 'gocui') library.
- Memorising docker commands is hard. Memorising aliases is slightly less hard. Keeping track of your containers across multiple terminal windows is near impossible. What if you had all the information you needed in one...
- Docker >= **29.0.0** (API >= **1.24**)

Basic usage or getting-started notes:
- [Usage](https://github.com/jesseduffield/lazydocker#usage)
- ### Homebrew
- Normally lazydocker formula can be found in the Homebrew core but we suggest you to tap our formula to get frequently updated one. It works with Linux, too.

- Source: https://github.com/jesseduffield/lazydocker
- Extracted from upstream docs: https://raw.githubusercontent.com/jesseduffield/lazydocker/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/lazydocker-terminal-docker-management/)
