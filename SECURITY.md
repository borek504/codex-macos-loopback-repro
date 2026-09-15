# Security and privacy

This repository is a diagnostic reproducer, not a security exploit.

## Reproducer safety

The included Python probe:

- performs one loopback bind attempt,
- does not accept connections,
- does not initiate outbound connections,
- does not transmit data,
- does not invoke subprocesses,
- does not modify files or configuration,
- does not request or escalate permissions.

## Privacy

Please do not attach raw logs that contain:

- access tokens or API keys,
- private filesystem paths,
- usernames or hostnames,
- unrelated environment variables,
- private repository names,
- customer or account information.

Sanitize logs down to the smallest evidence necessary to reproduce or explain the behavior.

## Reporting a security issue

If investigation uncovers an actual security vulnerability rather than a permission-model limitation or product bug, use the vendor's security reporting channel instead of publishing exploit details in this repository.
