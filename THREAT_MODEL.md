# Threat Model

## Assets
- User credentials
- Session tokens
- Admin privileges

## Threat Actors
- External attackers
- Malicious authenticated users

## Attack Vectors
- Password brute force
- Privilege escalation
- CSRF on admin actions
- Session reuse

## Mitigations
- Account lockout
- Role-based access control
- CSRF tokens
