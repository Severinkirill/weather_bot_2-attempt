import requests
from pprint import pprint
from config import weather_api

def get_weather(city, weather_api):
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api}&units=metric"
        )
        data = r.json()
        pprint(data)
        
    except Exception as ex:
        print(ex)
        print(f"An error occurred:")


def main():
    city = input("enter city name: ")
    get_weather(city, weather_api)

if __name__ == "__main__":
    main()