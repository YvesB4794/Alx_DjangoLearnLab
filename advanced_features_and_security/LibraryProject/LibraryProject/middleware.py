# LibraryProject/middleware.py
class SimpleCSPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        # Example policy - restrict to same origin
        response.setdefault('Content-Security-Policy', "default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data:;")
        return response
    
    
    # LibraryProject/middleware_security.py
class SecurityHeadersMiddleware:
    """
    Add or enforce security headers on every response.
    Keep this minimal — main security enforcement happens in web server.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response.setdefault('X-Frame-Options', 'DENY')
        response.setdefault('X-Content-Type-Options', 'nosniff')
        response.setdefault('X-XSS-Protection', '1; mode=block')
        return response

