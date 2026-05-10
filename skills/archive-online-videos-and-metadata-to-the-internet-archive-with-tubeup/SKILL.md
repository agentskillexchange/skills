---
title: "Archive online videos and metadata to the Internet Archive with Tubeup"
slug: "archive-online-videos-and-metadata-to-the-internet-archive-with-tubeup"
description: "Download a supported video URL with yt-dlp and upload the preserved file plus metadata to archive.org as a repeatable preservation job."
github_stars: 487
verification: "security_reviewed"
source: "https://github.com/bibanon/tubeup"
author: "Bibliotheca Anonoma / bibanon"
publisher_type: "individual"
category: "Media & Transcription"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "bibanon/tubeup"
  github_stars: 487
---

# Archive online videos and metadata to the Internet Archive with Tubeup

Download a supported video URL with yt-dlp and upload the preserved file plus metadata to archive.org as a repeatable preservation job.

## Prerequisites

Python 3.10+, pipx, yt-dlp, ffmpeg, Deno, Internet Archive account

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install prerequisites including `ffmpeg`, `deno`, and `pipx`, then install `yt-dlp[default,curl-cffi]`, `internetarchive`, and `tubeup` with pipx, run `ia configure`, and archive URLs with `tubeup <url>`.
```

## Documentation

- https://github.com/bibanon/tubeup

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/archive-online-videos-and-metadata-to-the-internet-archive-with-tubeup/)
