from datetime import datetime
from typing import Optional

from pydantic import UUID4, BaseModel, EmailStr, RootModel, field_validator
from app.config import settings


class GetUserSchema(BaseModel):
    guid: UUID4
    first_name: str
    second_name: str | None
    last_name: str
    is_superuser: bool = False
    phone_number: str
    telegram_id: int
    created_at: datetime
    update_at: datetime
    # role: 
    # user_image: str | None

    @field_validator("user_image")
    @classmethod
    def add_image_host(cls, image_url: str | None) -> str:
        if image_url:
            if "/static/" in image_url:
                return settings.STATIC_HOST + image_url
        return image_url


class CreateUserSchema(BaseModel):
    pass


class GetUsersSchema(RootModel[GetUserSchema]):
    root: list[GetUserSchema]