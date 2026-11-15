---
name: "Control launch behavior with GO Feature Flag"
slug: "control-launch-behavior-with-go-feature-flag"
description: "Use GO Feature Flag as an OpenFeature-compatible control plane for rollout rules, targeting, experiments, remote config, and launch verification."
github_stars: 2050
verification: "security_reviewed"
source: "https://github.com/thomaspoignant/go-feature-flag"
author: "Thomas Poignant"
publisher_type: "individual"
category: "Monitoring & Alerts"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "thomaspoignant/go-feature-flag"
  github_stars: 2050
---

# Control launch behavior with GO Feature Flag

Use GO Feature Flag as an OpenFeature-compatible control plane for rollout rules, targeting, experiments, remote config, and launch verification.

## Prerequisites

GO Feature Flag relay proxy or SDK, OpenFeature-compatible application client, flag configuration store

## Installation

Use the upstream install or setup path that matches your environment:
- docker run \
- _If you don't want to use docker to install the **relay proxy** you can follow other ways to install it in the [documentation](https://gofeatureflag.org/docs/relay-proxy/install_relay_proxy)._
- npm i @openfeature/server-sdk @openfeature/go-feature-flag-provider

Requirements and caveats from upstream:
- const {OpenFeature} = require("@openfeature/server-sdk");
- const {GoFeatureFlagProvider} = require("@openfeature/go-feature-flag-provider");
- // With GO Feature Flag you MUST provide a targetingKey that is a unique identifier of the user.

Basic usage or getting-started notes:
- [Getting started](#getting-started)
- [Example](#example)
- The solution has been built to facilitate the usage of feature flags in your code with the easiest setup possible.

- Source: https://github.com/thomaspoignant/go-feature-flag
- Extracted from upstream docs: https://raw.githubusercontent.com/thomaspoignant/go-feature-flag/HEAD/README.md

## Documentation

- https://gofeatureflag.org/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/control-launch-behavior-with-go-feature-flag/)
