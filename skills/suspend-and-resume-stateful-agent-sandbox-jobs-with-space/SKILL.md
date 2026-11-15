---
name: "Suspend and resume stateful agent sandbox jobs with SPACE"
slug: "suspend-and-resume-stateful-agent-sandbox-jobs-with-space"
description: "Run a stateful job in self-hosted SPACE, preserve sandbox state across suspension, and reconcile operation IDs, readiness and command transcripts before continuing."
verification: "security_reviewed"
source: "https://github.com/perplexityai/SPACE/blob/main/docs/first-sandbox.md"
author: "Perplexity AI"
publisher_type: "organization"
category: "Security & Verification"
framework: "Multi-Framework"
---

# Suspend and resume stateful agent sandbox jobs with SPACE

Run a stateful job in self-hosted SPACE, preserve sandbox state across suspension, and reconcile operation IDs, readiness and command transcripts before continuing.

## Prerequisites

Linux x86_64 host with KVM; privileged Docker and Kind deployment; Bash/Git/curl; Python 3.8+; configured SPACE native HTTP API and data plane

## Installation

Install or set up from the source-backed instructions:

Clone https://github.com/perplexityai/SPACE.git and review docs/installation.md at the chosen revision. The documented local setup requires apt-based Linux x86_64 with KVM, privileged local Docker, tun/loop devices and btrfs support. Follow the documented prerequisite, Firecracker vendor and Kind bootstrap steps; wait for template publication and node readiness. Configure SPACE_API_URL, SPACE_DATA_PLANE_URL and SPACE_API_TOKEN as documented without recording tokens in run artifacts. From the configured checkout run python3 examples/first_sandbox.py. This is a private local setup with development defaults; it is not a production deployment recipe.

- Source: https://github.com/perplexityai/SPACE/blob/main/docs/first-sandbox.md

## Documentation

- https://github.com/perplexityai/SPACE/blob/main/docs/first-sandbox.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/suspend-and-resume-stateful-agent-sandbox-jobs-with-space/)
