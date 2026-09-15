# codex-macos-loopback-repro

Minimal, sanitized reproducer for a macOS Codex sandbox behavior where a Python process attempts exactly one loopback bind to `127.0.0.1` on an OS-assigned ephemeral port and receives:

```text
PermissionError: [Errno 1] Operation not permitted
```

The observed macOS kernel message for the same process was:

```text
Sandbox: Python(<pid>) deny(1) network-bind local:*:0
```

## Scope

This repository is intentionally narrow. It demonstrates an observed bind denial under a specific Codex Desktop / macOS Seatbelt execution context.

It does **not** prove:

- which internal Desktop policy layer caused the denial,
- that every Codex version behaves the same way,
- that the behavior is a security bug,
- that a narrow loopback-listener permission already exists,
- that enabling broader network or local-binding permissions is safe.

Related upstream discussion:

- [openai/codex#35768](https://github.com/openai/codex/issues/35768) — project-scoped loopback listener allowlists without broadly enabling `allow_local_binding`.

## Safety properties of the reproducer

`repro_loopback_bind.py`:

- imports only the Python standard library,
- creates one `AF_INET/SOCK_STREAM` socket,
- attempts exactly one `bind(("127.0.0.1", 0))`,
- never calls `listen()`,
- never calls `connect()`,
- never sends or receives data,
- never changes Codex configuration or permissions,
- closes the socket in `finally`.

## Quick start

Read [REPRODUCE.md](REPRODUCE.md) before running.

Outside the relevant Codex sandbox, the bind will usually succeed. That is expected and does not invalidate the reproducer; the target observation is the behavior inside the relevant Codex Desktop / macOS Seatbelt context.

## Repository contents

- `repro_loopback_bind.py` — minimal probe
- `REPRODUCE.md` — controlled reproduction procedure
- `ENVIRONMENT.md` — known observed environment
- `EXPECTED_VS_ACTUAL.md` — precise claim boundary
- `evidence/observed-2026-09-09.txt` — sanitized evidence excerpt
- `SECURITY.md` — safety and disclosure notes

## Status

Reproducer package prepared from an observation collected on 2026-09-09.
No claim is made here that the upstream limitation has been fixed or that a specific implementation path has been accepted.
