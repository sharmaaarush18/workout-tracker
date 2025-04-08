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

1. **Python 3**
2. **Nutritionix API**
3. **Sheety API**
4. **`requests` Python Module**

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

3. **Configure Your Credentials**  
   Open `main.py` and replace the placeholders with:
   - Your **Nutritionix App ID**
   - Your **Nutritionix API Key**
   - Your **Sheety username** and **password** (Base64 encoded)
   - Your Sheety **project name** and **sheet name**

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
   - Understand it
   - Calculate the calories burned
   - Auto-log it to your connected Google Sheet 🎯

---

## 📁 File Structure

```bash
workout-tracker/
├── main.py               # Core logic of workout tracking
├── requirements.txt      # Required dependencies
├── LICENSE               # MIT License
└── README.md             # Project documentation
```

---

## 📦 requirements.txt

```bash
requests
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
