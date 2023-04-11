#this file contains direct postgress queries not including ORM(sqlalchemy)


from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
from . import models
from .database import engine, get_db
from sqlalchemy.orm import Session


models.Base.metadata.create_all(bind=engine)


app = FastAPI()





class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

while True:
    try:
        conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres',
                                password='admin', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print('Database connection successful')
        break
    except Exception as err:
        print('Connection to database failed')
        print(err)

my_post = [{
        "title": "akhilesh",
        "content": "akhilesh is a good guy",
        "published": False,
        "rating": 4,
        "id": 6327
    }]

def find_post(id):
    for p in my_post:
        if p['id'] == id:
            return p

def find_post_index(id):
    for i,p in enumerate(my_post):
        if p['id'] == id:
            return i

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/sqlalchemy")
def test_post(db: Session = Depends(get_db)):
    post = db.query(models.Post).all()
    return {"data": post}


@app.get("/posts")
def get_posts():
    cursor.execute("""SELECT * FROM posts""")
    posts = cursor.fetchall()
    return {"data": posts}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    cursor.execute("""INSERT into posts (title, content, published) VALUES (%s, %s, %s) RETURNING *""", (post.title, post.content, post.published))
    new_post = cursor.fetchone()
    conn.commit()
    return {"data": new_post}


@app.get("/posts/{id}")
def get_post(id: int):
    cursor.execute("""SELECT * from posts where id = %s""", (str(id),))
    post = cursor.fetchone()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"message: post with id {id} not found")
    return {"post_detail": post}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):

    cursor.execute("""DELETE from posts where id = %s returning *""", (str(id),))
    deleted_post = cursor.fetchone()
    conn.commit()
    if deleted_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"message: 'id: {id} doesn't exists")
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s where id = %s RETURNING *""", (post.title, post.content, post.published, str(id)))
    updated_post = cursor.fetchone()
    conn.commit()
    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"message: 'id: {id} doesn't exists")

    return {"data": updated_post}