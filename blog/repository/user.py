from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from .. import models, schemas
from blog.hash import Hash


def get_all(db: Session):
    users = db.query(models.User).all()
    return users


def show(user_id: int, db: Session):
    user = get_user_db(user_id, db).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {user_id} is not found!")

    return user


def create(request: schemas.User, db: Session):
    new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def delete(user_id: int, db: Session):
    user = get_user_db(user_id, db)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {user_id} is not found!")
    user.delete(synchronize_session=False)
    db.commit()
    return {"Detail": f"User with id {user_id} is deleted!"}


def update(user_id: int, request: schemas.User, db: Session):
    user = get_user_db(user_id, db)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {user_id} is not found!")
    user.update(request.dict())
    db.commit()
    return {"Detail": f"User with id {user_id} was updated!"}


def get_user_db(user_id: int, db: Session):
    return db.query(models.User).filter(models.User.id == user_id)
