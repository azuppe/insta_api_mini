from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File
from sqlalchemy.orm import Session

from .schemas import PostDisplay, PostBase, UserAuth
from dependencies import get_db
from db import db_post
from typing import List
import random
import string
import shutil
from auth.oauth2 import get_current_user


router = APIRouter(
    prefix='/post',
    tags=['post']
)

image_url_types =['absolute', 'relative']

@router.post('/', response_model=PostDisplay)
def create(request:PostBase, db:Session=Depends(get_db), current_user:UserAuth = Depends(get_current_user)):
    if not request.image_url_type in image_url_types:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail='Provided image url type is not supported')
    return db_post.create_posts(db, request, current_user.id)

@router.get('/all', response_model = List[PostDisplay])
def get(db:Session=Depends(get_db)):
    return db_post.get_all(db)

@router.delete('/{id}', response_model=PostDisplay)
def delete_post(id:int ,  db:Session = Depends(get_db) , current_user:UserAuth = Depends(get_current_user)):
    return db_post.delete(db, id, current_user.id)
    

@router.post('/image')
def upload_image(img:UploadFile = File(...), current_user:UserAuth = Depends(get_current_user)):
    letters = string.ascii_letters
    rand_str = ''.join(random.choice(letters) for i in range (6))
    new = f'_{rand_str}.'
    file_name = new.join(img.filename.rsplit('.', 1))
    path = f'images/{file_name}'
    
    with open(path, 'w+b') as buffer:
        shutil.copyfileobj(img.file, buffer)
    return {'filename': path}
    