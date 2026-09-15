# Reproduce

## Goal

Test one narrowly scoped operation:

```python
socket.bind(("127.0.0.1", 0))
```

The probe intentionally stops there. It does not listen, connect, exchange traffic, or alter permissions.

## Preconditions

Use a macOS Codex Desktop / CLI execution context whose effective process environment reflects the policy being investigated.

The 2026-09-09 observation reported:

```text
CODEX_PERMISSION_PROFILE=cig03_loopback
CODEX_SANDBOX=seatbelt
CODEX_NETWORK_PROXY_ACTIVE=1
CODEX_NETWORK_ALLOW_LOCAL_BINDING=0
```

The named profile itself is not required by this repository; what matters is that the effective execution context is equivalent in the properties being tested.

Do **not** broaden permissions merely to make this reproducer pass.

## Procedure

1. Inspect `repro_loopback_bind.py`.
2. Syntax-check it without executing the socket probe:

   ```bash
   python3 -m py_compile repro_loopback_bind.py
   ```

3. Run it once inside the target Codex execution context:

   ```bash
   python3 repro_loopback_bind.py
   ```

4. Record the complete stdout/stderr from that single run.
5. If the result is `PermissionError` / errno 1, optionally inspect macOS Console manually for a matching `network-bind` denial using the process PID and timestamp window from the run.
6. Do not infer a specific internal policy source solely from the kernel denial.

## Interpreting outcomes

### `bind_result=ERROR`, errno 1

This matches the observed behavior documented in this repository.

It demonstrates that this process was not permitted to complete the requested loopback bind in that execution context.

It does not, by itself, identify the exact policy layer responsible.

### `bind_result=SUCCESS`

Record:

- Codex Desktop / CLI version,
- bundled codex-cli version,
- macOS version,
- the four effective environment values printed by the script.

A success in a newer or differently configured environment may indicate a configuration or implementation difference. It is not proof that the upstream feature request is fully resolved for every least-privilege case.

## What not to do

Do not:

- enable broad/full network access just to obtain a success,
- disable the sandbox,
- add arbitrary raw Seatbelt rules,
- expose private project paths, tokens, hostnames, or unrelated logs,
- run project code alongside this probe.

The purpose is a minimal platform-level observation.
