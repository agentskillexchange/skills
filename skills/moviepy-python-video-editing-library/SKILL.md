---
name: "MoviePy Python Video Editing Library"
description: "MoviePy is a Python library for video editing — cuts, concatenations, title insertions, compositing, and custom effects. It reads and writes all common audio and video formats including GIF, powered by FFmpeg under the hood."
verification: security_reviewed
source: "https://github.com/Zulko/moviepy"
category:
  - "Media &amp; Transcription"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "zulko/moviepy"
  github_stars: 14491
---

# MoviePy Python Video Editing Library

MoviePy is an open-source Python library for video editing that enables programmatic cuts, concatenations, title insertions, video compositing (non-linear editing), video processing, and creation of custom effects. It can read and write all common audio and video formats including GIF, and runs on Windows, macOS, and Linux with Python 3.9+.
The library works by importing media — video frames, images, and sounds — and converting them into NumPy arrays, making every pixel accessible for manipulation. Video and audio effects can be defined in just a few lines of Python code. MoviePy provides built-in effects for common operations like fading, rotating, resizing, speed changes, and text overlays, while also supporting custom effect creation through simple Python functions.
A typical MoviePy workflow involves loading a video with VideoFileClip, applying transformations like subclipping or volume adjustment, compositing multiple clips together with CompositeVideoClip, adding text overlays with TextClip, and writing the result to a new file. The library handles format detection, codec selection, and FFmpeg invocation automatically.
MoviePy v2.0 introduced major improvements including a cleaner API, better memory management, and improved compositing performance. The library is particularly well-suited for batch video processing, automated video generation, social media content creation, and data visualization overlays. Under the hood, it delegates encoding and decoding to FFmpeg while providing a high-level Pythonic interface.
Install via pip install moviepy. Licensed under MIT with over 14,000 GitHub stars, comprehensive documentation at zulko.github.io/moviepy, and active maintenance with recent v2.0 release.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/moviepy-python-video-editing-library/)
