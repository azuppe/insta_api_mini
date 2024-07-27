from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm.session import Session
from fastapi.security import OAuth2PasswordRequestForm
from dependencies import get_db
from db.models import User
from db.hashing import Hash
from .oauth2 import create_access_token

router = APIRouter(
    tags=['authentication']
)

@router.post('/login')
def login(request:OAuth2PasswordRequestForm = Depends(), db:Session= Depends(get_db)):
    user = db.query(User).filter(User.username == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f'Invalid Credentials')
    if not Hash.verify( user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f'Invalid Credentials')
    
    access_token = create_access_token(data={
        "username":user.username
    })
    
    return {
        "access_token":access_token,
        "token_type":'bearer',
        "user_id":user.id,
        "username":user.username
    }
    