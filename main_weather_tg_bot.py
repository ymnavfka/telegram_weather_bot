import get_weather_class
import data_class
import states
from config import tg_bot_token, open_weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Привет! Напиши мне название города и я пришлю сводку погоды!")

@dp.message_handler()
async def get_weather(message: types.Message):
    city = message.text
    data = data_class.Data(city, open_weather_token).get_data()
    weather = get_weather_class.Get_weather(data, states.States.from_telegram).get_weather()
    await message.reply(weather)

if __name__ == "__main__":
    executor.start_polling(dp)