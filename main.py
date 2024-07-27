from fastapi import FastAPI
from db import models 
from db import database
from fastapi.middleware.cors import  CORSMiddleware
from fastapi.staticfiles import StaticFiles
from routers import user, post, comment
from auth import authentication

app = FastAPI()
app.include_router(user.router)
app.include_router(post.router)
app.include_router(comment.router)
app.include_router(authentication.router)

@app.get('/')
def root():
    return {
        "message":"hello world"
    }
    
models.Base.metadata.create_all(bind=database.engine)

origins=['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods =['*'],
    allow_headers=['*'],
)

app.mount('/images',StaticFiles(directory='images'), name='images')
 