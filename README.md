# Web Hardening Checker

⚠️ **EDUCATIONAL PURPOSE ONLY** - This tool is designed for authorized security testing and educational purposes. Only use on websites you own or have explicit written authorization to test.

## Overview

A comprehensive web security hardening checker that analyzes HTTP security headers and provides remediation recommendations. Combines security header analysis with actionable hardening guidance.

## Features

- **Security Header Analysis**: Checks for common security headers
- **Remediation Guidance**: Provides specific recommendations for missing headers
- **HTTP Security Check**: Integrates with HTTP security checker
- **Actionable Recommendations**: Clear steps to improve security

## Installation

### Requirements

- Python 3.8+
- Standard library only (no external dependencies!)

### Setup

```bash
# Clone the repository
git clone https://github.com/5h4d0wn1k/web-hardening-checker.git
cd web-hardening-checker

# No installation needed!
python web_hardening_check.py --help
```

## Usage

### Basic Usage

```bash
# Check web hardening
python web_hardening_check.py --url https://example.com
```

## Command-Line Options

| Option | Description |
|--------|-------------|
| `--url` | Target URL to check (required) |

## Output Format

```json
{
  "strict-transport-security": "missing",
  "content-security-policy": "missing",
  "x-frame-options": "present"
}

Remediation tips:
- strict-transport-security: Add HSTS (e.g., max-age=31536000; includeSubDomains; preload).
- content-security-policy: Define a CSP to limit sources (default-src 'self'; ...).
```

## Use Cases

- **Security Audits**: Check web security configuration
- **Hardening**: Implement web security best practices
- **Penetration Testing**: Authorized security assessments
- **Educational Purposes**: Learn about web security hardening

## Legal Disclaimer

⚠️ **IMPORTANT**: This tool is for authorized security testing and educational purposes only.

- Only check websites you own or have explicit written authorization to test
- Follow responsible disclosure practices
- Comply with all applicable laws and regulations

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is for educational purposes only. Use responsibly and ethically.

---

**Remember**: Always get explicit authorization before checking any website!
