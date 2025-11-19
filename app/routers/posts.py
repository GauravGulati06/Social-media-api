from .. import models, schemas, utils
from fastapi import Body, Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from typing import Optional
from ..database import get_db, engine
from ..oauth2 import get_current_user

router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)

@router.get("", response_model=list[schemas.PostResponse])
def get_posts(db: Session = Depends(get_db), user: int = Depends(get_current_user), limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    # cursor.execute("SELECT * FROM posts")
    # posts = cursor.fetchall()
    #------------------------------------------------------------
    posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    return posts

@router.post("", response_model=schemas.PostResponse)
def create_item(post: schemas.PostCreate = Body(...), db: Session = Depends(get_db),user: int = Depends(get_current_user)):
    # cursor.execute(
    #     "INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *",
    #     (post.title, post.content, post.published)
    # )
    # new_post = cursor.fetchone()
    # conn.commit()
    #------------------------------------------------------------
    new_post = models.Post(owner_id = user.id,**post.model_dump())
    
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@router.get("/{id}", response_model=schemas.PostResponse)
def get_post(id: int, db: Session = Depends(get_db), user: int = Depends(get_current_user)):
    # cursor.execute("SELECT * FROM posts WHERE id = %s", (str(id)))
    # post = cursor.fetchone()
    # if not post:
    #     raise HTTPException(status_code=404, detail=f"Post with id {id} not found")
    #------------------------------------------------------------
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=404, detail=f"Post with id {id} not found")
    return post



@router.delete("/{id}", status_code=204)
def delete_post(id: int, db: Session = Depends(get_db), user: int = Depends(get_current_user)):
    # cursor.execute("DELETE FROM posts WHERE id = %s RETURNING *", (str(id),))
    # deleted_post = cursor.fetchone()
    # conn.commit()
    #------------------------------------------------------------
    post = db.query(models.Post).filter(models.Post.id == id)
    deleted_post = post.first()
    if deleted_post.owner_id != user.id:
        raise HTTPException(status_code=403, detail="Not authorized to perform requested action")
    if deleted_post:
        post.delete(synchronize_session=False)
        db.commit()
    if deleted_post is None:
        raise HTTPException(status_code=404, detail=f"Post with id {id} not found")
    return {"message": "Post deleted successfully"}

@router.put("/{id}",response_model=schemas.PostResponse)
def update_post(id: int, post: schemas.PostCreate = Body(...), db: Session = Depends(get_db), user: int = Depends(get_current_user)):
    # cursor.execute(
    #     "UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *",
    #     (post.title, post.content, post.published, str(id))
    # )
    # updated_post = cursor.fetchone()
    # conn.commit()
    #------------------------------------------------------------
    post_query = db.query(models.Post).filter(models.Post.id == str(id))
    updated_post = post_query.first()
    if updated_post.owner_id != user.id:
        raise HTTPException(status_code=403, detail="Not authorized to perform requested action") 
    if updated_post:
        post_query.update(post.model_dump(), synchronize_session=False)
        db.commit()
    if updated_post is None:
        raise HTTPException(status_code=404, detail=f"Post with id {id} not found")
    return post_query.first()