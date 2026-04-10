---
name: "Camoufox Open Source Anti-Detect Browser for Python Automation"
description: "Camoufox is an open source anti-detect browser built on Firefox that provides robust fingerprint injection and anti-bot evasion for Python automation workflows. It integrates with Playwright to deliver stealth browsing capabilities that bypass modern bot detection systems."
verification: security_reviewed
source: "https://github.com/daijro/camoufox"
category:
  - "Browser Automation"
framework:
  - "Custom Agents"
---

# Camoufox Open Source Anti-Detect Browser for Python Automation

Camoufox is a purpose-built anti-detect browser that enables AI agents and automation scripts to interact with websites without being flagged by anti-bot systems. Built as a modified Firefox fork, Camoufox intercepts fingerprint data at the C++ implementation level rather than injecting JavaScript, making it fundamentally more resistant to detection than traditional browser automation approaches.
How It Works
Camoufox wraps around the Playwright API through its Python package. When launched, it automatically generates and injects unique device characteristics including OS fingerprints, CPU info, navigator properties, fonts, HTTP headers, screen dimensions, viewport sizes, WebGL parameters, and browser addons. It uses BrowserForge under the hood to produce realistic fingerprint combinations.
Key Capabilities

C++ Level Fingerprint Injection: All navigator properties, screen dimensions, geolocation, timezone, locale, and Intl spoofing are handled at the browser engine level, invisible to page JavaScript inspection.
WebRTC IP Spoofing: Operates at the protocol level, not through JavaScript overrides.
Anti-Graphical Fingerprinting: WebGL parameters, supported extensions, context attributes, shader precision formats, and font metrics are all spoofed consistently.
Human-like Mouse Movement: Built-in cursor path simulation that mimics natural human interaction patterns.
Ad Blocking and CSS Animation Removal: Reduces noise and improves performance for scraping tasks.
Memory Optimized: Debloated Firefox build optimized for automation workloads.

Integration Points
Install from PyPI with pip install camoufox and camoufox fetch to download the browser binary. The Python interface wraps Playwright, so existing Playwright scripts can be adapted with minimal changes. Camoufox supports both sync and async APIs, headless and headed modes, and can be configured with custom proxies, geolocation, and locale settings per session.
Agent Use Cases
Camoufox is particularly useful for agents that need to access websites protected by Cloudflare, DataDome, or similar WAFs. Web scraping agents can rotate fingerprints across sessions while maintaining realistic browser signatures. Research agents can access content without triggering CAPTCHA challenges. QA agents can test how applications behave with different device and browser configurations.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/camoufox-antidetect-browser-python/)
