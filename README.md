# 🏠 House Price Prediction Web App

A simple machine learning-powered web application that predicts house prices based on input features like number of rooms, location, size, etc. This app is built with **Flask**, trained using **scikit-learn**, and deployable on **Render** or any cloud platform.

---

## 🚀 Features

- 🧠 Predict house prices using a trained ML model.
- 🔢 Input fields for common house attributes (build year).
- 🌐 Deployed-ready Flask app with a clean HTML + CSS frontend.
- 📦 Supports `.pkl` (Pickle) model integration.

---

## 📁 Project Structure

```

House-Price-Prediction/
├── app.py                   # Main Flask application
├── house\_price\_model.pkl    # Trained ML model
├── requirements.txt         # Python dependencies
├── templates/
│   ├── index.html           # Input form page
│   └── result.html          # Result display page
├── static/
│   └── style.css            # Custom CSS styling
├── Procfile                 # For Render deployment
└── README.md                # Project documentation

````

---

## 💻 Local Setup

### 🔹 1. Clone the repo

```bash
git clone https://github.com/yourusername/House-Price-Prediction.git
cd House-Price-Prediction
````

### 🔹 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 🔹 3. Run the Flask app

```bash
python app.py
```

Now open your browser and visit:
`http://127.0.0.1:5000`

---

## 🌐 Deployment on Render

1. Push the project to GitHub.
2. Go to [https://render.com](https://render.com) and create a **New Web Service**.
3. Connect your GitHub repo.
4. Fill the deployment configuration:

* **Build Command**:

  ```bash
  pip install -r requirements.txt
  ```

* **Start Command**:

  ```bash
  gunicorn app:app
  ```

5. Deploy the service and enjoy your hosted app!

---

## 📌 Sample Prediction Script

```python
import pickle
import pandas as pd

# Load the model
model = pickle.load(open('house_price_model.pkl', 'rb'))

# Create a sample input
sample_input = pd.DataFrame({
    'Rooms': [3],
    'Area': [1200],
    'Location_Code': [5],
    'Age': [10]
})

# Predict
predicted_price = model.predict(sample_input)
print(f"Predicted House Price: ₹{predicted_price[0]:,.2f}")
```

---

## 🔗 Live Demo

**🌍 Deployed at:**
[https://house-price-prediction.onrender.com](https://house-price-prediction.onrender.com)

---

## 🏷️ License

This project is licensed under the **MIT License**. Free to use, customize, and distribute.

---

## 🙌 Author

Developed by **\[Saravanavel E]**
GitHub: [https://github.com/SaravanavelE](https://github.com/SaravanavelE)
LinkedIn: [https://linkedin.com/in/saravanavel-e](https://linkedin.com/in/saravanavel-e)

---

