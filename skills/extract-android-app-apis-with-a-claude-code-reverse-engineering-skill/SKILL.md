---
name: "Extract Android app APIs with a Claude Code reverse-engineering skill"
slug: "extract-android-app-apis-with-a-claude-code-reverse-engineering-skill"
description: "Use this Claude Code skill to decompile APK, XAPK, JAR, and AAR files, recover Kotlin names, and extract Android HTTP API behavior for authorized analysis."
github_stars: 7729
verification: "security_reviewed"
source: "https://github.com/SimoneAvogadro/android-reverse-engineering-skill"
author: "Simone Avogadro"
publisher_type: "individual"
category: "Security & Verification"
framework: "Claude Code"
tool_ecosystem:
  github_repo: "SimoneAvogadro/android-reverse-engineering-skill"
  github_stars: 7729
---

# Extract Android app APIs with a Claude Code reverse-engineering skill

Use this Claude Code skill to decompile APK, XAPK, JAR, and AAR files, recover Kotlin names, and extract Android HTTP API behavior for authorized analysis.

## Prerequisites

Claude Code plugin marketplace support, Java JDK 17+, jadx CLI, optional Vineflower or Fernflower, optional dex2jar, and an Android APK, XAPK, JAR, or AAR artifact the operator is authorized to analyze

## Installation

Install or set up from the source-backed instructions:

In Claude Code, run /plugin marketplace add SimoneAvogadro/android-reverse-engineering-skill, then /plugin install android-reverse-engineering@android-reverse-engineering-skill. Install Java JDK 17+ and jadx, add optional Vineflower/Fernflower and dex2jar for deeper analysis, then invoke /decompile path/to/app.apk or ask Claude Code to extract API endpoints from an authorized Android artifact.

- Source: https://github.com/SimoneAvogadro/android-reverse-engineering-skill

## Documentation

- https://github.com/SimoneAvogadro/android-reverse-engineering-skill

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/extract-android-app-apis-with-a-claude-code-reverse-engineering-skill/)
