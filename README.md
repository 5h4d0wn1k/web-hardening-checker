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

## Security Headers Checked

1. **Strict-Transport-Security (HSTS)**: Enforces HTTPS connections
2. **Content-Security-Policy (CSP)**: Prevents XSS attacks
3. **X-Frame-Options**: Prevents clickjacking
4. **X-Content-Type-Options**: Prevents MIME sniffing
5. **Referrer-Policy**: Controls referrer information
6. **Permissions-Policy**: Controls browser features

## Output Format

```json
{
  "strict-transport-security": "missing",
  "content-security-policy": "present",
  "x-frame-options": "missing",
  "x-content-type-options": "missing/invalid",
  "referrer-policy": "missing",
  "permissions-policy": "missing"
}

Remediation tips:
- strict-transport-security: Add HSTS (e.g., max-age=31536000; includeSubDomains; preload).
- x-frame-options: Set DENY or SAMEORIGIN to prevent clickjacking.
- x-content-type-options: Set nosniff to prevent MIME sniffing.
- referrer-policy: Set strict-origin-when-cross-origin (or stricter) to reduce referrer leakage.
- permissions-policy: Restrict powerful features (camera=(), geolocation=(), etc.).
```

## Remediation Examples

### 1. HSTS (Strict-Transport-Security)

**Apache**:
```apache
Header always set Strict-Transport-Security "max-age=31536000; includeSubDomains; preload"
```

**Nginx**:
```nginx
add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload" always;
```

### 2. Content-Security-Policy

**Apache**:
```apache
Header always set Content-Security-Policy "default-src 'self'; script-src 'self' 'unsafe-inline'"
```

**Nginx**:
```nginx
add_header Content-Security-Policy "default-src 'self'; script-src 'self' 'unsafe-inline'" always;
```

### 3. X-Frame-Options

**Apache**:
```apache
Header always set X-Frame-Options "DENY"
```

**Nginx**:
```nginx
add_header X-Frame-Options "DENY" always;
```

## Use Cases

- **Security Audits**: Check security headers on your websites
- **Hardening**: Implement web security best practices
- **Compliance**: Meet security compliance requirements
- **Educational Purposes**: Learn about web security

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

**Remember**: Always implement web hardening recommendations on your websites!
