# Security Assessment Report

## Test Cases
- Brute-force login simulation
- Unauthorized admin access attempt
- Session persistence after logout

## Findings
- Account lockout works as intended
- Admin access blocked for non-admin users
- Password hashes are secure

## Recommendations
- Convert admin actions to POST + CSRF
- Add audit logging
- Add MFA for admin users
