import jwt
from jwt.exceptions import InvalidTokenError
from src.utils.settings import settings
from fastapi import HTTPException, Request, Depends
from src.utils.db import get_db
from sqlalchemy.orm import Session
from src.user.models import UserModel

def is_authenticated(request:Request, db: Session =  Depends(get_db)):
    try:
        token  = request.headers.get("authorization")
        if not token:
            raise HTTPException(401, "Unauthorized error.")
            
        token =  token.split(" ")[-1]
        
        decoded_token = jwt.decode(token,settings.SECRET_KEY,settings.ALGORITHM )
        id = decoded_token.get('_id') 
        
        user =  db.query(UserModel).filter(UserModel.id == id).first()
        
        if not user:
                raise HTTPException(401,detail="Unauthorised access.")
        
        return user
    except InvalidTokenError:
        raise HTTPException(401,detail="Unauthorised access.")