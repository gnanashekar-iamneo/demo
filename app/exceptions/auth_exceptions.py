from .base import BaseHTTPException

class AuthenticationError(BaseHTTPException):
    def __init__(self, detail: str = "Authentication failed"):
        super().__init__(401, detail, error_code="AUTH_001")

class InvalidCredentialsError(BaseHTTPException):
    def __init__(self, detail: str = "Invalid email or password"):
        super().__init__(401, detail, error_code="AUTH_002")

class TokenExpiredError(BaseHTTPException):
    def __init__(self, detail: str = "Token has expired"):
        super().__init__(401, detail, error_code="AUTH_003")

class InvalidTokenError(BaseHTTPException):
    def __init__(self, detail: str = "Invalid token"):
        super().__init__(401, detail, error_code="AUTH_004")

class InsufficientPermissionsError(BaseHTTPException):
    def __init__(self, detail: str = "Insufficient permissions"):
        super().__init__(403, detail, error_code="AUTH_005")
