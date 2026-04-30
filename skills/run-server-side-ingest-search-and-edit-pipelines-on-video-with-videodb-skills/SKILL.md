---
title: "Run server-side ingest, search, and edit pipelines on video with VideoDB Skills"
description: "Let an agent ingest video, transcribe it, search moments, clip results, and return playable streams without wiring up its own media pipeline."
verification: "listed"
source: "https://github.com/video-db/skills"
author: "VideoDB"
publisher_type: "organization"
category:
  - "errors"
  - "error_data"
framework:
  - "errors"
  - "error_data"
tool_ecosystem:
  github_repo: "video-db/skills"
  github_stars: 73
---

# Run server-side ingest, search, and edit pipelines on video with VideoDB Skills

Let an agent ingest video, transcribe it, search moments, clip results, and return playable streams without wiring up its own media pipeline.

## Prerequisites

Python 3.9+, a VideoDB API key, network access to VideoDB services, and an agent that can load the skills repo

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install the repo with npx skills add video-db/skills or the documented plugin path, set VIDEO_DB_API_KEY in the environment or project .env, run the setup flow, then invoke the upload, search, transcription, clipping, or editing prompts from your agent.
```

## Documentation

- https://docs.videodb.io

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-server-side-ingest-search-and-edit-pipelines-on-video-with-videodb-skills/)
