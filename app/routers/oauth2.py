from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from app import schemas
from dotenv import load_dotenv
import os


load_dotenv()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


secret_key= os.getenv('SECRET_KEY')

def create_access_token(data: dict):
   to_encode= data.copy()

   expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
   to_encode.update({"exp": expire})

   encoded_jwt = jwt.encode(to_encode, secret_key, algorithm=ALGORITHM)

   return encoded_jwt

def verify_access_token(token: str, credentials_exception):

    try:
        payload = jwt.decode(token, secret_key, algorithms=[ALGORITHM])

        id: str = payload.get("user_id")


        if id is None: 
            raise credentials_exception
        token_data= schemas.TokenData(id=str(id))
    except JWTError: 
        raise credentials_exception
    

    return token_data
    
def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                          detail=f"Could not validate credentials", 
                                          headers={"WWW-Authenticate": "Bearer"})

    return verify_access_token(token, credentials_exception)


