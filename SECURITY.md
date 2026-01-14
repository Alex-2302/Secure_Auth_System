# Security Considerations

## Authentication
- Passwords are never stored in plaintext
- Hashing uses salted PBKDF2 via Werkzeug

## Authorization
- Admin routes are protected with server-side role checks
- Unauthorized access returns HTTP 403

## Brute Force Protection
- Accounts lock after 5 failed login attempts
- Lock duration is time-based

## Known Limitations
- Admin actions currently use GET (CSRF risk – documented)
- No MFA implemented
- No rate-limiting at network level

## Ethical Use
This project is for defensive security learning only.
