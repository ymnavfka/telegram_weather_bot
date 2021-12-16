import requests
import data_class
from pprint import pprint
from config import open_weather_token


def get_weather(city, open_weather_token):
    try:

        data = data_class.Data(city, open_weather_token)
        pprint(data.get_data())

    except Exception as ex:
        print(ex)
        print("Проверьте название города")


def main():
    city = input("Введите город: ")
    get_weather(city, open_weather_token)


if __name__ == '__main__':
    main()
