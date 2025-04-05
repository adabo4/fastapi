from typing import Optional, List
from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from . import models, schemas, utils
from .database import engine, get_db

from .routers import user, post, auth



models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)





while True:
    try: 
        conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='adabo', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connectipn was successful.")
        break
    except Exception as error:
        print("Connecting to database failed.")
        print("The Error was: ", error)
        time.sleep(2)  


@app.get("/")
async def root():
    return {"message": " World"}   