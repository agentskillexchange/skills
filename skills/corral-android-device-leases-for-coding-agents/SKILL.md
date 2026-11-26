---
name: "Corral — Exclusive Android Device Leases for Coding Agents"
slug: "corral-android-device-leases-for-coding-agents"
description: "Lease one Android device (USB, WiFi or emulator) exclusively to one agent session through the corral CLI or its MCP endpoint. Corral is a local Kotlin/Ktor daemon that queues competing sessions in FIFO order, gates raw adb and Gradle install/test commands at exec time, and refuses a second agent's call instead of letting two runs collide on the same phone."
category: "Developer Tools"
framework: "Claude Code"
verification: listed
source: "https://github.com/ciszkin/corral"
---

# Corral — Exclusive Android Device Leases for Coding Agents

Corral pools the Android devices attached to a host — USB, WiFi and emulators — and leases each
one to exactly one agent session at a time. The failure it prevents is concrete: one session runs
`./gradlew connectedAndroidTest` while another installs an APK to the same serial, and the run
fails in a way that reads as a flaky test. `ANDROID_SERIAL` only binds callers that cooperate,
and agents do not. Corral decides at exec time instead.

Use it before any device work: `adb shell`, `adb install`, a screenshot, `am instrument`, a
`./gradlew connectedAndroidTest` or `install*` task. Claim or lease first; do not start with
`adb devices` and grab a serial.

## The core loop

The form to prefer queues and holds: the command waits in the FIFO queue, then runs with the
served device leased until it exits.

```sh
corral lease --timeout 120 -- ./gradlew connectedAndroidTest
corral lease --timeout 180 --type emulator -- adb install app.apk
```

`--timeout` caps the queue wait (max 600 s, clamped with a warning). Omit it and a busy pool
prints a self-teaching line naming the holders and this exact form, then exits 1. Everything
after `--` is the command; nothing before it is run as a program. The CLI renews the lease while
the command runs, so the TTL bounds only a CLI that stopped renewing. Selectors compose:
`--serial`, `--model`, `--os` (minimum), `--type usb|wifi|emulator`, `--avd`.

For work spanning several commands, claim, use, free:

```sh
serial=$(corral claim)              # serial alone on stdout
ANDROID_SERIAL=$serial adb shell ...
corral free "$serial"
```

A claim's TTL is the hold (30 minutes from the CLI) and survives the process that made it; renew
a long session with `corral renew <serial>`, and run `corral free --all` in a trap so an
abandoned claim does not block the pool. `corral wait` is the poll-then-decide form: it prints a
serial and hands the lease back when the wait process exits, so use it only when you must know
which device you would get before deciding.

Read-only commands need no lease: `corral devices`, `corral status`, `corral queue`,
`corral owner`, `corral check`, `corral doctor`.

## The gate

Three independent layers enforce the lease on POSIX: an `adb` wrapper earlier on `PATH`, an SDK
`platform-tools/adb` shim for absolute-path calls, and a Gradle `init.d` gate, because AGP never
runs the adb binary and only a build-level gate can stop its `install*` and
`connected*AndroidTest` tasks. A Windows install has two layers — the `.bat` wrapper and the
Gradle gate — with no SDK `adb.exe` shim.

A refusal is the gate working, and it prints the way through (`corral lease -- <cmd>` or
`corral claim` plus `ANDROID_SERIAL`). The read-only allowlist is the `readonly=` line of
`~/.config/corral/rules`; a missing rules file fails closed and refuses every call. The gate
checks `-s <serial>` and `ANDROID_SERIAL` whatever that file says. Identity is self-declared —
this is a rail against accidental collision, not authentication.

## Emulators and demo devices

`corral avd list|start|stop <avd>` manages AVDs. A freshly started AVD joins the pool unbooted
and is not claimable until Android reports boot complete, so pair `corral avd start` with a
`corral lease --timeout … --type emulator -- …` ticket that is served at the boot flip.

`corral demo` starts a second, isolated daemon whose pool is simulated; `GET /api/config`
returns `"demo":true` and every demo model ends in `(demo)`. Those leases exercise the plumbing,
not hardware — never run a real build, test or install against a demo serial.

## Limits worth knowing

The threat model is cooperating agents. ddmlib clients that talk to the adb server on `:5037`
directly (Android Studio's Run/deploy, Logcat, Device Explorer) and any adb reached outside the
SDK path by absolute name (`adb.real`) are documented bypasses. macOS has no installer; Windows
is host-verified on one box. The daemon binds `127.0.0.1` only.

## Installation

### From the release bundle (Linux, JDK 17+; Windows uses the same installer)

```sh
curl -fsSLO https://github.com/ciszkin/corral/releases/download/v0.1.8/corral-0.1.8.zip &&
curl -fsSLO https://github.com/ciszkin/corral/releases/download/v0.1.8/corral-0.1.8.zip.sha256 &&
sha256sum -c corral-0.1.8.zip.sha256 &&
unzip corral-0.1.8.zip -d corral-0.1.8 &&
(cd corral-0.1.8 && ./install.sh --ui)
```

The installer is user-scoped and idempotent: it puts the `corral` CLI, an `adb` wrapper and the
console on `~/bin`, shims the SDK adb, drops the Gradle gate and the agent skill, and starts the
daemon at login. Requires JDK 17+ and an Android SDK with `platform-tools/adb` on `PATH`. Read
the installer before running it: https://github.com/ciszkin/corral/blob/v0.1.8/scripts/install.sh

### From source

```sh
git clone https://github.com/ciszkin/corral
cd corral
./gradlew :corral-daemon:shadowJar :corral-ui:shadowJar
scripts/install.sh --ui
```

### Install this skill directory

Clone the Agent Skill Exchange repository and copy the skill into the directory your agent reads:

```sh
git clone https://github.com/agentskillexchange/skills.git
mkdir -p ~/.claude/skills
cp -R skills/skills/corral-android-device-leases-for-coding-agents ~/.claude/skills/corral-android-device-leases-for-coding-agents
```

### Wire the MCP endpoint

```sh
claude mcp add --transport http corral http://127.0.0.1:8798/mcp
```

Eight tools: `list_devices`, `queue`, `claim`, `free`, `renew`, `screenshot`, `start_emulator`,
`stop_emulator`, one identity per MCP session, loopback only.

## Source

- Upstream: https://github.com/ciszkin/corral
- Skill source of truth: https://github.com/ciszkin/corral/blob/main/skills/corral/SKILL.md
- Full adoption guide: https://github.com/ciszkin/corral/blob/main/CUTOVER.md
- Threat model: https://github.com/ciszkin/corral/blob/main/SECURITY.md
