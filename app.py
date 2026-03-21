import streamlit as st
import pandas as pd
import joblib

# load model and encoders
model = joblib.load("energy_model.pkl")
encoders = joblib.load("encoders.pkl")

# page settings
st.set_page_config(page_title="Energy Consumption Predictor", page_icon="⚡", layout="centered")

# title
st.title("⚡ Energy Consumption Prediction")
st.write("Enter the details below to predict energy consumption.")

# input fields
building_type = st.selectbox(
    "Building Type",
    ["Select"] + list(encoders["Building Type"].classes_),
    key="building_type"
)

square_footage = st.number_input(
    "Square Footage",
    min_value=0.0,
    value=1000.0
)

number_of_occupants = st.number_input(
    "Number of Occupants",
    min_value=0,
    value=1
)

appliances_used = st.number_input(
    "Appliances Used",
    min_value=0,
    value=1
)

average_temperature = st.number_input(
    "Average Temperature",
    value=25.0
)

day_of_week = st.selectbox(
    "Day of Week",
    ["Select"] + list(encoders["Day of Week"].classes_),
    key="day_of_week"
)

# prediction button
if st.button("Predict Energy Consumption"):

    if building_type == "Select" or day_of_week == "Select":
        st.warning("Please select valid inputs!")
    else:
        input_data = pd.DataFrame({
            "Building Type": [building_type],
            "Square Footage": [square_footage],
            "Number of Occupants": [number_of_occupants],
            "Appliances Used": [appliances_used],
            "Average Temperature": [average_temperature],
            "Day of Week": [day_of_week]
        })

        # encode categorical columns
        for col in encoders:
            input_data[col] = encoders[col].transform(input_data[col])

        prediction = model.predict(input_data)[0]

        st.success(f"Predicted Energy Consumption: {prediction:.2f} kWh")