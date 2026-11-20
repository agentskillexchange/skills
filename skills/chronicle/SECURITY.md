# Security

Report vulnerabilities privately using GitHub's security advisory flow.

Chronicle can capture file contents, commands, prompts, and output. Keep data directories
and synchronized spines private. Path exclusions and text redaction cannot guarantee
detection of every secret. Review configuration before enabling capture.

Spine blob encryption does not encrypt event metadata. A public remote is unsuitable for
the ledger even with encrypted blobs. The optional canvas has no authentication; keep it
on loopback. Narration transmits trace content to your provider and may incur costs.

Hook installation never grants Codex trust. Approve reviewed commands in the host. The
gate relies on host support and is not a security sandbox.
