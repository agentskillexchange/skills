---
name: Wish SSH Application Framework by Charmbracelet
description: Wish is a Go library for building SSH-accessible applications with sensible
  defaults and composable middleware. It lets developers serve Bubble Tea TUIs, Git
  repos, and custom protocols over SSH without touching openssh-server.
verification: security_reviewed
source: https://github.com/charmbracelet/wish
category:
- Developer Tools
framework:
- Custom Agents
tool_ecosystem:
  github_repo: charmbracelet/wish
  github_stars: 5110
---
# Wish SSH Application Framework by Charmbracelet

Wish is an open-source Go library by Charmbracelet that makes building SSH-accessible applications straightforward. Built on top of gliderlabs/ssh, Wish provides a middleware-based architecture where developers compose handlers for authentication, terminal sessions, Git operations, logging, and custom protocols into a complete SSH server.
Why SSH as an Application Platform
SSH provides secure encrypted communication without HTTPS certificate management, user identification via SSH keys, and universal access from any terminal. Protocols like Git already run over SSH, and terminal UIs can render directly over SSH connections. Wish brings this platform capability to application developers with a clean, middleware-driven API.
Core Middleware
The Bubble Tea middleware lets you serve any Bubble Tea TUI application over SSH. Each SSH session gets its own tea.Program with the SSH pty input/output connected, plus native handling of client window dimensions and resize events. The Git middleware adds full Git server functionality including repo creation on initial push and public-key-based authentication. The logging middleware provides connection tracking with remote address, invoked command, TERM setting, window dimensions, and session duration. Access control middleware lets you restrict connections to specific terminal types or allowed commands.
How It Works
Wish includes automatic server key generation and an always-authenticating default configuration. You create a server, register middleware in order (composed last-to-first), and start serving. The library handles SSH protocol negotiation, key exchange, and session management. Developers focus on the application logic in their middleware handlers.
Real-World Usage
Wish powers several production applications including Soft Serve (self-hosted Git server with SSH TUI), Wishlist (SSH directory listing), and numerous community projects like SSHWordle and clidle. The Charmbracelet ecosystem (Bubble Tea, Lip Gloss, Glamour) integrates naturally with Wish for building polished terminal interfaces accessible over SSH.
Agent Integration
AI agents can use Wish to build SSH-accessible services: deploy TUI dashboards reachable from any terminal, create secure Git hosting, or build interactive CLI tools that multiple users access via SSH. The Go library integrates into automated deployment pipelines and the middleware architecture makes it composable with existing agent tooling.
Installation
Install via Go modules: go get github.com/charmbracelet/wish. The library requires Go 1.18+ and has comprehensive examples for Bubble Tea applications and Git server setups in the repository.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wish-ssh-application-framework/)
