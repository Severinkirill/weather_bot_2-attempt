import requests
import datetime
from config import weather_api, bot_token
from aiogram import Bot, types, Dispatcher
from aiogram.filters import Command
from aiogram import Router
import asyncio

bot = Bot(token=bot_token)
dp = Dispatcher()
router = Router()
dp.include_router(router)

@router.message(Command(commands=["start"]))
async def start_command(message: types.Message):
    await message.answer("Welcome to the Weather Bot! Send me a city name to get the weather information.")

async def get_weather(city, weather_api_key):
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
        "light intensity shower rain": "🌦️",
        "shower rain": "🌦️",
        "heavy intensity shower rain": "🌧️",
        "ragged shower rain": "🌧️",
        "light intensity drizzle": "🌦️",
        "drizzle": "🌦️",
        "heavy intensity drizzle": "🌧️",
        "light intensity drizzle rain": "🌧️",
        "drizzle rain": "🌧️",
        "heavy intensity drizzle rain": "🌧️",
        "shower drizzle": "🌦️",
        "heavy shower drizzle": "🌧️",
        "ragged shower drizzle": "🌧️",
        "thunderstorm with light rain": "⛈️",
        "thunderstorm with rain": "⛈️",
        "thunderstorm with heavy rain": "⛈️",
        "light thunderstorm": "⛈️",
        "thunderstorm": "⛈️",
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
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units=metric"
        )
        data = r.json()

        if data.get("cod") != 200:
            return f"City not found: {city}. Please check the city name."

        city_name = data["name"]
        weather_rn = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        weather_desc = data["weather"][0]["description"]

        display_desc = ""
        weather_desc_lower = weather_desc.lower()

        if weather_desc_lower in code_to_smile:
            display_desc = code_to_smile[weather_desc_lower]
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

        response_message = (
            f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}***\n"
            f"City/Город: {city_name}\n"
            f"Temperature/Температура: {weather_rn}°C \n"
            f"Feels Like/Ощущается как: {feels_like}°C\n"
            f"Weather Description/Описание: {weather_desc} {display_desc}\n"
            f"Humidity/Влажность: {humidity}%\n"
            f"Pressure/Давление: {pressure} hPa\n"
            f"Max Temperature/Макс. температура: {temp_max}°C\n"
            f"Min Temperature/Мин. температура: {temp_min}°C\n"
            f"Visibility/Видимость: {visibility} m\n"
            f"Wind Speed/Скорость ветра: {wind_speed} m/s\n"
            f"Wind Direction/Направление ветра: {wind_deg}°\n"
            f"Sunrise/Восход солнца:{sunrise_time_utc.strftime('%H:%M')}\n"
            f"Sunset/Заход солнца:{sunset_time_utc.strftime('%H:%M')}\n"
            f"Length of the Day/Длительность дня: {lenghth_of_the_day}"
        )
        return response_message

    except requests.exceptions.ConnectionError:
        return "Connection error. Please check your internet connection."
    except Exception as ex:
        return f"An error occurred: {ex}. Please check the city name and try again."

@router.message()
async def get_weather_by_city(message: types.Message):
    city = message.text
    weather_info = await get_weather(city, weather_api)
    await message.answer(weather_info)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
