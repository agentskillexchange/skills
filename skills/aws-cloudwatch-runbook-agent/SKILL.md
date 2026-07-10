---
name: "AWS CloudWatch Runbook Agent"
slug: "aws-cloudwatch-runbook-agent"
description: "Uses AWS SDK CloudWatchClient GetMetricData and CloudWatch Logs Insights StartQueryExecution to automate incident triage. Correlates alarms via DescribeAlarms with X-Ray trace segments for root cause analysis."
github_stars: 3607
verification: "security_reviewed"
source: "https://github.com/aws/aws-sdk-js-v3"
category: "Runbooks & Diagnostics"
framework: "ChatGPT Agents"
tool_ecosystem:
  github_repo: "aws/aws-sdk-js-v3"
  github_stars: 3607
---

# AWS CloudWatch Runbook Agent

Uses AWS SDK CloudWatchClient GetMetricData and CloudWatch Logs Insights StartQueryExecution to automate incident triage. Correlates alarms via DescribeAlarms with X-Ray trace segments for root cause analysis.

## Installation

Use the upstream install or setup path that matches your environment:
- Let’s walk through setting up a project that depends on DynamoDB from the SDK and makes a simple service call. The following steps use yarn as an example. These steps assume you have Node.js and yarn already installed.
- git clone https://github.com/aws/aws-sdk-js-v3.git
- yarn && yarn test:all
- yarn pack .

Requirements and caveats from upstream:
- To test your universal JavaScript code in Node.js, browser and react-native environments,
- [Node.js and ECMAScript Version Support Policy](#nodejs-and-ecmascript-version-support-policy)
- Create a new Node.js project.

Basic usage or getting-started notes:
- [Getting Started](#getting-started)
- Inside of the project, run: yarn add @aws-sdk/client-dynamodb. Adding packages results in update in lock file, [yarn.lock](https://yarnpkg.com/getting-started/qa/#should-lockfiles-be-committed-to-the-repository) or [p...
- Create a new file called index.js, create a DynamoDB service client and send a request.

- Source: https://github.com/aws/aws-sdk-js-v3
- Extracted from upstream docs: https://raw.githubusercontent.com/aws/aws-sdk-js-v3/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-cloudwatch-runbook-agent/)
