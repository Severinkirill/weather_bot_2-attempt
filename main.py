import requests
import datetime
from pprint import pprint
from config import weather_api

def get_weather(city, weather_api):
    code_to_smile = {
        "clear sky": "☀️",
        "few clouds": "🌤️",
        "scattered clouds": "🌥️",
        "broken clouds": "🌥️",
        "overcast clouds": "☁️",
        "light rain": "🌦️",
        "moderate rain": "🌧️",
        "heavy intensity rain": "🌧️",
        "very heavy rain": "🌧️",
        "extreme rain": "🌧️",
        "freezing rain": "🌨️",
        "light intensity shower rain":"🌦️",
        "shower rain": "🌦️",
        "heavy intensity shower rain": "🌧️",
        "ragged shower rain": "🌧️",
        "drizzle": "🌦️",
        "thunderstorm": "⛈️",
        "thunderstorm with light rain": "⛈️",
        "thunderstorm with rain": "⛈️",
        "thunderstorm with heavy rain": "⛈️",
        "light thunderstorm": "⛈️",
        "heavy thunderstorm": "⛈️",
        "ragged thunderstorm": "⛈️",
        "thunderstorm with light drizzle": "⛈️",
        "thunderstorm with drizzle": "⛈️",
        "thunderstorm with heavy drizzle": "⛈️",
        "light snow": "❄️",
        "snow": "❄️",
        "heavy snow": "❄️",
        "sleet": "🌨️",
        "light shower sleet": "🌨️",
        "shower sleet": "🌨️",
        "light rain and snow": "🌨️",
        "rain and snow": "🌨️",
        "light shower snow": "🌨️",
        "shower snow": "🌨️",
        "heavy shower snow": "🌨️",
        "mist": "🌫️",
        "smoke": "🌫️",
        "haze": "🌫️",
        "sand/dust whirls": "🌪️",
        "fog": "🌫️",
        "sand": "🌪️",
        "dust": "🌪️",
        "volcanic ash": "🌋",
        "squalls": "🌬️",
        "tornado": "🌪️",
        "default": "🌈"
    }

    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api}&units=metric"
        )
        data = r.json()

        city_name_from_api = data["name"]
        weather_rn = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        weather_desc = data["weather"][0]["description"]

        display_desc = ""

        if weather_desc in code_to_smile:
            display_desc = code_to_smile[weather_desc]
        else:
            display_desc = code_to_smile["default"]

        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        temp_max = data["main"]["temp_max"]
        temp_min = data["main"]["temp_min"]
        visibility = data["visibility"]
        wind_speed = data["wind"]["speed"]
        wind_deg = data["wind"]["deg"]
        sunrise_timestamp = data["sys"]["sunrise"]
        sunset_timestamp = data["sys"]["sunset"]

        sunrise_time_utc = datetime.datetime.fromtimestamp(sunrise_timestamp)
        sunset_time_utc = datetime.datetime.fromtimestamp(sunset_timestamp)
        lenghth_of_the_day = sunset_time_utc - sunrise_time_utc

        print(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}***")
        print(f"City/Город: {city_name_from_api}")
        print(f"Temperature/Температура: {weather_rn}°C ")
        print(f"Feels Like/Ощущается как: {feels_like}°C")
        print(f"Weather Description/Описание: {weather_desc} {display_desc}")
        print(f"Humidity/Влажность: {humidity}%")
        print(f"Pressure/Давление: {pressure} hPa")
        print(f"Max Temperature/Макс. температура: {temp_max}°C")
        print(f"Min Temperature/Мин. температура: {temp_min}°C")
        print(f"Visibility/Видимость: {visibility} m")
        print(f"Wind Speed/Скорость ветра: {wind_speed} m/s")
        print(f"Wind Direction/Направление ветра: {wind_deg}°")
        print(f"Sunrise/Восход солнца:{sunrise_time_utc.strftime('%H:%M')}")
        print(f"Sunset/Заход солнца:{sunset_time_utc.strftime('%H:%M')}")
        print(f"Length of the Day/Длительность дня: {lenghth_of_the_day}")

    except Exception as ex:
        print(ex)
        print(f"An error occurred:{ex}. Please check the city name and try again.")


def main():
    city = input("enter city name: ")
    get_weather(city, weather_api)

if __name__ == "__main__":
    main()