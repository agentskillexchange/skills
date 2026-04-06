---
name: "Navidrome Self-Hosted Music Streaming Server and Subsonic API"
description: "Integrate Navidrome’s self-hosted music server into AI agent workflows. Agents can manage music libraries, create playlists, control playback, and search collections through the Subsonic-compatible API and Navidrome’s native REST endpoints."
category: "Media &amp; Transcription"
framework: "Multi-Framework"
verification: security_reviewed
source: "https://github.com/navidrome/navidrome"
tool_ecosystem:
  github_repo: "https://github.com/navidrome/navidrome"
  github_stars: 20161
---
# Navidrome Self-Hosted Music Streaming Server and Subsonic API

Integrate Navidrome’s self-hosted music server into AI agent workflows. Agents can manage music libraries, create playlists, control playback, and search collections through the Subsonic-compatible API and Navidrome’s native REST endpoints.

Navidrome is an open-source, self-hosted music server and streamer with over 20,000 GitHub stars. Written in Go, it provides a lightweight yet feature-rich platform for managing and streaming personal music collections. Its Subsonic API compatibility means it works with dozens of existing music clients while also offering its own modern web interface.

What This Skill Enables

An agent skill built around Navidrome allows AI agents to manage music libraries intelligently. Through the Subsonic API (compatible with all Subsonic/OpenSubsonic clients) and Navidrome’s native API, agents can search music collections by artist, album, genre, or full-text query, create and manage playlists, control playback, rate and star tracks, and retrieve detailed metadata including album art, lyrics, and artist information.

Core Capabilities

The Subsonic API implemented by Navidrome provides endpoints for browsing the music library (getArtists, getAlbumList2, getRandomSongs), searching (search3 with full-text support), playlist management (createPlaylist, updatePlaylist, deletePlaylist), user and share management, media retrieval (stream, download, getCoverArt), and annotation (star, rate, scrobble). Navidrome extends the standard Subsonic API with additional features like smart playlists based on dynamic criteria, multi-user support with individual preferences, and real-time library monitoring.

Integration Points

Navidrome supports all major audio formats (MP3, FLAC, AAC, OGG, WMA, OPUS, and more) with on-the-fly transcoding. It integrates with Last.fm for scrobbling and artist metadata, Spotify for artist images, and MusicBrainz for album identification. The Subsonic API compatibility means agents can leverage any Subsonic-compatible client library available in Python, JavaScript, Go, and other languages. Navidrome also supports Jukebox mode for controlling playback on the server itself.

Technical Details

Navidrome is a single Go binary that can be deployed via Docker (deluan/navidrome) or as a standalone executable on Linux, macOS, and Windows. It uses SQLite for its database and requires minimal system resources. The Subsonic API authenticates via username/password with token-based authentication (salt + MD5 hash). API responses are available in XML and JSON formats. The server automatically monitors the music folder for changes and updates the library index in real time.

Use Cases

AI agents can use this skill to build smart music assistants that create playlists based on mood or activity descriptions, manage music library organization by fixing tags and metadata, generate listening statistics and recommendations, automate the discovery of new music by cross-referencing the library with external sources, and provide voice-controlled music playback through the streaming endpoints.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill navidrome-self-hosted-music-streaming-subsonic-api
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill navidrome-self-hosted-music-streaming-subsonic-api -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill navidrome-self-hosted-music-streaming-subsonic-api -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill navidrome-self-hosted-music-streaming-subsonic-api -a codex
```

### OpenClaw

```bash
clawhub install navidrome-self-hosted-music-streaming-subsonic-api
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/navidrome-self-hosted-music-streaming-subsonic-api/)
