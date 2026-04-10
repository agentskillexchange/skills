---
name: "wp-browser WordPress Integration Testing with Codeception"
description: "wp-browser is a PHP library that provides Codeception modules for testing WordPress plugins and themes. It supports unit, integration, functional, and acceptance testing with WordPress-aware test environments and database isolation."
verification: security_reviewed
source: "https://github.com/lucatume/wp-browser"
category:
  - "WordPress &amp; CMS"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "lucatume/wp-browser"
  github_stars: 634
---

# wp-browser WordPress Integration Testing with Codeception

wp-browser is an open-source PHP library created by Luca Tumedei (lucatume) that provides a comprehensive set of Codeception modules specifically designed for testing WordPress projects. With over 10 years of proven success and active maintenance, it is the standard tool for structured WordPress testing across unit, integration, functional, and acceptance test levels.
The library integrates with Codeception, a popular PHP testing framework, and adds WordPress-specific modules that handle the complexity of bootstrapping WordPress for tests. It provides the WPLoader module for loading WordPress in integration tests, the WPDb module for database interaction and fixture management, the WPBrowser module for browser-based acceptance testing, and the WPWebDriver module for Selenium/WebDriver-based testing.
Key capabilities include: isolated database environments for each test run using transactions or cleanup, WordPress function and hook availability in integration tests, WP-CLI integration for site setup and configuration, support for testing custom post types, taxonomies, REST API endpoints, and AJAX handlers, multisite testing support, and PHP built-in web server support for running tests without Apache/Nginx.
wp-browser is installed via Composer (composer require --dev lucatume/wp-browser) and includes a guided initialization wizard that configures the test environment for your specific WordPress project setup. Documentation is available at wpbrowser.wptestkit.dev with detailed guides for each test type and module configuration.
With 630+ GitHub stars, 87 forks, MIT license, and active development, wp-browser is a mature tool that AI agents can use to scaffold and run comprehensive test suites for WordPress plugins and themes. It enables automated testing workflows including database state verification, REST API endpoint testing, hook and filter assertion, and full browser-based acceptance tests.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wp-browser-wordpress-integration-testing-codeception/)
