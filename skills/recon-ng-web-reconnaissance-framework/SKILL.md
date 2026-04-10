---
title: "Recon-ng Modular Web Reconnaissance Framework for OSINT"
description: "Recon-ng is a full-featured modular reconnaissance framework written in Python, designed to conduct web-based open source intelligence (OSINT) gathering quickly and thoroughly. Its Metasploit-like interface and extensible module system make it the standard tool for structured OSINT workflows."
slug: "recon-ng-web-reconnaissance-framework"
category:
  - "Research &amp; Scraping"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/lanmaster53/recon-ng"
tool_ecosystem:
  github_repo: "lanmaster53/recon-ng"
  github_stars: 5499
listed: true
---

# Recon-ng Modular Web Reconnaissance Framework for OSINT

Recon-ng is a full-featured modular reconnaissance framework written in Python, designed to conduct web-based open source intelligence (OSINT) gathering quickly and thoroughly. Its Metasploit-like interface and extensible module system make it the standard tool for structured OSINT workflows.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install recon-ng-web-reconnaissance-framework
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Recon-ng is a comprehensive web reconnaissance framework created by Tim Tomes (lanmaster53) at Black Hills Information Security. Designed exclusively for web-based open source reconnaissance, it provides a powerful environment for gathering intelligence from open sources with a workflow-oriented approach that separates reconnaissance into discrete, repeatable modules.
Architecture and Module System
The framework follows a modular design inspired by Metasploit, which significantly reduces the learning curve for security professionals already familiar with that ecosystem. Recon-ng organizes its functionality into module categories: discovery, exploitation, import, recon, and reporting. Each module performs a specific OSINT task — from harvesting email addresses and enumerating subdomains to querying WHOIS data and searching breach databases. The marketplace system allows users to install only the modules they need, keeping the base installation lightweight.
Database-Driven Workflow
Unlike ad-hoc OSINT scripts, Recon-ng maintains a SQLite database (workspace) that stores all gathered intelligence across module runs. This means the output of one module (e.g., discovered domains) automatically becomes input for the next (e.g., DNS resolution). Workspaces can be created per engagement, exported, and shared. The reporting modules can generate HTML, CSV, JSON, and other output formats from the accumulated workspace data.
Agent Integration Patterns
AI agents can drive Recon-ng through its CLI interface or by scripting resource files. A resource file is a text file containing Recon-ng commands executed sequentially, enabling fully automated reconnaissance workflows: recon-ng -r /path/to/resource_file.rc. Agents can create resource files dynamically based on target parameters, execute them, then query the workspace database directly for structured results. The recon-cli mode supports non-interactive execution for pipeline integration. Key API keys (Shodan, BuiltWith, HackerTarget, etc.) are configured once per installation via the keys management system.
Installation
Clone the repository and install dependencies: git clone https://github.com/lanmaster53/recon-ng.git && cd recon-ng && pip install -r REQUIREMENTS. Recon-ng is also available in Kali Linux and BlackArch repositories. It requires Python 3 and relies on standard Python libraries plus a few OSINT-specific dependencies.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/recon-ng-web-reconnaissance-framework/)
