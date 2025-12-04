# 🚴‍♂️ Bike Rental Demand Forecasting  
### A Machine Learning + Flask Web App for Predicting Daily Bike Rentals

This project predicts **daily bike rental demand** using the **Seoul Bike Sharing Dataset**.  
Multiple ML models were trained—Linear Regression, Lasso, Random Forest, and XGBoost—with **XGBoost** delivering the best accuracy.

The web application provides:

- Real-time weather-powered predictions  
- User authentication (Signup/Login)  
- Prediction history stored using **SQLAlchemy ORM**  
- Interactive charts and visual insights  
- Clean and responsive UI  
- Deployed on Render for public access  

---

# 🌐 Live Deployment

Your project is now **successfully deployed online**:

👉 **Live Website:** [Click here](https://sekhar-bike-rental-demand-forecasting.onrender.com)

---

## 🎥 Demo Assets (Images & Videos)

All project screenshots and demonstration video are available here:

👉 **Google Drive Demo Folder:** [Check it out](https://drive.google.com/drive/folders/1OZElAn-6nIO5DnFWY758l91NmiA2beZG?usp=sharing)

---

# 🧠 Machine Learning Workflow

### 🔹 Models Tested
- Linear Regression  
- Lasso Regression  
- Random Forest Regressor  
- XGBoost Regressor ✔ *(Selected model)*  

### 🔹 Training Instructions  
📌 **Important:**  
- `e_Bike_colab.ipynb` must be run in **Google Colab** for faster training.  
- `inference.ipynb` is used only to test the model after training.  

#### Steps:
1. Open **`e_Bike_colab.ipynb`** in Google Colab  
2. Train all models  
3. Export the best model + scaler:  
   - `xgboost_regressor_r2_0_928_v1.pkl`  
   - `sc.pkl`  
4. Download them  
5. Place them in your local `models/` directory  
6. Run `inference.ipynb` to verify predictions locally  

---

# 🔧 Installation & Setup Guide (Local Machine)

## **1️⃣ Clone the Repository**

```bash
git clone https://github.com/Sekhar098/Bike-Rental-Demand-Forecasting.git
cd Bike-Rental-Demand-Forecasting
```

---

## **2️⃣ Install Dependencies**

This project includes **two** requirement files:

### ✔ `requirements.txt`  
Used for **deployment (Render)**  
Contains only the minimal packages needed to *run* Flask + SQLAlchemy + XGBoost model inference.

### ✔ `requirements-full.txt`  
Used for **model training + development**  
Contains *all* packages, including:  
`xgboost`, `jupyter`, `sklearn`, `matplotlib`, `numpy`, `pandas`, etc.

Install minimal dependencies:

```bash
pip install -r requirements.txt
```

Install full development environment:

```bash
pip install -r requirements-full.txt
```

---

## **3️⃣ Create Your `.env` File**

Your project requires API keys for:

- **OpenWeather API** (for weather data)
- **Flask SECRET_KEY** (for session management)

Create a `.env` file in the project root:

```
API_KEY = "your_openweather_api_key"
SECRET_KEY = "your_flask_secret_key"
```

✔ Required for both **local use** and **deployment**  
✔ The app will not run without these values  

---

## **4️⃣ Ensure Model Files Exist**

Place your trained model files inside:

```
models/
 ├── sc.pkl
 └── xgboost_regressor_r2_0_928_v1.pkl
```

---

## **5️⃣ Start the Flask Application**

Only **ONE** command is required:

```bash
python app.py
```

The app will run locally at:

```
http://127.0.0.1:5000/
```

---

# 🌤 Weather Data Integration

The application uses the **OpenWeather API** to fetch:

- Temperature  
- Humidity  
- Wind speed  
- Rainfall  

These values are passed into the ML model to improve prediction accuracy.

---

# 📊 Prediction Dashboard

The dashboard includes:

- Daily bike rental forecast  
- User-specific prediction history  
- Weather vs. rental trend comparison  
- Chart.js-powered analytics  

---

# 🔐 User Authentication

Includes:

- Secure registration  
- Login system  
- Password hashing (bcrypt)  
- SQLAlchemy-based user prediction logs  

---

# 📁 Folder Structure (Actual Project Structure)

```
Bike-Rental-Demand-Forecasting/
│── app.py
│── models.py
│── extensions.py
│── e_Bike_colab.ipynb
│── inference.ipynb
│── requirements.txt                # minimal, used for deployment
│── requirements-full.txt           # full environment for training
│── .env
│── Procfile
│── instance/
│   └── site.db                     # SQLite database created automatically
│── models/
│   ├── sc.pkl
│   └── xgboost_regressor_r2_0_928_v1.pkl
│── data/
│   └── SeoulBikeData.csv
│── templates/
│   ├── index.html
│   ├── login.html
│   ├── signup.html
│   ├── prediction_history.html
│   ├── weather.html
│   └── how-it-works.html
│── static/
│   ├── images/
│   ├── styles.css
│   ├── style2.css
│   ├── sty.css
│   └── styles1.css
└── README.md
```

---

# 🚀 Features

✔ XGBoost-based forecasting  
✔ Real-time weather integration  
✔ SQLAlchemy ORM  
✔ Interactive & responsive dashboard  
✔ Secure authentication  
✔ Deployed on Render  
✔ Single-command local execution (`python app.py`)  

---

# 🛠 Future Enhancements

- Multi-city demand forecasting  
- Improved mobile UI  
- Admin dashboard  
- Automated model retraining  
- CI/CD pipeline integration  

---

# ✍️ Author

**Sekhar Gauda**  
[GitHub](https://github.com/Sekhar098)  
[LinkedIn](https://www.linkedin.com/in/sekhargauda) 

---

# 🤝 Contributing

Contributions are welcome!  
Open an issue or submit a PR.

---

# 📜 License

This project is licensed under the **MIT License**.

---

# ⭐ Support

If you like this project, please ⭐ the repository!

