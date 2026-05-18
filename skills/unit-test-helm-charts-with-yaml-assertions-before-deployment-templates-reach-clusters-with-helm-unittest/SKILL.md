---
name: "Unit-test Helm charts with YAML assertions before deployment templates reach clusters with helm-unittest"
slug: "unit-test-helm-charts-with-yaml-assertions-before-deployment-templates-reach-clusters-with-helm-unittest"
description: "Render a Helm chart locally and assert on the generated Kubernetes objects before a broken template makes it to a cluster."
github_stars: 1305
verification: "listed"
source: "https://github.com/helm-unittest/helm-unittest"
author: "helm-unittest"
publisher_type: "organization"
category: "CI/CD Integrations"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "helm-unittest/helm-unittest"
  github_stars: 1305
---

# Unit-test Helm charts with YAML assertions before deployment templates reach clusters with helm-unittest

Render a Helm chart locally and assert on the generated Kubernetes objects before a broken template makes it to a cluster.

## Prerequisites

Helm, the helm-unittest plugin or container image, a Helm chart repository, and chart test files written in YAML.

## Installation

Use the upstream install or setup path that matches your environment:
- docker run -ti --rm -v $(pwd):/apps helmunittest/helm-unittest
- docker run -ti --rm -v $(pwd):/apps helmunittest/helm-unittest:3.11.1-0.3.0
- docker run -ti --rm -v $(pwd):/apps helmunittest/helm-unittest:3.11.1-0.3.0 .
- docker run -ti --rm -v $(pwd):/apps helmunittest/helm-unittest:3.11.1-0.3.0 -o test-output.xml -t junit .

Requirements and caveats from upstream:
- [Docker Usage](#docker-usage)
- <sup>*</sup> for Helm 4, installation using webhooks GPG verification is not supported, so --verify=false is required when installing from git repository. </br>
- ## Docker Usage

Basic usage or getting-started notes:
- [Usage](#usage)
- [Example](#example)
- When not defining any versions, it will install the latest version of binary into helm plugin directory, otherwise it will install the specified version.

- Source: https://github.com/helm-unittest/helm-unittest
- Extracted from upstream docs: https://raw.githubusercontent.com/helm-unittest/helm-unittest/HEAD/README.md

## Documentation

- https://github.com/helm-unittest/helm-unittest

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/unit-test-helm-charts-with-yaml-assertions-before-deployment-templates-reach-clusters-with-helm-unittest/)
