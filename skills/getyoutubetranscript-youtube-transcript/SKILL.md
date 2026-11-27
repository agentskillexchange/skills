---
name: "GetYouTubeTranscript: YouTube Transcripts, Search and Channel Data"
slug: "getyoutubetranscript-youtube-transcript"
description: "Fetch YouTube transcripts, search videos and channels, browse a channel's uploads and playlists, and find where something is said, through the getyoutubetranscript.com REST API with bundled shell scripts."
verification: "listed"
source: "https://github.com/tubeagentkit/youtube-transcript-skills/blob/26bac904df785ab75ba2840ea10d33b591b9b018/skills/youtube-transcript/SKILL.md"
category: "Media & Transcription"
framework: "Claude Code"
---

# GetYouTubeTranscript: YouTube Transcripts, Search and Channel Data

Use this skill when a user shares a YouTube link or video ID and wants its transcript, a summary, notes, quotes with timestamps, or an answer about what is said in the video. It also covers the steps before reading: searching YouTube for videos or channels, resolving a channel handle to its channel ID, listing a channel's uploads, Shorts, live streams, playlists and posts, searching inside one channel, and listing every video in a playlist. Everything goes through the [getyoutubetranscript.com](https://getyoutubetranscript.com) REST API at `https://getyoutubetranscript.com/api/v1`, so no Google Cloud project or YouTube Data API key is needed.

## What the skill does

1. Fetch a transcript with `GET /transcript`. The response includes the title, author and thumbnail, the caption type (manual or auto-generated) and the language actually returned. Add `timestamps=true` for per-line segments with start time and duration, which is what quotes, chapters and "where does the video say X" questions need.
2. List a video's caption languages with `GET /transcript/languages`, then request a specific language.
3. Pull transcripts for up to 100 videos in one call with `POST /batch`, then poll `GET /batch` for results. Failed videos are not charged.
4. Search YouTube with `GET /search` (videos or channels), resolve a handle or URL with `GET /resolve`, and browse a channel with `GET /channel/latest`, `GET /channel/videos` and `GET /channel/search`.
5. List a playlist's videos with `GET /playlist`, and check the remaining balance for free with `GET /credits`.

Individual metered endpoints cost one credit per successful request or page. Batch transcripts cost one credit per successfully processed video; failed videos are not charged. Batch polling and credit-balance checks are free. New accounts get 100 free credits with no card.

## Getting an API key

If no key is configured, the skill tells the user the cost, asks for an email address, sends it to the signup endpoint, and then exchanges the 6-digit code the user receives for an API key. The key is saved to `~/.config/getyoutubetranscript/api_key` with permissions readable only by the user and is never printed in the chat. A user who cannot receive the code can sign up in the dashboard and paste a key instead.

## Installation

### Claude Code, Cursor, Codex and other Agent Skills clients

```bash
npx skills add tubeagentkit/youtube-transcript-skills --skill youtube-transcript
```

### OpenClaw

```bash
npx clawhub@latest install tubeagentkit/youtube-transcript
```

### Direct repo/manual install

```bash
git clone https://github.com/tubeagentkit/youtube-transcript-skills.git
git -C youtube-transcript-skills checkout 26bac904df785ab75ba2840ea10d33b591b9b018
mkdir -p ~/.claude/skills
cp -r youtube-transcript-skills/skills/youtube-transcript ~/.claude/skills/
```

A hosted MCP server with the same capabilities is available at `https://getyoutubetranscript.com/api/mcp` for clients that prefer MCP over a skill.
