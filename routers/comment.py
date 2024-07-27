from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .schemas import  CommentBase, UserAuth
from dependencies import get_db
from db import db_comment
from auth.oauth2 import get_current_user

router = APIRouter(
    prefix='/comment',
    tags=['comment']
)

@router.post('/')
def create_comment(request:CommentBase, db:Session = Depends(get_db), current_user:UserAuth = Depends(get_current_user)):
    return db_comment.create(db, request, current_user.username) 

@router.get('/all/{post_id}')
def get_all_comments( post_id:int, db:Session = Depends(get_db), current_user:UserAuth = Depends(get_current_user)):
    return db_comment.get_all(db, post_id)
    