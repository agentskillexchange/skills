---
title: "Posting Terminal API Client"
description: "Posting is an open-source terminal-based HTTP client created by Darren Burns, built with the Textual framework for Python. With over 11,000 GitHub stars and an Apache 2.0 license, it fills a gap for developers who want Postman-class API development and testing capabilities without leaving the command line.\nHow It Works\nPosting runs as a TUI (terminal user interface) application, rendering a full graphical interface inside any terminal emulator. Users compose HTTP requests with method, URL, headers, query parameters, and body content using an intuitive panel-based layout. Requests are stored as plain YAML files on disk, making them human-readable and trivially version-controllable with Git. The interface supports jump mode navigation for rapid keyboard-driven workflows, eliminating the need for mouse interaction entirely.\nKey Features\nPosting includes environment and variable management, letting you define per-environment values for base URLs, tokens, and other configuration that varies between development, staging, and production. Syntax highlighting powered by tree-sitter renders JSON, XML, and HTML response bodies with full color coding. Vim keybindings are available for developers who prefer modal editing. The application supports custom keybinding configuration, user-defined color themes, and the ability to open request or response content in your system editor or pager via $EDITOR and $PAGER integration.\nIntegration and Workflow\nPosting imports curl commands by pasting them directly into the URL bar, converting them to its native request format. It can also import collections from Postman exports and OpenAPI specification files. Requests can be exported as cURL commands for sharing. A command palette provides fuzzy-searchable access to all application functions. Users can run Python scripts as pre-request and post-response hooks, enabling authentication flows, dynamic header injection, or response validation logic. Because it runs in a standard terminal, Posting works over SSH connections, making it practical for API testing on remote servers, containers, and headless environments.\nOutput and Results\nResponse panels display status codes, timing information, headers, and formatted body content. The interface supports multiple request tabs and collection organization. Posting installs via pip, pipx, or uv, requires Python 3.12 or later, and runs on macOS, Linux, and Windows. Its lightweight footprint and terminal-native design make it suitable for embedding in development containers and CI debugging workflows."
verification: security_reviewed
source: "https://github.com/darrenburns/posting"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "darrenburns/posting"
  github_stars: 11673
---

# Posting Terminal API Client

Posting is an open-source terminal-based HTTP client created by Darren Burns, built with the Textual framework for Python. With over 11,000 GitHub stars and an Apache 2.0 license, it fills a gap for developers who want Postman-class API development and testing capabilities without leaving the command line.
How It Works
Posting runs as a TUI (terminal user interface) application, rendering a full graphical interface inside any terminal emulator. Users compose HTTP requests with method, URL, headers, query parameters, and body content using an intuitive panel-based layout. Requests are stored as plain YAML files on disk, making them human-readable and trivially version-controllable with Git. The interface supports jump mode navigation for rapid keyboard-driven workflows, eliminating the need for mouse interaction entirely.
Key Features
Posting includes environment and variable management, letting you define per-environment values for base URLs, tokens, and other configuration that varies between development, staging, and production. Syntax highlighting powered by tree-sitter renders JSON, XML, and HTML response bodies with full color coding. Vim keybindings are available for developers who prefer modal editing. The application supports custom keybinding configuration, user-defined color themes, and the ability to open request or response content in your system editor or pager via $EDITOR and $PAGER integration.
Integration and Workflow
Posting imports curl commands by pasting them directly into the URL bar, converting them to its native request format. It can also import collections from Postman exports and OpenAPI specification files. Requests can be exported as cURL commands for sharing. A command palette provides fuzzy-searchable access to all application functions. Users can run Python scripts as pre-request and post-response hooks, enabling authentication flows, dynamic header injection, or response validation logic. Because it runs in a standard terminal, Posting works over SSH connections, making it practical for API testing on remote servers, containers, and headless environments.
Output and Results
Response panels display status codes, timing information, headers, and formatted body content. The interface supports multiple request tabs and collection organization. Posting installs via pip, pipx, or uv, requires Python 3.12 or later, and runs on macOS, Linux, and Windows. Its lightweight footprint and terminal-native design make it suitable for embedding in development containers and CI debugging workflows.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/posting-terminal-api-client
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/posting-terminal-api-client` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/posting-terminal-api-client/)
