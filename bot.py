import requests
import datetime
from config import weather_api, bot_token
from aiogram import Bot,types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=bot_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer("Welcome to the Weather Bot! Send me a city name to get the weather information.")

if __name__ == "__main__":
    executor.start_polling(dp)
