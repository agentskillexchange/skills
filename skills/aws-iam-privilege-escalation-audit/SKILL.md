---
name: "AWS IAM Privilege Escalation Audit"
slug: "aws-iam-privilege-escalation-audit"
description: "Uses boto3 and the AWS IAM Access Analyzer API to enumerate all roles, policies, and users, then flags permission combinations that could allow privilege escalation to AdministratorAccess. Outputs findings mapped to MITRE ATT&CK TA0004 with remediation steps and least-privilege replacement policy JSON."
github_stars: 3607
verification: "listed"
source: "https://github.com/aws/aws-sdk-js-v3"
category: "Security & Verification"
framework: "Claude Code"
tool_ecosystem:
  github_repo: "aws/aws-sdk-js-v3"
  github_stars: 3607
---

# AWS IAM Privilege Escalation Audit

Uses boto3 and the AWS IAM Access Analyzer API to enumerate all roles, policies, and users, then flags permission combinations that could allow privilege escalation to AdministratorAccess. Outputs findings mapped to MITRE ATT&CK TA0004 with remediation steps and least-privilege replacement policy JSON.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-iam-privilege-escalation-audit/)
