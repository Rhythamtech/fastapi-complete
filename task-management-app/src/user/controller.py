from fastapi import HTTPException
from src.user.dtos import UserSchema
from sqlalchemy.orm import Session
from src.user.models import UserModel
from pwdlib import PasswordHash 


password_hash = PasswordHash.recommended()

def get_hash_password(password):
    return password_hash.hash(password)

def register(body : UserSchema, db:Session):
    
    is_username =  db.query(UserModel).filter(UserModel.username == body.username).first()
    
    if is_username :
        raise HTTPException(400,detail="Username already existing")
    
    is_email = db.query(UserModel).filter(UserModel.email == body.username).first()
    
    if is_email:
        raise HTTPException(400,detail="Email already existing")
        
    hash_password = get_hash_password(body.password )
    new_user =  UserModel(
        name = body.name,
        username = body.username,
        hash_password =  hash_password,
        email = body.email
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user