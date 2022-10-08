from typing import List

from fastapi import APIRouter, status, Depends, Response
from sqlalchemy.orm import Session

from blog import schemas, oauth2
from blog.database import get_db
from ..repository import blog

router = APIRouter(
    prefix="/blog",
    tags=["Blogs"],
    dependencies=[Depends(oauth2.get_current_user)]
)


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[schemas.ShowBlog])
def all_blogs(db: Session = Depends(get_db)):
    return blog.get_all(db)


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def show(blog_id, response: Response, db: Session = Depends(get_db)):
    return blog.show(blog_id, db)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.create(request, db)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(blog_id, db: Session = Depends(get_db)):
    return blog.delete(blog_id, db)


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(blog_id, request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.update(blog_id, request, db)

