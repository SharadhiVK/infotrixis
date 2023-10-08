import requests
import argparse
import time

API_KEY = "df32d5575b7d4e18988122636230810"
BASE_URL = "https://api.weatherapi.com/v1/"

def get_weather_by_city(city_name):
    # Make a request to the WeatherAPI to get weather data by city name
    response = requests.get(f"{BASE_URL}current.json?key={API_KEY}&q={city_name}")
    
    if response.status_code == 200:
        data = response.json()
        # Extract and display relevant weather information
        # You can format and print the data as per your requirements
        print(f"Weather in {city_name}: {data['current']['condition']['text']}")
        print(f"Temperature: {data['current']['temp_c']}°C")
    else:
        print("Error: Unable to fetch weather data")

def main():
    parser = argparse.ArgumentParser(description="Command-line Weather App")
    parser.add_argument("--city", help="Get weather by city name")
    # Add more options for CRUD operations on favorite cities and auto-refresh
    
    args = parser.parse_args()

    if args.city:
        get_weather_by_city(args.city)
    # Implement CRUD and auto-refresh functionalities here

if __name__ == "__main__":
    main()
