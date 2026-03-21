# ⚡ Energy Consumption Prediction App

This project is a **Machine Learning-based web application** that predicts the **energy consumption (kWh)** of a building based on various input features such as building type, square footage, number of occupants, and environmental conditions.

The application is built using **Python, Scikit-learn, and Streamlit**, and allows users to get real-time predictions through an interactive web interface.

---

## 🚀 Live Demo

👉 https://energy-consumption-prediction-by-janhavi.streamlit.app/

---

## 📌 Features

* 🔮 Predict energy consumption in real-time
* 🏢 Input building-related details easily
* ⚡ Fast and accurate predictions using ML model
* 🎯 User-friendly and interactive interface

---

## 🧠 Machine Learning Model

* Algorithm Used: **Random Forest Regressor**
* Model trained on energy consumption dataset
* Includes:

  * Data preprocessing
  * Feature encoding
  * Model training and evaluation

---

## 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Joblib

---

## 📂 Project Structure

```
energy-consumption-prediction/
│
├── app.py                  # Streamlit application
├── energy_model.pkl        # Trained ML model
├── encoders.pkl            # Label encoders for categorical data
├── requirements.txt        # Required Python libraries
├── train_energy_data.csv   # Dataset used for training
└── README.md               # Project documentation
```

---

## ⚙️ How to Run Locally

1️⃣ Clone the repository:

```
git clone https://github.com/janhavisawant03/energy-consumption-prediction.git
```

2️⃣ Navigate to the project folder:

```
cd energy-consumption-prediction
```

3️⃣ Create virtual environment:

```
python -m venv venv
```

4️⃣ Activate virtual environment:

```
venv\Scripts\activate
```

5️⃣ Install dependencies:

```
pip install -r requirements.txt
```

6️⃣ Run the app:

```
streamlit run app.py
```

---

## 📊 Input Features

* Building Type
* Square Footage
* Number of Occupants
* Appliances Used
* Average Temperature
* Day of Week

---

## 🎯 Output

* Predicted **Energy Consumption (kWh)**

---

## 📈 Future Improvements

* Add data visualization (graphs & charts)
* Improve UI/UX design
* Add more advanced ML models
* Deploy using Docker or cloud platforms

---

## 👩‍💻 Author

**Janhavi Sawant**
BSc Computer Science Student | Aspiring Data Scientist
