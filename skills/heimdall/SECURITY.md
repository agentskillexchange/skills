# Security

Please report vulnerabilities privately through GitHub's security advisory flow rather
than opening a public issue.

Heimdall can execute browser actions and HTTP requests against real systems. Review test
plans before running them, keep credentials in environment variables or untracked
Playwright storage-state files, and use the container driver for untrusted targets.

The `destructive`, `paid`, and `prod` risk labels are coordination controls, not a
sandbox. Only grant a risk class when you understand the target and recovery path.
