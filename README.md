# Secure Authentication System (Security-Focused)

This project demonstrates a security-first implementation of a web authentication system,
designed and analyzed from a cyber-security perspective.

## Security Objectives
- Prevent brute-force attacks
- Secure password storage
- Enforce role-based access control
- Protect against CSRF
- Detect and respond to authentication abuse

## Threats Addressed
- Broken Authentication
- Privilege Escalation
- Account Takeover
- Session Hijacking
- CSRF Attacks

## Implemented Security Controls
- Password hashing (PBKDF2)
- Account lockout after failed attempts
- Session-based authentication
- Role-based authorization (admin / user)
- CSRF protection for forms

## Technologies
- Python (Flask)
- SQLite (local, isolated)
- Flask-WTF (CSRF)
- Werkzeug (password hashing)

## Disclaimer
This application is intentionally simple and runs on localhost.
It is designed for security learning and analysis, not production deployment.
