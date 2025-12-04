# 🚴‍♂️ Bike Rental Demand Forecasting  
### A Machine Learning + Flask Web App for Predicting Daily Bike Rentals

This project predicts **daily bike rental demand** using the **Seoul Bike Sharing Dataset**.  
Multiple ML models were trained—Linear Regression, Lasso, Random Forest, and XGBoost—with **XGBoost** delivering the best accuracy.

The web application provides:

- ✔ Real-time weather-powered predictions  
- ✔ User authentication (Signup/Login)  
- ✔ Prediction history stored using **SQLAlchemy ORM**  
- ✔ Interactive charts and visual insights  
- ✔ Clean and responsive UI  

---

## 🎥 Demo Assets (Images & Videos)

All project screenshots and demonstration video are available publicly here:

👉 **Google Drive Demo Folder:**  
https://drive.google.com/drive/folders/1OZElAn-6nIO5DnFWY758l91NmiA2beZG?usp=sharing

---

## 🧠 Machine Learning Workflow

### 🔹 Models Tested
- Linear Regression  
- Lasso Regression  
- Random Forest Regressor  
- XGBoost Regressor ✔ *(Selected model)*  

### 🔹 Training Instructions  
📌 **Important:**  
- `e_Bike_colab.ipynb` must be **run in Google Colab Terminal** because it requires more compute and uses Colab’s Python environment.  
- `inference.ipynb` is used **only to check the working of the model** after training.

#### Steps:
1. Open **`e_Bike_colab.ipynb`** in **Google Colab**  
2. Train all models  
3. Save the best-performing files:  
   - `xgboost_regressor.pkl`  
   - `sc.pkl`  
4. Download these model files  
5. Place them into the local `models/` directory  
6. Run **`inference.ipynb`** to verify predictions  

---

# 🔧 Installation & Setup Guide

## **1️⃣ Clone the Repository**

```bash
git clone https://github.com/Sekhar098/Bike-Rental-Demand-Forecasting.git
cd Bike-Rental-Demand-Forecasting
```

---

## **2️⃣ Install Dependencies**

```bash
pip install -r requirements.txt
```

---

## **3️⃣ Ensure Model Files Exist**

Your final trained model files should be inside:

```
models/
 ├── xgboost_regressor.pkl
 └── sc.pkl
```

If not, train using Google Colab.

---

## **4️⃣ Setup Database via SQLAlchemy**

This project uses **SQLAlchemy ORM**, not MySQL.  
Tables are created automatically using Python scripts.

Run:

```bash
python create_table.py
python my_inspect.py
```

These scripts:

- Initialize database tables  
- Verify SQLAlchemy models  
- Ensure SQLite DB (`site.db`) is created properly  

---

## **5️⃣ Start the Flask Application**

```bash
python app.py
```

Your app will run at:

```
http://127.0.0.1:5000/
```

Open this address in your browser.

---

# 🌤 Weather Data Integration

The app uses **OpenWeather API** to fetch:

- Temperature  
- Humidity  
- Wind speed  
- Rainfall  

These live weather inputs improve the prediction accuracy dynamically.

---

# 📊 Prediction Dashboard

The dashboard provides:

- Daily bike demand prediction  
- SQLAlchemy-based user prediction history  
- Visual analytics using Chart.js  
- Weather vs. rental trend comparisons  

Add screenshots or GIF demos here.

---

# 🔐 User Authentication

Includes:

- User registration  
- Login system  
- Password hashing with bcrypt  
- Personalized prediction logs stored via SQLAlchemy  

---

# 📁 Folder Structure

```
Bike-Rental-Demand-Forecasting/
│── app.py
│── models.py
│── extensions.py
│── create_table.py
│── my_inspect.py
│── requirements.txt
│── models/                 # trained ML model files
│── static/
│   ├── images/
│   └── styles/
│── templates/
│   ├── index.html
│   ├── login.html
│   ├── signup.html
│   ├── prediction_history.html
│── data/
│── e_Bike_colab.ipynb
│── inference.ipynb
└── README.md
```

---

# 🚀 Features

✔ XGBoost-based demand forecasting  
✔ Real-time weather integration  
✔ SQLAlchemy ORM for database operations  
✔ Interactive dashboards & charts  
✔ Secure login/signup system  
✔ Scalable and modular architecture  

---

# 🛠 Future Enhancements

- Deployment on Render or Heroku  
- Mobile-responsive UI improvements  
- Automatic model retraining pipeline  
- Multi-city demand prediction  
- Admin analytics dashboard  

---

# ✍️ Author

**Sekhar**  
GitHub: [Sekhar Gauda](https://github.com/Sekhar098)  
LinkedIn: [Sekhar Gauda](https://www.linkedin.com/in/sekhargauda)


# 🤝 Contributing

Contributions are welcome!  
Feel free to open issues or submit a PR.

---

# 📜 License

This project is licensed under the **MIT License**.

---

# ⭐ Support

If you like this project, please ⭐ the repository to show your support!

