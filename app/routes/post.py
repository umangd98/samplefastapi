from fastapi import APIRouter, Depends, HTTPException, status, File, UploadFile
from sqlalchemy.orm import Session
from app import schemas, crud, auth
from app.database import get_db
from cachetools import TTLCache

router = APIRouter()

# In-memory cache
cache = TTLCache(maxsize=100, ttl=300)

@router.post("/addpost", response_model=schemas.Post)
def add_post(post: schemas.PostCreate, db: Session = Depends(get_db), current_user: schemas.User = Depends(auth.get_current_active_user)):
    if len(post.text.encode('utf-8')) > 1024*1024:
        raise HTTPException(status_code=400, detail="Payload size exceeds 1 MB")
    return crud.create_post(db=db, post=post, user_id=current_user.id)

@router.get("/getposts", response_model=list[schemas.Post])
def get_posts(db: Session = Depends(get_db), current_user: schemas.User = Depends(auth.get_current_active_user)):
    user_id = current_user.id
    if user_id in cache:
        return cache[user_id]
    posts = crud.get_posts(db=db, user_id=user_id)
    cache[user_id] = posts
    return posts

@router.delete("/deletepost/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(post_id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(auth.get_current_active_user)):
    if not crud.delete_post(db=db, post_id=post_id, user_id=current_user.id):
        raise HTTPException(status_code=404, detail="Post not found")
    return {"message": "Post deleted successfully"}
