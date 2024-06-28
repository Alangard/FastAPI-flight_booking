from typing import List
from fastapi import APIRouter

from app.users.schemas import GetUserSchema, GetUsersSchema, CreateUserSchema

router = APIRouter()

@router.get("/users", response_model=GetUsersSchema)
async def get_users():
    return 

@router.post("/users", response_model=GetUserSchema)
async def create_user(user_data: CreateUserSchema):
    return 

@router.get("/user/{user_id}", response_model=GetUserSchema)
async def get_user(user_id: int):
    return 