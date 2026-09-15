# Expected vs actual

## Requested operation

One Python standard-library socket attempts:

```python
server.bind(("127.0.0.1", 0))
```

## Desired least-privilege capability

For local test servers, the desired capability is to allow a narrowly scoped loopback listener on an OS-assigned ephemeral port without granting unrelated local/LAN/public network authority.

The corresponding upstream design request is tracked in [`openai/codex#35768`](https://github.com/openai/codex/issues/35768).

## Observed actual result

The controlled 2026-09-09 probe returned:

```text
PermissionError: [Errno 1] Operation not permitted
```

A manually inspected macOS Console entry for the matching process and time window reported:

```text
Sandbox: Python(<pid>) deny(1) network-bind local:*:0
```

## Claim boundary

The evidence supports this narrow statement:

> In the observed Codex Desktop / macOS Seatbelt execution context, the Python process did not receive permission to complete its single `bind(("127.0.0.1", 0))` call.

It does not prove:

- that `127.0.0.1` was interpreted internally as a wildcard address,
- which exact Desktop policy layer produced the denial,
- that `allow_local_binding=true` is an acceptable least-privilege solution,
- that the behavior is universal across Codex versions,
- that any currently proposed upstream change fixes this specific case.
