---
name: "Mailpit SMTP Testing and Email Capture Workbench"
slug: "mailpit-smtp-testing-email-capture-workbench"
description: "This skill uses Mailpit as a safe SMTP sink for development, QA, and automated test runs. It helps teams capture, inspect, search, and validate transactional email without sending anything to real inboxes."
github_stars: 9051
verification: "listed"
source: "https://github.com/axllent/mailpit"
category: "Calendar, Email & Productivity"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "axllent/mailpit"
  github_stars: 9051
---

# Mailpit SMTP Testing and Email Capture Workbench

This skill uses Mailpit as a safe SMTP sink for development, QA, and automated test runs. It helps teams capture, inspect, search, and validate transactional email without sending anything to real inboxes.

## Installation

Use the upstream install or setup path that matches your environment:
- If installed using homebrew, you may run brew services start mailpit to always run mailpit automatically.

Requirements and caveats from upstream:
- <a href="https://github.com/axllent/mailpit/actions/workflows/build-docker.yml"><img src="https://github.com/axllent/mailpit/actions/workflows/build-docker.yml/badge.svg" alt="CI Docker build status"></a>
- <a href="https://hub.docker.com/r/axllent/mailpit"><img src="https://img.shields.io/docker/pulls/axllent/mailpit.svg" alt="Docker pulls"></a>
- Runs entirely from a single [static binary](https://mailpit.axllent.org/docs/install/) or multi-architecture [Docker images](https://mailpit.axllent.org/docs/install/docker/)

Basic usage or getting-started notes:
- Modern web UI with advanced [mail search](https://mailpit.axllent.org/docs/usage/search-filters/) to view emails (formatted HTML, highlighted HTML source, text, headers, raw source, and MIME attachments
- Real-time web UI updates using web sockets for new mail & optional [browser notifications](https://mailpit.axllent.org/docs/usage/notifications/) when new mail is received
- [HTML check](https://mailpit.axllent.org/docs/usage/html-check/) to test & score mail client compatibility with HTML emails

- Source: https://github.com/axllent/mailpit
- Extracted from upstream docs: https://raw.githubusercontent.com/axllent/mailpit/HEAD/README.md

## Documentation

- https://mailpit.axllent.org/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/mailpit-smtp-testing-email-capture-workbench/)
