from typing import Annotated, Union
from fastapi import APIRouter
from fastapi.params import Body, Path, Query
from pydantic import BaseModel, EmailStr

from ..models.item import Item
from ..models.user import User

router = APIRouter()

class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str | None = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None
    
@router.post("/", response_model=UserOut)
async def create_user(user: UserIn) -> any:
    return user