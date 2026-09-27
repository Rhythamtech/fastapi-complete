from fastapi import HTTPException
from src.user.dtos import UserSchema, LoginSchema
from sqlalchemy.orm import Session
from src.user.models import UserModel
from pwdlib import PasswordHash 
import jwt
from src.utils.settings import settings
from datetime import datetime, timedelta

password_hash = PasswordHash.recommended()

def get_hash_password(password):
    return password_hash.hash(password)


def verify_password(hash_password, plain_password):
    return password_hash.verify(plain_password, hash_password)

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


def login(body:LoginSchema, db:Session):
    user =  db.query(UserModel).filter(UserModel.username == body.username).first()
        
    if not user:
        raise HTTPException(401,detail="Unauthorised access.")
    
    if not verify_password(hash_password = user.hash_password, plain_password=body.password):
        raise HTTPException(401,detail="Unauthorised access.")
    
    exp_time  =  datetime.now() + timedelta(minutes= settings.EXP_TIME)
    token =  jwt.encode({"_id":user.id,"username":user.username, "exp":exp_time},settings.SECRET_KEY,settings.ALGORITHM)
    
    
    return {
        "token":token
    }
    