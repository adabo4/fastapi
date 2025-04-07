from typing import List, Optional

from app.routers import oauth2
from .. import models, schemas
from fastapi import APIRouter, Response, status, HTTPException, Depends
from sqlalchemy.orm import Session
from ..database import get_db


router = APIRouter(prefix="/posts", tags=['Posts'])

# GET ALL POSTS
@router.get("/", response_model=List[schemas.Post])
def get_posts(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user), limit: int = 10, skip: int = 0, search: Optional[str] = ""): 

    posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    
    return posts

#CREATE POST
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    new_post= models.Post(owner_id=current_user.id, **post.model_dump()) # models.Post je tabulka a do nej vkkladam data post: from schemas.Post
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post

# GET ONE POST
@router.get("/{id}")
def get_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)): 

    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found.")   
    
    return post

#DELETE POST
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT) 
def delete_post(id:int,db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
  
    post_query = db.query(models.Post).filter(models.Post.id==id)

    post = post_query.first()


    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Index not found.")

    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Not allowed to perform requested action.")
   
    post_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

#UPDATE POST
@router.put("/{id}", response_model=schemas.Post)
def update_post(id:int, updated_post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

   post_query = db.query(models.Post).filter(models.Post.id == id)

   post = post_query.first()

   if current_user.id != post.owner_id:
       raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Not allowed to perform requested action.")

   post_query.update(updated_post.model_dump(),synchronize_session=False)

   db.commit()
 
   if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Index not found.")

   return post_query.first()
    

