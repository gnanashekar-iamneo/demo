from .base import BaseHTTPException

class TeamNotFoundError(BaseHTTPException):
    def __init__(self, detail: str = "Team not found"):
        super().__init__(404, detail, error_code="TEAM_001")

class TeamAlreadyExistsError(BaseHTTPException):
    def __init__(self, detail: str = "Team name already exists"):
        super().__init__(409, detail, error_code="TEAM_002")

class TeamFullError(BaseHTTPException):
    def __init__(self, detail: str = "Team is full (maximum 4 members)"):
        super().__init__(409, detail, error_code="TEAM_003")

class NotTeamLeaderError(BaseHTTPException):
    def __init__(self, detail: str = "Only team leader can perform this action"):
        super().__init__(403, detail, error_code="TEAM_004")

class UserNotInTeamError(BaseHTTPException):
    def __init__(self, detail: str = "User is not in any team"):
        super().__init__(404, detail, error_code="TEAM_005")

class TeamAlreadyHasThemeError(BaseHTTPException):
    def __init__(self, detail: str = "Team already has a theme selected"):
        super().__init__(409, detail, error_code="TEAM_006")

class CannotLeaveAsLeaderError(BaseHTTPException):
    def __init__(self, detail: str = "Team leader cannot leave team. Transfer leadership or delete team."):
        super().__init__(409, detail, error_code="TEAM_007")

class UserAlreadyTeamLeaderError(BaseHTTPException):
    def __init__(self, detail: str = "User is already a team leader"):
        super().__init__(409, detail, error_code="TEAM_008")
