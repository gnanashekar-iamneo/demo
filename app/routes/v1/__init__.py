from fastapi import APIRouter
from .auth import router as auth_router
from .user import router as user_router
from .team import router as team_router
from .theme import router as theme_router
from .submission import router as submission_router

api_router = APIRouter()

api_router.include_router(auth_router, prefix="/auth", tags=["authentication"])
api_router.include_router(user_router, prefix="/users", tags=["users"])
api_router.include_router(team_router, prefix="/teams", tags=["teams"])
api_router.include_router(theme_router, prefix="/themes", tags=["themes"])
api_router.include_router(submission_router, prefix="/submissions", tags=["submissions"])
