from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from db.db_connection import get_db
from db.user_db import UserInDB

from models.user_models import UserIn, UserOut

router = APIRouter()


@router.post("/user/auth/")
async def auth_user(user_in: UserIn, db: Session = Depends(get_db)):
    user_in_db = db.query(UserInDB).get(user_in.username)

    if user_in_db is None:
        raise HTTPException(status_code=404, detail="El usuario no existe")

    if user_in_db.password != user_in.password:
        raise HTTPException(status_code=403, detail="Error de autenticacion")

    return {"Autenticado": True}


@router.get("/user/balance/{username}", response_model=UserOut)
async def get_balance(username: str, db: Session = Depends(get_db)):
    user_in_db = db.query(UserInDB).get(username)

    if user_in_db is None:
        raise HTTPException(status_code=404, detail="El usuario no existe")

    return user_in_db
