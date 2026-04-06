---
name: Git Updater WordPress Plugin and Theme Auto-Updater from Git Repositories
description: Git Updater enables automatic updates for WordPress plugins and themes
  hosted on GitHub, Bitbucket, GitLab, and Gitea repositories, with support for release
  assets, language packs, and branch switching.
category: "WordPress &amp; CMS"
framework: Multi-Framework
verification: security_reviewed
source: "https://github.com/afragen/git-updater"
tool_ecosystem:
  github_repo: "https://github.com/afragen/git-updater"
  github_stars: 3316
  license: GPL-3.0
---
# Git Updater WordPress Plugin and Theme Auto-Updater from Git Repositories

Git Updater enables automatic updates for WordPress plugins and themes hosted on GitHub, Bitbucket, GitLab, and Gitea repositories, with support for release assets, language packs, and branch switching.

Git Updater is a WordPress plugin that enables automatic updates for plugins and themes hosted on Git repositories. While WordPress.org provides update infrastructure for plugins in its directory, many custom and private plugins are distributed via GitHub, GitLab, Bitbucket, or Gitea. Git Updater bridges this gap by checking these repositories for new releases and applying updates through the standard WordPress update flow.

How It Works

Add a header to your plugin or theme file like GitHub Plugin URI: https://github.com/owner/repo or GitHub Theme URI: https://github.com/owner/repo. Git Updater reads this header, checks the repository for new releases or tags, and presents updates in the WordPress admin dashboard just like any WordPress.org-hosted plugin.

Multi-Platform Support

The core plugin handles GitHub repositories. API plugins for Bitbucket, GitLab, Gitea, and Gist are available as one-click installs from the Add-Ons tab. Each API plugin extends Git Updater with platform-specific authentication and repository checking. The plugin supports language pack distribution from Git repositories as well.

Agent Integration

For AI agents managing WordPress infrastructure, Git Updater provides programmatic control over plugin deployment pipelines. Agents can manage custom plugin repositories, trigger updates via WP-CLI, and ensure private plugins stay current without manual intervention. The plugin requires PHP 8.0+ and WordPress 5.9+. Licensed under GPL-3.0. A Slack community and comprehensive knowledge base are available at git-updater.com.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill git-updater-wordpress-plugin-theme-auto-updater
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill git-updater-wordpress-plugin-theme-auto-updater -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill git-updater-wordpress-plugin-theme-auto-updater -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill git-updater-wordpress-plugin-theme-auto-updater -a codex
```

### OpenClaw

```bash
clawhub install git-updater-wordpress-plugin-theme-auto-updater
```


## Source

- [GitHub](https://github.com/afragen/git-updater)
