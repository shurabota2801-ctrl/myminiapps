import requests
import json
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

class ConsoleWeatherApp():
    def get_weather(self):

        api_key = os.getenv('API_KEY')

        city = str(input("Введите город: "))
        now = datetime.now()
        formated_now = now.strftime('%d-%m-%Y')

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru"

        response = requests.get(url)
        data = response.json()
        if data['cod'] == 200:

            temp = data["main"]["temp"]
            feels = data["main"]["feels_like"]
            wind = data["wind"]["speed"]
            description = data["weather"][0]["description"] 

            print(f"\n{'='*10} Погода на {formated_now} {'='*10}")
            print(f"Город: {city}")
            print(f"Температура: {round(temp)}°C")
            print(f"Ощущается как: {round(feels)}°C")
            print(f"Ветер: {round(wind)} м/с")
            print(f"Описание: {description}")
            print(f"{'='*42}\n")

        else:
            print(f"Ошибка: {data.get('message')}")