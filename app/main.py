from fastapi import FastAPI
from app.routes import auth, post
from app.database import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(post.router, prefix="/post", tags=["post"])
