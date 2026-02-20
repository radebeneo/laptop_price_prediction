import pandas as pd
import streamlit as st
import numpy as np
import joblib

model = joblib.load('rf_model.pkl')

st.title("Laptop Price Prediction")

st.divider()

st.write("Get price estimation for your laptop by entering Processor Speed, RAM Size, and Storage Capacity.")

st.divider()

processor_speed = st.number_input("Enter Processor Speed", value = 2.50, step = 0.50)
ram_size = st.number_input("Enter RAM Size", value = 16, step = 4)
storage_capacity = st.number_input("Enter Storage Capacity", value = 512, step = 256)


X = [processor_speed, ram_size, storage_capacity]

st.divider()

prediction = st.button("Estimate Price")

st.divider()

if prediction:

    x1 = pd.DataFrame([[processor_speed, ram_size, storage_capacity]], columns=["Processor_Speed", "RAM_Size", "Storage_Capacity"])
    prediction_val = model.predict(x1)[0]
    st.warning(f"Price estimate for your laptop is {prediction_val:,.2f}")

else:
    st.write("Click button to get your price estimate")




