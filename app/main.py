from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.v1 import api_router
from utils.logger import logger
from config import settings

app = FastAPI(
    title="Hackathon API",
    description="API for managing users, teams, themes, and submissions",
    version="1.0.0"
)

# Allow all origins for dev; restrict in production
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Replace with frontend domain in production
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# Register API routes
app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "Welcome to Hackathon API"}

# Startup and shutdown logs
@app.on_event("startup")
def on_startup():
    logger.info(" FastAPI application is starting...")

@app.on_event("shutdown")
def on_shutdown():
    logger.info(" FastAPI application is shutting down...")
