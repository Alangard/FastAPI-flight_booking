from datetime import datetime

from pydantic import UUID4, BaseModel, EmailStr, RootModel, field_validator

from app.config import settings


class GetScheduleSchema(BaseModel):
   pass

class SetBusyDatesSchema(BaseModel):
   pass