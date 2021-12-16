import requests

class Data(object):

    def __init__(self, city, open_weather_token):
        self.data = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        ).json()
    
    def get_data(self):
        return self.data

    def set_data(self, city, open_weather_token):
        self.data = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        ).json()