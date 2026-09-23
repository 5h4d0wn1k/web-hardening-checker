> **⚠️ EDUCATIONAL USE ONLY — AUTHORIZED TESTING ONLY.**
> This project exists for education, research, and **defense of systems you own
> or hold explicit written authorization to assess**. Unauthorized use is
> prohibited and may be illegal. Read [ETHICS.md](ETHICS.md) and
> [SCOPE.md](SCOPE.md) before use. Use at your own risk; **AS IS**, no warranty.

# Web Hardening Checker

Web security hardening checker with remediation guidance: runs an HTTP security-header scan and prints actionable fixes for the six most common missing headers.

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/5h4d0wn1k/web-hardening-checker.svg)](https://github.com/5h4d0wn1k/web-hardening-checker)
[![Last commit](https://img.shields.io/github/last-commit/5h4d0wn1k/web-hardening-checker.svg)](https://github.com/5h4d0wn1k/web-hardening-checker)
[![Issues](https://img.shields.io/github/issues/5h4d0wn1k/web-hardening-checker.svg)](https://github.com/5h4d0wn1k/web-hardening-checker)

## Why

Most web breaches start as missing or misconfigured HTTP security headers. This tool checks a target URL against the baseline security-header set — HSTS, Content-Security-Policy, X-Frame-Options, X-Content-Type-Options, Referrer-Policy and Permissions-Policy — and pairs every gap with concrete remediation (Apache and Nginx config snippets). It turns a one-line command into a prioritized hardening checklist for sites you own or are authorized to test.

## Features

- **Security-header scan** — checks 6 common headers on a target URL
- **Remediation guidance** — concrete fix for every missing/invalid header (HSTS `max-age`/`includeSubDomains`/`preload`, CSP `default-src 'self'`, `X-Frame-Options DENY`, `nosniff`, and more)
- **Web-server examples** — Apache and Nginx snippets for each recommendation
- **Zero-setup CLI** — `python3 web_hardening_check.py --help` works out of the box

## Quickstart

```bash
# CLI reference
python3 web_hardening_check.py --help

# Check a URL you own or are authorized to test
python3 web_hardening_check.py --url https://example.com
```

> **Note:** the scanner wraps a sibling `http_security_check.py` scanner (expects it at an `offensive/web/` location in a larger toolkit layout). If the sibling scanner is not present, the tool reports it and exits 1 instead of scanning. Run from a checkout where that dependency exists, or supply it yourself.

## Project structure

- `web_hardening_check.py` — hardening wrapper + remediation tips
- `CHANGELOG.md` — versioned changes; `VERSION` — current release (1.1.0)
- `requirements.txt` — optional `requests` for enhanced scanning

## Documentation

- [CHANGELOG.md](CHANGELOG.md) — version history
- [ETHICS.md](ETHICS.md) — educational purpose and authorized use only
- [SCOPE.md](SCOPE.md) — authorized-testing scope checklist
- [SECURITY.md](SECURITY.md) — vulnerability reporting
- [CONTRIBUTING.md](CONTRIBUTING.md) — safe contribution guidelines

## Contributing

New header checks, remediation entries and automated tests are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md); scan only sites you own or hold authorization for.

## License

MIT — see [LICENSE](LICENSE). Provided **AS IS**, without warranty, for education and authorized security testing only.