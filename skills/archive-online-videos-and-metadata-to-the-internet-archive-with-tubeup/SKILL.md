---
name: "Archive online videos and metadata to the Internet Archive with Tubeup"
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

Use the upstream install or setup path that matches your environment:
- pipx ensurepath
- Use pipx to install the required python packages.
- pipx install "yt-dlp[default,curl-cffi]" internetarchive tubeup
- pipx upgrade-all ; deno upgrade

Requirements and caveats from upstream:
- Linux VPS with Python 3.10 or higher and pipx installed
- Install ffmpeg, pip3 (typically python3-pipx or in Arch python-pipx), and Deno (external java script support required by yt-dlp for Youtube extractor).

Basic usage or getting-started notes:
- tubeup uses yt-dlp to download a Youtube video (or [any other provider supported by yt-dlp](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md)), and then uploads it with all metadata to the Internet Archi...
- This script strongly recommends Linux or some sort of POSIX system (such as macOS), preferably from a rented VPS and not your personal machine or phone.
- Reccomended system specifications:

- Source: https://github.com/bibanon/tubeup
- Extracted from upstream docs: https://raw.githubusercontent.com/bibanon/tubeup/HEAD/README.md

## Documentation

- https://github.com/bibanon/tubeup

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/archive-online-videos-and-metadata-to-the-internet-archive-with-tubeup/)
