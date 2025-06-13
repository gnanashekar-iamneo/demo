from .base import BaseHTTPException

class UserNotFoundError(BaseHTTPException):
    def __init__(self, detail: str = "User not found"):
        super().__init__(404, detail, error_code="USER_001")

class UserAlreadyExistsError(BaseHTTPException):
    def __init__(self, detail: str = "User already exists"):
        super().__init__(409, detail, error_code="USER_002")

class UserInactiveError(BaseHTTPException):
    def __init__(self, detail: str = "User account is inactive"):
        super().__init__(403, detail, error_code="USER_003")

class UserAlreadyInTeamError(BaseHTTPException):
    def __init__(self, detail: str = "User is already in a team"):
        super().__init__(409, detail, error_code="USER_004")

class UserNotTeamMemberError(BaseHTTPException):
    def __init__(self, detail: str = "User is not a member of this team"):
        super().__init__(403, detail, error_code="USER_005")
