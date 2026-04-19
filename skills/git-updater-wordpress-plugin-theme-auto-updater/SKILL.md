---
title: "Git Updater WordPress Plugin and Theme Auto-Updater from Git Repositories"
description: "Git Updater is a WordPress plugin that enables automatic updates for plugins and themes hosted on Git repositories. While WordPress.org provides update infrastructure for plugins in its directory, many custom and private plugins are distributed via GitHub, GitLab, Bitbucket, or Gitea. Git Updater bridges this gap by checking these repositories for new releases and applying updates through the standard WordPress update flow. How It Works Add a header to your plugin or theme file like GitHub Plugin URI: https://github.com/owner/repo or GitHub Theme URI: https://github.com/owner/repo . Git Updater reads this header, checks the repository for new releases or tags, and presents updates in the WordPress admin dashboard just like any WordPress.org-hosted plugin. Multi-Platform Support The core plugin handles GitHub repositories. API plugins for Bitbucket, GitLab, Gitea, and Gist are available as one-click installs from the Add-Ons tab. Each API plugin extends Git Updater with platform-specific authentication and repository checking. The plugin supports language pack distribution from Git repositories as well. Agent Integration For AI agents managing WordPress infrastructure, Git Updater provides programmatic control over plugin deployment pipelines. Agents can manage custom plugin repositories, trigger updates via WP-CLI, and ensure private plugins stay current without manual intervention. The plugin requires PHP 8.0+ and WordPress 5.9+. Licensed under GPL-3.0. A Slack community and comprehensive knowledge base are available at git-updater.com."
source: "https://github.com/afragen/git-updater"
verification: "security_reviewed"
category:
  - "WordPress &amp; CMS"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "afragen/git-updater"
  github_stars: 3316
---

# Git Updater WordPress Plugin and Theme Auto-Updater from Git Repositories

Git Updater is a WordPress plugin that enables automatic updates for plugins and themes hosted on Git repositories. While WordPress.org provides update infrastructure for plugins in its directory, many custom and private plugins are distributed via GitHub, GitLab, Bitbucket, or Gitea. Git Updater bridges this gap by checking these repositories for new releases and applying updates through the standard WordPress update flow. How It Works Add a header to your plugin or theme file like GitHub Plugin URI: https://github.com/owner/repo or GitHub Theme URI: https://github.com/owner/repo . Git Updater reads this header, checks the repository for new releases or tags, and presents updates in the WordPress admin dashboard just like any WordPress.org-hosted plugin. Multi-Platform Support The core plugin handles GitHub repositories. API plugins for Bitbucket, GitLab, Gitea, and Gist are available as one-click installs from the Add-Ons tab. Each API plugin extends Git Updater with platform-specific authentication and repository checking. The plugin supports language pack distribution from Git repositories as well. Agent Integration For AI agents managing WordPress infrastructure, Git Updater provides programmatic control over plugin deployment pipelines. Agents can manage custom plugin repositories, trigger updates via WP-CLI, and ensure private plugins stay current without manual intervention. The plugin requires PHP 8.0+ and WordPress 5.9+. Licensed under GPL-3.0. A Slack community and comprehensive knowledge base are available at git-updater.com.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/git-updater-wordpress-plugin-theme-auto-updater/)
