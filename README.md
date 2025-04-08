# 🏋️‍♂️ Workout Tracker with Nutritionix & Sheety

This Python project uses the Nutritionix API to analyze your workout and log the calories burned into a Google Sheet using the Sheety API.

## 🔧 Features

- Understands natural language workouts (e.g., "Ran 3km and did 20 pushups")
- Calculates calories burned using Nutritionix
- Logs data into Google Sheets using Sheety
- Uses Basic Auth for secure access

## 🛠️ Tech Stack

- Python 3
- Nutritionix API
- Sheety API
- `requests` module

## ▶️ How to Run

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/workout-tracker.git
   cd workout-tracker
Install Dependencies Make sure you have Python installed, then run:
pip install -r requirements.txt
Configure Credentials Open main.py and update the following with your own API keys:
Nutritionix App ID
Nutritionix API Key
Sheety username & password
Project name and sheet name (from your Sheety dashboard)
Run the Script
python main.py
Track Your Workout You'll be prompted to enter your workout like:
Ran 3km and did 15 minutes of yoga
It will calculate calories burned and automatically log the data to your connected Google Sheet.
