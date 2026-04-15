from fastapi import FastAPI
from pydantic import BaseModel
from model import predict

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Weather Prediction API (User-Friendly)"}


class WeatherInput(BaseModel):
    temp: float
    humidity: float
    temp_lag1: float
    temp_lag2: float


@app.post("/predict")
def predict_weather(data: WeatherInput):
    temp, condition = predict(data.dict())

    return {
        "predicted_temperature": temp,
        "predicted_condition": condition
    }