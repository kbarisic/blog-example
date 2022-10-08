from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from .. import models, schemas


def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def show(blog_id: int, db: Session):
    blog = get_blog_db(blog_id, db).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {blog_id} is not found!")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"Detail": f"Blog with id {blog_id} is not found!"}
    return blog


def create(request: schemas.Blog, db: Session):
    new_blog = models.Blog(title=request.title, body=request.body, published=request.published, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def delete(blog_id: int, db: Session):
    blog = get_blog_db(blog_id, db)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {blog_id} is not found!")

    blog.delete(synchronize_session=False)
    db.commit()
    return {"detail": f"Blog with id {blog_id} is deleted!"}


def update(blog_id: int, request: schemas.Blog, db: Session):
    blog = get_blog_db(blog_id, db)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {blog_id} is not found!")

    blog.update(request.dict())
    db.commit()
    return {"Detail": f"Blog with id {blog_id} was updated!"}


def get_blog_db(blog_id: int, db: Session):
    return db.query(models.Blog).filter(models.Blog.id == blog_id)
