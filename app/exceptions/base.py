from fastapi import HTTPException
from typing import Any, Optional

class BaseHTTPException(HTTPException):
    """Base exception class for all custom HTTP exceptions"""
    
    def __init__(
        self,
        status_code: int,
        detail: Any = None,
        headers: Optional[dict] = None,
        error_code: Optional[str] = None
    ):
        super().__init__(status_code=status_code, detail=detail, headers=headers)
        self.error_code = error_code
