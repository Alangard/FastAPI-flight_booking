from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from contextlib import asynccontextmanager

from aiogram import types, Dispatcher, Bot
from app.bot.bot import dp, bot

from app.config import settings
from app.database import BaseModel, engine
from app.populate_db import generate_fake_data
from app.api.router import router as api_router
from app.users.router import router as users_router

import logging
import uvicorn


WEBHOOK_PATH = f"/bot/{settings.TG_BOT_TOKEN}"
WEBHOOK_URL = f"{settings.TUNNEL_URL}{WEBHOOK_PATH}"


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Async context manager for startup and shutdown lifecycle events.
    - Creates database tables.
    - Sets up bot commands and webhook.

    Yields control during application's lifespan and performs cleanup on exit.
    - Disposes all database connections.
    - Deletes bot webhook and commands.
    - Closes aiohttp session
    """ 

    async with engine.begin() as connection:
        await connection.run_sync(BaseModel.metadata.create_all)

    # # Инициализация фабрики моковых данных
    # generate_fake_data()


    await bot.set_webhook(
        url=WEBHOOK_URL,
        allowed_updates=dp.resolve_used_update_types(),
        drop_pending_updates=True)
    yield
    await bot.delete_webhook()
    await bot.session.close()


application = FastAPI(title="FastAPI-booking", lifespan=lifespan)
application.mount("/static", StaticFiles(directory="app/static"), name="static")

application.include_router(api_router, prefix=settings.api_prefix)
application.include_router(users_router, prefix=settings.api_prefix)


@application.post(WEBHOOK_PATH)
async def bot_webhook(update: dict):
    telegram_update = types.Update(**update)

    """
    Bot webhook endpoint. Receives updates and feeds them to the bot dispatcher.
    :param update: The update received from the bot webhook.
    """

    await dp.feed_webhook_update(bot=bot, update=telegram_update)


    # await dp.process_update(telegram_update)

@application.get("/")
async def root(request: Request):
    return 

    
