import requests
import tkinter as tk
from tkinter import messagebox

def fetch_weather_data(api_key, city, unit='m'):
    try:
        # Make a request to the weather API
        response = requests.get(f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&unit={unit}")
        response.raise_for_status()  # Raise an exception if the request fails

        # Parse the JSON response
        weather_data = response.json()

        # Extract relevant information from the response
        location = weather_data['location']['name']
        
        temperature = weather_data['current']['temp_f'] if unit == 'imperial' else weather_data['current']['temp_c']
        
        condition = weather_data['current']['condition']['text']

        # Display the weather information
        unit_label = 'F' if unit == 'imperial' else 'C'
        messagebox.showinfo("Weather Information", f"Location: {location}\nTemperature: {temperature}°{unit_label}\nCondition: {condition}")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Failed to fetch weather data: {e}")

# Example usage
api_key = "ENTER API KEY HERE"
city = "Asheville"
unit = 'imperial'
fetch_weather_data(api_key, city, unit)
