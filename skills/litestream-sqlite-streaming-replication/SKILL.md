---
name: "Litestream SQLite Streaming Replication"
description: "Litestream is a streaming replication tool for SQLite databases that continuously replicates changes to S3, Azure, GCS, SFTP, or local storage. Written in Go with 13k+ GitHub stars, it enables SQLite to be used as a production database with disaster recovery."
verification: security_reviewed
source: "https://github.com/benbjohnson/litestream"
category:
  - "Developer Tools"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "benbjohnson/litestream"
  github_stars: 13400
---

# Litestream SQLite Streaming Replication

Litestream is a standalone streaming replication tool for SQLite databases. With over 13,000 GitHub stars and an Apache-2.0 license, it solves the biggest limitation of SQLite in production: the lack of built-in replication and backup. Litestream runs as a background process alongside your application and safely replicates changes incrementally to external storage.
The replication mechanism works by monitoring SQLite WAL (Write-Ahead Logging) frames and streaming them to one or more replica destinations. Supported destinations include Amazon S3, Google Cloud Storage, Azure Blob Storage, SFTP servers, and local file paths. Because it operates through the SQLite API rather than copying raw database files, Litestream never corrupts your database and never requires your application to pause.
Recovery is straightforward. The litestream restore command reconstructs a complete SQLite database from the replica, replaying WAL frames to reach the latest consistent state. Point-in-time recovery is supported: you can restore to any specific timestamp, not just the latest backup. This makes Litestream suitable for production applications where data loss windows must be minimized.
Litestream operates with minimal configuration. A simple YAML config file specifies the database path and replica destinations. The litestream replicate command starts continuous replication, and it can be managed as a systemd service for production deployments. Retention policies control how long historical WAL frames are kept, balancing storage costs against recovery flexibility.
For AI agents managing applications that use SQLite as their primary database, Litestream provides automated disaster recovery without requiring a switch to a client-server database like PostgreSQL. An agent can configure replication to cloud storage, verify replica health with litestream snapshots, test recovery procedures, and monitor replication lag. The tool installs via Homebrew, apt, or standalone binary downloads.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/litestream-sqlite-streaming-replication/)
