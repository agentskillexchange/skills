# Security

## Supported versions

Security fixes are applied to the latest release on the default branch.

## Reporting a vulnerability

Please use GitHub's private vulnerability reporting for this repository. Do not include real transcripts, credentials, or personal data in an issue.

## Data boundary

Cross-Agent Sync reads local agent transcripts. Import packets can therefore contain sensitive user text and absolute filesystem paths. They are written under `.agent-sync/imports/`, which is ignored by Git, and the CLI rejects import destinations outside that directory.

The tool performs no network requests. Operators remain responsible for reviewing curated summaries before committing or sharing them.
