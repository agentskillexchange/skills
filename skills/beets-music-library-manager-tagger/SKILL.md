---
name: "Beets Music Library Manager and Tagger"
description: "Manage and tag music libraries with beets, the Python-based CLI tool that auto-tags audio files using MusicBrainz metadata. Import, organize, deduplicate, and query your music collection with a powerful plugin system and flexible query language."
category: "Media &amp; Transcription"
framework: "Custom Agents"
verification: security_reviewed
source: "https://github.com/beetbox/beets"
tool_ecosystem:
  github_repo: "https://github.com/beetbox/beets"
  github_stars: 14901
  license: "MIT"
---
# Beets Music Library Manager and Tagger

Manage and tag music libraries with beets, the Python-based CLI tool that auto-tags audio files using MusicBrainz metadata. Import, organize, deduplicate, and query your music collection with a powerful plugin system and flexible query language.

beets is an open-source music library management tool written in Python. It provides a CLI for importing, organizing, and maintaining music collections with accurate metadata sourced primarily from the MusicBrainz database. Available via pip (pip install beets), it runs on Linux, macOS, and Windows.

The core workflow centers on the beet import command, which scans audio files (MP3, FLAC, OGG, AAC, and more), fingerprints them using the Chromaprint/AcoustID algorithm, matches them against MusicBrainz records, and writes corrected tags (artist, album, track number, year, genre) back to the files. It handles edge cases like multi-disc albums, various artists compilations, and partial matches with configurable similarity thresholds.

beets maintains a SQLite database of your library that supports a powerful query language. Commands like beet list artist:Beatles year:1969 filter your collection instantly, while beet stats provides aggregate information. The beet modify command applies bulk tag changes, and beet move reorganizes files on disk according to configurable path templates (e.g. $artist/$album/$track - $title).

The plugin ecosystem is where beets truly excels. Over 50 built-in and community plugins extend its capabilities: fetchart downloads album art from Cover Art Archive and Amazon, lyrics fetches song lyrics, lastgenre assigns genres from Last.fm, duplicates finds redundant tracks, convert transcodes audio formats, and web provides a browsable HTTP interface to your library. The acousticbrainz plugin adds acoustic analysis metadata like BPM, key, and mood.

For AI agents, beets serves as the foundation for automated music library curation workflows. An agent can invoke beets to import new downloads, verify metadata accuracy, detect duplicate tracks, generate library statistics, and maintain consistent file organization — all through CLI subprocess calls with structured output. Configuration lives in config.yaml, making it version-controllable.

Source: github.com/beetbox/beets | Website: beets.io — MIT licensed, 14,800+ GitHub stars, 1,900+ forks, actively maintained.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill beets-music-library-manager-tagger
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill beets-music-library-manager-tagger -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill beets-music-library-manager-tagger -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill beets-music-library-manager-tagger -a codex
```

### OpenClaw

```bash
clawhub install beets-music-library-manager-tagger
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/beets-music-library-manager-tagger/)
