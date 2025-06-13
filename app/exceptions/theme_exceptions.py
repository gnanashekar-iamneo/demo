from .base import BaseHTTPException

class ThemeNotFoundError(BaseHTTPException):
    def __init__(self, detail: str = "Theme not found"):
        super().__init__(404, detail, error_code="THEME_001")

class ThemeAlreadyExistsError(BaseHTTPException):
    def __init__(self, detail: str = "Theme already exists"):
        super().__init__(409, detail, error_code="THEME_002")

class ThemeInactiveError(BaseHTTPException):
    def __init__(self, detail: str = "Theme is not active"):
        super().__init__(403, detail, error_code="THEME_003")
