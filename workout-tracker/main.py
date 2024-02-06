import requests
from datetime import datetime

APP_ID = "18f94ed5"
API_KEY = "79ec3aa83e1205601e004c812d02d96c"
GENDER = "male"
WEIGHT_KG = 70.2
HEIGHT_CM = 168
AGE = 25

today = datetime.now()
today_date = today.strftime("%d/%m/%Y")
time = today.strftime("%H:%M:%S")
# I am going to use Nutritionix API for tracking Nutrition and Exercise burn calories

Nutritionix_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    'Content-Type' : "application/json",
    'x-app-id' : APP_ID,
    'x-app-key' : API_KEY
}

exercise_text = input("Tell me which exercise you did : ")


query_param = {
    "query" : exercise_text,
    "gender" : GENDER,
    "weight_kg" : WEIGHT_KG,
    "height_cm" : HEIGHT_CM,
    "age" : AGE
}

Sheet_ENDPOINT = "https://api.sheety.co/671c9b1e6adf7cd6ccf025ec0da209c1/workoutTracking/workouts"



responce = requests.post(url=Nutritionix_ENDPOINT, json=query_param, headers=headers)
responce.raise_for_status()
data = responce.json()
tasks = data["exercises"]
# print(tasks)

for task in tasks:
    sheet_inputs = {
        "workout" : {
            "date" : today_date,
            "time" : time,
            "exercise" : task["name"].title(),
            "duration" : task["duration_min"],
            "calories" : task["nf_calories"]
        }
    }


    posting_res = requests.post(url=Sheet_ENDPOINT, json=sheet_inputs, auth=("devesh","Dev12345"))
    print(posting_res.text)
