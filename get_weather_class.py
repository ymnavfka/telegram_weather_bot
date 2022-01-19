import datetime

from aiogram.types.message import Message
import states

class Get_weather(object):

    def __init__(self, data, state):
        self.set_weather(data, state)

    code_to_smile = {
            "Clear": "Ясно \U00002600",
            "Clouds": "Облачно \U00002601",
            "Rain": "Дождь \U00002614",
            "Drizzle": "Дождь \U00002614",
            "Thunderstorm": "Гроза \U000026A1",
            "Snow": "Снег \U0001F328",
            "Mist": "Туман \U0001F32B"
        }

    async def set_weather(self, data, state):
        if (state.name == states.States.from_console.name):
            self.set_weather_from_console(data)
        else: 
            if (state.name == states.States.from_telegram.name):
                self.set_weather_from_telegram(data)

    def transform_data(self, data):
        city = data["name"]
        cur_weather = data["main"]["temp"]

        weather_description = data["weather"][0]["main"]
        if weather_description in self.code_to_smile:
            wd = self.code_to_smile[weather_description]
        else:
            wd = "Посмотри в окно, не пойму что там за погода!"

        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(data["sys"]["sunrise"])

        self.output_weather_data = f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n" \
            f"Погода в городе: {city}\nТемпература: {cur_weather}C° {wd}\n" \
            f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind} м/с\n" \
            f"Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\nПродолжительность дня: {length_of_the_day}\n" \
            f"Хорошего дня!"

    def set_weather_from_console(self, data):
        try:
            self.transform_data(data)

        except Exception as ex:
            print(ex)
            print("Проверьте название города")

    async def set_weather_from_telegram(self, data):
        try:
            self.transform_data(data)

        except Exception as ex:
            await Message.reply("\U00002620 Проверьте название города \U00002620")

    def get_weather(self):
        return self.output_weather_data
