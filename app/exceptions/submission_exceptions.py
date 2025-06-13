from .base import BaseHTTPException

class SubmissionNotFoundError(BaseHTTPException):
    def __init__(self, detail: str = "Submission not found"):
        super().__init__(404, detail, error_code="SUBMISSION_001")

class FileUploadError(BaseHTTPException):
    def __init__(self, detail: str = "File upload failed"):
        super().__init__(400, detail, error_code="SUBMISSION_002")

class InvalidFileTypeError(BaseHTTPException):
    def __init__(self, detail: str = "Invalid file type"):
        super().__init__(400, detail, error_code="SUBMISSION_003")

class FileSizeExceededError(BaseHTTPException):
    def __init__(self, detail: str = "File size exceeds limit"):
        super().__init__(413, detail, error_code="SUBMISSION_004")

class TeamAlreadySubmittedError(BaseHTTPException):
    def __init__(self, detail: str = "Team has already submitted"):
        super().__init__(409, detail, error_code="SUBMISSION_005")
class SubmissionError(Exception):
    def __init__(self, detail: str = "An error occurred during submission."):
        self.message = detail
        super().__init__(self.message)