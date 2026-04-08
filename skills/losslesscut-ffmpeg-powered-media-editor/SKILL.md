---
title: LosslessCut FFmpeg-Powered Media Editor
description: 'What is LosslessCut? LosslessCut is an open-source cross-platform application
  for extremely fast, lossless operations on video, audio, subtitle, and other media
  files. Built as a GUI frontend for FFmpeg, it performs direct data copy (remux)
  operations that trim, cut, merge, and rearrange media segments without re-encoding
  — preserving the original codec quality while completing in seconds what traditional
  video editors take minutes or hours to process. How This Skill Works This skill
  enables agents to automate media editing workflows using LosslessCut’s capabilities.
  The tool accepts virtually any media format that FFmpeg supports (MP4, MKV, MOV,
  AVI, WebM, MP3, FLAC, WAV, and hundreds more) and performs lossless operations by
  copying codec data directly without decoding and re-encoding. Agents can define
  cut points, segment boundaries, and merge operations either through the GUI or by
  importing/exporting segment data as CSV or JSON for batch processing. Key Capabilities
  Lossless cutting: Trim and split video/audio files at precise timestamps without
  quality loss. Smart cut mode enables frame-accurate cutting by re-encoding only
  the frames at cut boundaries while copying the rest losslessly. Segment management:
  Cut out unwanted sections (commercials, dead air), rearrange segment order, and
  export individual segments or merged output. Import/export segment lists as CSV
  for batch automation. Multi-track editing: Add, remove, replace, or re-order individual
  tracks (video, audio, subtitle, attachment) from media files. Combine tracks from
  multiple source files into a single output. Format remuxing: Convert container formats
  (MP4 to MKV, MOV to MP4, etc.) instantly without transcoding the underlying streams.
  Fix broken or incomplete media files by remuxing. Frame extraction: Export full-resolution
  snapshots as JPEG or PNG at any point in the video. Batch export every Nth frame,
  one per second, or based on scene change detection for thumbnail generation. Metadata
  editing: View and edit file-level metadata, per-track metadata, chapter markers,
  and track disposition flags. Inspect detailed codec and format information via embedded
  MediaInfo. Integration Points LosslessCut is built on Electron and uses FFmpeg for
  all media operations. It supports CLI invocation for headless batch processing scenarios.
  Segment lists can be imported/exported as CSV, enabling programmatic generation
  of edit decision lists from external analysis tools. The application reads any format
  FFmpeg supports and writes to major container formats including MP4 (H.264/H.265),
  MKV, MOV, WebM, and audio containers like MP3, M4A, FLAC, and OGG. It runs on Windows,
  macOS, and Linux. Source GitHub: mifi/lossless-cut (39.4K+ stars, GPL-2.0 license)'
verification: security_reviewed
source: https://github.com/mifi/lossless-cut
category:
- Media &amp; Transcription
framework:
- Custom Agents
tool_ecosystem:
  github_repo: mifi/lossless-cut
  github_stars: 39480
---

# LosslessCut FFmpeg-Powered Media Editor

What is LosslessCut? LosslessCut is an open-source cross-platform application for extremely fast, lossless operations on video, audio, subtitle, and other media files. Built as a GUI frontend for FFmpeg, it performs direct data copy (remux) operations that trim, cut, merge, and rearrange media segments without re-encoding — preserving the original codec quality while completing in seconds what traditional video editors take minutes or hours to process. How This Skill Works This skill enables agents to automate media editing workflows using LosslessCut’s capabilities. The tool accepts virtually any media format that FFmpeg supports (MP4, MKV, MOV, AVI, WebM, MP3, FLAC, WAV, and hundreds more) and performs lossless operations by copying codec data directly without decoding and re-encoding. Agents can define cut points, segment boundaries, and merge operations either through the GUI or by importing/exporting segment data as CSV or JSON for batch processing. Key Capabilities Lossless cutting: Trim and split video/audio files at precise timestamps without quality loss. Smart cut mode enables frame-accurate cutting by re-encoding only the frames at cut boundaries while copying the rest losslessly. Segment management: Cut out unwanted sections (commercials, dead air), rearrange segment order, and export individual segments or merged output. Import/export segment lists as CSV for batch automation. Multi-track editing: Add, remove, replace, or re-order individual tracks (video, audio, subtitle, attachment) from media files. Combine tracks from multiple source files into a single output. Format remuxing: Convert container formats (MP4 to MKV, MOV to MP4, etc.) instantly without transcoding the underlying streams. Fix broken or incomplete media files by remuxing. Frame extraction: Export full-resolution snapshots as JPEG or PNG at any point in the video. Batch export every Nth frame, one per second, or based on scene change detection for thumbnail generation. Metadata editing: View and edit file-level metadata, per-track metadata, chapter markers, and track disposition flags. Inspect detailed codec and format information via embedded MediaInfo. Integration Points LosslessCut is built on Electron and uses FFmpeg for all media operations. It supports CLI invocation for headless batch processing scenarios. Segment lists can be imported/exported as CSV, enabling programmatic generation of edit decision lists from external analysis tools. The application reads any format FFmpeg supports and writes to major container formats including MP4 (H.264/H.265), MKV, MOV, WebM, and audio containers like MP3, M4A, FLAC, and OGG. It runs on Windows, macOS, and Linux. Source GitHub: mifi/lossless-cut (39.4K+ stars, GPL-2.0 license)

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/losslesscut-ffmpeg-powered-media-editor/)
