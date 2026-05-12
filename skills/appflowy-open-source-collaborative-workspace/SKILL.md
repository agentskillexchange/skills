---
title: "AppFlowy Open Source Collaborative Workspace"
slug: "appflowy-open-source-collaborative-workspace"
description: "AppFlowy brings documents, projects, wikis, and AI-assisted collaboration into a self-hosted or desktop-friendly workspace. This skill helps agents work from the real AppFlowy project, docs, and deployment methods when users need an open source Notion-style environment with local control."
verification: "security_reviewed"
source: "https://github.com/AppFlowy-IO/AppFlowy"
author: "AppFlowy-IO"
publisher_type: "Open Source Project"
category: "Calendar, Email & Productivity"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "AppFlowy-IO/AppFlowy"
  github_stars: 69650
---

# AppFlowy Open Source Collaborative Workspace

AppFlowy brings documents, projects, wikis, and AI-assisted collaboration into a self-hosted or desktop-friendly workspace. This skill helps agents work from the real AppFlowy project, docs, and deployment methods when users need an open source Notion-style environment with local control.

## Prerequisites

Docker, Docker Compose, desktop app runtime, local storage

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
docker run --rm -v $HOME/.Xauthority:/root/.Xauthority:rw -v /tmp/.X11-unix:/tmp/.X11-unix -v /dev/dri:/dev/dri -v /var/run/dbus/system_bus_socket:/var/run/dbus/system_bus_socket -v appflowy-data:/home/appflowy -e DISPLAY=${DISPLAY} appflowyio/appflowy_client:main
```

## Documentation

- https://docs.appflowy.io/docs

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/appflowy-open-source-collaborative-workspace/)
