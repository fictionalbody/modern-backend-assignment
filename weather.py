import sys
import requests
from datetime import date
from typing import Tuple


def get_weather(city: str, api_key: str) -> Tuple[float, str]:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    resp = requests.get(url)

    if resp.status_code == 404:
        raise ValueError("City not found.")
    
    if not resp.ok:
        raise Exception("Failed to fetch weather data.")
    
    data = resp.json()

    try:
        return data["main"]["temp"], data["name"]
    
    except (KeyError, TypeError):
        raise Exception("Malformed response from weather service.")

def main():
    api_key = "a1547a86bee2f05d5a63696643afd8fe"

    if len(sys.argv) != 2:
        print("Error: сity name is required.")
        sys.exit(1)

    city = sys.argv[1].strip()
    
    try:
        temp, city_name = get_weather(city, api_key)

    except ValueError as ve:
        print(str(ve))
        sys.exit(1)

    except Exception as e:
        print("Error:", str(e))
        sys.exit(1)

    today = date.today().strftime("%Y/%m/%d")
    print(f"{today} | {city_name} | {temp:.1f} C")

main()
