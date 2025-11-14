# Security Notes for LibraryProject

## Key settings
- DEBUG is controlled by `DJANGO_DEBUG` env var. Set to False in production.
- `SECURE_BROWSER_XSS_FILTER = True`, `X_FRAME_OPTIONS = 'DENY'`, `SECURE_CONTENT_TYPE_NOSNIFF = True`
- `CSRF_COOKIE_SECURE` and `SESSION_COOKIE_SECURE` set True for HTTPS.

## CSRF protection
- All templates rendering forms must include `{% csrf_token %}`.
- Forms are implemented using Django forms (`bookshelf/forms.py`) which validates input.

## Preventing SQL injection
- Use Django ORM (`.filter(title__icontains=q)`), not string-interpolated raw SQL.
- Use parameterized `.raw()` with params or avoid `.raw()` entirely.

## CSP
- Implemented via `django-csp` (recommended) or `LibraryProject/middleware.py` (simple fallback).
- CSP limits sources for scripts/styles/images to reduce XSS risk.

## Testing
- Manual tests for CSRF, XSS, CSP headers and permissions are described in the developer checklist.

