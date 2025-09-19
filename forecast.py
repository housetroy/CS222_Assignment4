import requests

def get_forecast_url(lat=40.1934, lon=-85.3864):
    url = f"https://api.weather.gov/points/{lat},{lon}"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()
    return data['properties']['forecast']

def get_forecast_data(forecast_url):
    response = requests.get(forecast_url, timeout=10)
    response.raise_for_status()
    data = response.json()
    return data['properties']['periods']

def display_forecast(periods):
    for period in periods:
        print(f"{period['name']}: {period['temperature']}F")
        print(period['detailedForecast'])
        print('-' * 40)

forecast_url = get_forecast_url()
periods = get_forecast_data(forecast_url)
display_forecast(periods)