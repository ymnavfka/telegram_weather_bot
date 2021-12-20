import requests

from aiogram.types.message import Message

class Weather_data(object):

    data = {}

    def __init__(self, city, open_weather_token):
        self.set_data(city, open_weather_token)
    
    def get_data(self):
        return self.data

    async def set_data(self, city, open_weather_token):
        try:
            self.data = requests.get(
                f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
            ).json()
        except:
            await Message.reply("\U00002620 Проверьте название города data \U00002620")