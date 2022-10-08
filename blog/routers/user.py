from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from blog import schemas, oauth2
from blog.database import get_db
from ..repository import user

router = APIRouter(
    prefix="/user",
    tags=["Users"],
    dependencies=[Depends(oauth2.get_current_user)]
)


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[schemas.ShowUser])
def all_users(db: Session = Depends(get_db)):
    return user.get_all(db)


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.ShowUser)
def show(user_id: int, db: Session = Depends(get_db)):
    return user.show(user_id, db)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def create(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(user_id: int, db: Session = Depends(get_db)):
    return user.delete(user_id, db)


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(user_id: int, request: schemas.User, db: Session = Depends(get_db)):
    return user.update(user_id, request, db)
