---
name: "Create and debug local-first declarative workflow jobs with Dagu"
slug: "create-and-debug-local-first-declarative-workflow-jobs-with-dagu"
description: "Use Dagu to define file-backed workflow jobs in YAML, run them locally or across workers, and inspect failures through a lightweight operator surface instead of a heavyweight orchestrator."
github_stars: 3303
verification: "listed"
source: "https://github.com/dagucloud/dagu"
author: "Dagu Cloud"
publisher_type: "organization"
category: "Templates & Workflows"
framework: "Custom Agents"
tool_ecosystem:
  github_repo: "dagucloud/dagu"
  github_stars: 3303
---

# Create and debug local-first declarative workflow jobs with Dagu

Use Dagu to define file-backed workflow jobs in YAML, run them locally or across workers, and inspect failures through a lightweight operator surface instead of a heavyweight orchestrator.

## Prerequisites

Dagu binary or Docker, YAML workflow files, optional web UI access

## Installation

Use the upstream install or setup path that matches your environment:
- brew install dagu
- docker run --rm -v ~/.dagu:/var/lib/dagu -p 8080:8080 ghcr.io/dagucloud/dagu:latest dagu start-all
- git clone https://github.com/dagucloud/dagu.git && cd dagu
- make build # Build frontend + Go binary

Requirements and caveats from upstream:
- Keep your existing automation as shell scripts, Python scripts, containers, SSH commands, SQL jobs, HTTP calls, AI harnesses, and reusable action packages. Define the workflow in plain YAML, run it with one binary, an...
- │ Python Runtime │ Self-hosted by default.
- Dagu stores state in local files by default. How much it can run depends on the machine and the workload. CPU, disk speed, workflow duration, queue settings, and worker capacity all matter.

Basic usage or getting-started notes:
- Dagu gives your automation a home. Run your existing scripts, containers, SQL jobs, and HTTP calls as visible, governed workflows with schedules, retries, logs, artifacts, human-in-the-loop, and observability without...
- For a quick look at how workflows are defined, see the [examples](https://docs.dagu.sh/writing-workflows/examples). For a compact repository-level map of the YAML shape and current run:, action:, and actions: syntax,...
- | Run Details | Step Logs | Documents |

- Source: https://github.com/dagucloud/dagu
- Extracted from upstream docs: https://raw.githubusercontent.com/dagucloud/dagu/HEAD/README.md

## Documentation

- https://docs.dagu.sh/oss

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/create-and-debug-local-first-declarative-workflow-jobs-with-dagu/)
