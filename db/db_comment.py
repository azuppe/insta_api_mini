from fastapi import HTTPException, status
from routers.schemas import CommentBase
from sqlalchemy.orm.session import Session
from db.models import Comment
import datetime

def create(db:Session,  request:CommentBase, username:str):

    new_comment = Comment(
        text= request.text,
        username=username,
        timestamp = datetime.datetime.now(),
        post_id= request.post_id
    )
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment

def get_all(db:Session, id:int):
    return db.query(Comment).filter(Comment.post_id == id).all()
    