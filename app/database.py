from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

import psycopg2
from psycopg2.extras import RealDictCursor
import time

load_dotenv()

database_url = os.getenv('SQLALCHEMY_DATABASE_URL')

engine = create_engine(database_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base=declarative_base()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

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