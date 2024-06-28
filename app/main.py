from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.config import settings
from app.schedule.router import router as schedule_router
from app.users.router import router as users_router

app = FastAPI(title="FastAPI-telegram_bot")
app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(schedule_router, prefix=settings.api_prefix)
app.include_router(users_router, prefix=settings.api_prefix)