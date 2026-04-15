from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

from utils import load_data, preprocess_data, create_features, encode_condition, get_features_targets

df = load_data()
df = preprocess_data(df)
df = create_features(df)

df, encoder = encode_condition(df)

X, y_temp, y_cond = get_features_targets(df)

X_train, X_test, y_temp_train, y_temp_test = train_test_split(
    X, y_temp, test_size=0.2, shuffle=False
)

_, _, y_cond_train, y_cond_test = train_test_split(
    X, y_cond, test_size=0.2, shuffle=False
)

# Models
temp_model = RandomForestRegressor(n_estimators=100)
temp_model.fit(X_train, y_temp_train)

cond_model = RandomForestClassifier(n_estimators=100)
cond_model.fit(X_train, y_cond_train)

# Save models
joblib.dump(temp_model, "temp_model.pkl")
joblib.dump(cond_model, "cond_model.pkl")
joblib.dump(encoder, "encoder.pkl")

print("✅ Models + Encoder trained successfully!")