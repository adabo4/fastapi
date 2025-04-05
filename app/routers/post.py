from typing import List

from app.routers import oauth2
from .. import models, schemas
from fastapi import APIRouter, Response, status, HTTPException, Depends
from sqlalchemy.orm import Session
from ..database import get_db


router = APIRouter(prefix="/posts", tags=['Posts'])

# GET ALL POSTS
@router.get("/", response_model=List[schemas.Post])
def get_posts(db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)): 
    posts = db.query(models.Post).all()
    return posts


#CREATE POST
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)):

    print(user_id)
    new_post= models.Post(**post.model_dump()) # models.Post je tabulka a do nej vkkladam data post: from schemas.Post
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post

# GET ONE POST
@router.get("/{id}")
def get_post(id: int, db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)): 

    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found.")   
    
    return post

#DELETE POST
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT) 
def delete_post(id:int,db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)):
  
    post = db.query(models.Post).filter(models.Post.id==id)


    if post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Index not found.")

    post.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

#UPDATE POST
@router.put("/{id}", response_model=schemas.Post)
def update_post(id:int, updated_post: schemas.PostCreate, db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)):

   post_query = db.query(models.Post).filter(models.Post.id == id)

   post = post_query.first()

   post_query.update(updated_post.model_dump(),synchronize_session=False)

   db.commit()
 
   if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Index not found.")

   return post_query.first()
    

