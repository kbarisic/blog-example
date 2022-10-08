from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import database
from ..repository import auth

router = APIRouter(
    tags=["Auth"],
    prefix="/login"
)


@router.post('/')
def login(db: Session = Depends(database.get_db), request: OAuth2PasswordRequestForm = Depends()):
    return auth.login(db, request)
