# Security policy

Agent Orchestra describes how autonomous agents may read repositories and produce patches. Treat
all agent output as untrusted input and execute it only inside boundaries you control.

Please report a vulnerability privately through GitHub's security-advisory feature. Do not include
secrets, private repository contents, or exploit details in a public issue.

The maintainers currently support the latest commit on the default branch. This repository does
not provide a sandbox, credential broker, or permission system; those controls belong to the host
runtime.
