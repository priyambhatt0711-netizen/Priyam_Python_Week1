import requests
import os

def get_weather(city):
    api_key = os.getenv("WEATHER_API_KEY")

    if not api_key:
        print("Error: API key not found. Set WEATHER_API_KEY.")
        return

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        print("\n--- Weather Report ---")
        print(f"City       : {data['name']}")
        print(f"Temperature: {data['main']['temp']} °C")
        print(f"Humidity   : {data['main']['humidity']} %")
        print(f"Condition  : {data['weather'][0]['description'].title()}")
        print(f"Wind Speed : {data['wind']['speed']} m/s")

    except requests.exceptions.HTTPError:
        print("Error: City not found.")
    except requests.exceptions.RequestException:
        print("Error: Network problem.")
    except KeyError:
        print("Error: Unexpected response format.")

def main():
    print("=== Weather Forecast App ===")
    city = input("Enter city name: ").strip()

    if not city:
        print("Error: City name cannot be empty.")
        return

    get_weather(city)

if __name__ == "__main__":
    main()
