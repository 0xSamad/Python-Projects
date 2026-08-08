import requests
import os
from dotenv import load_dotenv
from datetime import datetime


load_dotenv()

GENDER = "male"
WEIGHT_KG = 65
HEIGHT_CM = 5.5
AGE = 22

QUERY = input("What exercises you did? : ")

headers = {
    "x-app-id": os.getenv("X_APP_ID"),
    "x-app-key": os.getenv("X_APP_KEY"),
    "content-type": "application/json"
}

ENDPOINT = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")


data = {
    "query": QUERY,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=ENDPOINT,headers=headers,json=data)

result = response.json()

today_date = datetime.now().strftime("%d/%m/%y")
now_time = datetime.now().strftime("%X")


for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }


bearer_headers ={
"Authorization": f"Bearer {os.getenv("BEARER_TOKEN")}"
}



sheety_response = requests.post(url=SHEETY_ENDPOINT,json=sheet_inputs,headers=bearer_headers)
print(sheety_response.text)