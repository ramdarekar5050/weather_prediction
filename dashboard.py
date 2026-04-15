import streamlit as st
import requests
import pandas as pd

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Weather AI", layout="wide")

st.title("🌦️ AI Weather Prediction Dashboard")

st.write("Predict next day's weather using simple inputs")

col1, col2 = st.columns(2)

with col1:
    temp = st.number_input("🌡️ Temperature (°C)", value=30.0)
    humidity = st.number_input("💧 Humidity (%)", value=60)

with col2:
    temp_lag1 = st.number_input("Yesterday Temp", value=29.0)
    temp_lag2 = st.number_input("Day Before Temp", value=28.0)

if st.button("🔮 Predict"):

    payload = {
        "temp": temp,
        "humidity": humidity,
        "temp_lag1": temp_lag1,
        "temp_lag2": temp_lag2
    }

    res = requests.post(f"{API_URL}/predict", json=payload)

    if res.status_code == 200:
        data = res.json()

        st.metric("🌡️ Predicted Temperature", f"{data['predicted_temperature']} °C")
        st.success(f"🌤️ Condition: {data['predicted_condition']}")

        # Graph
        st.subheader("📈 Temperature Trend")

        df = pd.DataFrame({
            "Day": ["Day-2", "Day-1", "Today"],
            "Temp": [temp_lag2, temp_lag1, temp]
        })

        st.line_chart(df.set_index("Day"))