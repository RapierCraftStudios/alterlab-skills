#!/usr/bin/env python3
"""AlterLab monitor helper (stdlib only). Reads the API key from $ALTERLAB_API_KEY."""

import argparse
import json
import os
import sys
import urllib.request


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("url", help="URL to monitor")
    parser.add_argument("--name", default='Monitored page', help="Monitor name")
    parser.add_argument("--interval", default='0 */6 * * *', help="Cron expression")
    args = parser.parse_args()
    api_key = os.environ.get("ALTERLAB_API_KEY")
    if not api_key:
        print("Set ALTERLAB_API_KEY (create a key at https://alterlab.io/dashboard)", file=sys.stderr)
        return 2
    request = urllib.request.Request(
        "https://api.alterlab.io/v1/monitors",
        data=json.dumps({"name": args.name, "url": args.url, "check_interval": args.interval}).encode(),
        headers={"X-API-Key": api_key, "Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=120) as response:
        print(json.dumps(json.loads(response.read()), indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
