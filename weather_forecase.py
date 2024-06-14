import requests

url = "https://api.tomorrow.io/v4/timelines?location=27.688574692388197%2C%2085.33097134810889&fields=temperature&units=metric&timesteps=1h&startTime=now&endTime=nowPlus6h&apikey=E9dCUxAA0Bba90XrE1Y99iQ9K27Jh6N0"

headers = {
    "accept": "application/json",
    "Accept-Encoding": "gzip"
}

response = requests.get(url, headers=headers)



t = response.json()['data']['timelines'][0]['intervals'][0]['values']['temperature']
print("Weather Forecast")
print("================")

results = response.json()['data']['timelines'][0]['intervals']
for daily_result in results:
    date = daily_result['startTime'][0:10]
    temp = round(daily_result['values']['temperature'])
    print("On",date,"it will be", temp, "F")