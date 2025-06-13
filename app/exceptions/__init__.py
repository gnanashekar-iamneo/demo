from .base import BaseHTTPException
from .auth_exceptions import *
from .user_exceptions import *
from .team_exceptions import *
from .theme_exceptions import *
from .submission_exceptions import *

__all__ = [
    "BaseHTTPException",
    # Auth exceptions
    "AuthenticationError", "InvalidCredentialsError", "TokenExpiredError", "InvalidTokenError",
    # User exceptions
    "UserNotFoundError", "UserAlreadyExistsError", "UserInactiveError", "UserAlreadyInTeamError",
    # Team exceptions
    "TeamNotFoundError", "TeamAlreadyExistsError", "TeamFullError", "NotTeamLeaderError", 
    "UserNotInTeamError", "TeamAlreadyHasThemeError", "CannotLeaveAsLeaderError",
    # Theme exceptions
    "ThemeNotFoundError", "ThemeAlreadyExistsError", "ThemeInactiveError",
    # Submission exceptions
    "SubmissionNotFoundError", "FileUploadError", "InvalidFileTypeError", "FileSizeExceededError"
]
