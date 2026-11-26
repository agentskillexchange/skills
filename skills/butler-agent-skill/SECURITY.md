# Security

This is a local, single-user runtime, not a multi-user service. Never expose its HTTP port to a network, use a reverse proxy without authentication, or run as root. A local process running as you already has access to your state. HTTP Host checks resist DNS rebinding; same-origin JSON mutation checks resist browser CSRF. There is no remote authentication layer.

Keep state and source inputs private. Do not attach real ledgers, transcripts, account caches, machine inventories, tokens, or local paths to public issues. Use synthetic reproductions. Report sensitive vulnerabilities through the repository's private security reporting feature if enabled; otherwise open an issue asking for a private channel without exploit details or private data.

The release is not a security certification. Back up your own state. Files and configuration controlled by the local user are trusted; provider reports may be stale and external adapters require separate review and authorization.
