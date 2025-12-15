"""
Web hardening quick guidance combining HTTP security check results.
This script simply wraps http_security_check and prints remediation tips.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


TIPS = {
    "strict-transport-security": "Add HSTS (e.g., max-age=31536000; includeSubDomains; preload).",
    "content-security-policy": "Define a CSP to limit sources (default-src 'self'; ...).",
    "x-frame-options": "Set DENY or SAMEORIGIN to prevent clickjacking.",
    "x-content-type-options": "Set nosniff to prevent MIME sniffing.",
    "referrer-policy": "Set strict-origin-when-cross-origin (or stricter) to reduce referrer leakage.",
    "permissions-policy": "Restrict powerful features (camera=(), geolocation=(), etc.).",
}


def main() -> None:
    parser = argparse.ArgumentParser(description="Web hardening helper (uses http_security_check).")
    parser.add_argument("--url", required=True)
    args = parser.parse_args()

    # Call sibling script
    script = Path(__file__).resolve().parents[2] / "offensive" / "web" / "http_security_check.py"
    if not script.exists():
        print("http_security_check.py not found.", file=sys.stderr)
        sys.exit(1)

    proc = subprocess.run(
        [sys.executable, str(script), "--url", args.url],
        capture_output=True,
        text=True,
        check=False,
    )
    if proc.returncode != 0:
        print(proc.stderr)
        sys.exit(proc.returncode)

    try:
        data = json.loads(proc.stdout)
    except Exception:
        print(proc.stdout)
        sys.exit(0)

    findings = data.get("findings", {})
    print(json.dumps(findings, indent=2))
    print("\nRemediation tips:")
    for h, status in findings.items():
        if isinstance(status, str) and status.startswith("missing"):
            tip = TIPS.get(h, "Add secure configuration.")
            print(f"- {h}: {tip}")


if __name__ == "__main__":
    main()
