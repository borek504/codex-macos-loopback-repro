#!/usr/bin/env python3
"""Minimal loopback bind probe for Codex macOS sandbox investigation.

Safety contract:
- one IPv4 TCP socket
- one bind attempt to 127.0.0.1:0
- no listen(), connect(), send(), recv(), subprocess, filesystem mutation,
  configuration mutation, or permission escalation
"""

from __future__ import annotations

import datetime as dt
import os
import platform
import socket
import sys


ENV_KEYS = (
    "CODEX_PERMISSION_PROFILE",
    "CODEX_SANDBOX",
    "CODEX_NETWORK_PROXY_ACTIVE",
    "CODEX_NETWORK_ALLOW_LOCAL_BINDING",
)


def utc_now() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec="microseconds")


def main() -> int:
    print(f"python={sys.version.split()[0]}")
    print(f"platform={platform.system()} {platform.release()}")
    for key in ENV_KEYS:
        print(f"{key}={os.environ.get(key, '<unset>')}")

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        started = utc_now()
        print(f"bind_started_utc={started}")
        try:
            server.bind(("127.0.0.1", 0))
        except OSError as exc:
            ended = utc_now()
            print("bind_result=ERROR")
            print(f"exception_type={type(exc).__name__}")
            print(f"errno={getattr(exc, 'errno', None)}")
            print(f"message={exc}")
            print(f"bind_ended_utc={ended}")
            return 1
        else:
            ended = utc_now()
            address, port = server.getsockname()
            print("bind_result=SUCCESS")
            print(f"bound_address={address}")
            print(f"bound_port={port}")
            print(f"bind_ended_utc={ended}")
            return 0
    finally:
        server.close()
        print(f"socket_closed={server.fileno() == -1}")


if __name__ == "__main__":
    raise SystemExit(main())
