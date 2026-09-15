# Environment

## Observed case — 2026-09-09

Publicly shareable environment facts from the original controlled probe:

- Product: ChatGPT Desktop
- Desktop version: `26.825.51511`
- Desktop build: `7377`
- Bundled Codex CLI: `0.151.0-alpha.7.2`
- OS family: macOS
- Sandbox: Seatbelt
- Interpreter: Apple Command Line Tools Python 3
- Requested socket: IPv4 TCP
- Requested address: `127.0.0.1`
- Requested port: `0` (OS-assigned ephemeral port)
- Number of bind attempts: `1`

Effective process values reported:

```text
CODEX_PERMISSION_PROFILE=cig03_loopback
CODEX_SANDBOX=seatbelt
CODEX_NETWORK_PROXY_ACTIVE=1
CODEX_NETWORK_ALLOW_LOCAL_BINDING=0
```

The execution context had network enabled and used a managed proxy. The only explicitly allowed domain in the investigated profile was the literal `127.0.0.1`.

## Intentionally excluded

This public package does not include:

- local usernames,
- hostnames,
- home-directory paths,
- private repository names,
- support ticket identifiers,
- tokens or credentials,
- unrelated system logs,
- private project source or configuration.

Those details are unnecessary for the claim being tested.
