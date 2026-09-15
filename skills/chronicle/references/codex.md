# Codex integration status

The CLI and record-keeping discipline work independently of host hooks. Automatic Codex
capture is experimental: configuration schema, events, trust, and payload shapes vary by
host version. A configuration file does not establish active capture.

`chron install-hooks --codex --dry-run` previews the experimental configuration. The local
installer also prepares Claude Code hooks, so review the complete preview. Applying it
merges configuration with backups. It never writes `trusted_hash` entries or grants
approval; the legacy `--trust-codex` option refuses.

Approve reviewed commands using the host's supported interactive mechanism. Make a
harmless edit and inspect its captured event for the correct harness, session, path, and
file contents. Verify gate behavior separately with a harmless test. Until these checks
succeed, record the integration as unverified.

Without verified hooks, CLI entries still work. Shell and Git capture depend on those
specific hooks being installed and invoked; noninteractive shells may not source shell
hooks. Missing file events mean missing intermediate versions. Record gaps explicitly.
