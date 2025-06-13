from sqlalchemy.orm import Session
from models.submission import Submission
from models.user import User
from schemas.submission import SubmissionCreate
from exceptions.submission_exceptions import SubmissionError
from typing import List


class SubmissionCRUD:

    def create(self, db: Session, user: User, submission_data: SubmissionCreate) -> Submission:
        """Create a submission for the user's team"""
        if not user.team_id:
            raise SubmissionError("User must be part of a team to submit.")

        db_submission = Submission(
            title=submission_data.title,
            description=submission_data.description,
            file_url=submission_data.file_url,
            team_id=user.team_id,
            submitted_by_id=user.id
        )
        db.add(db_submission)
        db.commit()
        db.refresh(db_submission)
        return db_submission

    def get_team_submissions(self, db: Session, user: User) -> List[Submission]:
        """Get all submissions for the user's team"""
        if not user.team_id:
            raise SubmissionError("User is not part of any team.")

        return db.query(Submission).filter(Submission.team_id == user.team_id).all()


submission = SubmissionCRUD()
