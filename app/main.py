from fastapi import FastAPI
from . import models
from .database import engine
from .routers import posts, users, auth, vote
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {
        "message": "Welcome to the FastAPI application!",
        "details": "This is a social media API where you can create posts, manage users, authenticate, and vote on posts.",
        "note": "Enjoy your stay!",
        "docs": "Hit /docs for API documentation."
    }
models.Base.metadata.create_all(bind=engine)