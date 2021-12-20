import requests
import weather_info_transformation
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

    try:
        data = requests.get(
                                f"http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric"
                            ).json()
        weather = weather_info_transformation.Weather_info_transformation(data).get_weather()
        await message.reply(weather)

    except:
        await message.reply("\U00002620 Проверьте название города \U00002620\n")


if __name__ == '__main__':
    executor.start_polling(dp)
     