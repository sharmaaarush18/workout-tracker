import requests as req
import base64
import datetime

# Nutritionix API credentials
APP_ID = "YOUR_APP_ID"
API_KEY = "YOUR_API_KEY"
URL = "https://trackapi.nutritionix.com/v2/natural/exercise"

# Sheety setup
USERNAME = "YOUR_SHEETY_USERNAME"
PASSWORD = "YOUR_SHEETY_PASSWORD"
PROJECT_NAME = "YOUR_PROJECT_NAME"
SHEET_NAME = "YOUR_SHEET_NAME"
SHEETY_URL = f"https://api.sheety.co/YOUR_PROJECT_ID/{PROJECT_NAME}/{SHEET_NAME}"

# Nutritionix headers
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json",
}

# Sheety headers (Basic Auth)
auth_string = f"{USERNAME}:{PASSWORD}"
auth_encoded = base64.b64encode(auth_string.encode()).decode()
sheety_headers = {
    "Authorization": f"Basic {auth_encoded}"
}

# Input workout from user
user_data = {
    "query": input("Enter your workout for today:\n> ")
}

# Step 1: Get calories burned from Nutritionix
calorie_res = req.post(url=URL, headers=headers, json=user_data)
calorie_res.raise_for_status()
exercise_data = calorie_res.json()["exercises"][0]
print(exercise_data)

exercise_name = exercise_data["name"].title()
duration = exercise_data["duration_min"]
calorie_count = exercise_data["nf_calories"]

# Step 2: Log the workout to Google Sheet via Sheety
now = datetime.datetime.now()
sheet_input = {
    "workout": {
        "date": now.strftime("%d/%m/%Y"),
        "time": now.strftime("%H:%M:%S"),
        "exercise": exercise_name,
        "duration": duration,
        "calories": calorie_count
    }
}

post_res = req.post(url=SHEETY_URL, json=sheet_input, headers=sheety_headers)
post_res.raise_for_status()

print("✅ Workout logged to Google Sheet!")

# Step 3: (Optional) Show current sheet data
auth_res = req.get(url=SHEETY_URL, headers=sheety_headers)
auth = auth_res.json()

print(f"🔥 Total calories burned: {calorie_count} kcal.")
