from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, reply_keyboard_markup, keyboard_button, web_app_info

from app.config import settings
from random import shuffle


bot = Bot(token=settings.TG_BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    button = keyboard_button.KeyboardButton(text='Open website', web_app=web_app_info.WebAppInfo(url='https://habr.com/ru/articles/819955/'))
    markup = reply_keyboard_markup.ReplyKeyboardMarkup(keyboard=[[button]])
    await message.answer(f"Hello ", reply_markup=markup)
    # await message.answer(f"{message.from_user}")