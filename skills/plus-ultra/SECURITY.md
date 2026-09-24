# Security policy

Plus Ultra is a workflow gate, not a sandbox. Its command classifier recognizes common mutation
shapes but cannot safely interpret arbitrary shell syntax, aliases, interpreters, or programs.
Use operating-system permissions, isolated worktrees or containers, and credential boundaries for
real enforcement.

Report vulnerabilities privately through GitHub's security-advisory feature. Do not publish a
working bypass before a fix is available, and never include secrets or private repository content.

The latest commit on the default branch is supported.
