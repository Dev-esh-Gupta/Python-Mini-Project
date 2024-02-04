import requests
from twilio.rest import Client

# Twilio related setup
account_sid = "ACa056ee0729ae9b0a149c46b49834549d"
auth_token = "43bb804ddadb16bae8c0c5347e6e3728"

MY_LAT = "17.968901"
MY_LONG = "79.594055"
KEY = "4b8576faca7afdde9b04d37b8d702196"

parameter = {
    "lat" : 29.487425,
    "lon" : -94.922562,
    "appid" : KEY,
    "cnt" : "4"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params= parameter)
response.raise_for_status()
weather_data = response.json()

it_will_rain = False

for hour_data in weather_data["list"]:
    print(hour_data["weather"][0])
    if hour_data["weather"][0]["id"] < 700:
         it_will_rain = True

if it_will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It will gonna rain today! Don't forget to bring umbrella☔",
        from_='+14432620275',
        to='+916307703807'
    )

    print(message.status)