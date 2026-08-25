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

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

## ⚠️ Legal Disclaimer

### Educational Purpose Only
This tool is provided strictly for **educational purposes** and **authorized security testing** only. It is intended to help security professionals and students learn about security concepts in controlled environments.

### Authorized Use Only
- You must have **explicit written authorization** before testing any system you do not own
- Unauthorized access to computer systems is **illegal** and punishable under laws including but not limited to the Computer Fraud and Abuse Act (CFAA), Computer Misuse Act, and similar legislation worldwide
- Only use this tool on systems you own, have permission to test, or in isolated lab environments

### No Warranty
This software is provided "AS IS" without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and noninfringement. The author makes no representations or warranties regarding the accuracy, completeness, or reliability of this software.

### Limitation of Liability
**In no event shall the author (Nikhil Nagpure) be liable for any direct, indirect, incidental, special, exemplary, or consequential damages (including, but not limited to, procurement of substitute goods or services; loss of use, data, or profits; or business interruption) however caused and on any theory of liability, whether in contract, strict liability, or tort (including negligence or otherwise) arising in any way out of the use of this software, even if advised of the possibility of such damage.**

### User Responsibility
- The user assumes **full responsibility** for any consequences resulting from the use of this tool
- The author is **not responsible** for any misuse, damage, or illegal activities performed with this software
- Users are solely responsible for ensuring compliance with all applicable local, state, national, and international laws and regulations

### Indemnification
By using this software, you agree to **indemnify, defend, and hold harmless** the author from and against any and all claims, liabilities, damages, losses, costs, and expenses (including reasonable attorneys fees) arising from or related to your use of this software.

### Responsible Disclosure
If you discover vulnerabilities using this tool, please follow responsible disclosure practices and report them to the affected parties through appropriate channels.

---

**By using this software, you acknowledge that you have read, understood, and agree to be bound by this disclaimer.**
## License

This project is for educational purposes only. Use responsibly and ethically.

---

**Remember**: Always implement web hardening recommendations on your websites!
