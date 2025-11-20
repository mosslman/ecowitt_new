from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()


def get_current_weather(city="Aberdeen"):

    request_url = f'https://api.ecowitt.net/api/v3/device/history?application_key={os.getenv("APP_KEY")}&api_key={os.getenv("API2_KEY")}&mac={os.getenv("MAC")}&start_date=2025-11-20 00:00:00&end_date=2025-11-20 23:59:59&call_back=outdoor.temperature,indoor.temperature&cycle_type=30min&temp_unitid=1'
    print(request_url)
   
   #    request_url = f'http://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'

    weather_data = requests.get(request_url).json()

    return weather_data


if __name__ == "__main__":
    print('\n*** Get Current Weather Conditions ***\n')

    city = input("\nPlease enter a city name: ")

    # Check for empty strings or string with only spaces
    # This step is not required here
    if not bool(city.strip()):
         city = "London"

    weather_data = get_current_weather(city)

    print("\n")
    pprint(weather_data)