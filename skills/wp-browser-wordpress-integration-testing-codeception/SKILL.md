---
title: "wp-browser WordPress Integration Testing with Codeception"
description: "wp-browser is a PHP library that provides Codeception modules for testing WordPress plugins and themes. It supports unit, integration, functional, and acceptance testing with WordPress-aware test environments and database isolation."
slug: "wp-browser-wordpress-integration-testing-codeception"
category:
  - "WordPress &amp; CMS"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/lucatume/wp-browser"
tool_ecosystem:
  github_repo: "lucatume/wp-browser"
  github_stars: 634
---

# wp-browser WordPress Integration Testing with Codeception

wp-browser is a PHP library that provides Codeception modules for testing WordPress plugins and themes. It supports unit, integration, functional, and acceptance testing with WordPress-aware test environments and database isolation.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install wp-browser-wordpress-integration-testing-codeception
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

wp-browser is an open-source PHP library created by Luca Tumedei (lucatume) that provides a comprehensive set of Codeception modules specifically designed for testing WordPress projects. With over 10 years of proven success and active maintenance, it is the standard tool for structured WordPress testing across unit, integration, functional, and acceptance test levels.
The library integrates with Codeception, a popular PHP testing framework, and adds WordPress-specific modules that handle the complexity of bootstrapping WordPress for tests. It provides the WPLoader module for loading WordPress in integration tests, the WPDb module for database interaction and fixture management, the WPBrowser module for browser-based acceptance testing, and the WPWebDriver module for Selenium/WebDriver-based testing.
Key capabilities include: isolated database environments for each test run using transactions or cleanup, WordPress function and hook availability in integration tests, WP-CLI integration for site setup and configuration, support for testing custom post types, taxonomies, REST API endpoints, and AJAX handlers, multisite testing support, and PHP built-in web server support for running tests without Apache/Nginx.
wp-browser is installed via Composer (composer require --dev lucatume/wp-browser) and includes a guided initialization wizard that configures the test environment for your specific WordPress project setup. Documentation is available at wpbrowser.wptestkit.dev with detailed guides for each test type and module configuration.
With 630+ GitHub stars, 87 forks, MIT license, and active development, wp-browser is a mature tool that AI agents can use to scaffold and run comprehensive test suites for WordPress plugins and themes. It enables automated testing workflows including database state verification, REST API endpoint testing, hook and filter assertion, and full browser-based acceptance tests.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wp-browser-wordpress-integration-testing-codeception/)
