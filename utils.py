import pandas as pd
from pathlib import Path
from sklearn.preprocessing import LabelEncoder

FILE_PATH = Path(__file__).resolve().parent / "weather.csv"

def load_data():
    df = pd.read_csv(FILE_PATH)
    df['last_updated'] = pd.to_datetime(df['last_updated'])
    return df


def preprocess_data(df):
    df = df[df['last_updated'] >= '2023-01-01']

    df = df[['last_updated', 'location_name',
             'temperature_celsius', 'humidity',
             'condition_text']]

    df.columns = ['date', 'city', 'temp', 'humidity', 'condition']

    df = df.sort_values(['city', 'date'])
    df = df.ffill()

    return df


def create_features(df):
    df['temp_lag1'] = df.groupby('city')['temp'].shift(1)
    df['temp_lag2'] = df.groupby('city')['temp'].shift(2)

    df['target_temp'] = df.groupby('city')['temp'].shift(-1)

    df = df.dropna()
    return df


def encode_condition(df):
    encoder = LabelEncoder()
    df['condition_encoded'] = encoder.fit_transform(df['condition'])
    return df, encoder


def get_features_targets(df):
    features = ['temp', 'humidity', 'temp_lag1', 'temp_lag2']

    X = df[features]
    y_temp = df['target_temp']
    y_cond = df['condition_encoded']

    return X, y_temp, y_cond