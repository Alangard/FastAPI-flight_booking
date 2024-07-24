import enum
import uuid
from datetime import datetime
from typing import Any, List

from sqlalchemy import Boolean, Column, DateTime, Enum, ForeignKey, Index, Integer, String, Table, text
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import BaseModel



class User(BaseModel):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    guid: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), unique=True, default=uuid.uuid4)
    password: Mapped[str] = mapped_column(String(25))
    first_name: Mapped[str] = mapped_column(String(150), default="")
    last_name: Mapped[str] = mapped_column(String(150), default="", index=True)
    phone_number: Mapped[str] = mapped_column(String, unique=True)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False)
    telegram_id: Mapped[int] = mapped_column(Integer, index=True, nullable=True)
    telegram_username: Mapped[str] = mapped_column(String(32), unique=True, nullable=True)
    user_image: Mapped[str] = mapped_column(String(1048), nullable=True)

    def get_full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.get_full_name()

