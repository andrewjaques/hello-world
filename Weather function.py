import requests
import json

response = requests.get(
            "https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20u%3D'c'%20and%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22eastleigh%2C%20uk%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys")
json_data = json.loads(response.text)

print(json_data)

now_day = json_data['query']['results']['channel']['item']['condition']['date']
now_condition = json_data['query']['results']['channel']['item']['condition']['text']
now_temp = json_data['query']['results']['channel']['item']['condition']['temp']
forecast_high = json_data['query']['results']['channel']['item']['forecast'][0]['high']
forecast_low = json_data['query']['results']['channel']['item']['forecast'][0]['low']
next_day = json_data['query']['results']['channel']['item']['forecast'][0]['day']
next_condition = json_data['query']['results']['channel']['item']['forecast'][0]['text']




print(now_day, now_condition, now_temp)

print("High: ", forecast_high, "°C, Low:", forecast_low, "°C", sep="")

print(next_day, next_condition)

