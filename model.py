import joblib

temp_model = joblib.load("temp_model.pkl")
cond_model = joblib.load("cond_model.pkl")
encoder = joblib.load("encoder.pkl")

def predict(features):
    data = [[
        features["temp"],
        features["humidity"],
        features["temp_lag1"],
        features["temp_lag2"]
    ]]

    temp_pred = round(temp_model.predict(data)[0], 2)

    cond_pred = cond_model.predict(data)[0]
    condition = encoder.inverse_transform([cond_pred])[0]

    return temp_pred, condition