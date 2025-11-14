# HTTPS & Secure Redirects — LibraryProject

## What we changed in settings.py
- `SECURE_SSL_REDIRECT`: redirects HTTP to HTTPS (enable in production).
- `SECURE_HSTS_SECONDS`: HTTP Strict Transport Security value (set to 0 during rollout; set to 31536000 after verification).
- `SECURE_HSTS_INCLUDE_SUBDOMAINS`, `SECURE_HSTS_PRELOAD`: included.
- `SESSION_COOKIE_SECURE` and `CSRF_COOKIE_SECURE`: True.
- `SECURE_BROWSER_XSS_FILTER`, `SECURE_CONTENT_TYPE_NOSNIFF`, `X_FRAME_OPTIONS` set for browser security.
- Optionally `SECURE_PROXY_SSL_HEADER` if running behind a TLS-terminating proxy.

## Web server
- Recommended: terminate SSL at Nginx/Load balancer.
- Nginx should add HSTS, Content Security Policy, and other headers (example in repo).

## Local testing tips
- Use `mkcert` or self-signed certs for local HTTPS testing.
- Keep `DEBUG=True` locally; ensure `DEBUG=False` in production.

## Rollout
1. Deploy with HTTPS available but start with low `SECURE_HSTS_SECONDS` (e.g., 3600).
2. After verifying everything works, set `SECURE_HSTS_SECONDS=31536000` and add domain to preload if desired.

## Caveats
- `SECURE_SSL_REDIRECT` can interfere with local development if you don't have HTTPS.
- Always ensure `ALLOWED_HOSTS` is set correctly in production.
