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

* **Algorithm used:** Random Forest Regressor (tuned)
* **Pipeline:** EDA → missing value/duplicate checks → label encoding → train/test split → model comparison → 5-fold cross-validation → hyperparameter tuning → final model

### 📊 Model Performance

Two models were trained and compared on a held-out validation set (20% of training data):

| Model                            | R² Score  | MAE (kWh) |
|----------------------------------|-----------|-----------|
| Linear Regression (baseline)     | 0.845     | 330.4     |
| Random Forest (default)          | 0.978     | 109.4     |
| **Random Forest (tuned, final)** | **0.976** | **114.3** |

**5-fold cross-validation** on the tuned Random Forest confirms the model generalizes well and isn't overfitting to a single split:
* Average R²: **0.971**
* Average MAE: **125.4 kWh**

Random Forest was chosen as the final model since it captures non-linear relationships between building features and energy usage far better than a linear baseline.

### Feature Importance
The notebook includes a feature importance plot showing which inputs (square footage, occupants, appliances used, temperature, etc.) drive the model's predictions most strongly.

---

## 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Joblib
* Matplotlib / Seaborn (EDA)

---

## 📂 Project Structure

```
energy-consumption-prediction/
│
├── app.py                              # Streamlit application
├── energy_model.pkl                    # Trained ML model
├── encoders.pkl                        # Label encoders for categorical data
├── energy_consumption_analysis.ipynb   # Full EDA + model training notebook
├── requirements.txt                    # Required Python libraries
├── train_energy_data.csv               # Dataset used for training
├── test_energy_data.csv                # Held-out dataset used for final predictions
└── README.md                           # Project documentation
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

* Add data visualization directly in the Streamlit app (not just the notebook)
* Improve UI/UX design
* Try gradient boosting models (XGBoost/LightGBM) for comparison
* Deploy using Docker or cloud platforms
* Add automated tests for the prediction pipeline

---

## 👩‍💻 Author

**Janhavi Suhas Sawant**
BSc Computer Science Student | Aspiring Data Analyst
