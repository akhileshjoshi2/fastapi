from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post, user,auth, vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware

#we are using alembic to maintain db so we don't need this
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# origins = ["https://www.google.com"]
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
async def root():
    return {"message": "Hello World "}



