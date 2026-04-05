---
name: "Monolith Web Page Archiver and Single-File Bundler"
description: "Monolith is a CLI tool and Rust library that saves complete web pages as a single HTML file by embedding CSS, images, JavaScript, and fonts as data URLs. It produces self-contained HTML5 documents that render correctly offline without external dependencies."
category: "Research &amp; Scraping"
framework: "Custom Agents"
verification: security_reviewed
source: "https://github.com/Y2Z/monolith"
tool_ecosystem:
  github_repo: "y2z/monolith"
  github_stars: 14932
  license: "CC0-1.0"
---
# Monolith Web Page Archiver and Single-File Bundler

Monolith is a CLI tool and Rust library that saves complete web pages as a single HTML file by embedding CSS, images, JavaScript, and fonts as data URLs. It produces self-contained HTML5 documents that render correctly offline without external dependencies.

Monolith is a command-line tool written in Rust that bundles any web page into a single, self-contained HTML file. Unlike browser “Save As” functions that create folders of separate assets, Monolith embeds all CSS, images, JavaScript, and font resources directly into the HTML as data URLs, producing one portable file.

How It Works Monolith fetches the target URL, parses the HTML, resolves all referenced assets (stylesheets, images, scripts, fonts, videos), downloads them, and encodes them as base64 data URLs inline within the HTML document. The result is a single .html file that browsers render exactly as the original page appeared, even without network access.

Filtering and Control Fine-grained control over what gets embedded is available through command-line flags: exclude audio (-a), CSS (-c), images (-i), JavaScript (-j), video (-v), or web fonts (-F). Domain whitelisting (-d) and blacklisting (-B) control which external domains assets are fetched from. The isolation flag (-I) prevents the saved page from making any network requests when opened. Output format can be set to MHTML (-m) instead of HTML5.

Pipeline Integration Monolith reads from stdin and writes to stdout, making it composable with other tools. For JavaScript-heavy single-page applications, it can be chained with headless Chromium to first render the page, then pipe the DOM output to Monolith for asset embedding. Custom User-Agent strings, cookie files, timeout settings, and proxy support (via environment variables) are all configurable.

Agent Integration AI agents can use Monolith for web research archiving, creating offline snapshots of documentation, preserving evidence of web content, and building local knowledge bases. The stdin/stdout pipeline support makes it straightforward to integrate into automated workflows. The Rust library (available as a crate) enables programmatic use within larger applications.

Installation Available via cargo install monolith, Homebrew (brew install monolith), Snap, Chocolatey, Scoop, winget, MacPorts, Nix, Guix, pacman (Arch), apk (Alpine), and pre-built binaries for Windows, Linux, and macOS from GitHub releases.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill monolith-web-page-single-file-archiver
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill monolith-web-page-single-file-archiver -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill monolith-web-page-single-file-archiver -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill monolith-web-page-single-file-archiver -a codex
```

### OpenClaw

```bash
clawhub install monolith-web-page-single-file-archiver
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/monolith-web-page-single-file-archiver/)
