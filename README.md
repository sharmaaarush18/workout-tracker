# 🏋️‍♂️ Workout Tracker with Nutritionix & Sheety

This Python project uses the Nutritionix API to analyze your workout and log the calories burned into a Google Sheet using the Sheety API.

---

## 🔧 Features

1. **Natural Language Input**  
   Enter workouts like "Ran 3km and did 20 pushups" — the program understands it.

2. **Calorie Calculation**  
   Calories burned are automatically calculated using the Nutritionix API.

3. **Google Sheet Logging**  
   The workout data is logged into a Google Sheet via the Sheety API.

4. **Secure Auth**  
   Uses Basic Auth (Base64 encoded) for secure Sheety access.

---

## 🛠️ Tech Stack

- **Python 3**
- **Nutritionix API**
- **Sheety API**
- **`requests` Python Module**

---

## ▶️ How to Run

1. **Clone the Repository**
   ```bash
   git clone https://github.com/sharmaaarush18/workout-tracker.git
   cd workout-tracker
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Your Environment Variables**
   Create a file named `.env` in the root directory and add:

   ```dotenv
   # Nutritionix API
   APP_ID=your_nutritionix_app_id
   API_KEY=your_nutritionix_api_key

   # Sheety API
   USERNAME=your_sheety_username
   PASSWORD=your_sheety_password

   # Optional: Link to your workout Google Sheet
   GOOGLE_SHEET_LINK=https://docs.google.com/spreadsheets/d/your_spreadsheet_id/edit#gid=0
   ```

   > ⚠️ **Never commit this file to GitHub** — add `.env` to your `.gitignore`.

4. **Run the Program**
   ```bash
   python main.py
   ```

5. **Log Your Workout**
   When prompted, type something like:
   ```
   Ran 3km and did 15 minutes of yoga
   ```
   The program will:
   - Understand the input using Nutritionix
   - Calculate calories burned
   - Auto-log the workout into your connected Google Sheet ✅

---

## 📝 Google Sheet Setup

1. Go to [Google Sheets](https://sheets.google.com) and create a new spreadsheet.
2. Add the following headers in **Row 1** exactly:

| Date       | Time     | Exercise | Duration | Calories |
|------------|----------|----------|----------|----------|
| 21/07/2020 | 15:00:00 | Running  | 22       | 130      |

**Header Notes:**
- `Date`: `DD/MM/YYYY`
- `Time`: `HH:MM:SS` (24-hour format)
- `Exercise`: The workout type
- `Duration`: In minutes
- `Calories`: Auto-fetched from Nutritionix

3. Set up a [Sheety](https://sheety.co/) project connected to this sheet.
4. In `main.py`, make sure `PROJECT_NAME` and `SHEET_NAME` match your Sheety project:
   ```python
   PROJECT_NAME = "workoutTracking"
   SHEET_NAME = "workouts"
   ```

---

## 📁 File Structure

```bash
workout-tracker/
├── main.py               # Core logic of workout tracking
├── .env                  # Your personal API keys (not committed)
├── requirements.txt      # Required dependencies
├── LICENSE               # MIT License
└── README.md             # Project documentation
```

---

## 📦 requirements.txt

```text
requests
python-dotenv
```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🧠 Project Description

This project is a natural-language-powered calorie tracker using **Nutritionix API** and **Sheety API**. You just type your workouts the way you would speak, and it calculates your calories and logs the session to your own Google Sheet. A simple yet smart automation system to track your fitness journey daily! ✅

---

## ✨ Credits

- Built with 💪 by Aarush Sharma  
- APIs used:  
  - [Nutritionix API](https://www.nutritionix.com/business/api)  
  - [Sheety API](https://sheety.co/)
