from pydantic import BaseModel
from datetime import datetime
from typing import List

class UserBase(BaseModel):
    username : str
    email : str
    password : str
    


class UserDisplay(BaseModel):
    id:int
    username : str
    email : str
    
    class Config():
        orm=True
        
# For post display
class User(BaseModel):
    username:str
    email : str
    
    class Config():
        orm=True
      
# For post Display
class Comment(BaseModel):
    text: str
    username: str
    timestamp: datetime
    class Config():
        orm=True
        
class PostBase(BaseModel):
    image_url:str
    image_url_type:str
    caption:str
    creator_id:int
    
class PostDisplay(BaseModel):
    id:int
    image_url:str
    image_url_type:str
    caption:str
    timestamp:datetime
    user:User
    comments:List[Comment]
    
    class Config():
        orm=True
        
class UserAuth(BaseModel):
    id:int
    username:str
    email:str
    
class CommentBase(BaseModel):
    id:int
    username:str
    text:str
    post_id:int
    