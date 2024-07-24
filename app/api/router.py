from datetime import datetime
from typing import List
from fastapi import APIRouter, Depends
from app.api.schemas import SearchParams, TicketResponse
from app.api.services import search_tickets
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_async_session


router = APIRouter()

@router.get("/flights/", response_model=List[TicketResponse])
async def get_tickets(params: SearchParams = Depends(), session: AsyncSession = Depends(get_async_session)):
    tickets = await search_tickets(session, params)
    return tickets


# @router.get("/tickets/")
# async def get_tickets(params: SearchParams = Depends(), session: AsyncSession = Depends(get_async_session)):
#     tickets = await search_tickets(session, params)
#     return tickets



