import data_class
import get_weather_class
from pprint import pprint
from config import open_weather_token

def main():
    city = input("Введите город: ")
    data = data_class.Data(city, open_weather_token).get_data()
    weather = get_weather_class.Get_weather(data).get_weather()
    print(weather)


if __name__ == '__main__':
    main()
