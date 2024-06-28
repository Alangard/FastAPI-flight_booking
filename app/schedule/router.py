from datetime import datetime
from typing import List
from fastapi import APIRouter

from app.schedule.schemas import GetScheduleSchema, SetBusyDatesSchema

router = APIRouter()

@router.get("/schedule/", response_model=List[GetScheduleSchema])
async def get_schedule(
    datetime_gte: datetime | None = None, 
    datetime_lte: datetime | None = None, 
    datetime_gt: datetime | None = None, 
    datetime_lt: datetime | None = None, 
    skip: int = 0, 
    limit: int = 10):
    return

@router.post("/schedule/set_busy_dates")
async def set_busy_dates(data: SetBusyDatesSchema):
    return


