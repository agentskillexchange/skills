# Security contract

## Invariants

- Keep the Bitwarden master password only in the secure-dialog result and the
  anonymous one-use pipe to `bw unlock --passwordfile /dev/stdin`.
- Keep `BW_SESSION` only in the broker process environment for child `bw`
  operations. Never serialize or return it.
- Use an owner-only directory (`0700`) and Unix socket (`0600`).
- Keep the service per-user; never install a privileged system daemon.
- Use a monotonic clock for the 86,400-second lease.
- Serialize unlock interactions so concurrent clients cannot open duplicate
  dialogs or invalidate one another's sessions.
- Allow only `get`, `list`, `sync`, and `status`; reject caller credential
  options.
- Keep logs free of request payloads, stdout, passwords, sessions, and vault
  data.

## Threat boundary

The broker protects against accidental disclosure through chat, terminals,
command arguments, shell history, project files, logs, and cross-task session
loss. It does not defend against another process already executing as the same
macOS user; that process shares the user's authority and can connect to the
owner-only socket.

## Persistence boundary

Only code, LaunchAgent configuration, empty/diagnostic logs, and a socket path
persist. Passwords, Bitwarden sessions, and retrieved secrets do not. Process
restart therefore means lease loss and a required new prompt.

## Change gate

Any change that persists a password/session/secret, broadens socket access,
adds arbitrary shell execution, returns `BW_SESSION`, imports shell profiles,
or removes the three-attempt/native-dialog behavior is a security-model change,
not a refactor. Stop and obtain explicit user approval before implementing it.
