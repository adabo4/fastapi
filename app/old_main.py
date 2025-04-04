# from typing import Optional
# from fastapi import FastAPI, Response, status, HTTPException, Depends
# from fastapi.params import Body
# from pydantic import BaseModel
# from random import randrange
# import psycopg2
# from psycopg2.extras import RealDictCursor
# import time
# from sqlalchemy.orm import Session
# from . import models
# from .database import engine, get_db

# models.Base.metadata.create_all(bind=engine)

# app = FastAPI()



# while True:
#     try: 
#         conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='adabo', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connectin was successful.")
#         break
#     except Exception as error:
#         print("Connecting to database failed.")
#         print("The Error was: ", error)
#         time.sleep(2)



# # cursor.execute("SELECT * FROM posts;")

# # records = cursor.fetchall()


# class Post(BaseModel):
#     title: str
#     content: str
#     published: bool = True


# my_posts = [{
#         "id": 1,
#         "title" : "title of post 1",
#         "content": "Content of post 1"
#     }, 
#     {
#         "id": 2,
#         "title": "favourite foods",
#         "content": "i like pizza"
#     }]

# def find_post(id):
#     for post in my_posts:
#           if post['id'] == id :
#               return post
          

# def find_index_post(id):
#     for i,p in enumerate(my_posts):
#         if p['id'] == id:
#             return i
        

         


# @app.get("/")
# async def root():
#     return {"message": " World"}   

# @app.get("/sqlalchemy")
# def test_posts(db: Session = Depends(get_db)):

#     posts = db.query(models.Post).all()
#     return {"data": posts}




# @app.get("/posts")
# def get_posts():
#     cursor.execute("SELECT * FROM posts;")
#     posts = cursor.fetchall()
#     return {"data": posts}

# @app.post("/posts", status_code=status.HTTP_201_CREATED)
# def create_posts(post: Post):
#     # post_dict = post.model_dump()
#     # post_dict["id"]= randrange(0, 100000)
#     # my_posts.append(post_dict)

#     cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """, 
#                    (post. title, post.content, post.published))
#     new_post= cursor.fetchone()
#     conn.commit()
#     return {"data": new_post}


# @app.get("/posts/{id}")
# def get_post(id: int): 
    
#     cursor.execute("SELECT * FROM posts WHERE id = %s;", [id])
#     post = cursor.fetchone()

#     # post = find_post(id)
#     if not post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found.")   
    
#     return {"post_detail": post}


# @app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT) 
# def delete_post(id:int):
  
#     # index = find_index_post(id)

#     cursor.execute("DELETE FROM posts WHERE id = %s returning *;",(id,))
    
#     post = cursor.fetchone()
#     conn.commit()

#     if not post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Index not found.")
#     # my_posts.pop(index)

#     return Response(status_code=status.HTTP_204_NO_CONTENT)

# @app.put("/posts/{id}")
# def update_post(id:int, post: Post):

# #    index = find_index_post(id)
#    cursor.execute("UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *", (post.title, post.content, post.published, (id,)))
#    post = cursor.fetchone()
  

#    if post == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Index not found.")
   
# #    post_dict=post.model_dump()
# #    post_dict['id'] = id
# #    my_posts[index] = post_dict
#    return {"data": post}
    